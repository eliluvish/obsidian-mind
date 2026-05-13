---
date: "2026-04-06"
description: "FreezerPro service with REDCap integration — REDCap is system of record, RC Services handles billing only, PR #1854 on hold"
project: "rcservices"
status: on-hold
tags:
  - work-note
---

# FreezerPro RedCap Integration

## Status

PR [#1854](https://github.com/csb-ric/eris/pull/1854) open on branch `1844-add-freezerproservice-service`. On hold — waiting on REDCap team to finalize schema before building the importer.

## Integration Model

REDCap is the system of record for all FreezerPro data. RC Services consumes only a minimal, validated dataset to perform billing after explicit approval. See [[001-FreezerPro REDCap Integration Model]] for the full decision record.

### Workflow

- **New onboarding**: REDCap submission → validation → approval → RC Services import → billing
- **Annual renewals**: Triggered by each lab's start date (not a fixed calendar date). REDCap prompts labs to review users and funding; approved records pulled monthly by RC Services for billing

### Billing Model

- Billing occurs once per year, after onboarding is finalized
- Invoices generated one month in arrears, posted on the 3rd of each month
- Annual renewal is the single opportunity to update funding — no frequent fund changes

### User Experience

- FreezerPro appears as a service in RC Services with an order button linking to REDCap
- Users see invoices in RC Services but not the subscription itself
- ServiceNow Knowledge Base articles for navigation and FAQs

## 2026-05-13 — RC Form Field & Billing Alignment

Email thread with [[Svetlana Rojevsky]] (REDCap side) and [[Alissa Scharf]] aligning on the field set REDCap will pipe into the RC Form, and confirming the billing model.

### Agreed Field Set (REDCap → RC Services)

REDCap instrument: `rc_services`. Eli's contract requirement: REDCap must validate funding during form submission. If invalid, subscription creation fails and breaks the importer.

| Field | Token | Keep? | Notes |
|-------|-------|-------|-------|
| Account Number | `acc_num_rc` | yes | |
| Grant number | `billing_fund_rc` | yes | Validated upstream at license-request step; SR may re-validate at billing step |
| Billing fund validation status | `billing_fund_is_valid_rc` | yes (operational) | Secondary check, kept for ops not data |
| Cost Tier | `cost_tier_calc_rc` | yes | Value is `1`, `2`, or `3` — line item, not multiplier |
| PI MGB username | _to be added_ | yes | **Eli requested** — only reliable MGB identifier; email lookup is unreliable. SR to wire up. |
| PI email / first / last | — | **drop** | Not needed |
| Billing contact Email | `email_billing_calc_rc` | **drop** | Not needed |
| Business Unit | `billing_business_unit_rc` | **drop** | Not needed |
| Subscription cost | `cost_value_rc` | **drop** | RCS must own cost-per-unit for recalculations + audit; SR agreed to remove |

### Confirmed Cost Tiers (from Finance via Alissa)

- Tier 1 (1–5 users) — $2,200
- Tier 2 (6–10 users) — $3,300
- Tier 3 (11+ users) — $4,400

Cost tier is supplied as a line-item identifier, not a multiplier. See [[001-FreezerPro REDCap Integration Model]].

### Billing Cadence (clarified)

- First invoice sent **after lab successfully onboards** — that date becomes the subscription effective date.
- Yearly invoicing thereafter on that anniversary.
- Renewal process to be discussed after first test cycle; SR has options to walk through.

### Open Questions

- SR asked whether Eli knows of billing scenarios not contemplated in the 2026-02-03 meeting notes. Need to think through edge cases (mid-year user count changes crossing tier boundaries, PI departure mid-cycle, fund expiration before renewal).
- SR asked whether Eli has worked with REDCap before — pending response.

## Action Items — RC Services

- [ ] Configure FreezerPro as a non-visible subscription
- [ ] Ensure invoice visibility in Billing
- [ ] Build the importer once the REDCap schema is final
- [ ] Perform monthly pulls of approved records (around the 1st–2nd)
- [ ] Handle owner changes if PI MGB ID changes
- [ ] Reply to SR with billing-scenario edge cases (tier boundary crossings, PI departure, fund expiration mid-cycle)

## Action Items — REDCap Team

- [ ] Finalize data model (events vs. forms, tier, fund, PI MGB ID, approval state)
- [ ] Implement Insight-based fund validation and MGB ID checks
- [ ] Wire PI MGB username into RC Form (`rc_services` instrument)
- [ ] Remove `cost_value_rc` (subscription cost) from RC Form
- [ ] Define an explicit "approved/finalized" state
- [ ] Add admin override for non-responsive labs
- [ ] Publish Knowledge Base content and provide API details to RC Services

## Action Items — Operations / Billing

- [ ] Finalize billing details with Research Finance
- [ ] Set up monitoring for monthly reports
- [ ] Support admin access and website placement

## Stakeholders

- [[Lynn Simpson]] — Director, Digital Research Applications
- [[Alissa Scharf]] — Manager, Research Computing Core
- [[Svetlana Rojevsky]] — Senior Applications Analyst

## Related

- [[RC Services (Eris)|rcservices]]
- [[001-FreezerPro REDCap Integration Model]]
