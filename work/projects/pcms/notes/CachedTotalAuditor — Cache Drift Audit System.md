---
date: "2026-06-04"
description: "PCMS Trackings::CachedTotalAuditor + audit:cached_totals cron — continuous monitoring of cached_total drift; closes #2280 and the cached-charges arc. Second root cause: recalc jobs skipping updated_at via update_column."
project: pcms
github_issue: 2280
status: completed
tags:
  - work-note
---

# CachedTotalAuditor — Cache Drift Audit System

## Context

Trackings store `cached_total` mirroring `charges` so billing reads don't recompute per request. The standing "do cached charges work?" question on the [[North Star]] asked whether that cache could silently drift. [[Cached Total Resync on SR Cancel-Uncancel|#2337]] closed one known *source* of drift (cancel/uncancel via `update_all`) but did nothing for rows already stale, or for vectors not yet found. This work — **PR [#2307](https://github.com/csb-ric/pcms/pull/2307), merged 2026-06, closing [#2280](https://github.com/csb-ric/pcms/issues/2280)** — is the diagnostic + monitoring layer that closes the arc.

## What shipped

- **`Trackings::CachedTotalAuditor`** — compares each `Tracking#cached_total` against a live recompute of `#charges` over a configurable period (`:last_week`, `:last_month`, `:last_year`). Returns a `Report` struct: accuracy rate, mismatch counts sorted by absolute dollar delta, and error records. N+1 preloads added; improved error reporting when `cache_total` fails at import time.
- **`audit:cached_totals` rake task** — cron-driven, runs the auditor across all three period tiers and fires **Honeybadger on drift**. This is the "daily monitoring job" the README previously flagged as the next step — now live.
- **Second root cause fixed** — all eight `recalculate-*` jobs switched from `update_column` to `update_columns`, so cache writes now stamp `updated_at`. Previously cache writes left no freshness signal, masking staleness. This was the *other* drift vector beyond #2337's `update_all` path. See [[Gotchas#`update_column` skips `updated_at` — use `update_columns` for cache writes]].
- 197-line spec suite ships with the auditor.

## Why it matters

Together with #2337 this resolves the cached-charges question end to end:

- **#2337** stops the cancel/uncancel bleeding (the live source).
- **`update_columns` switch** stops a second silent source (recalc jobs not stamping freshness).
- **CachedTotalAuditor + cron** reports any existing wound and keeps watching, so future drift surfaces via Honeybadger instead of as a billing surprise.

The [[North Star]] cached-charges goal is marked resolved as of this merge.

## Follow-ups

- [ ] Run the auditor (or let the cron run) against production and triage any reported mismatches — see [[Cached Total Resync on SR Cancel-Uncancel#Action Items]].
- [ ] Decide whether other `update_all` callsites on trackings need `after_commit` recalc treatment.

## Related

- [[PCMS]]
- [[Cached Total Resync on SR Cancel-Uncancel]] — the source-side fix (#2337); this note is its diagnostic companion
- [[North Star]]
- [[Gotchas]]
- [[Index]]
