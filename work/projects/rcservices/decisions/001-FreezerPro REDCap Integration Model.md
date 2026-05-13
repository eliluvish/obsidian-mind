---
date: "2026-04-06"
description: "REDCap is system of record for FreezerPro; RC Services ingests approved data for billing only"
project: "rcservices"
status: accepted
tags:
  - decision
---

# 001 — FreezerPro REDCap Integration Model

## Context

FreezerPro is being onboarded as a service in [[RC Services (Eris)|rcservices]]. The team needed to decide how data flows between REDCap (lab data management) and RC Services (billing), who validates what, and how renewals work.

## Decision

1. **System Roles**: REDCap manages all lab data, validations, history, renewals, and approvals. RC Services ingests only approved, clean data and handles billing. A single identifier (REDCap record ID or UUID) links records across systems.
2. **Validation**: Fund numbers validated via Insight (expiration + title). MGB ID validated in REDCap. REDCap stores full history but passes only current required fields (tier, fund, owner) to RC Services.
3. **Billing**: Once per year after onboarding. Invoices one month in arrears, posted on the 3rd. Annual renewal is the only opportunity to update funding. First invoice sent after successful onboarding becomes the subscription effective date; yearly invoices thereafter on that anniversary. Tiers (confirmed 2026-05-13 via Finance/[[Alissa Scharf]]):
   - Tier 1 (1–5 users) — $2,200
   - Tier 2 (6–10 users) — $3,300
   - Tier 3 (11+ users) — $4,400

   Tier passed as line item (not multiplier). RCS owns cost-per-unit definitions for recalculation and audit; REDCap does not pipe subscription cost.
4. **UX**: Users don't manage FreezerPro directly in RC Services. It appears as a service with an order button linking to REDCap. Users see invoices but not the subscription.

## Consequences

- RC Services importer is blocked until REDCap team finalizes their schema and API
- Monthly pull cadence (1st–2nd of each month) means billing changes lag up to a month
- No mid-year fund changes simplifies billing but may frustrate labs needing corrections

## Related

- [[FreezerPro RedCap Integration]] — work note with action items
- [[Lynn Simpson]]
- [[Alissa Scharf]]
- [[RC Services (Eris)|rcservices]]
