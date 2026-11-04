"""Five rate limiters (six, counting both leaky buckets), each one atomic Redis Lua script.

Every script reads the clock with Redis TIME, so every caller shares one clock,
and returns {allowed, now_us, extra}.
"""
import itertools
import os

import redis

REDIS_URL = os.environ.get("REDIS_URL", "redis://127.0.0.1:6390/0")

# shared prelude: one clock for everyone
NOW = """
local t = redis.call('TIME')
local now_us = tonumber(t[1]) * 1000000 + tonumber(t[2])
local now = now_us / 1000                                  -- ms, with µs precision
"""

# fixed window: one counter per key per window. INCR and PEXPIRE in one script,
# so a crash can't leave a counter that never expires.
FIXED_WINDOW = NOW + """
local limit, win = tonumber(ARGV[1]), tonumber(ARGV[2])
local k = KEYS[1] .. ':' .. math.floor(now / win)
local n = redis.call('INCR', k)
if n == 1 then redis.call('PEXPIRE', k, win) end
if n <= limit then return {1, now_us, n} end
return {0, now_us, n}
"""

# sliding log: one sorted-set entry per accepted request. exact, and memory-hungry.
SLIDING_LOG = NOW + """
local limit, win = tonumber(ARGV[1]), tonumber(ARGV[2])
redis.call('ZREMRANGEBYSCORE', KEYS[1], '-inf', now - win)  -- forget anything older than the window
local n = redis.call('ZCARD', KEYS[1])
if n >= limit then return {0, now_us, n} end                -- rejected requests are not logged
redis.call('ZADD', KEYS[1], now, ARGV[3])
redis.call('PEXPIRE', KEYS[1], win)
return {1, now_us, n + 1}
"""

# sliding window counter: two counters and a weighted estimate (Cloudflare's version).
SLIDING_COUNTER = NOW + """
local limit, win = tonumber(ARGV[1]), tonumber(ARGV[2])
local w = math.floor(now / win)
local curr_k, prev_k = KEYS[1] .. ':' .. w, KEYS[1] .. ':' .. (w - 1)
local curr = tonumber(redis.call('GET', curr_k) or '0')
local prev = tonumber(redis.call('GET', prev_k) or '0')
local est = prev * (1 - (now % win) / win) + curr
if est + 1 > limit then return {0, now_us, math.floor(est * 1000)} end
redis.call('INCR', curr_k)
redis.call('PEXPIRE', curr_k, 2 * win)
return {1, now_us, math.floor((est + 1) * 1000)}
"""

# token bucket: capacity C, refills at `rate` tokens per second, lazily (no timer).
TOKEN_BUCKET = NOW + """
local cap, rate, cost = tonumber(ARGV[1]), tonumber(ARGV[2]), tonumber(ARGV[3])
local s = redis.call('HMGET', KEYS[1], 'tokens', 'ts')
local tokens = tonumber(s[1]) or cap                        -- a new bucket starts full
local ts = tonumber(s[2]) or now
tokens = math.min(cap, tokens + math.max(0, now - ts) * rate / 1000)
local ok = 0
if tokens >= cost then tokens = tokens - cost; ok = 1 end
redis.call('HSET', KEYS[1], 'tokens', tokens, 'ts', now)
redis.call('PEXPIRE', KEYS[1], math.ceil(cap / rate * 1000))
return {ok, now_us, math.floor(tokens)}
"""

# leaky bucket as a meter: a level that leaks at `leak` per second. full = reject.
LEAKY_METER = NOW + """
local cap, leak = tonumber(ARGV[1]), tonumber(ARGV[2])
local s = redis.call('HMGET', KEYS[1], 'level', 'ts')
local level = tonumber(s[1]) or 0
local ts = tonumber(s[2]) or now
level = math.max(0, level - math.max(0, now - ts) * leak / 1000)
local ok = 0
if level + 1 <= cap then level = level + 1; ok = 1 end
redis.call('HSET', KEYS[1], 'level', level, 'ts', now)
redis.call('PEXPIRE', KEYS[1], math.ceil(cap / leak * 1000))
return {ok, now_us, math.floor(level)}
"""

# leaky bucket as a queue: requests wait their turn and leave one every T ms.
# like NGINX limit_req, the queue is a schedule: each accepted request gets a release
# time, and the caller sleeps until then. returns the wait in µs.
LEAKY_QUEUE = NOW + """
local size, T = tonumber(ARGV[1]), tonumber(ARGV[2])         -- queue size, ms between releases
local next_free = tonumber(redis.call('GET', KEYS[1]) or '0')
local release = math.max(now, next_free)
if (release - now) / T >= size then return {0, now_us, 0} end
redis.call('SET', KEYS[1], release + T, 'PX', math.ceil(release + T - now) + 1000)
return {1, now_us, math.floor((release - now) * 1000)}
"""

LIMIT, WINDOW_MS = 100, 60_000          # the running example: 100 requests per minute
RATE = LIMIT / (WINDOW_MS / 1000)       # 1.67 per second

_seq = itertools.count()


class Limiters:
    """Register every script once, then call them by name."""

    NAMES = ["fixed window", "sliding log", "sliding counter", "token bucket", "leaky meter", "leaky queue"]

    def __init__(self, r=None):
        self.r = r or redis.Redis.from_url(REDIS_URL)
        self.scripts = {
            "fixed window": self.r.register_script(FIXED_WINDOW),
            "sliding log": self.r.register_script(SLIDING_LOG),
            "sliding counter": self.r.register_script(SLIDING_COUNTER),
            "token bucket": self.r.register_script(TOKEN_BUCKET),
            "leaky meter": self.r.register_script(LEAKY_METER),
            "leaky queue": self.r.register_script(LEAKY_QUEUE),
        }

    def args(self, name, cost=1):
        return {
            "fixed window": [LIMIT, WINDOW_MS],
            "sliding log": [LIMIT, WINDOW_MS, f"{os.getpid()}-{next(_seq)}"],
            "sliding counter": [LIMIT, WINDOW_MS],
            "token bucket": [LIMIT, RATE, cost],
            "leaky meter": [LIMIT, RATE],
            "leaky queue": [LIMIT, WINDOW_MS / LIMIT],
        }[name]

    def call(self, name, key, client=None, cost=1):
        """One decision. `client` can be a pipeline."""
        return self.scripts[name](keys=[key], args=self.args(name, cost), client=client)


def redis_now_us(r):
    sec, usec = r.time()
    return sec * 1_000_000 + usec
