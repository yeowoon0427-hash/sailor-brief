"""Turn the stored aggregates into public/data/brief.json.

Thresholds are frozen in cases.py. The coverage guard discards any week whose
global event volume fell below half its trailing median — without it a thin
collection week reads as an escalation.
"""
import json, os, sys
from datetime import datetime, timezone

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cases import CASES, BASELINE_WEEKS, COVERAGE_MIN, COVERAGE_WINDOW, LEVELS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGG = os.path.join(ROOT, "data", "agg")
OUT = os.path.join(ROOT, "public", "data", "brief.json")
COUNTS = ["events", "conflict", "threat_coerce", "sanction", "military_pair",
          "military_geo", "keyword_articles", "tone_num", "tone_den", "day_total"]


def load():
    parts = [pd.read_csv(os.path.join(AGG, f), dtype={"date": str})
             for f in sorted(os.listdir(AGG)) if f.endswith(".csv")]
    if not parts:
        raise SystemExit("no aggregates yet — run scripts/ingest.py --days 400 first")
    df = pd.concat(parts)
    df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")
    return df.drop_duplicates(["date", "case"]).sort_values("date")


def weekly(df, case):
    d = df[df["case"] == case].set_index("date")[COUNTS]
    d = d[d["day_total"] > 0]
    key = d.index.to_period("W-SUN").start_time
    w = d.groupby(key).sum()
    w["n_days"] = d.groupby(key).size()
    w = w[w["n_days"] >= 7]          # complete weeks only — a partial week reads as thin coverage
    per = 1e5 / w["day_total"]
    w["conflict_rate"] = w["conflict"] * per
    w["threat_rate"] = w["threat_coerce"] * per
    w["military_rate"] = (w["military_pair"] + w["military_geo"]) * per
    w["sanction_rate"] = w["sanction"] * per
    w["keyword_rate"] = w["keyword_articles"] * per
    w["neg_tone"] = -(w["tone_num"] / w["tone_den"].replace(0, np.nan))

    med = w["day_total"].shift(1).rolling(COVERAGE_WINDOW, min_periods=4).median()
    w["coverage"] = w["day_total"] / med
    low = w["coverage"] < COVERAGE_MIN

    for sg in ["conflict_rate", "threat_rate", "military_rate", "sanction_rate",
               "keyword_rate", "neg_tone"]:
        b = w[sg].shift(1).rolling(BASELINE_WEEKS, min_periods=13)
        w["z_" + sg] = ((w[sg] - b.mean()) / b.std().replace(0, np.nan)).clip(-5, 10)

    sig = CASES[case]["signals"]
    w["composite"] = w[["z_" + s for s in sig]].mean(axis=1, skipna=True)
    w.loc[low, "composite"] = np.nan
    w["level"] = pd.cut(w["composite"], [-np.inf, 1, 2, 3, np.inf],
                        labels=[1, 2, 3, 4], right=False).astype(float)
    return w


def main():
    df = load()
    complete = df.groupby("date")["day_total"].first()
    last_day = complete.index.max()
    board, history = [], {}

    for name, c in CASES.items():
        w = weekly(df, name)
        ok = w.dropna(subset=["composite"])
        if ok.empty:
            continue
        row = ok.iloc[-1]
        prev = ok["composite"].iloc[-5:-1].mean() if len(ok) > 4 else np.nan
        board.append({
            "case": name,
            "title": c["title"],
            "group": c["group"],
            "week": ok.index[-1].strftime("%Y-%m-%d"),
            "composite": round(float(row["composite"]), 2),
            "level": int(row["level"]),
            "level_name": LEVELS[int(row["level"])],
            "change": None if pd.isna(prev) else round(float(row["composite"] - prev), 2),
            "coverage": round(float(row["coverage"]), 2),
        })
        history[name] = [
            {"week": i.strftime("%Y-%m-%d"), "c": None if pd.isna(v) else round(float(v), 2)}
            for i, v in w["composite"].tail(26).items()
        ]

    board.sort(key=lambda r: -r["composite"])
    suppressed = 0
    for n in CASES:
        w = weekly(df, n)
        if len(w) and float(w["coverage"].iloc[-1]) < COVERAGE_MIN:
            suppressed += 1

    brief = {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "data_through": last_day.strftime("%Y-%m-%d"),
        "week_of": board[0]["week"] if board else None,
        "days_stored": int(df["date"].nunique()),
        "suppressed_cases": suppressed,
        "board": board,
        "history": history,
        "thresholds": {"watch": 1, "alert": 2, "critical": 3,
                       "baseline_weeks": BASELINE_WEEKS, "coverage_min": COVERAGE_MIN},
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(brief, fh, indent=1)
    print(f"wrote {OUT}: week of {brief['week_of']}, {len(board)} cases, "
          f"{brief['days_stored']} days stored")
    for r in board[:4]:
        print(f"  {r['level_name']:9s} {r['composite']:+5.2f}  {r['case']}")


if __name__ == "__main__":
    main()
