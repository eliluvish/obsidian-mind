---
date: "2026-04-07"
description: "Taking over billing for new RFA services — Powerscale replacing RFA. API approach decided: daily point-in-time usage queries, store locally, aggregate later."
project: "rcservices"
status: active
tags:
  - work-note
---

# RFA Billing Takeover and Powerscale Migration

## Context

Eli is taking over billing for the new RFA services. Powerscale is a new vendor replacing RFA. Meeting scheduled for 2026-04-14 at 4pm to align on API access, service ownership, and billing aggregation.

## Meeting — 2026-04-14 4:00 PM

**Attendees**: [[Alissa Scharf]], [[Chris Mow]], [[Michael Oates]], [[Richard Kenny]]

### Agenda

**MAD and New RFA**
- Outcome: develop API call directly from Powerscale for both services
- Service ownership for future issues/needs

**BriefCase**
- Outcome: can we pull via API?
- If no API, need to hand off responsibility of billing script from [[Chris Mow]] to [[Richard Kenny]]
- Update how billing is aggregated

## Meeting Outcomes — 2026-04-14

- Sent service account credentials to [[Naresh Mallidi]] (Digital Storage Operations contractor) — he will set us up in Powerscale and send API documentation
- **Architecture decision**: query Powerscale API daily to capture point-in-time usage snapshots; store locally; aggregation approach TBD
- Powerscale API only provides usage at a point in time (no historical rollup), so daily polling is required

## API Access — 2026-04-21

- Service account: **`cri6`** — set up by [[Naresh Mallidi]]
- API client: **[isilon_sdk_python](https://github.com/Isilon/isilon_sdk_python)** (official Isilon Python SDK, in lieu of formal docs)
- Parent issue: [eris#1918](https://github.com/csb-ric/eris/issues/1918) — Add powerscale importing (has sample CLI output)
- Next step: scoped prerequisite issue to prove connection and pull a sample response before building the import

## Isilon Meeting — 2026-05-11

- Outcome: Eli will attempt to match the Powerscale shares/quotas to known billing customers; anything that can't be matched gets sent to [[Rolf Fabre]] (MGB Digital Storage) for resolution
- Tracking: [eris#1939](https://github.com/csb-ric/eris/issues/1939)

## Action Items

- [x] Attend meeting 2026-04-14
- [x] Receive Powerscale API access from [[Naresh Mallidi]] — `cri6` service account + isilon_sdk_python
- [x] Prove connection to Powerscale API — [eris#1921](https://github.com/csb-ric/eris/issues/1921) _(closed 2026-04-22)_
- [ ] Merge Powerscale importing PR — [eris#1918](https://github.com/csb-ric/eris/issues/1918) _(also covers storage billing pipeline takeover; [[Alissa Scharf]] OOO 2026-04-24 — find time with her 2026-04-27)_
- [ ] Match Powerscale shares/quotas to billing customers; escalate unmatched to [[Rolf Fabre]] — [eris#1939](https://github.com/csb-ric/eris/issues/1939)
- [ ] Decide on aggregation strategy once connection is proven
- [ ] Determine RFA billing requirements with [[Alissa Scharf]] (see [[RFA ServiceNow Provisioning Pipeline]])

## Related

- [[RC Services (Eris)|rcservices]]
- [[Storage Usage Billing Pipeline Takeover]] — related billing handoff from Chris
- [[Alissa Scharf]]
- [[Chris Mow]]
- [[Michael Oates]]
- [[Richard Kenny]]
- [[Nicholas Yale]]
- [[Peter Gray]]
- [[Naresh Mallidi]]
- [[Rolf Fabre]]
- [[RFA ServiceNow Provisioning Pipeline]]
