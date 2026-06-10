---
date: "2026-06-04"
description: "PCMS Weekly Sync — recap and prep covering May 28 – Jun 4, 2026"
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

# PCMS Weekly Sync — 2026-06-04

## Attendees

- [[Jessica Cho]]
- [[Tera Morse]]
- [[Daniel Guettler]]
- [[Yovani Edwards]] _(occasional)_

## Recap

_Window: May 28 – Jun 4, 2026._

### New features

- _None this week — the week's work was fixes and behind-the-scenes billing-accuracy work._

### Bug fixes & improvements

- A user with several outstanding invoices now gets **one combined past-due reminder** instead of a separate email for each invoice [#2350](https://github.com/csb-ric/pcms/issues/2350)
- Fixed a case where a BPC invoice would not regenerate correctly [#2351](https://github.com/csb-ric/pcms/issues/2351)
- Resolved an error that blocked a tech from opening the service request page [#2343](https://github.com/csb-ric/pcms/issues/2343)

### Resolved this week

- [#2351](https://github.com/csb-ric/pcms/issues/2351) — BPC invoice not regenerating _(reported by Tera)_
- [#2350](https://github.com/csb-ric/pcms/issues/2350) — outstanding invoices not aggregating by user _(reported by Jessica)_
- [#2343](https://github.com/csb-ric/pcms/issues/2343) — tech cannot access service request page _(reported by Jessica)_
- [#2349](https://github.com/csb-ric/pcms/issues/2349) — import RSMG copier files since Feb 2026
- [#2348](https://github.com/csb-ric/pcms/issues/2348) — RSMG importer files missing from share
- [#2280](https://github.com/csb-ric/pcms/issues/2280) — confirmed cached billing charges are accurate (now monitored continuously)

### Waiting for RFCO review (work already in production for some time)

See the [RFCO review board](https://github.com/orgs/csb-ric/projects/7/views/1).

### Requires resolution / finalization / clarification or closing

- [#1845](https://github.com/csb-ric/pcms/issues/1845) — RIIFC: not respecting limit of 1 per day per person equipment booking between 12pm–5pm
- [#1848](https://github.com/csb-ric/pcms/issues/1848) — include link to filtered invoice page
- [#1849](https://github.com/csb-ric/pcms/issues/1849) — Kraft about-page links do not open in a new page
- [#1851](https://github.com/csb-ric/pcms/issues/1851) — add link to "Modified Invoice" email pointing to the filtered invoice page
- [#1856](https://github.com/csb-ric/pcms/issues/1856) — downloading invoices doesn't respect filters
- [#1911](https://github.com/csb-ric/pcms/issues/1911) — cores with auto-approval, when regenerated after the 15th, should remain approved
- [#1935](https://github.com/csb-ric/pcms/issues/1935) — export core with all settings, users and services
- [#1936](https://github.com/csb-ric/pcms/issues/1936) — import core with all settings, users and services
- [#1945](https://github.com/csb-ric/pcms/issues/1945) — remove all whitespace from invoice number field when entering checks
- [#2043](https://github.com/csb-ric/pcms/issues/2043) — RSMG copier: before importing, check if the file is open
- [#2049](https://github.com/csb-ric/pcms/issues/2049) — upgrade jsonapi-resources to > 0.10 _(tech debt)_
- [#2080](https://github.com/csb-ric/pcms/issues/2080) — invoice isn't flagged for regeneration
- [#2086](https://github.com/csb-ric/pcms/issues/2086) — error message formatting
- [#2164](https://github.com/csb-ric/pcms/issues/2164) — restore data-protection functionality
- [#2169](https://github.com/csb-ric/pcms/issues/2169) — when resending, option to skip the report
- [#2170](https://github.com/csb-ric/pcms/issues/2170) — double-click adding fund still exists somewhere
- [#2220](https://github.com/csb-ric/pcms/issues/2220) — updating a setting results in an error
- [#2223](https://github.com/csb-ric/pcms/issues/2223) — speeding up the external payment logging process (BPC)
- [#2224](https://github.com/csb-ric/pcms/issues/2224) — P&L reporting: PeopleSoft to Workday
- [#2225](https://github.com/csb-ric/pcms/issues/2225) — new general tracking upload template
- [#2226](https://github.com/csb-ric/pcms/issues/2226) — search feature for core services & equipment
- [#2263](https://github.com/csb-ric/pcms/issues/2263) — BPC service request blocked from reopening for invoiced records
- [#2272](https://github.com/csb-ric/pcms/issues/2272) — working potential enhancement list
- [#2292](https://github.com/csb-ric/pcms/issues/2292) — reduce schedule view for services if filtered
- [#2306](https://github.com/csb-ric/pcms/issues/2306) — editable document page (core)
- [#2317](https://github.com/csb-ric/pcms/issues/2317) — /cm/checks/edit performance (247 queries per row)
- [#2331](https://github.com/csb-ric/pcms/issues/2331) — usage analytics causing a crash
- [#2333](https://github.com/csb-ric/pcms/issues/2333) — remove noise from unknown funds
- [#2336](https://github.com/csb-ric/pcms/issues/2336) — allow splitting an invoice by service-to-grant, not just by percentage
- [#2340](https://github.com/csb-ric/pcms/issues/2340) — replace string-name link between pricing tier and assignments with a proper reference
- [#2344](https://github.com/csb-ric/pcms/issues/2344) — Ragon flow cytometry: editing early completion _(waiting on external resolution)_
- [#2345](https://github.com/csb-ric/pcms/issues/2345) — equipment filter on schedule does not persist when switching calendar day
- [#2346](https://github.com/csb-ric/pcms/issues/2346) — filter services view to selected services and equipment
- [#2347](https://github.com/csb-ric/pcms/issues/2347) — when an SR moves back to active, unarchive it in RPR

### Behind-the-scenes work

_Internal improvements with no user-visible change. Kept high-level on purpose._

This week included maintenance on the automated process that imports usage files, and a new internal check that continuously verifies billing totals stay accurate. That check confirmed the long-standing question of whether cached charges keep up — they do — and the system now watches for any drift automatically.

## Unresolved Questions from Vault Notes

**[[External Fund PI Field Issues]]**
- Can the PI field be edited/unlocked after fund creation?
- If not, do users need to create a new fund? What's the workaround?
- What's the correct PI entry format for external funds?
- Can blank PI fields be backfilled?

**[[Equipment and Services Tag Taxonomy]]**
- Some equipment entries appear to actually be services (Proposal Assistance, Post-Award Management, Financial Analysis, Overall Project Management, Clinical Trial Invoicing — all "Consultant"). Are these mislabeled in the source, or do we need a tag/flag to distinguish service-type entries that live in the equipment model?

**[[General Upload Template Service Request Sync]]**
- What does the "change message" look like on the service request — a banner, an event log entry, an email notification, or all three?
- Is the retraining owned by Finance ([[Tera Morse]] / [[Jessica Cho]] / [[Yovani Edwards]]) or by Eli?
- Is there a new GitHub issue for this, or does it roll under [#2225](https://github.com/csb-ric/pcms/issues/2225)?

**[[PCMS Chatbot]]**
- Where does the chatbot UI live in PCMS? Per-page widget, global modal, dedicated page?
- Where do current user and authorization context flow through to the tools?
- Does spec/capability structure need its own data modeling pass, or can it ride on the tag taxonomy work?
- Once the SOW is signed, which surface ships first — Ragon or a broader equipment search across cores?

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
- [[PCMS Chatbot]]
- [[Cached Total Resync on SR Cancel-Uncancel]]
- [[CachedTotalAuditor — Cache Drift Audit System]]
