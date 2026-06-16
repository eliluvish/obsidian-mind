---
date: "2026-05-21"
description: "PCMS trackings cached_total went stale on SR cancel/uncancel because update_all skipped callbacks; fix enqueues RecalculateServiceRequestTrackingsJob via after_commit (PR #2337)"
project: pcms
github_issue: 2337
status: active
tags:
  - work-note
---

# Cached Total Resync on SR Cancel/Uncancel

## Context

Trackings store a `cached_total` that mirrors `charges` so billing reads don't recompute on every request. Cancelling or uncancelling a `ServiceRequest` flips `billable` on its trackings via `update_all`, which intentionally skips ActiveRecord callbacks. Result: `cached_total` silently went stale on every cancel/uncancel — a concrete staleness vector for the standing "PCMS: do cached charges work?" question on the [[North Star]].

## Notes

- **PR [#2337](https://github.com/csb-ric/pcms/issues/2337)** — `fix(trackings): refresh cached_total after SR cancel/uncancel`. Shipped to master 2026-05-14 (`9c29f4f`).
- Fix shape: `after_commit` hook on `ServiceRequest` enqueues `RecalculateServiceRequestTrackingsJob`, which recomputes `cached_total = charges` for every **unlocked** (non-invoiced) tracking on the SR. Locked/invoiced trackings are deliberately not touched.
- Paired with the switch to delayed_job in production (`94bf0ee3`) — the recalc job depends on a working background queue.
- Covered by a job spec and an SR spec (regression coverage for the cancel→uncancel→cached_total path).

### Relationship to PR #2307 (CachedTotalAuditor)

This fix closes the cancel/uncancel **source** of drift. It does not address rows that may already be stale from prior cancel/uncancel cycles or any other vector that hasn't surfaced yet. That sweep is the job of [PR #2307](https://github.com/csb-ric/pcms/issues/2307) — `feat(trackings): add CachedTotalAuditor` — **merged 2026-06, closing [#2280](https://github.com/csb-ric/pcms/issues/2280).** The auditor walks trackings with tolerance-based matching and reports mismatches sorted by absolute delta, and now runs continuously via the `audit:cached_totals` cron. See [[CachedTotalAuditor — Cache Drift Audit System]] for the full system.

Treat the two together: **#2337 stops the bleeding; #2307 reports the existing wound.**

**Second root cause found during #2307:** beyond the cancel/uncancel `update_all` vector this note covers, the eight `recalculate-*` jobs were using `update_column`, which skips `updated_at`. Cache writes left no freshness signal, masking staleness. Fixed by switching to `update_columns`. See [[Gotchas#`update_column` skips `updated_at` — use `update_columns` for cache writes]].

## Action Items
- [x] Revisit PR #2307 — rebased against master (post-#2337), reviewed and **merged 2026-06**, closing #2280.
- [x] Run the auditor in production (or via the `audit:cached_totals` cron) and triage any reported mismatches — first cron run 2026-06-16 found 2 overstating mismatches (trackings `970431`, `970869`); triage in [#2360](https://github.com/csb-ric/pcms/issues/2360). See [[CachedTotalAuditor — Cache Drift Audit System#First production run (2026-06-16)]].
- [ ] Decide whether other `update_all` callsites on trackings need the same after_commit treatment

## Related
- [[PCMS]]
- [[CachedTotalAuditor — Cache Drift Audit System]] — the diagnostic companion (#2307); closes #2280
- [[North Star]]
- [[Calendar Refactor and Drag-Drop Proposal]]
- [[Index]]
