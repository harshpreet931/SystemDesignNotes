"""The boundary attack, against all six limiters at once.

limit: 100 requests per minute. the attacker:
  1. waits until 50 ms before a minute boundary (by Redis's clock)
  2. sends 100 requests
  3. sends 100 more at 50 ms after the boundary
  4. then sends 10 requests per second for the next 62 seconds

every request is checked by all six limiters (separate keys), so they all see the
exact same traffic. results go to results/attack.json.
"""
import json
import os
import sys
import time
import uuid

from limiters import WINDOW_MS, Limiters, redis_now_us

PACE_HZ, PACE_S = 10, 62
OUT = os.path.join(os.path.dirname(__file__), "results", "attack.json")


def sleep_until(target_us, offset_us):
    """Sleep until Redis's clock reads target_us (offset = redis - local)."""
    while True:
        left = (target_us - offset_us) / 1e6 - time.time()
        if left <= 0:
            return
        time.sleep(min(left, 0.2) if left > 0.003 else 0)


def send(L, run, n, log, phase):
    """n requests, each checked by every limiter, in one pipeline (a burst)."""
    p = L.r.pipeline(transaction=False)
    for _ in range(n):
        for name in L.NAMES:
            L.call(name, f"rl:{run}:{name}", client=p)
    res = p.execute()
    for i, (ok, now_us, extra) in enumerate(res):
        log.append({"alg": L.NAMES[i % len(L.NAMES)], "phase": phase, "ok": int(ok),
                    "t_us": int(now_us), "extra": int(extra)})


def main():
    L = Limiters()
    run = uuid.uuid4().hex[:8]
    offset = min((redis_now_us(L.r) - int(time.time() * 1e6)) for _ in range(5))
    now = redis_now_us(L.r)
    win_us = WINDOW_MS * 1000
    boundary = (now // win_us + 1) * win_us
    if boundary - now < 3_000_000:            # too close, use the next one
        boundary += win_us
    print(f"run {run}: waiting {(boundary - now) / 1e6:.1f} s for the next minute boundary...", flush=True)

    log = []
    sleep_until(boundary - 50_000, offset)
    send(L, run, 100, log, "burst before")
    sleep_until(boundary + 50_000, offset)
    send(L, run, 100, log, "burst after")
    print("bursts sent, now pacing at 10/s for 62 s...", flush=True)
    start = boundary + 100_000
    for k in range(PACE_HZ * PACE_S):
        sleep_until(start + k * 1_000_000 // PACE_HZ, offset)
        send(L, run, 1, log, "paced")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump({"run": run, "boundary_us": boundary, "limit": 100, "window_ms": WINDOW_MS,
                   "pace_hz": PACE_HZ, "pace_s": PACE_S, "decisions": log}, f)
    summarize(OUT)


def rolling_max(ts_us, width_us):
    ts, best, j = sorted(ts_us), 0, 0
    for i in range(len(ts)):
        while ts[i] - ts[j] >= width_us:
            j += 1
        best = max(best, i - j + 1)
    return best


def summarize(path):
    d = json.load(open(path))
    B, W = d["boundary_us"], d["window_ms"] * 1000
    rows = []
    print(f"\nlimit {d['limit']}/min. 200 requests in the 0.1 s around the minute mark, then 10/s.\n")
    print(f"{'algorithm':16s} {'allowed in the 0.1 s burst':>27s} {'most in any 60 s':>17s} {'longest wait':>13s}")
    for name in Limiters.NAMES:
        mine = [x for x in d["decisions"] if x["alg"] == name]
        ok = [x for x in mine if x["ok"]]
        burst = [x for x in ok if x["phase"] != "paced"]
        if name == "leaky queue":                 # what reaches the server is the release time
            out = [x["t_us"] + x["extra"] for x in ok]
            wait = max(x["extra"] for x in ok) / 1e6
        else:
            out, wait = [x["t_us"] for x in ok], 0.0
        span = (max(x["t_us"] for x in burst) - min(x["t_us"] for x in burst)) / 1e6 if burst else 0
        row = {"alg": name, "burst_allowed": len(burst), "burst_span_s": round(span, 3),
               "max_rolling_60s": rolling_max(out, W), "max_wait_s": round(wait, 2),
               "total_allowed": len(ok), "total_requests": len(mine)}
        rows.append(row)
        print(f"{name:16s} {len(burst):>12d} in {span:.3f} s {row['max_rolling_60s']:>17d} {wait:>12.1f}s")
    with open(path.replace(".json", "_summary.json"), "w") as f:
        json.dump(rows, f, indent=1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--summary":
        summarize(OUT)
    else:
        main()
