---
date: "2026-05-21"
description: "PCMS Weekly Sync — recap and prep covering 2026-05-14 → 2026-05-21"
project: "pcms"
meeting_type: weekly
attendees:
  - Jessica Cho
  - Tera Morse
  - Daniel Guettler
  - Yovani Edwards
tags:
  - work-note
  - meeting
---

# PCMS Weekly Sync — 2026-05-21

## Attendees

- [[Jessica Cho]]
- [[Tera Morse]]
- [[Daniel Guettler]]
- [[Yovani Edwards]] (occasional)

## Recap

_Window: 2026-05-14 → 2026-05-21._

### New features

- The calendar's schedule filter now lets you narrow the week view to a specific piece of equipment — the same way you can already filter by service ([#2291](https://github.com/csb-ric/pcms/issues/2291)).

### Bug fixes & improvements

- Renaming a pricing tier now updates the matching fund-specific pricing tier automatically — previously the fund-level name could fall out of sync ([#2339](https://github.com/csb-ric/pcms/issues/2339)).
- Cached totals on a service request now refresh correctly after a cancel or un-cancel, so the displayed total stays accurate ([#2337](https://github.com/csb-ric/pcms/pull/2337)).

### Resolved this week

- [#2241](https://github.com/csb-ric/pcms/issues/2241) — Change source of internal funding information from Workday instead of Insight (closed by [[Jessica Cho]])
- [#2342](https://github.com/csb-ric/pcms/issues/2342) — Cannot Find CCP Admin and Tech User Group (closed by [[Jessica Cho]])
- [#2090](https://github.com/csb-ric/pcms/issues/2090) — Investigate adding a search page that shows both equipment and services (closed; superseded by the Core Browse UI design work)

### Waiting for RFCO review (work already in production for some time)

- [RFCO review board](https://github.com/orgs/csb-ric/projects/7/views/1)

### Requires resolution / finalization / clarification or closing

- [#1845](https://github.com/csb-ric/pcms/issues/1845) — RIIFC: not respecting limit 1 per day per person equipment booking between 12pm–5pm ([[Daniel Guettler]])
- [#1848](https://github.com/csb-ric/pcms/issues/1848) — Include link to filtered invoice page ([[Daniel Guettler]])
- [#1849](https://github.com/csb-ric/pcms/issues/1849) — Kraft about page links do not open in a new page ([[Daniel Guettler]])
- [#1851](https://github.com/csb-ric/pcms/issues/1851) — Add link to "Modified Invoice" email pointing to the filtered invoice page ([[Daniel Guettler]])
- [#1856](https://github.com/csb-ric/pcms/issues/1856) — Downloading invoices doesn't respect filters ([[Daniel Guettler]])
- [#1911](https://github.com/csb-ric/pcms/issues/1911) — Cores with auto approval, when regenerated after 15th, should remain approved
- [#1935](https://github.com/csb-ric/pcms/issues/1935) — Export Core with all settings, users and services ([[Daniel Guettler]])
- [#1936](https://github.com/csb-ric/pcms/issues/1936) — Import Core with all settings, users and services ([[Daniel Guettler]])
- [#1945](https://github.com/csb-ric/pcms/issues/1945) — Remove all whitespace from invoice number field when entering checks
- [#2043](https://github.com/csb-ric/pcms/issues/2043) — RSMG copier: before importing check if the file is open
- [#2049](https://github.com/csb-ric/pcms/issues/2049) — Upgrade `jsonapi-resources` to > 0.10 (Tech Debt)
- [#2080](https://github.com/csb-ric/pcms/issues/2080) — Invoice isn't flagged for regeneration
- [#2086](https://github.com/csb-ric/pcms/issues/2086) — Error message formatting ([[Daniel Guettler]])
- [#2164](https://github.com/csb-ric/pcms/issues/2164) — Restore data-protection functionality ([[Daniel Guettler]])
- [#2169](https://github.com/csb-ric/pcms/issues/2169) — `_resend` or manually resending, option to skip report
- [#2170](https://github.com/csb-ric/pcms/issues/2170) — Double click adding fund still exists somewhere
- [#2220](https://github.com/csb-ric/pcms/issues/2220) — Updating setting results in `ActiveModel::ForbiddenAttributesError`
- [#2223](https://github.com/csb-ric/pcms/issues/2223) — Speeding up the External Payment logging Process - BPC
- [#2224](https://github.com/csb-ric/pcms/issues/2224) — P&L Reporting - PeopleSoft to Workday
- [#2225](https://github.com/csb-ric/pcms/issues/2225) — New General Tracking Upload Template
- [#2226](https://github.com/csb-ric/pcms/issues/2226) — Search Feature for Core Services & Equipment
- [#2263](https://github.com/csb-ric/pcms/issues/2263) — BPC Service Request blocked reopening for invoiced records
- [#2267](https://github.com/csb-ric/pcms/issues/2267) — Download of Services on Import Tasks Upload [DRAFT]
- [#2272](https://github.com/csb-ric/pcms/issues/2272) — Working Potential Enhancement List
- [#2280](https://github.com/csb-ric/pcms/issues/2280) — Investigate if cached charges are keeping up (PR [#2307](https://github.com/csb-ric/pcms/pull/2307) pending merge)
- [#2292](https://github.com/csb-ric/pcms/issues/2292) — Reduce Schedule view for Services if Filtered
- [#2306](https://github.com/csb-ric/pcms/issues/2306) — Editable Document Page Core
- [#2317](https://github.com/csb-ric/pcms/issues/2317) — `/cm/checks/edit` is 247 queries per row
- [#2331](https://github.com/csb-ric/pcms/issues/2331) — Usage Analytics causing a crash
- [#2333](https://github.com/csb-ric/pcms/issues/2333) — Remove noise from unknown funds
- [#2336](https://github.com/csb-ric/pcms/issues/2336) — Allow splitting an invoice by service-to-grant, not just by percentage

### Behind-the-scenes work

_Internal improvements with no user-visible change. Kept high-level on purpose._

Light week on internal-only work — most of what shipped landed in the user-facing buckets above. Continued investigation on the cached-charges accuracy work (a pull request is staged and awaiting merge), and ongoing design work on the Core Browse UI and the structured About-page template.

## Unresolved Questions from Vault Notes

From [[PCMS Chatbot]]:

- Where does the chatbot UI live in PCMS? Per-page contextual widget, global modal, dedicated page?
- Where do `current_user` and authorization context flow through to tool calls?
- Does spec/capability structure need its own data modeling pass, or can it ride on the equipment/services tag taxonomy work?

From [[Equipment and Services Tag Taxonomy]]:

- Some equipment entries appear to actually be services — how should the tag taxonomy handle these? Examples: Proposal Assistance / Development, Post-Award Management, Financial Analysis, Overall Project Management, Clinical Trial Invoicing (all "Consultant"). Are these mislabeled in the source, or do we need a tag/flag to distinguish service-type entries that live in the equipment model?

From [[General Upload Template Service Request Sync]]:

- What does the "change message" look like on the service request — a banner, an event log entry, an email notification, or all three?
- Is the retraining owned by Finance ([[Tera Morse]] / [[Jessica Cho]] / [[Yovani Edwards]]) or by Eli?
- Is there a new GitHub issue for this, or does it roll under [#2225](https://github.com/csb-ric/pcms/issues/2225) "New General Tracking Upload Template"?

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
- [[Calendar Refactor and Drag-Drop Proposal]]
- [[Core Browse UI Design]]
- [[002-About Page as Auto-Populated Standardized Template]]
