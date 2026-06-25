---
date: "2026-06-25"
description: "PCMS Weekly Sync — recap and prep covering 2026-06-18 to 2026-06-25"
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

# PCMS Weekly Sync — 2026-06-25

## Attendees

- [[Jessica Cho]]
- [[Tera Morse]] (goes by Sarah)
- [[Daniel Guettler]]
- [[Yovani Edwards]] (occasional)

## Recap

_Window: 2026-06-18 to 2026-06-25._

### New features

- The schedule view can now be filtered by service and equipment. Filters apply instantly without reloading the page, and your selection stays active as you navigate between weeks. [[#2345](https://github.com/csb-ric/pcms/issues/2345), [#2346](https://github.com/csb-ric/pcms/issues/2346), [#2292](https://github.com/csb-ric/pcms/issues/2292)]

### Bug fixes & improvements

- When a calendar event is moved to a new time, the slot it originally occupied is now properly freed up for others to book.
- Service requests that are reactivated from completed or cancelled status now automatically reinstate the linked study payment record. [[#2347](https://github.com/csb-ric/pcms/issues/2347)]
- Fixed an issue where the grants list was displaying incorrect data. [[#2353](https://github.com/csb-ric/pcms/issues/2353)]
- Addressed a security issue where service requests could be linked to the wrong account when submitted through public forms. [[#2372](https://github.com/csb-ric/pcms/pull/2372)]

### Resolved this week

- [#2347](https://github.com/csb-ric/pcms/issues/2347) — Remunc: unarchive RPR study when SR reactivated from completed/cancelled
- [#2346](https://github.com/csb-ric/pcms/issues/2346) — Filter Services View to Selected Services and Equipment (@jcho11mgborg)
- [#2345](https://github.com/csb-ric/pcms/issues/2345) — Equipment Filter on Schedule does not remain when switching calendar day (@jcho11mgborg)
- [#2353](https://github.com/csb-ric/pcms/issues/2353) — Bad grant list
- [#2292](https://github.com/csb-ric/pcms/issues/2292) — Reduce Schedule view for Services if Filtered (@jcho11mgborg)
- [#2272](https://github.com/csb-ric/pcms/issues/2272) — Working Potential Enhancement List (@jcho11mgborg)
- [#2263](https://github.com/csb-ric/pcms/issues/2263) — BPC Service Request blocked reopening for invoiced records (@jcho11mgborg)
- [#2226](https://github.com/csb-ric/pcms/issues/2226) — Search Feature for Core Services & Equipment (@jcho11mgborg)
- [#2225](https://github.com/csb-ric/pcms/issues/2225) — New General Tracking Upload Template (@jcho11mgborg)
- [#2224](https://github.com/csb-ric/pcms/issues/2224) — P&L Reporting - PeopleSoft to Workday (@jcho11mgborg)
- [#2223](https://github.com/csb-ric/pcms/issues/2223) — Speeding up the External Payment logging Process - BPC (@jcho11mgborg)
- [#2086](https://github.com/csb-ric/pcms/issues/2086) — Error message formatting (@dguettler)
- [#2043](https://github.com/csb-ric/pcms/issues/2043) — RSMG copier: check if file is open before importing

### Waiting for RFCO review (work already in production for some time)

See the [RFCO project board](https://github.com/orgs/csb-ric/projects/7/views/1) for the full list.

### Requires resolution / finalization / clarification or closing

- [#2356](https://github.com/csb-ric/pcms/issues/2356) — [Feature] Regeneration for change in Fund Number **[PR #2362 in review]**
- [#2344](https://github.com/csb-ric/pcms/issues/2344) — Pending Feature - Ragon Flow Cytometry - Schedule Event - Editing Early Completion [Waiting on external resolution]
- [#2336](https://github.com/csb-ric/pcms/issues/2336) — Allow splitting an invoice by service-to-grant, not just by percentage
- [#2333](https://github.com/csb-ric/pcms/issues/2333) — Remove noise from unknown funds
- [#2331](https://github.com/csb-ric/pcms/issues/2331) — [Bug]: Usage Analytics causing a crash
- [#2317](https://github.com/csb-ric/pcms/issues/2317) — /cm/checks/edit is 247 queries per row
- [#2306](https://github.com/csb-ric/pcms/issues/2306) — [Feature] Editable Document Page Core [Waiting on external resolution]
- [#2220](https://github.com/csb-ric/pcms/issues/2220) — Updating setting results in ActiveModel::ForbiddenAttributesError
- [#2170](https://github.com/csb-ric/pcms/issues/2170) — Double click adding fund still exists somewhere
- [#2169](https://github.com/csb-ric/pcms/issues/2169) — `_resend` or manually resending, option to skip report
- [#2164](https://github.com/csb-ric/pcms/issues/2164) — Restore data-protection functionality
- [#2080](https://github.com/csb-ric/pcms/issues/2080) — Invoice isn't flagged for regeneration ⚠️ _ask: do we still need this?_
- [#2049](https://github.com/csb-ric/pcms/issues/2049) — Upgrade jsonapi-resources to > 0.10
- [#1945](https://github.com/csb-ric/pcms/issues/1945) — Remove all whitespace from invoice number field when entering checks
- [#1936](https://github.com/csb-ric/pcms/issues/1936) — Import Core with all settings, users and services
- [#1935](https://github.com/csb-ric/pcms/issues/1935) — Export Core with all settings, users and services
- [#1911](https://github.com/csb-ric/pcms/issues/1911) — Cores with auto approval, when regenerated after 15th, should remain approved
- [#1856](https://github.com/csb-ric/pcms/issues/1856) — Downloading invoices doesn't respect filters
- [#1851](https://github.com/csb-ric/pcms/issues/1851) — Add link to "Modified Invoice" email pointing to the filtered invoice page
- [#1849](https://github.com/csb-ric/pcms/issues/1849) — Kraft about page links do not open in a new page
- [#1848](https://github.com/csb-ric/pcms/issues/1848) — Include link to filtered invoice page
- [#1845](https://github.com/csb-ric/pcms/issues/1845) — RIIFC: not respecting limit 1 per day per person equipment booking between 12pm-5pm

### Behind-the-scenes work

_Internal improvements with no user-visible change. Kept high-level on purpose._

The team completed a major platform upgrade this week, bringing the application to the latest version of Rails. This work was backed by a large expansion of automated testing across all areas of the app — which is what made the upgrade safe to ship. Several internal code quality improvements and a security hardening pass also landed as part of the same push.

## Unresolved Questions from Vault Notes

- From [[General Upload Template Service Request Sync]]: When an upload modifies a service request, what should the change notification look like — a banner, a log entry, an email, or all three? Is user retraining on the new upload flow owned by Finance or by Eli?
- From [[Equipment and Services Tag Taxonomy]]: Some equipment entries appear to actually be services (e.g., Proposal Assistance, Post-Award Management — Consultant). Are these mislabeled in the source, or do we need a flag in the taxonomy to distinguish them?
- From [[PCMS Chatbot]]: Once the SOW is accepted, which surface ships first — Ragon (original scope) or broader equipment search across cores? Where does the chatbot UI live — per-page widget, global modal, or dedicated page?

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
- [[Index]]
