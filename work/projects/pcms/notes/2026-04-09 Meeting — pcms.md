---
date: "2026-04-09"
description: "PCMS Weekly Sync — shipped 6 PRs, scoped Insight vs Workday data sources, confirmed general upload template behavior, Apr 8 focus group recap"
project: pcms
meeting_type: weekly
attendees:
  - Jessica Cho
  - Daniel Guettler
absent:
  - Tera Morse
  - Yovani Edwards
tags:
  - work-note
  - meeting
---

# PCMS Weekly Sync — 2026-04-09

## Attendees

- [[Jessica Cho]]
- [[Daniel Guettler]]
- Eli

**Absent**: [[Tera Morse]] (PTO), [[Yovani Edwards]] (occasional attendee)

## Since Last Meeting

_Window: 2026-04-02 → 2026-04-09._

### Shipped (6 PRs merged)

| # | Title | For |
|---|-------|-----|
| #2289 | `fix(billing): bust browser cache for regenerated invoices` | [[Tera Morse]] (closed #2288) |
| #2285 | `feat(api): add calendar event creation endpoint` | — |
| #2284 | `feat(api): add JSONAPI calendar event creation endpoint` | — |
| #2283 | `fix(funds): fix Create PI modal on fund edit page` | [[Jessica Cho]] (partial fix for #2273) |
| #2282 | `fix(bpc): validate date_collected is within reasonable range` | closed #2279 |
| #2281 | `fix(billing): handle invalid encoding in invoice PDFs` | [[Jessica Cho]] (closed #2271 — see [[Prawn UTF-8 Encoding Bug in Invoice PDFs]]) |

### Closed Without Code

- #2275 Add Project Name to Service Request download — [[Jessica Cho]]
- #2274 Split funding upload question — [[Tera Morse]]
- #2270 Update User Pamphlet — [[Jessica Cho]]

### New on the Plate (Eli)

- #2287 Remove RPR reactivation Honeybadger alerts
- #2286 `Date::Error: invalid date` on `params[:start_date]`
- #2280 Investigate if cached charges are keeping up
- #2277 `NoMethodError: undefined method 'assigned_funds' for nil`

### Stale PRs

- **#2234** `fix(billing): reconcile check payments logged before invoice generation` — open since 2026-02-17 (~7 weeks). Needs testing help from LMM/Jessica/Yovani.

### Unresolved Questions Going In

From [[External Fund PI Field Issues]] (#2273, only partially fixed):
- Can the PI field be unlocked after fund creation?
- Correct format for PI entry on external funds?
- Should external PIs receive the PI Statement with invoices?
- Can blank PI fields be backfilled?
- Default-fund side effect — still happening?

## Discussion

- **General upload template behavior** — Jessica confirmed the Finance team met and decided that the general upload should **update the service request** when processed, with a **change message** surfaced on the SR so users understand what happened. Existing upload users will need to be retrained or at least notified. Split funding in the general upload will be represented with a **percentage** format. See [[General Upload Template Service Request Sync]].
- **Insight Integration scope** — clarified in real time:
  - **Expenses and revenue → Insight.** Insight is now in Digital and the team has been responsive. Jessica will send Daniel the Insight columns PCMS needs; Daniel will request them from the Insight team in parallel with any Workday work.
  - **Internal grant funding info → Workday (optional).** Jessica: "if it's easy, we're totally fine with pulling that... not a huge necessity right now." Cost centers not needed.
  - **Principle**: Workday is source of truth; better to depend on one system than two. Eli will compare Savient → Insight pipeline against Workday to quantify how many fund numbers Insight is actually missing for PCMS before committing.
  - Daniel noted the Insight team is aware of the fund-number gap and working on it — the discrepancy may shrink on its own.
- **Apr 8 focus group** — Jessica and Eli agreed the first focus group went well. Turnout was strong, users "gung ho", lots of good feedback already captured. Session was **not transcribed**; relying on live notes from Finance. See [[Stakeholder Focus Groups for User Feedback]].

## Decisions

- [[001-Insight vs Workday Data Source Scoping]] — **accepted** in this meeting. Splits the Insight Integration line item into Insight (primary, expense/revenue) and Workday (optional, internal funding). Unblocks the expense/revenue path without waiting on Workday API access.
- **General upload template will mutate service requests** (not just record them) — planning-level agreement, see [[General Upload Template Service Request Sync]] for the full behavior spec.

## Action Items

- [ ] [[Jessica Cho]] sends the list of Insight columns PCMS needs to [[Daniel Guettler]]
- [ ] [[Daniel Guettler]] files the column request with the Insight team
- [ ] Eli compares Savient → Insight output against Workday to quantify the missing-fund gap
- [ ] Eli: revisit Workday internal-funding pull once the comparison is done
- [ ] Resolve open UX questions on [[External Fund PI Field Issues]] (#2273) — bring back next week
- [ ] Ask Finance about testing help for stale PR #2234
- [ ] Decide whether future focus groups are recorded or scribed

## Related

- [[PCMS]]
- [[001-Insight vs Workday Data Source Scoping]]
- [[General Upload Template Service Request Sync]]
- [[Proposed Feature Prioritization from Finance]]
- [[Stakeholder Focus Groups for User Feedback]]
- [[External Fund PI Field Issues]]
- [[Workday API Access for Missing Grant Fields]] — CADE's parallel Workday ask
- [[Jessica Cho]]
- [[Daniel Guettler]]
- [[Tera Morse]]
- [[Yovani Edwards]]
