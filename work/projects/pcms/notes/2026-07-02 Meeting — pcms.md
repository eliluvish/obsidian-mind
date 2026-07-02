---
date: "2026-07-02"
description: "PCMS Weekly Sync — recap and prep covering 2026-06-25 to 2026-07-02"
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

# PCMS Weekly Sync — 2026-07-02

## Attendees

- [[Jessica Cho]]
- [[Tera Morse]]
- [[Daniel Guettler]]
- [[Yovani Edwards]] (occasional)

## Recap

_Window: 2026-06-25 → 2026-07-02._

### New features

- None this week - focus was on fixes and internal cleanup.

### Bug fixes & improvements

- The Usage Analytics page no longer crashes on longer date ranges - it now loads year-long views for large cores that previously timed out [[#2331](https://github.com/csb-ric/pcms/issues/2331)].
- The check / payment entry page is dramatically faster to open, especially for checks covering many payments [[#2317](https://github.com/csb-ric/pcms/issues/2317)].
- Saving changes on the admin settings page works again - it was throwing an error before [[#2220](https://github.com/csb-ric/pcms/issues/2220)].

### Resolved this week

- [#2331](https://github.com/csb-ric/pcms/issues/2331) — Usage Analytics causing a crash (closed by @eliluvish)
- [#2317](https://github.com/csb-ric/pcms/issues/2317) — /cm/checks/edit is 247 queries per row (closed by @eliluvish)
- [#2220](https://github.com/csb-ric/pcms/issues/2220) — Updating setting results in ForbiddenAttributesError (closed by @eliluvish)
- [#2333](https://github.com/csb-ric/pcms/issues/2333) — Remove noise from unknown funds (closed by @eliluvish, internal)
- [#2374](https://github.com/csb-ric/pcms/issues/2374) / [#2375](https://github.com/csb-ric/pcms/issues/2375) / [#2376](https://github.com/csb-ric/pcms/issues/2376) — retired-core cleanup (closed by @eliluvish, internal)
- [#2377](https://github.com/csb-ric/pcms/issues/2377) — billing-figure precision follow-up (closed by @eliluvish, internal)

_Dropped as not planned (no work shipped): [#2356](https://github.com/csb-ric/pcms/issues/2356) Fund-number regeneration (closed by @jcho11mgborg) and [#2080](https://github.com/csb-ric/pcms/issues/2080) invoice regeneration flag (closed by @mpivov)._

### Waiting for RFCO review (work already in production for some time)

See the [RFCO review board](https://github.com/orgs/csb-ric/projects/7/views/1).

### Requires resolution / finalization / clarification or closing

- [#1845](https://github.com/csb-ric/pcms/issues/1845) — RIIFC: not respecting limit of 1 per day per person equipment booking between 12pm-5pm
- [#1848](https://github.com/csb-ric/pcms/issues/1848) — Include link to filtered invoice page
- [#1849](https://github.com/csb-ric/pcms/issues/1849) — Kraft about-page links do not open in a new page
- [#1851](https://github.com/csb-ric/pcms/issues/1851) — Add link to "Modified Invoice" email pointing to the filtered invoice page
- [#1856](https://github.com/csb-ric/pcms/issues/1856) — Downloading invoices doesn't respect filters
- [#1911](https://github.com/csb-ric/pcms/issues/1911) — Cores with auto-approval, when regenerated after the 15th, should remain approved
- [#1935](https://github.com/csb-ric/pcms/issues/1935) — Export core with all settings, users and services
- [#1936](https://github.com/csb-ric/pcms/issues/1936) — Import core with all settings, users and services
- [#1945](https://github.com/csb-ric/pcms/issues/1945) — Remove all whitespace from invoice-number field when entering checks
- [#2049](https://github.com/csb-ric/pcms/issues/2049) — Upgrade jsonapi-resources to > 0.10 (tech debt, internal)
- [#2164](https://github.com/csb-ric/pcms/issues/2164) — Restore data-protection functionality
- [#2169](https://github.com/csb-ric/pcms/issues/2169) — Option to skip report when resending / manually resending
- [#2170](https://github.com/csb-ric/pcms/issues/2170) — Double-click adding fund still exists somewhere
- [#2306](https://github.com/csb-ric/pcms/issues/2306) — Editable Document Page Core (waiting on external resolution)
- [#2336](https://github.com/csb-ric/pcms/issues/2336) — Allow splitting an invoice by service-to-grant, not just by percentage
- [#2344](https://github.com/csb-ric/pcms/issues/2344) — Ragon Flow Cytometry: schedule-event editing on early completion (waiting on external resolution)

### Behind-the-scenes work

_Internal improvements with no user-visible change. Kept high-level on purpose._

Cleared out several retired cores and their leftover customizations, and started building a repeatable way to retire a core cleanly in the future. Improved how billing figures are stored and monitored so totals stay precise, quieted some noisy internal alerts, and modernized the development setup and test suite. None of this changes anything you'll see in the app day to day.

## Unresolved Questions from Vault Notes

- **[[Equipment and Services Tag Taxonomy]]** — Some equipment entries appear to actually be services (Proposal Assistance, Post-Award Management, Financial Analysis, Overall Project Management, Clinical Trial Invoicing - all "Consultant"). Are these mislabeled at the source, or do we need a flag to distinguish service-type entries living in the equipment model?
- **[[PCMS Chatbot]]** — Where does the chatbot UI live (per-page widget, global modal, dedicated page)? How do user + authorization context flow into tool calls? Does capability structure need its own data modeling, or can it ride the equipment/services tag taxonomy? Once the SOW is signed, which surface ships first - Ragon or a broader cross-core equipment search?
- **[[General Upload Template Service Request Sync]]** (backburner) — What does the "change message" on the service request look like (banner, event-log entry, email, all three)? Is retraining owned by Finance or by Eli? New GitHub issue, or does it roll under #2225?

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
