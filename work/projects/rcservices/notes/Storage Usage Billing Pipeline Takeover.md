---
date: "2026-04-05"
description: "Taking over storage usage billing from Chris Mow — stalled since Nov 2025, legacy VM instability risk"
project: "rcservices"
tags:
  - work-note
---

# Storage Usage Billing Pipeline Takeover

## Context

Eli is taking over the storage usage billing pipeline from [[Chris Mow]]. The pipeline generates daily storage reports that feed into RC billing via [[RC Services (Eris)|rcservices]].

## Current State (stalled since 2025-11-07)

No movement since November 2025. Last communication was between Richard Kenny (rkenny@mgb.org) and Chris Mow.

## How It Works

1. Daily cron job generates storage reports to `/apps/cluster/system/var/YYYY-MM-DD_storage_report.txt`
2. Chris's code parses/processes the reports
3. Data is handed over to RC billing

## Infrastructure Risk

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

## Open Questions

- Did Chris ever validate the `test-*` prefixed report files?
- Is eris1pm01 still running or has it died?
- What does Eli need to take over the pipeline? Access, code, cron config?

## Related

- [[RC Services (Eris)|rcservices]]
- [[Chris Mow]]
- [[Alissa Scharf]]
