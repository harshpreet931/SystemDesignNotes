"""The race condition: N gateways share one token bucket in Redis.

naive: each gateway reads the bucket, does the math in Python, and writes it back
       (read → compute → write, two round trips, nothing atomic).
lua:   the exact same math, inside one Lua script, which Redis runs atomically.

bucket: 100 tokens, refills 100/min. 1,000 requests in total, split across N gateways
(threads, each with its own connection), all starting at the same moment.
the right answer is 100, plus whatever refilled while the test ran (about 1.7 per second).
results go to results/race.json.
"""
import json
import os
import statistics
import threading
import time
import uuid

import redis

from limiters import LIMIT, RATE, REDIS_URL, Limiters

TOTAL, TRIALS = 1000, 5
GATEWAYS = [1, 2, 5, 10, 20, 50]
OUT = os.path.join(os.path.dirname(__file__), "results", "race.json")


def naive_take(r, key, cap=LIMIT, rate=RATE):
    tokens, ts = r.hmget(key, "tokens", "ts")                    # 1. read
    now = time.time() * 1000
    tokens = float(tokens) if tokens else cap
    ts = float(ts) if ts else now
    tokens = min(cap, tokens + max(0, now - ts) * rate / 1000)   # 2. compute
    ok = tokens >= 1
    if ok:
        tokens -= 1
    r.hset(key, mapping={"tokens": tokens, "ts": now})          # 3. write
    return ok


def trial(mode, n):
    key = f"race:{mode}:{n}:{uuid.uuid4().hex[:8]}"
    clients = [redis.Redis.from_url(REDIS_URL) for _ in range(n)]
    lims = [Limiters(c) for c in clients] if mode == "lua" else None
    admitted = [0] * n
    go = threading.Barrier(n)

    def gateway(i):
        r, per = clients[i], TOTAL // n
        r.ping()                                                 # connect before the start line
        go.wait()
        for _ in range(per):
            if mode == "naive":
                ok = naive_take(r, key)
            else:
                ok = int(lims[i].call("token bucket", key)[0]) == 1
            admitted[i] += ok

    threads = [threading.Thread(target=gateway, args=(i,)) for i in range(n)]
    t0 = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    dur = time.perf_counter() - t0
    for c in clients:
        c.close()
    return {"admitted": sum(admitted), "duration_s": dur, "allowed_max": LIMIT + int(dur * RATE)}


def main():
    rows = []
    print(f"bucket {LIMIT} tokens, {TOTAL} requests, {TRIALS} trials each. median admitted:\n")
    print(f"{'gateways':>8s} {'naive':>8s} {'lua':>6s} {'right answer':>13s}")
    for n in GATEWAYS:
        row = {"gateways": n}
        for mode in ("naive", "lua"):
            ts = [trial(mode, n) for _ in range(TRIALS)]
            row[mode] = {"admitted": [t["admitted"] for t in ts],
                         "median": statistics.median(t["admitted"] for t in ts),
                         "allowed_max": max(t["allowed_max"] for t in ts),
                         "duration_s": [round(t["duration_s"], 3) for t in ts]}
        rows.append(row)
        print(f"{n:>8d} {row['naive']['median']:>8.0f} {row['lua']['median']:>6.0f}"
              f"   ≤ {max(row['naive']['allowed_max'], row['lua']['allowed_max'])}", flush=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(rows, f, indent=1)


if __name__ == "__main__":
    main()
