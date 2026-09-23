# Sailor — Pre-Registration No. 1

**Published 2026-09-23. Data snapshot: week of 2026-09-14.**
**First resolution 2026-11-10 · final resolution 2026-12-01.**

Four predictions about geopolitical and geo-economic risk, written down before
the events they describe, with the criteria that decide them fixed in advance.

---

## Why this exists

Sailor scores eleven predefined geopolitical situations from public news event
data and raises an alert level when a situation moves outside its own normal
range. We have tested it against 21 past events and caught 15 of them, a median
of 34 days before impact.

Every one of those 21 is a backtest, and a backtest can always be accused of
hindsight — thresholds chosen once the answer was known. The only answer to that
is to publish predictions before the fact and let them be checked. This file is
that record. It will be updated once, with the outcomes, and not otherwise.

## The method, in one paragraph

For each situation we count conflict, coercion, sanction and military-coded
events between a named pair of actors, expressed per 100,000 global events, plus
average tone. Each measure is compared with that situation's own 26-week rolling
baseline. The mean of those standardised scores is the composite: **Normal**
below 1σ, **Watch** 1–2σ, **Alert** 2–3σ, **Critical** at 3σ and above. A week
whose global event volume falls below half its trailing median is discarded
rather than scored, because a collapsed denominator inflates every rate.

The code that computes this is in `scripts/build.py` and `scripts/cases.py` in
this repository, frozen as of today.

## State at the time of writing

All eleven situations, week of 14 September 2026. Coverage ratio 1.08 — healthy.
Nothing is currently elevated.

| Situation | Composite | vs prior 4 wks | Level |
|---|---:|---:|---|
| US export controls on China | +0.98 | +0.46 | Normal |
| North Korea | +0.67 | −1.09 | Normal |
| US–China tariffs & rare earths | +0.63 | +0.23 | Normal |
| India–Pakistan | +0.51 | +0.82 | Normal |
| China–Japan (Takaichi remarks) | +0.26 | +0.75 | Normal |
| China–Japan seafood ban | +0.24 | +0.74 | Normal |
| Russia–Ukraine | +0.11 | −0.12 | Normal |
| South China Sea (Philippines) | −0.21 | +0.38 | Normal |
| Thailand–Cambodia | −0.34 | −0.29 | Normal |
| Israel–Iran | −0.79 | −0.25 | Normal |
| Taiwan Strait | −0.85 | −0.94 | Normal |

---

## The predictions

### P1 — Predicted miss · resolves 2026-09-26
**We will not have called the Trump–Xi summit.**

A summit is scheduled for 24 September 2026, one day after this file is
published. Neither the tariff case (+0.63) nor the export-control case (+0.98)
is at Watch, and a single week cannot produce the two consecutive weeks our rule
requires.

> We predict Sailor will **not** have raised either case to Watch before the
> summit. We are recording this as a miss in advance.

We include it because a register that contains only predicted successes is worth
nothing. Our signal measures conflict, coercion and sanction activity; a
scheduled cooperative meeting is the kind of event it is not built to
anticipate, and saying so before the fact is more useful than explaining it
afterwards.

### P2 — Open · resolves 2026-11-10
**Rare earths: Watch at least two weeks before the deadline.**

China's export controls of 9 October 2025 — which reach any foreign-made product
containing 0.1% or more of Chinese-origin rare-earth input — are suspended
through **10 November 2026**. On that date they take effect unless the suspension
is extended or modified.

> We predict the **US–China tariffs & rare earths** case reaches Watch —
> composite at or above 1.0 for two consecutive weeks — **on or before
> 27 October 2026**, at least 14 days before the deadline.

```
Hit    two consecutive weeks >= 1.0, both with coverage >= 0.6,
       first week starting on or before 2026-10-27
Miss   no such run by 2026-10-27, or the first run begins after a
       public announcement of the outcome
Void   the deadline moves before 2026-10-20, or more than two weeks
       in the window are discarded for low coverage
Now    +0.63, Normal. No two-week Watch run since the backtest began
```

This is the hard one. Rulemaking is our weakest category — we caught 2 of 4 in
the backtest, and one of the two we missed was the October 2025 announcement
this deadline descends from. We are re-testing the thing we are worst at, on a
date everyone can see coming. Stated confidence: **60%**.

