---
date: "2026-05-14"
description: "PCMS Weekly Sync — recap and prep covering 2026-05-07 → 2026-05-14"
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

# PCMS Weekly Sync — 2026-05-14

## Attendees

- [[Jessica Cho]]
- [[Tera Morse]]
- [[Daniel Guettler]]
- [[Yovani Edwards]] _(occasional)_

## Recap Sent to Client

_Sent 2026-05-14 ahead of the sync. Window: 2026-05-07 → 2026-05-14._

### Shipped this week

- [#2334](https://github.com/csb-ric/pcms/pull/2334) — `fix(billing): encode fund text fields for Windows-1252 PDF render` — resolves [#2332](https://github.com/csb-ric/pcms/issues/2332) (Prawn BPC UTF-8 invoice bug)

### Resolved this week

- [#2335](https://github.com/csb-ric/pcms/issues/2335) — Reactivate BPC-26-JT-1390 — closed
- [#2330](https://github.com/csb-ric/pcms/issues/2330) — PI Statements for CRMFCC not being sent — closed

### Waiting for RFCO review (work already in production for some time)

- 8 items on the [RFCO review board](https://github.com/orgs/csb-ric/projects/7/views/1)

### Requires resolution / finalization / clarification or closing

- [#2263](https://github.com/csb-ric/pcms/issues/2263) — `[Question]: BPC Service Request blocked reopening for invoiced records`
- [#2272](https://github.com/csb-ric/pcms/issues/2272) — Working Potential Enhancement List
- [#2267](https://github.com/csb-ric/pcms/issues/2267) — `[Feature] Download of Services on Import Tasks Upload [DRAFT]`
- [#2226](https://github.com/csb-ric/pcms/issues/2226) — Search Feature for Core Services & Equipment
- [#2225](https://github.com/csb-ric/pcms/issues/2225) — New General Tracking Upload Template
- [#2224](https://github.com/csb-ric/pcms/issues/2224) — P&L Reporting — PeopleSoft to Workday
- [#2223](https://github.com/csb-ric/pcms/issues/2223) — Speeding up the External Payment logging Process — BPC
- [#2080](https://github.com/csb-ric/pcms/issues/2080) — Invoice isn't flagged for regeneration

## Unresolved Questions from Vault Notes

- **[[Equipment and Services Tag Taxonomy]]** — Some equipment entries appear to be services (Proposal Assistance, Post-Award Management, Financial Analysis, Overall Project Management, Clinical Trial Invoicing — all "Consultant"). Mislabeled in source, or need a tag/flag to distinguish service-type entries living in the equipment model?
- **[[General Upload Template Service Request Sync]]** _(backburner)_ — What does the "change message" look like on the SR (banner / event log / email)? Is retraining owned by Finance or Eli? New issue or rolls under #2225?
- **[[Ragon Equipment Chatbot]]** — Where does the chatbot UI live (per-page widget / global modal / dedicated page)? How does `current_user` flow through to tool calls? Does spec/capability structure need its own modeling pass or can it ride on the tag taxonomy work?

## Discussion

-

## Decisions

-

## Action Items

- [ ]

## Related

- [[PCMS]]
- [[2026-04-30 Meeting — pcms]] _(previous sync)_
