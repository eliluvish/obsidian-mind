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

## First production run (2026-06-16)

The daily `last_week` cron fired its first drift alert (run 03:30, range `2026-06-08..2026-06-14`). The monitoring layer works end to end — Honeybadger surfaced real drift instead of it landing as a billing surprise.

- **Accuracy 99.92%** — 2 mismatches in 2524 trackings, 0 errors. Net cache overstates charges by `$136.98` (`488233.92` cached vs `488096.94` recomputed).
- Both mismatches **overstate** (cache > live charges):
  - `970431` (2026-06-09): cached `100.0` vs recomputed `0.0` — delta `-100.0`
  - `970869` (2026-06-10): cached `55.5` vs recomputed `18.5` — delta `-37.0`
- These are either rows left stale from before #2337 shipped or a drift vector not yet found — #2337 was meant to close the cancel/uncancel source. Triage tracked in **[#2360](https://github.com/csb-ric/pcms/issues/2360)**.

## Drift root-caused + fixed (2026-06-16)

Both mismatches traced to a single uncaught vector: when a `CalendarEvent` commits, `update_or_create_tracking` only re-caches the event's *own* tracking. A **cancelled reservation whose slot overlapped** the event had its rebooked time — and therefore `accountable_units` / `cached_total` — changed, but no invalidation path re-cached it. This is the "drift vector not yet found" hypothesized above, distinct from the #2337 cancel/uncancel source.

**Fix** ([#2360](https://github.com/csb-ric/pcms/issues/2360) / [#2361](https://github.com/csb-ric/pcms/issues/2361), merged 2026-06-16): `RefreshOverlappingCancelledTrackingsJob` — an `after_commit` on `CalendarEvent` enqueues a job that finds all cancelled reservations overlapping the event's slot and re-caches them off the request cycle (guarded by `no_callbacks`). Both flagged trackings (`970431`, `970869`) resolved.

## Follow-ups

- [x] Run the auditor (or let the cron run) against production and triage any reported mismatches — first run 2026-06-16 surfaced 2 mismatches; **root-caused + fixed** via [#2360](https://github.com/csb-ric/pcms/issues/2360) / [#2361](https://github.com/csb-ric/pcms/issues/2361) (see above). See [[Cached Total Resync on SR Cancel-Uncancel#Action Items]].
- [ ] Decide whether other `update_all` callsites on trackings need `after_commit` recalc treatment.

## Related

- [[PCMS]]
- [[Cached Total Resync on SR Cancel-Uncancel]] — the source-side fix (#2337); this note is its diagnostic companion
- [[North Star]]
- [[Gotchas]]
- [[Index]]
