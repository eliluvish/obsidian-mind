---
date: "2026-04-05"
description: "Software reselling and pass-through billing platform for the research hospital community"
project: rcservices
status: active
rails_version: "8.1"
ruby_version:
aliases:
  - RC Services (Eris)
  - rcservices
tags:
  - project
---

# RC Services (Eris)

## Overview
Software reselling to the research hospital community and pass-through billing for various services. Internal name: Eris.

## Repository & Deploy
- **Repo**: https://github.com/csb-ric/eris
- **Default branch**: master
- **Production**:
- **Staging**:
- **Deploy method**: TBD — no deploy target yet

## Tech Stack
- **Rails**: 8.1
- **Ruby**:
- **Database**:
- **Key gems**:

## Stakeholders
- **Department**: [[Research Computing Core]]
- [[Alissa Scharf]] — Manager, Research Computing Core
- [[Laura Brown]] — Analyst
- [[Michael Oates]] — Director, Research Computing

## Compliance Notes
None currently.

## Architecture Notes

## Active Notes

- [[ServiceNow Ticket Analysis for Alissa]] — **completed** (2026-06-10). Analysis delivered to [[Alissa Scharf]].
- [[RFA Billing Takeover and Powerscale Migration]] — **active**. Billing code deployed to production; usage importer not yet written ([eris#1962](https://github.com/csb-ric/eris/issues/1962)).
- [[Storage Usage Billing Pipeline Takeover]] — **active**. MAD3 takeover from Chris Mow restarted; Isilon API path in production. June: run alongside Chris's scripts; July: full cutover.
- [[Briefcase Billing Takeover]] — **active**. Third leg of the Chris Mow billing handoff. Importer ✅ merged to master 2026-05-26 (PR #1976); post-merge validation rerun + shadow run ([eris#1973](https://github.com/csb-ric/eris/issues/1973)) and monthly aggregator ([eris#1974](https://github.com/csb-ric/eris/issues/1974)) next. See [[BriefCase Volume Matching Logic]] for the matching iterations.
- [[Prepaid Remaining Balance on Invoices]] — **active**. [[Alissa Scharf]] request (2026-06-16): show prepaid accounts' remaining balance on invoices (Prepaid / Remaining balance / Subtotal), updated monthly. ⛔ **Deploy hold until after July 5** ([eris#1998](https://github.com/csb-ric/eris/issues/1998)).
- [[SAS Enclave License Type]] — **active**. [[Alissa Scharf]] request (2026-06-16, discuss Wed 6/17): new SAS Enclave license whose ticket routes to the Enclave team. New service vs. SAS platform option TBD ([eris#1997](https://github.com/csb-ric/eris/issues/1997)).
- [[FreezerPro RedCap Integration]] — **active**. Schema blocker resolved 2026-06-11: report field set + REDCap report-API delivery agreed, pull on the 2nd for the prior month. Importer build gated only on [[Svetlana Rojevsky]] delivering test/prod API tokens + Report ID. Open: service cancellation handling. PR [#1854](https://github.com/csb-ric/eris/pull/1854).
- [[Fund Expiry Enforcement]] — **completed** (master 2026-05-27, #1983). Strict `Fund#expired?` across every fund-attach path; removed the 6-month internal-fund grace. See [[Key Decisions]].
- [[RFA ServiceNow Provisioning Pipeline]] — **completed** (live in production 2026-04-16).
- [[AzureVM Import via Azure Export API]] — **completed** ([eris#1913](https://github.com/csb-ric/eris/issues/1913)).

## Decisions

- [[001-FreezerPro REDCap Integration Model]] — REDCap is system of record; RC Services consumes a minimal validated dataset for billing only.
- [[002-Fluent 2 Modal Design System]] — modal UI in eris adopts Microsoft's Fluent 2 as the visual / interaction baseline; mirrors in-repo `.claude/DECISION_LOG.md`.
- [[003-BriefCase Usage Billing Statistic]] — **proposed**. Which statistic to bill BriefCase usage on (avg vs 75th percentile); leaning p75 to match Chris's legacy scripts.

## Related
- [[Index]]
- [[Azure Usage Dashboard]] — separate app spun out of the eris Azure work (researcher-facing usage reporting; [[001-Standalone Azure Usage Dashboard App]])
