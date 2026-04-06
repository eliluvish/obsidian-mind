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

## Action Items — RC Services

- [ ] Configure FreezerPro as a non-visible subscription
- [ ] Ensure invoice visibility in Billing
- [ ] Build the importer once the REDCap schema is final
- [ ] Perform monthly pulls of approved records (around the 1st–2nd)
- [ ] Handle owner changes if PI MGB ID changes

## Action Items — REDCap Team

- [ ] Finalize data model (events vs. forms, tier, fund, PI MGB ID, approval state)
- [ ] Implement Insight-based fund validation and MGB ID checks
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
