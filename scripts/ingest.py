"""Incremental GDELT ingest.

Downloads one day at a time, keeps only the rows that touch a case, reduces them
to eleven rows of counts, and appends to data/agg/<year>.csv. The raw files are
never stored — a year of aggregates is about 250 KB.

    python scripts/ingest.py               # everything since the last stored day
    python scripts/ingest.py --days 400    # first run: backfill the baseline
"""
import argparse, io, os, sys, zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, timedelta

import numpy as np
import pandas as pd
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cases import CASES, COLS, MILITARY_ROOTS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGG = os.path.join(ROOT, "data", "agg")
URL = "http://data.gdeltproject.org/events/{}.export.CSV.zip"
FIELDS = ["events", "conflict", "threat_coerce", "sanction", "military_pair",
          "military_geo", "keyword_articles", "tone_num", "tone_den"]


def url_match(url, words):
    return url.str.contains("|".join(words), regex=True, na=False)


def keep_mask(df, c):
    root = df["EventRootCode"].astype(str).str.zfill(2)
    url = df["SOURCEURL"].fillna("").str.lower()
    pair = ((df["A1C"].isin(c["actors"]) & df["A2C"].isin(c["targets"])) |
            (df["A1C"].isin(c["targets"]) & df["A2C"].isin(c["actors"]))) & (df["A1C"] != df["A2C"])
    mil = df["GeoCountry"].isin(c["geo"]) & root.isin(MILITARY_ROOTS)
    a, b = c["response_keywords"]
    return pair | mil | url_match(url, c["keywords"]) | (url_match(url, a) & url_match(url, b))


def one_day(d):
    """Return a DataFrame of 11 rows, or None if GDELT has no file for that day."""
    ymd = d.strftime("%Y%m%d")
    last = ""
    for _ in range(3):
        try:
            r = requests.get(URL.format(ymd), timeout=180)
            if r.status_code == 404:
                return pd.DataFrame([{"date": ymd, "case": n, "day_total": 0,
                                      **{f: 0 for f in FIELDS}} for n in CASES])
            r.raise_for_status()
            with zipfile.ZipFile(io.BytesIO(r.content)) as z, z.open(z.namelist()[0]) as fh:
                raw = pd.read_csv(fh, sep="\t", header=None, usecols=list(COLS), dtype=str,
                                  quoting=3, on_bad_lines="skip").rename(columns=COLS)
            break
        except Exception as e:
            last = str(e)
    else:
        raise RuntimeError(f"{ymd}: {last}")

    total = len(raw)
    keep = np.zeros(total, dtype=bool)
    for c in CASES.values():
        keep |= keep_mask(raw, c).values
    d2 = raw[keep]

    q = pd.to_numeric(d2["QuadClass"], errors="coerce")
    nm = pd.to_numeric(d2["NumMentions"], errors="coerce").fillna(1).clip(lower=1)
    tn = pd.to_numeric(d2["AvgTone"], errors="coerce")
    root = d2["EventRootCode"].astype(str).str.zfill(2)
    c3 = d2["EventCode"].astype(str).str.zfill(4).str[:3]
    url = d2["SOURCEURL"].fillna("").str.lower()
    a1, a2, geo = d2["A1C"], d2["A2C"], d2["GeoCountry"]
    ismil = root.isin(MILITARY_ROOTS)

    rows = []
    for n, c in CASES.items():
        pair = a1.isin(c["actors"]) & a2.isin(c["targets"]) & (a1 != a2)
        kw = url_match(url, c["keywords"])
        ok = pair & tn.notna()
        rows.append({
            "date": ymd, "case": n, "day_total": total,
            "events": int(pair.sum()),
            "conflict": int((pair & q.isin([3, 4])).sum()),
            "threat_coerce": int((pair & root.isin(["13", "16", "17"])).sum()),
            "sanction": int((pair & c3.isin(["163", "172"])).sum()),
            "military_pair": int((pair & ismil).sum()),
            "military_geo": int((geo.isin(c["geo"]) & ismil).sum()),
            "keyword_articles": int(url[kw].nunique()),
            "tone_num": float((tn[ok] * nm[ok]).sum()),
            "tone_den": float(nm[ok].sum()),
        })
    return pd.DataFrame(rows)


def stored():
    os.makedirs(AGG, exist_ok=True)
    got = set()
    for f in sorted(os.listdir(AGG)):
        if f.endswith(".csv"):
            got |= set(pd.read_csv(os.path.join(AGG, f), usecols=["date"])["date"].astype(str))
    return got


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30, help="how far back to look for gaps")
    ap.add_argument("--threads", type=int, default=6)
    args = ap.parse_args()

    end = date.today() - timedelta(days=2)          # GDELT lags about a day
    start = end - timedelta(days=args.days - 1)
    have = stored()
    todo = [d for d in pd.date_range(start, end, freq="D") if d.strftime("%Y%m%d") not in have]
    if not todo:
        print("nothing to fetch — already current through", end)
        return

    print(f"fetching {len(todo)} days: {todo[0].date()} -> {todo[-1].date()}")
    out, failed = [], []
    with ThreadPoolExecutor(args.threads) as ex:
        futs = {ex.submit(one_day, d): d for d in todo}
        for i, f in enumerate(as_completed(futs), 1):
            try:
                out.append(f.result())
            except Exception as e:
                failed.append(str(e))
            if i % 25 == 0:
                print(f"  {i}/{len(todo)}", flush=True)

    if not out:
        raise SystemExit("every day failed:\n" + "\n".join(failed[:5]))
    new = pd.concat(out)
    for year, part in new.groupby(new["date"].str[:4]):
        path = os.path.join(AGG, f"{year}.csv")
        if os.path.exists(path):
            part = pd.concat([pd.read_csv(path, dtype={"date": str}), part])
        part = part.drop_duplicates(["date", "case"]).sort_values(["date", "case"])
        part.to_csv(path, index=False)
        print(f"  wrote {path}: {part['date'].nunique()} days")

    if failed:
        print(f"{len(failed)} days failed — re-run to pick them up:", failed[:3])


if __name__ == "__main__":
    main()
