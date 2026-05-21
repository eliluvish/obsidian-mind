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

This fix closes the cancel/uncancel **source** of drift. It does not address rows that may already be stale from prior cancel/uncancel cycles or any other vector that hasn't surfaced yet. That sweep is the job of [PR #2307](https://github.com/csb-ric/pcms/issues/2307) — `feat(trackings): add CachedTotalAuditor` — sitting open since 2026-04-24 on branch `2280-investigate-if-cached-charges-are-keeping-up`. The auditor walks trackings with tolerance-based matching and reports mismatches sorted by absolute delta. It is the diagnostic companion to this fix.

Treat the two together: **#2337 stops the bleeding; #2307 reports the existing wound.**

## Action Items
- [ ] Revisit PR #2307 next week — rebase against current master (now that #2337 is in), get it reviewed and merged. Deferred from this week.
- [ ] Once #2307 is merged, run the auditor in production and triage any reported mismatches
- [ ] Decide whether other `update_all` callsites on trackings need the same after_commit treatment

## Related
- [[PCMS]]
- [[North Star]]
- [[Calendar Refactor and Drag-Drop Proposal]]
- [[Index]]
