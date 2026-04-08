---
date: "2026-04-07"
description: "ServiceNow provisioning pipeline for RFA service — Nick Yale and Peter Gray requesting staging setup, pending billing requirements from Alissa"
project: "rcservices"
status: active
tags:
  - work-note
---

# RFA ServiceNow Provisioning Pipeline

## Context

[[Nicholas Yale]] and [[Peter Gray]] are requesting the RFA service be added to RC Services staging so they can test the ServiceNow provisioning pipeline. This is the same RFA service from the [[RFA Billing Takeover and Powerscale Migration]] — the SN pipeline is how new RFA subscriptions will be provisioned.

Peter has already achieved a successful SMB request to RC Services. He needs the API details (similar to what Eli provided for Azure Cold Storage) to complete the end-to-end test. NFS testing is also in progress, plus a negative test API call.

## Eli's Response

Before adding the service to staging, Eli emailed [[Alissa Scharf]] to:

1. Get requirements from Alissa
2. Determine if there is billing-related data needed from Nick/Peter's process
3. Assess whether the RFA service has special billing requirements that could require a **new API**

## Key Details

- SN pipeline pattern follows the Azure Cold Storage precedent (Peter built that too)
- Peter needs: RC Services API details for the new RFA subscription
- Open question: does RFA billing require a custom API or can it use the existing subscription API?

## Action Items

- [ ] Get billing requirements from [[Alissa Scharf]]
- [ ] Determine if RFA needs a new API or can reuse existing
- [ ] Provide API details to [[Peter Gray]] once requirements are clear
- [ ] Add RFA service to RCS staging

## Related

- [[RC Services (Eris)|rcservices]]
- [[RFA Billing Takeover and Powerscale Migration]]
- [[Storage Usage Billing Pipeline Takeover]]
- [[Alissa Scharf]]
- [[Nicholas Yale]]
- [[Peter Gray]]
- [[Thomas McShane]]
