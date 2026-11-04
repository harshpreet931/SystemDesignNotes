"""Charts for the video, from the measured results. white, black, one red."""
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = os.path.dirname(os.path.abspath(__file__))
RES, OUT = os.path.join(HERE, "results"), os.path.join(HERE, "plots")
INK, GREY, RED = "#111111", "#c9c9c9", "#e03131"

for f in ("/System/Library/Fonts/Supplemental/Andale Mono.ttf",):
    if os.path.exists(f):
        font_manager.fontManager.addfont(f)
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=f).get_name()
plt.rcParams.update({"font.size": 15, "axes.edgecolor": INK, "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK, "figure.facecolor": "white"})


def clean(ax, left=False):
    for s in ("top", "right") + (() if left else ("left",)):
        ax.spines[s].set_visible(False)
    if not left:
        ax.set_yticks([])


def boundary():
    """fixed window: the two stacks of 100 on either side of the minute mark."""
    d = json.load(open(os.path.join(RES, "attack.json")))
    B = d["boundary_us"]
    ok = sorted((x["t_us"] - B) / 1e3 for x in d["decisions"] if x["alg"] == "fixed window" and x["ok"]
                and x["phase"] != "paced")
    fig, ax = plt.subplots(figsize=(12, 5.2))
    for side in (-1, 1):
        pts = [t for t in ok if (t < 0) == (side < 0)]
        x0 = sum(pts) / len(pts)
        for i in range(len(pts)):
            ax.add_patch(plt.Rectangle((x0 - 25 + (i % 10) * 5, (i // 10) * 5), 4.2, 4.2, color=INK, lw=0))
    ax.axvline(0, color=RED, lw=2, ls=(0, (4, 3)))
    ax.text(0, 56, "01:00.000\nnew window, counter resets", color=RED, ha="center", va="bottom", fontsize=14,
            bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="none"))
    ax.text(-50, -6, "100 allowed\n(window 0)", ha="center", va="top", fontsize=14)
    ax.text(50, -6, "100 allowed\n(window 1)", ha="center", va="top", fontsize=14)
    span = (max(ok) - min(ok)) / 1e3
    ax.set_title(f"limit: 100/min  →  {len(ok)} allowed in {span:.2f} s", loc="left", fontsize=20, pad=18)
    ax.set_xlim(-110, 110)
    ax.set_ylim(-22, 78)
    ax.set_xticks([-100, -50, 0, 50, 100], ["−0.10 s", "−0.05 s", "0", "+0.05 s", "+0.10 s"])
    clean(ax)
    fig.text(0.99, 0.01, "measured: fixed window counter, Redis 7.4", ha="right", fontsize=11, color="#777")
    fig.savefig(os.path.join(OUT, "fig_boundary.png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


def attack():
    """same traffic, six limiters: what actually reaches the server."""
    d = json.load(open(os.path.join(RES, "attack.json")))
    rows = {r["alg"]: r for r in json.load(open(os.path.join(RES, "attack_summary.json")))}
    B, names = d["boundary_us"], [r for r in rows]
    fig, ax = plt.subplots(figsize=(15, 6.8))
    for k, name in enumerate(names):
        y = len(names) - 1 - k
        mine = [x for x in d["decisions"] if x["alg"] == name]
        rej = [(x["t_us"] - B) / 1e6 for x in mine if not x["ok"]]
        if name == "leaky queue":
            ok = [(x["t_us"] + x["extra"] - B) / 1e6 for x in mine if x["ok"]]
        else:
            ok = [(x["t_us"] - B) / 1e6 for x in mine if x["ok"]]
        ax.vlines(rej, y - 0.16, y + 0.16, color=GREY, lw=0.6)
        ax.vlines(ok, y - 0.32, y + 0.32, color=INK, lw=0.9)
        burst = rows[name]["burst_allowed"]
        ax.add_patch(plt.Rectangle((-0.45, y - 0.32), 0.9, 0.64, color=INK, lw=0, zorder=3))
        ax.text(0.7, y + 0.2, f"{burst} at once" if name != "leaky queue" else f"{burst} in, 1 at a time out",
                fontsize=11, va="bottom", ha="left", zorder=4,
                bbox=dict(boxstyle="square,pad=0.15", fc="white", ec="none"))
        n = rows[name]["max_rolling_60s"]
        hot = n >= 150
        label = f"{n}" if name != "leaky queue" else f"{min(n, 100)}*"
        ax.text(64.5, y, label, va="center", ha="left", fontsize=20, color=RED if hot else INK)
        ax.text(-2.0, y, name, va="center", ha="right", fontsize=15)
    ax.text(64.5, len(names) - 0.25, "most in\nany 60 s", va="bottom", ha="left", fontsize=12, color="#555")
    ax.axvline(0, color=RED, lw=1.2, ls=(0, (4, 3)), zorder=1)
    ax.set_xlim(-1, 63)
    ax.set_ylim(-0.7, len(names) - 0.2)
    ax.set_xticks([0, 10, 20, 30, 40, 50, 60], ["01:00", ":10", ":20", ":30", ":40", ":50", "02:00"])
    clean(ax)
    ax.set_title("limit 100/min. attack: 100 at 00:59.95, 100 at 01:00.05, then 10 per second",
                 loc="left", fontsize=16, pad=14)
    fig.text(0.01, 0.0, "black = let through   grey = rejected   * leaky queue: released one every 0.6 s, "
             "the last one waited 60 s", fontsize=11, color="#555")
    fig.savefig(os.path.join(OUT, "fig_attack.png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


def race():
    rows = json.load(open(os.path.join(RES, "race.json")))
    fig, ax = plt.subplots(figsize=(12, 5.6))
    xs = range(len(rows))
    w = 0.38
    naive = [r["naive"]["median"] for r in rows]
    lua = [r["lua"]["median"] for r in rows]
    ax.bar([x - w / 2 for x in xs], naive, w, color=RED, label="read → compute → write (in app code)")
    ax.bar([x + w / 2 for x in xs], lua, w, color=INK, label="one Lua script (atomic)")
    for x, v in zip(xs, naive):
        ax.text(x - w / 2, v + 15, f"{v:.0f}", ha="center", fontsize=13, color=RED)
    for x, v in zip(xs, lua):
        ax.text(x + w / 2, v + 15, f"{v:.0f}", ha="center", fontsize=13)
    ax.axhline(100, color=INK, lw=1, ls=(0, (4, 3)), label="the limit: 100", zorder=0)
    ax.set_xticks(list(xs), [str(r["gateways"]) for r in rows])
    ax.set_xlabel("gateways sharing one bucket in Redis")
    ax.set_ylabel("requests let through (of 1,000)")
    ax.set_ylim(0, 1100)
    clean(ax, left=True)
    ax.legend(frameon=False, loc="upper left", fontsize=12)
    ax.set_title("same token bucket, same math. only one is atomic.", loc="left", fontsize=18, pad=14)
    fig.savefig(os.path.join(OUT, "fig_race.png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


def tokens():
    d = json.load(open(os.path.join(RES, "llm_tokens.json")))
    fig, ax = plt.subplots(figsize=(10, 4.2))
    modes = ["no cache", "with cache"]
    vals = [d[m]["allowed"] for m in modes]
    ax.barh([1, 0], vals, 0.5, color=[INK, RED])
    for y, m, v in zip([1, 0], modes, vals):
        ax.text(v + 0.8, y, f"{v} of 50   ({d[m]['counted_toward_limit']:,} tokens counted)", va="center", fontsize=13)
    ax.set_yticks([1, 0], modes)
    ax.set_xlim(0, 80)
    ax.set_xticks([])
    for s in ("top", "right", "bottom"):
        ax.spines[s].set_visible(False)
    ax.set_title("2M input tokens/min. 50 requests, each a 200k-token doc + a question",
                 loc="left", fontsize=14, pad=12)
    fig.savefig(os.path.join(OUT, "fig_tokens.png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    boundary()
    attack()
    race()
    tokens()
    print("wrote", sorted(os.listdir(OUT)))
