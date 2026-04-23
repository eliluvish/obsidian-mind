---
date: "2026-04-23"
description: "PCMS Weekly Sync — recap and prep covering 2026-04-16 to 2026-04-23"
project: pcms
meeting_type: weekly
attendees:
  - "Jessica Cho"
  - "Tera Morse"
  - "Daniel Guettler"
  - "Yovani Edwards (occasional)"
tags:
  - work-note
  - meeting
---

# PCMS Weekly Sync — 2026-04-23

## Attendees

- [[Jessica Cho]]
- [[Tera Morse]]
- [[Daniel Guettler]]
- [[Yovani Edwards]] _(occasional)_

## Since Last Meeting

_Auto-filled by `/meeting-prep`. Window: 2026-04-16 → 2026-04-23._

### Shipped

| # | Title | For |
|---|-------|-----|
| [#2305](https://github.com/csb-ric/pcms/pull/2305) | feat(pi/funds): PI-managed fund account assignments | #2290 (Yovani) |
| [#2304](https://github.com/csb-ric/pcms/pull/2304) | fix(check): recompute AR on check_payment delete | #2296 (Tera) |
| [#2303](https://github.com/csb-ric/pcms/pull/2303) | fix(notifications): race on lazy notification_preference creation | #2297 |
| [#2302](https://github.com/csb-ric/pcms/pull/2302) | fix(wiki): add missing wiki_example_image asset | #2300 |
| [#2301](https://github.com/csb-ric/pcms/pull/2301) | fix(billing): render preview PDFs inline | #2299 |

### Closed Without Code

- [#2294](https://github.com/csb-ric/pcms/issues/2294) — [Bug]: Cannot Delete or Update a Funding start date on Service Request _(Jessica)_
- [#2287](https://github.com/csb-ric/pcms/issues/2287) — Remove RPR reactivation Honeybadger alerts

### New Bugs / Issues

- [#2298](https://github.com/csb-ric/pcms/issues/2298) — **[Bug] Tracking: editing an event after downloading a report re-downloads on save/cancel and leaves edit modal stuck** _(still open)_

### Open Items Waiting on Stakeholders

**Jessica Cho + Tera Morse + Yovani Edwards**
- [#2272](https://github.com/csb-ric/pcms/issues/2272) — Working Potential Enhancement List _(all three assigned)_

**Jessica Cho + Daniel Guettler**
- [#2263](https://github.com/csb-ric/pcms/issues/2263) — [Question]: BPC Service Request blocked reopening for invoiced records

**Yovani Edwards**
- [#2292](https://github.com/csb-ric/pcms/issues/2292) — [Feature] Reduce Schedule view for Services if Filtered
- [#2291](https://github.com/csb-ric/pcms/issues/2291) — [Feature] Block Off in Calendar for Filtered Week View
- [#2241](https://github.com/csb-ric/pcms/issues/2241) — Change source of internal funding from Workday instead of Insight _(Feb, stale)_

**Daniel Guettler**
- [#1936](https://github.com/csb-ric/pcms/issues/1936) — Import Core with all settings, users and services _(2025, very stale)_
- [#1935](https://github.com/csb-ric/pcms/issues/1935) — Export Core with all settings, users and services _(2025, very stale)_

### Stale PRs

_No open PRs in the queue._

### Unresolved Questions from Vault Notes

**From [[General Upload Template Service Request Sync]]:**
- What does the "change message" look like on the service request — a banner, an event log entry, an email notification, or all three?
- Is the retraining owned by Finance (Tera / Jessica / Yovani) or by Eli?
- Is there a new GitHub issue for this, or does it roll under #2225 "New General Tracking Upload Template"?

**From [[External Fund PI Field Issues]]:**
- Can the PI field be edited/unlocked after fund creation?
- If not, do users need to create a new fund? What's the workaround?
- What's the correct PI entry format for external funds?
- Can blank PI fields be backfilled?

## Summary for Stakeholders

This week we shipped three updates:

- **PI-managed fund account assignments** — PIs can now manage account assignments on their own funds directly.
- **Invoice preview fix** — Invoice PDFs now open inline in the browser instead of automatically downloading, making it easier to review before printing or saving.
- **Accounts receivable recalculation fix** — Deleting a check payment now correctly updates the AR balance on the core page. Previously, deleted entries were still pulling into the AR total.

## Discussion

-

## Decisions

-

## Action Items

- [ ]

## Related

- [[PCMS]]
- [[Jessica Cho]]
- [[Tera Morse]]
- [[Daniel Guettler]]
- [[Yovani Edwards]]
- [[General Upload Template Service Request Sync]]
- [[External Fund PI Field Issues]]
- [[Proposed Feature Prioritization from Finance]]
