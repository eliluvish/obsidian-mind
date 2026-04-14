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

## Action Items

- [x] Attend meeting 2026-04-14
- [ ] Receive Powerscale API documentation from [[Naresh Mallidi]]
- [ ] Decide on aggregation strategy once API docs arrive
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
- [[RFA ServiceNow Provisioning Pipeline]]
