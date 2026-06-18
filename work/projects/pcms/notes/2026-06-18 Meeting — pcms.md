---
date: "2026-06-18"
description: "PCMS Weekly Sync — recap and prep covering 2026-06-11 to 2026-06-18"
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

# PCMS Weekly Sync — 2026-06-18

## Attendees

- [[Jessica Cho]]
- [[Tera Morse]]
- [[Daniel Guettler]]
- [[Yovani Edwards]] _(occasional)_

## Recap

_Window: 2026-06-11 to 2026-06-18._

### New features

- _None this week — a quiet shipping week focused on fixes and monitoring._

### Bug fixes & improvements

- Fixed a rare case where cancelling and then rebooking a reservation could leave an invoice total slightly overstated — these now correct themselves automatically [#2360](https://github.com/csb-ric/pcms/issues/2360).
- The funding source now displays correctly on tracking records that previously showed up blank [#2358](https://github.com/csb-ric/pcms/issues/2358).
- Fixed an issue where certain BPC service requests could not be marked complete [#2357](https://github.com/csb-ric/pcms/issues/2357).

### Resolved this week

- [#2360](https://github.com/csb-ric/pcms/issues/2360) — cached_total drift on trackings 970431, 970869 (first audit alert)
- [#2358](https://github.com/csb-ric/pcms/issues/2358) — Funding Source not showing in tracking
- [#2357](https://github.com/csb-ric/pcms/issues/2357) — BPC Service Request cannot be completed

### Waiting for RFCO review (work already in production for some time)

- See the [RFCO review board](https://github.com/orgs/csb-ric/projects/7/views/1).

### Requires resolution / finalization / clarification or closing

- [#1845](https://github.com/csb-ric/pcms/issues/1845) — RIIFC: not respecting limit 1 per day per person equipment booking between 12pm–5pm
- [#1848](https://github.com/csb-ric/pcms/issues/1848) — Include link to filtered invoice page
- [#1849](https://github.com/csb-ric/pcms/issues/1849) — Kraft about page links do not open in a new page
- [#1851](https://github.com/csb-ric/pcms/issues/1851) — Add link to "Modified Invoice" email pointing to the filtered invoice page
- [#1856](https://github.com/csb-ric/pcms/issues/1856) — Downloading invoices doesn't respect filters
- [#1911](https://github.com/csb-ric/pcms/issues/1911) — Cores with auto approval, when regenerated after 15th, should remain approved
- [#1935](https://github.com/csb-ric/pcms/issues/1935) — Export Core with all settings, users and services
- [#1936](https://github.com/csb-ric/pcms/issues/1936) — Import Core with all settings, users and services
- [#1945](https://github.com/csb-ric/pcms/issues/1945) — Remove all whitespace from invoice number field when entering checks
- [#2043](https://github.com/csb-ric/pcms/issues/2043) — RSMG copier: before importing check if the file is open
- [#2049](https://github.com/csb-ric/pcms/issues/2049) — Upgrade `jsonapi-resources` to > 0.10
- [#2080](https://github.com/csb-ric/pcms/issues/2080) — Invoice isn't flagged for regeneration
- [#2086](https://github.com/csb-ric/pcms/issues/2086) — Error message formatting
- [#2164](https://github.com/csb-ric/pcms/issues/2164) — Restore data-protection functionality
- [#2169](https://github.com/csb-ric/pcms/issues/2169) — `_resend` or manually resending, option to skip report
- [#2170](https://github.com/csb-ric/pcms/issues/2170) — Double click adding fund still exists somewhere
- [#2220](https://github.com/csb-ric/pcms/issues/2220) — Updating setting results in `ActiveModel::ForbiddenAttributesError`
- [#2223](https://github.com/csb-ric/pcms/issues/2223) — Speeding up the External Payment logging Process - BPC
- [#2224](https://github.com/csb-ric/pcms/issues/2224) — P&L Reporting - PeopleSoft to Workday
- [#2225](https://github.com/csb-ric/pcms/issues/2225) — New General Tracking Upload Template
- [#2226](https://github.com/csb-ric/pcms/issues/2226) — Search Feature for Core Services & Equipment
- [#2263](https://github.com/csb-ric/pcms/issues/2263) — BPC Service Request blocked reopening for invoiced records
- [#2272](https://github.com/csb-ric/pcms/issues/2272) — Working Potential Enhancement List
- [#2292](https://github.com/csb-ric/pcms/issues/2292) — Reduce Schedule view for Services if Filtered
- [#2306](https://github.com/csb-ric/pcms/issues/2306) — Editable Document Page Core
- [#2317](https://github.com/csb-ric/pcms/issues/2317) — /cm/checks/edit is 247 queries per row
- [#2331](https://github.com/csb-ric/pcms/issues/2331) — Usage Analytics causing a crash
- [#2333](https://github.com/csb-ric/pcms/issues/2333) — Remove noise from unknown funds
- [#2336](https://github.com/csb-ric/pcms/issues/2336) — Allow splitting an invoice by service-to-grant, not just by percentage
- [#2340](https://github.com/csb-ric/pcms/issues/2340) — Replace string-name link between PricingTier and assignments with a FK
- [#2344](https://github.com/csb-ric/pcms/issues/2344) — Pending Feature - Ragon Flow Cytometry - Schedule Event - Editing Early Completion _(waiting on external resolution)_
- [#2345](https://github.com/csb-ric/pcms/issues/2345) — Equipment Filter on Schedule does not remain when switching calendar day
- [#2346](https://github.com/csb-ric/pcms/issues/2346) — Filter Services View to Selected Services and Equipment
- [#2347](https://github.com/csb-ric/pcms/issues/2347) — Remunc: when SR status changed from completed/cancelled to active, unarchive in RPR
- [#2353](https://github.com/csb-ric/pcms/issues/2353) — Bad grant list
- [#2356](https://github.com/csb-ric/pcms/issues/2356) — Regeneration for change in Fund Number _(in progress — PR #2362 open; see [[Fund-Number Change Regeneration Flag]])_

### Behind-the-scenes work

_Internal improvements with no user-visible change. Kept high-level on purpose._

A continuous monitoring check now runs automatically to catch and correct rare billing-total discrepancies before they reach an invoice, and the underlying components were kept up to date. No action needed from the team.

## Unresolved Questions from Vault Notes

- From [[Equipment and Services Tag Taxonomy]]: Some equipment entries appear to actually be services (e.g. Proposal Assistance, Post-Award Management, Financial Analysis, Overall Project Management, Clinical Trial Invoicing — all "Consultant"). Are these mislabeled in the source, or do we need a tag/flag to distinguish service-type entries living in the equipment model?
- From [[General Upload Template Service Request Sync]]:
  - What does the "change message" look like on the service request — banner, event log entry, email, or all three?
  - Is retraining owned by Finance ([[Tera Morse]] / [[Jessica Cho]] / [[Yovani Edwards]]) or by Eli?
  - Is there a new GitHub issue for this, or does it roll under #2225?
- From [[PCMS Chatbot]]:
  - Where does the chatbot UI live — per-page widget, global modal, dedicated page?
  - Once the SOW is signed, which surface ships first — Ragon (original scope) or broader equipment-search across cores?
- From [[Proposed Feature Prioritization from Finance]]:
  - Workday API access for the Insight Integration is the biggest open dependency ([[Daniel Guettler]] flagged it as the main lift).
  - Do PET and LMM cores have interfacing data, or remain manual entry?

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
