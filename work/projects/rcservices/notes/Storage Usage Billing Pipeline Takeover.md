---
date: "2026-04-05"
description: "Taking over MAD3 storage usage billing from Chris Mow — restarted; Isilon API path in production, switching off the eris usage DB. July cutover target."
project: "rcservices"
status: active
tags:
  - work-note
---

# Storage Usage Billing Pipeline Takeover

## Context

Eli is taking over the **MAD3** storage usage billing pipeline from [[Chris Mow]]. The new approach **skips the eris usage database** entirely — usage is pulled directly from the Isilon API into RC Services. The legacy report-parsing pipeline is being retired.

## Current State (2026-05-18) — restarted, in production

Work resumed after the Nov 2025 stall and is now largely in production. The plan is a phased cutover: run alongside Chris's existing billing for June, validate, then switch fully to the new implementation for July.

### Completed (in production)

- Isilon API access
- Confirmed the relationships between active MAD3 subscriptions in RCS and their quotas in Isilon
- Daily job imports usage into RCS
- New billing process code — uses our internal import data instead of the eris usage DB

### Cutover Plan

- **June billing**: rely on existing billing (Chris's scripts), then compare against the new implementation; make changes as needed
- **July billing**: switch to the new implementation for good (target)

## Superseded — Legacy Pipeline (historical)

The notes below describe the old report-parsing pipeline being replaced. Kept for context; not the path forward.

### How It Worked (legacy)

1. Daily cron job generates storage reports to `/apps/cluster/system/var/YYYY-MM-DD_storage_report.txt`
2. Chris's code parses/processes the reports
3. Data is handed over to RC billing

### Infrastructure Risk (legacy pipeline)

- The cron job runs on **eris1pm01**, a legacy VM (old erisone infra) that has become increasingly unstable
- Instability may relate to network upgrades for the **eristwo → eristwo-nucleus migration**
- Result: **gaps in storage report data**
- Richard Kenny set up a precautionary backup cron on **eristwo** generating `test-YYYY-MM-DD_storage_report.txt` files
- Chris was asked to validate whether his script can process the `test-*` prefixed files — unclear if this was ever confirmed

## Key People

- [[Chris Mow]] — current owner, handing off to Eli
- [[Richard Kenny]] (rkenny@mgb.org) — implemented the backup cron job
- [[Alissa Scharf]] — CC'd on the thread
- [[RFA Billing Takeover and Powerscale Migration]] — related RFA billing handoff
- Edmund Ng (edng@mgb.org) — CC'd on the thread

## Action Items

- [x] Isilon API access
- [x] Confirm relationships between active MAD3 subscriptions in RCS and Isilon quotas
- [x] Daily job imports usage into RCS
- [x] New billing process code using internal import data (not eris usage DB)
- [ ] June: run new implementation alongside Chris's existing billing; compare results
- [ ] July: cut over fully to the new implementation

## Related

- [[RC Services (Eris)|rcservices]]
- [[Chris Mow]]
- [[Alissa Scharf]]