### P3 — Open · resolves 2026-12-01
**Taiwan elections: the current configuration fails, the fix works.**

Taiwan holds local elections on **28 November 2026** across six municipalities
and sixteen counties. Cross-strait activity has risen before every comparable
date since 2022, and the Taiwan Strait case is our quietest right now at −0.85.

The backtest showed why we miss Taiwan: we pool China-toward-Taiwan activity with
China-toward-United States activity, and the Taiwan signal is diluted. In the
week of the 2022 Pelosi drills it measured 0.0σ. Narrowing the actor pair is the
fix we identified, and it has not been implemented yet.

> We predict the **current pooled configuration misses** — no two-week Watch run
> before 14 November 2026 — and that the **narrowed China-to-Taiwan
> configuration hits**, reaching Watch on or before that date.

```
Spec   narrowed = actors CHN, targets TWN only; USA removed from
       targets; every other parameter unchanged
Hit    both halves correct: pooled produces no run, narrowed produces
       one, by 2026-11-14
Split  one half correct — reported as such, not as a win
Miss   pooled fires and narrowed does not
Now    pooled -0.85, Normal. Narrowed not yet computed; the
       specification above is frozen as of today
```

Both configurations will be run over the same weeks with the same thresholds.
Stated confidence in the full result: **45%**.

### P4 — Open · resolves 2026-12-01
**Most of the board stays quiet.**

A detection claim means nothing without a false-alarm claim beside it. Across the
backtest, quiet weeks reached Watch or above roughly one time in ten.

> We predict that **at least 7 of the 11 situations** record no two-week Watch
> run at any point between 23 September and 1 December 2026.

```
Hit    7 or more situations stay below the Watch run for the whole window
Miss   5 or more situations produce a run
Now    11 of 11 Normal
```

If this one fails, the others do not matter. A system that fires everywhere
catches everything and is worth nothing. Stated confidence: **75%**.

---

## What we bind ourselves to

1. Thresholds, signal definitions, baseline lengths and the coverage rule are
   fixed as described above. None will be changed before 1 December 2026.
2. The eleven situations are fixed. No case will be added, removed or redefined
   during the window — including the narrowed Taiwan configuration, whose
   specification is frozen today and which is reported alongside the pooled one,
   never instead of it.
3. Outcomes will be reported for all four predictions, including the ones we get
   wrong, in this file.
4. Underlying weekly figures will be published with the outcomes so the
   arithmetic can be checked.
5. If a prediction turns out to be ambiguous as written, it is reported as
   ambiguous, not resolved in our favour.

## Outcomes

Pending — first resolution 2026-11-10.

## What happened last time, out of sample

One data point exists already, after the backtest window closed on 31 December
2025 and before this file was written. On **27 July 2026** the North Korea case
reached Watch at 1.31. North Korea launched a short-range ballistic missile on
**6 August** and a 700-kilometre ballistic missile on **12 August**; the case
peaked at Critical, 3.16, in the week of 10 August, and held Alert through the
start of the Ulchi Freedom Shield exercise on 17 August. Global event volume that
week was more than twice its median, so the score was not a coverage artifact.

That is one event, caught once. It is the reason this register exists rather than
the proof this register is meant to replace.

## Sources

- [China's rare-earth export controls and the 10 November 2026 deadline](https://rareearthexchanges.com/news/china-rare-earth-controls-trump-xi-deadline/)
- [2026 Taiwanese local elections — 28 November 2026](https://en.wikipedia.org/wiki/2026_Taiwanese_local_elections)
- [North Korea's 12 August 2026 ballistic missile launch](https://www.aljazeera.com/news/2026/8/12/n-korea-launches-ballistic-missile-as-s-korea-us-plan-military-drills)
- [Ulchi Freedom Shield, beginning 17 August 2026](https://www.stripes.com/theaters/asia_pacific/2026-08-13/ulchi-freedom-shield-exercise-korea-22537947.html)
- Event data: GDELT 1.0 event files, 2021-01-01 to 2026-09-20.

---

*Sailor · non-financial risk early warning.*
*Published 2026-09-23. This file will be edited once, to add outcomes.*
