---
date: "2026-05-11"
description: "Contact at MGB Digital Storage — triage point for Powerscale shares/quotas that can't be matched to billing customers"
tags:
  - person
team: "Digital Storage Operations"
---

# Rolf Fabre

## Role & Team

- **Team**: MGB Digital Storage
- **Role**: Storage contact
- **Scope**: Powerscale shares/quotas — resolves ownership of records that can't be matched to known billing customers

## Relationship

Introduced at the 2026-05-11 Isilon meeting. Eli will attempt to match Powerscale shares/quotas to billing customers; anything unmatched goes to Rolf for resolution.

## Key Moments

- **2026-05-11** — Isilon meeting: agreed that Eli matches what he can, sends unmatched shares/quotas to Rolf
- **2026-05-22** — First BriefCase triage email sent and **replied same day** with per-row dispositions. Group A: `miket` is a bind mount artifact (cancelled 2019), `awad1` deleted today, remaining 11 to be deleted next week. Group B: cluster-internal paths confirmed (filter), `ccr`/`cctm` are prepaid (pattern TBD), `bwh-comppath-img3` is mid-migration, `rftest` deleted, `whaas` unknown. `/hpc/scratch/{a..z}` + home confirmed never billable. See [[BriefCase Unbilled Volume Triage]].

## Notes

New contact as of 2026-05-11. The escalation pattern (Eli matches → Rolf resolves unmatched) now covers both Powerscale shares and BriefCase pasxml volumes.

## Related

- [[RFA Billing Takeover and Powerscale Migration]]
- [[Briefcase Billing Takeover]]
- [[BriefCase Unbilled Volume Triage]]
- [[BriefCase Volume Matching Logic]]
- [[RC Services (Eris)|rcservices]]
