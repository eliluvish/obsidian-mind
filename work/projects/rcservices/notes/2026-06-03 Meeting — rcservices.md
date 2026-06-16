---
date: "2026-06-03"
description: "RC Services weekly sync — recap and prep covering 2026-05-21 → 2026-06-03 (window widened to cover the gap since the 2026-05-20 meeting)"
project: "rcservices"
meeting_type: weekly
attendees:
  - Alissa Scharf
  - Laura Brown
tags:
  - work-note
  - meeting
---

# RC Services Weekly Sync — 2026-06-03

## Attendees

- [[Alissa Scharf]]
- [[Laura Brown]]

## Recap

_Window: 2026-05-21 → 2026-06-03._

### New features

- **BriefCase storage billing now runs in-house.** The system pulls daily BriefCase usage on its own and matches each volume to the right subscription, flagging anything it can't match for review. This is the next service moved off the old legacy script in the billing takeover from [[Chris Mow]]. [#1969](https://github.com/csb-ric/eris/issues/1969)
- **A formatting toolbar for the service description editor** — bold, italic, headings, links, and lists with a reliable live preview, plus quick shortcuts to remove bold/italic. [#1978](https://github.com/csb-ric/eris/issues/1978), [#1965](https://github.com/csb-ric/eris/issues/1965)
- **Vendor emails now show on the services page**, so you can see when a vendor has sent something without leaving the page. [#1966](https://github.com/csb-ric/eris/issues/1966)

### Bug fixes & improvements

- **Expired funds can no longer be attached to a subscription** — this closes the gap that previously let an order go through on an expired fund. [#1983](https://github.com/csb-ric/eris/issues/1983)
- **Adding a funding source on a brand-new project works again** — the button wasn't responding. [#1964](https://github.com/csb-ric/eris/issues/1964)
- **Service charges now always use the correct rate** when two rates share the same start date; previously it could occasionally pick the wrong one. [#1980](https://github.com/csb-ric/eris/issues/1980)
- **The sent-email tool now shows the full message body** for instruction emails, which were previously coming up blank. [#1979](https://github.com/csb-ric/eris/issues/1979)
- **The account/fund picker no longer lists removed users.** [#1975](https://github.com/csb-ric/eris/pull/1975)

### Resolved this week

Closed by Eli this window: [#1981](https://github.com/csb-ric/eris/issues/1981), [#1979](https://github.com/csb-ric/eris/issues/1979), [#1972](https://github.com/csb-ric/eris/issues/1972), [#1971](https://github.com/csb-ric/eris/issues/1971), [#1970](https://github.com/csb-ric/eris/issues/1970), [#1969](https://github.com/csb-ric/eris/issues/1969), [#1966](https://github.com/csb-ric/eris/issues/1966), [#1965](https://github.com/csb-ric/eris/issues/1965), [#1964](https://github.com/csb-ric/eris/issues/1964), [#1963](https://github.com/csb-ric/eris/issues/1963), [#1960](https://github.com/csb-ric/eris/issues/1960), [#1945](https://github.com/csb-ric/eris/issues/1945).

### Requires resolution / finalization / clarification or closing

- [#1680](https://github.com/csb-ric/eris/issues/1680) — Convert stimulus controllers that use templates from the DOM to instead use an endpoint ([[Daniel Guettler]])
- [#1682](https://github.com/csb-ric/eris/issues/1682) — Update stimulus subscription_users controller to take in a template ([[Daniel Guettler]])
- [#1811](https://github.com/csb-ric/eris/issues/1811) — Refactor invoice generation / sending
- [#1812](https://github.com/csb-ric/eris/issues/1812) — Split invoices into sent and unsent tabs
- [#1844](https://github.com/csb-ric/eris/issues/1844) — Add `FreezerProService` service
- [#1863](https://github.com/csb-ric/eris/issues/1863) — New concern: when cancelled within the month, mark tracking record unbillable
- [#1926](https://github.com/csb-ric/eris/issues/1926) — Create a mock-up for ordering where they have to enter their finance person
- [#1952](https://github.com/csb-ric/eris/issues/1952) — Retire legacy MAD3 import path after the Isilon import job goes live
- [#1955](https://github.com/csb-ric/eris/issues/1955) — Add settings tab to services
- [#1962](https://github.com/csb-ric/eris/issues/1962) — Write RFA usage importer
- [#1968](https://github.com/csb-ric/eris/issues/1968) — Admin chatbot list
- [#1973](https://github.com/csb-ric/eris/issues/1973) — BriefCase shadow run + cutover from legacy CentOS 6 pipeline
- [#1974](https://github.com/csb-ric/eris/issues/1974) — Add BriefCase monthly billing aggregator

### Behind-the-scenes work

_Internal improvements with no user-visible change. Kept high-level on purpose._

Groundwork for the billing assistant continued — the nightly billing jobs now record their results so the assistant can report on them. Under the hood, the text editor was moved to a more reliable rendering engine, the account picker was tidied up, the way sent-email bodies are stored was fixed, some old unused code was removed, and the billing math was made more precise. The PRISM-48686 case — an order placed on an expired fund — was investigated and traced to the gap now closed in the fixes above.

## Unresolved Questions from Vault Notes

From [[2026-05-20 Meeting — rcservices]]:
- Fund financial contacts most often reach out to [[Laura Brown]] *after* invoices land — and it's the fund-level financial contact, not a project- or subscription-level one. **Ask [[Alissa Scharf]]**: should fund financial contacts be given access to all of the grant's subscriptions, so they can self-serve on invoice questions instead of routing through Laura?

From [[FreezerPro RedCap Integration]] (on-hold):
- SR asked whether there are billing scenarios not contemplated in the 2026-02-03 meeting notes — edge cases to think through: mid-year user-count changes crossing tier boundaries, PI departure mid-cycle, fund expiration before renewal.
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
- [[2026-05-20 Meeting — rcservices]]
