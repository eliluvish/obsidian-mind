---
date: "2026-04-30"
description: "PCMS Weekly Sync — recap and prep covering 2026-04-23 → 2026-04-30"
project: "pcms"
meeting_type: weekly
attendees:
  - "Jessica Cho"
  - "Tera Morse"
  - "Daniel Guettler"
  - "Yovani Edwards"
tags:
  - work-note
  - meeting
---

# PCMS Weekly Sync — 2026-04-30

## Attendees

- [[Jessica Cho]]
- [[Tera Morse]]
- [[Daniel Guettler]]
- [[Yovani Edwards]] _(occasional)_

## Since Last Meeting

_Auto-filled by `/meeting-prep`. Window: 2026-04-23 → 2026-04-30._

### Shipped

| # | Title | For |
|---|-------|-----|
| [#2322](https://github.com/csb-ric/pcms/pull/2322) | fix(admin/invoices): surface validation errors on bulk update | Eli / closes #2309 |
| [#2319](https://github.com/csb-ric/pcms/pull/2319) | fix(billing): surface validation errors on invoice update | [[Tera Morse]] / [[Jessica Cho]] / closes #2316 |
| [#2318](https://github.com/csb-ric/pcms/pull/2318) | Fix BPC External Payments fund_number corruption | [[Tera Morse]] / closes #2313 |
| [#2314](https://github.com/csb-ric/pcms/pull/2314) | feat(equipment): add capabilities tag system | Ragon chatbot groundwork |
| [#2312](https://github.com/csb-ric/pcms/pull/2312) | Add multi modality | Ragon chatbot groundwork |
| [#2311](https://github.com/csb-ric/pcms/pull/2311) | Add support fields to equipment | Ragon chatbot groundwork |
| [#2310](https://github.com/csb-ric/pcms/pull/2310) | build(docker): upgrade MySQL to 8.0.44 | Infra |

### Closed Without Code

- [#2320](https://github.com/csb-ric/pcms/issues/2320) — BillingInvoice: relocating trackings between invoices doesn't recompute source amount columns
- [#2315](https://github.com/csb-ric/pcms/issues/2315) — [Bug]: Unable to reconcile invoice as paid on AR page ([[Tera Morse]])
- [#2298](https://github.com/csb-ric/pcms/issues/2298) — Tracking: editing an event after downloading a report re-downloads on save/cancel
- [#2290](https://github.com/csb-ric/pcms/issues/2290) — [Feature] PIs to be able to remove an account from a fund they are PI for ([[Jessica Cho]])
- [#2252](https://github.com/csb-ric/pcms/issues/2252) — Tango import reporting
- [#1924](https://github.com/csb-ric/pcms/issues/1924) — Investigate charges vs. cached_charges

### New Bugs / Issues

| # | Title | Reporter | Type |
|---|-------|----------|------|
| [#2323](https://github.com/csb-ric/pcms/issues/2323) | `[ActionController::UrlGenerationError]` No route matches `{id: nil}` in my/funds#update | Eli | bug |
| [#2317](https://github.com/csb-ric/pcms/issues/2317) | `/cm/checks/edit` is 247 queries per row | Eli | perf |
| [#2308](https://github.com/csb-ric/pcms/issues/2308) | [Bug]: Cannot block event creation for Saturday without blocking all days | [[Jessica Cho]] | bug |
| [#2306](https://github.com/csb-ric/pcms/issues/2306) | [Feature] Editable Document Page Core | [[Jessica Cho]] | feature |

### Open Items Waiting on Stakeholders

**[[Jessica Cho]] + [[Tera Morse]] + [[Yovani Edwards]]**
- [#2272](https://github.com/csb-ric/pcms/issues/2272) — Working Potential Enhancement List

**[[Jessica Cho]] + [[Daniel Guettler]]**
- [#2263](https://github.com/csb-ric/pcms/issues/2263) — [Question]: BPC Service Request blocked reopening for invoiced records

**[[Daniel Guettler]]**
- [#1936](https://github.com/csb-ric/pcms/issues/1936) — Import Core with all settings, users and services
- [#1935](https://github.com/csb-ric/pcms/issues/1935) — Export Core with all settings, users and services

**[[Yovani Edwards]]**
- [#2292](https://github.com/csb-ric/pcms/issues/2292) — [Feature] Reduce Schedule view for Services if Filtered
- [#2291](https://github.com/csb-ric/pcms/issues/2291) — [Feature] Block Off in Calendar for Filtered Week View
- [#2241](https://github.com/csb-ric/pcms/issues/2241) — Change source of internal funding information from Workday instead of Insight

### Stale PRs

- [#2307](https://github.com/csb-ric/pcms/pull/2307) — feat(trackings): add CachedTotalAuditor service (#2280) — opened 2026-04-24, not yet reviewed

### Unresolved Questions from Vault Notes

> [!todo] From [[Equipment and Services Tag Taxonomy]] — **ask today**
> Some equipment entries appear to actually be services (e.g., "Proposal Assistance / Proposal Development — Consultant", "Post-Award Management — Consultant"). How should the tag taxonomy handle these? Are they mislabeled in the source, or do we need a tag/flag to distinguish service-type entries living in the equipment model?

From [[Ragon Equipment Chatbot]]:
- Where does the chatbot UI live in PCMS? Per-page widget, global modal, or dedicated page?
- How does `current_user` and authorization context flow through to tool calls?
- Does spec/capability structure need its own data modeling pass, or can it ride on the tag taxonomy work?

From [[General Upload Template Service Request Sync]] _(backburner)_:
- What does the "change message" look like on service requests — banner, event log, email, or all three?
- Is retraining on upload behavior owned by Finance (Tera/Jessica/Yovani) or by Eli?
- Is there a new GitHub issue for this, or does it roll under #2225?

Also: Is [#2080](https://github.com/csb-ric/pcms/issues/2080) still needed?

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
- [[Ragon Equipment Chatbot]]
- [[Equipment and Services Tag Taxonomy]]
