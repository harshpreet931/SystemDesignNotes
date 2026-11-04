"""LLM APIs limit tokens per minute, not requests. same token bucket, the cost just isn't 1.

the setup is from Anthropic's rate-limit docs: a 2,000,000 input-tokens-per-minute limit,
and requests that each send a 200,000-token document plus a 50-token question.
for most Claude models, tokens read from the prompt cache don't count toward that limit.

we send the same 50 requests twice, using the exact Lua token bucket from limiters.py:
  no cache:   every request costs 200,050 tokens
  with cache: the first one writes the cache (200,050), the rest cost 50
"""
import json
import os
import uuid

from limiters import TOKEN_BUCKET, Limiters

ITPM = 2_000_000
DOC, QUESTION, N = 200_000, 50, 50
OUT = os.path.join(os.path.dirname(__file__), "results", "llm_tokens.json")


def main():
    L = Limiters()
    bucket = L.r.register_script(TOKEN_BUCKET)
    results = {}
    for mode in ("no cache", "with cache"):
        key = f"itpm:{uuid.uuid4().hex[:8]}"
        costs = [DOC + QUESTION if (mode == "no cache" or i == 0) else QUESTION for i in range(N)]
        p = L.r.pipeline(transaction=False)
        for c in costs:
            bucket(keys=[key], args=[ITPM, ITPM / 60, c], client=p)
        ok = [int(x[0]) for x in p.execute()]
        # every allowed request still reads the full 200,050 tokens, cached or not
        results[mode] = {"sent": N, "allowed": sum(ok), "input_tokens_processed": sum(ok) * (DOC + QUESTION),
                         "counted_toward_limit": sum(c for c, o in zip(costs, ok) if o)}
        print(f"{mode:10s}: {sum(ok):>2d} of {N} requests allowed, "
              f"{results[mode]['input_tokens_processed']:,} input tokens processed, "
              f"{results[mode]['counted_toward_limit']:,} counted toward the limit")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(results, f, indent=1)


if __name__ == "__main__":
    main()
