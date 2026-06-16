---
date: "2026-06-12"
description: "RC Services Weekly Sync — recap and prep covering 2026-06-05 to 2026-06-12"
project: "rcservices"
meeting_type: weekly
attendees:
  - "Alissa Scharf"
  - "Laura Brown"
tags:
  - work-note
  - meeting
---

# RC Services Weekly Sync — 2026-06-12

## Attendees

- [[Alissa Scharf]]
- [[Laura Brown]]

## Recap

_Window: 2026-06-05 to 2026-06-12._

### New features

- RC Services now collects RFA storage usage automatically every day, so it can be billed without anyone running the old manual scripts — a key step in taking RFA billing fully in-house [[#1994](https://github.com/csb-ric/eris/pull/1994)].

### Bug fixes & improvements

-

### Resolved this week

- [#1962](https://github.com/csb-ric/eris/issues/1962) — RFA usage collection is now in place (closed by Eli).

### Requires resolution / finalization / clarification or closing

- [#1680](https://github.com/csb-ric/eris/issues/1680) — Convert stimulus controllers that use templates from the dom to instead use an endpoint
- [#1682](https://github.com/csb-ric/eris/issues/1682) — Update stimulus subscription_users controller to take in a template
- [#1811](https://github.com/csb-ric/eris/issues/1811) — Refactor invoice generation / sending
- [#1812](https://github.com/csb-ric/eris/issues/1812) — Split invoices in to sent and unsent tabs
- [#1844](https://github.com/csb-ric/eris/issues/1844) — Add `FreezerProService` service
- [#1863](https://github.com/csb-ric/eris/issues/1863) — New concern: when cancelled within the month, mark tracking record unbillable
- [#1926](https://github.com/csb-ric/eris/issues/1926) — Create a mock up for ordering where they have to enter their finance person
- [#1952](https://github.com/csb-ric/eris/issues/1952) — Retire legacy MAD3 import path (Mad3Usage SQL view) after Isilon::ImportMad3UsageJob goes live
- [#1955](https://github.com/csb-ric/eris/issues/1955) — Add settings tab to services
- [#1968](https://github.com/csb-ric/eris/issues/1968) — Admin chatbot list
- [#1973](https://github.com/csb-ric/eris/issues/1973) — BriefCase shadow run + cutover from legacy CentOS 6 pipeline
- [#1974](https://github.com/csb-ric/eris/issues/1974) — Add BriefCase monthly billing aggregator
- [#1984](https://github.com/csb-ric/eris/issues/1984) — MAD3/Briefcase: make share path and full path searchable in the subscriptions admin index
- [#1991](https://github.com/csb-ric/eris/issues/1991) — Subscriptions: let grant administrators change funding source on subscriptions they don't own (delegated self-service)

### Behind-the-scenes work

_Internal improvements with no user-visible change. Kept high-level on purpose._

- Continued groundwork on moving the storage billing pipelines off the older legacy scripts — validation and parallel runs so the cutover is safe before anything changes for users.

## Unresolved Questions from Vault Notes

**From [[2026-05-20 Meeting — rcservices]]:**
- Laura reports that fund financial contacts most often reach out to her *after* invoices land. She confirmed it's the fund-level fin contact (not a project- or subscription-level contact) doing the outreach. **Ask Alissa**: should fund fin contacts be given access to all of the grant's subscriptions, so they can self-serve on invoice questions instead of routing through Laura?

**From [[FreezerPro RedCap Integration]]:**
- SR asked whether Eli knows of billing scenarios not contemplated in the 2026-02-03 meeting notes. Need to think through edge cases (mid-year user count changes crossing tier boundaries, PI departure mid-cycle, fund expiration before renewal).
- SR asked whether Eli has worked with REDCap before — pending response.

## Discussion

-

## Decisions

-

## Action Items

- [ ]

## Related

- [[RC Services (Eris)|rcservices]]
- [[Alissa Scharf]]
- [[Laura Brown]]
