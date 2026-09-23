# Sailor — weekly brief

Eleven geopolitical and geo-economic situations, scored weekly against their own
baseline from public event data. Runs itself: a GitHub Action fetches new days,
rebuilds `public/data/brief.json`, commits it, and redeploys the page.

Raw GDELT files are never stored. Each day is reduced to eleven rows of counts
before anything is written, so a year of history is about 250 KB.

## Setup, once

The repo stays private. GitHub runs the job; Vercel serves the page.

**GitHub**
1. Create a private repo and push this folder.
2. **Actions → Weekly brief → Run workflow**, with **days = 400**.
   The first run takes 60-90 minutes: it is downloading a year of daily files to
   build the 26-week baseline. Later runs take 2-3 minutes.

**Vercel** (free, and it reads private repos)
3. vercel.com → sign in with GitHub → **Add New → Project** → import this repo.
4. Framework Preset **Other**, Output Directory **public**, no build command.
   `vercel.json` already says this, so the defaults should be right.
5. Deploy. The address is `https://<project>.vercel.app`.

After that it runs by itself at 03:00 UTC every Monday (noon in Seoul): the job
commits the new data, Vercel sees the commit and redeploys.

## Running it locally

    pip install -r requirements.txt
    python scripts/ingest.py --days 400     # first time
    python scripts/build.py
    python -m http.server -d public 8000

## What is frozen

`scripts/cases.py` holds the eleven case definitions and the thresholds, frozen
on 2026-09-23 alongside the pre-registration. Changing any of it breaks
comparison with the backtest — if a change is needed, record it and say so.

    Watch 1σ · Alert 2σ · Critical 3σ
    26-week rolling baseline
    a week below half its trailing median volume is withheld, not scored

## Layout

    scripts/cases.py    case definitions and thresholds (frozen)
    scripts/ingest.py   incremental download → data/agg/<year>.csv
    scripts/build.py    aggregates → public/data/brief.json
    public/index.html   the page
    data/agg/           per-day per-case counts, committed
