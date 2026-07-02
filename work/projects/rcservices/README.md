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

## Meeting Cadence

- **RC Services sync** — [[Alissa Scharf]], [[Laura Brown]], and Eli. **Moving to weekly** (or a 45-min slot) as of 2026-06-17 — was biweekly Wednesday 9:00–9:30am; agreed too infrequent. To be scheduled before Eli's 1:1 with [[Daniel Guettler]].

## Compliance Notes
None currently.

## Architecture Notes

## Active Notes

- [[ServiceNow Ticket Analysis for Alissa]] — **completed** (2026-06-10). Analysis delivered to [[Alissa Scharf]].
- [[RFA Billing Takeover and Powerscale Migration]] — **active**. Billing code deployed to production; usage importer not yet written ([eris#1962](https://github.com/csb-ric/eris/issues/1962)).
- [[Storage Usage Billing Pipeline Takeover]] — **active**. MAD3 takeover from Chris Mow restarted; Isilon API path in production. June: run alongside Chris's scripts; July: full cutover. MAD3/RFA now bill logical usage (`fslogical`, #2008/#2009).
- [[MAD3 Billing Basis — Average vs Month-End Snapshot]] — **active**. MAD3 import temporarily bills the month-end snapshot during the logical cutover; revert to monthly average in July before August billing ([eris#2010](https://github.com/csb-ric/eris/issues/2010)).
- [[Briefcase Billing Takeover]] — **active**. Third leg of the Chris Mow billing handoff. Importer ✅ merged to master 2026-05-26 (PR #1976); post-merge validation rerun + shadow run ([eris#1973](https://github.com/csb-ric/eris/issues/1973)); monthly aggregator **in progress** ([eris#1974](https://github.com/csb-ric/eris/issues/1974), PR #2007). See [[BriefCase Volume Matching Logic]] for the matching iterations.
- **Self-service funding correction** — newly surfaced (PR [#1996](https://github.com/csb-ric/eris/pull/1996), branch `self-serv-funding`): PI-facing funding change with invoice restatement. No vault note yet — candidate when it merges.
- [[Prepaid Remaining Balance on Invoices]] — **active**. [[Alissa Scharf]] request (2026-06-16): show prepaid accounts' remaining balance on invoices (Prepaid / Remaining balance / Subtotal), updated monthly. ⛔ **Deploy hold until after July 5** ([eris#1998](https://github.com/csb-ric/eris/issues/1998)).
- [[SAS Enclave License Type]] — **completed** (master 2026-06-18, #1997/#2020). `SasEnclaveService` + `SasEnclaveSubscription` STI pair shipped: new installs prorate Oct–Mar at $25/mo, renewals auto-provision and skip creation-month check, annual billing fires April only, confirmation email routes to AnalyticsEnclave@Partners.org.
- [[FreezerPro RedCap Integration]] — **active**. Schema blocker resolved 2026-06-11: report field set + REDCap report-API delivery agreed, pull on the 2nd for the prior month. Importer build gated only on [[Svetlana Rojevsky]] delivering test/prod API tokens + Report ID. Open: service cancellation handling. PR [#1854](https://github.com/csb-ric/eris/pull/1854).
- **Azure subscriptions API feed** — **completed** (master 2026-06-18, [eris#2017](https://github.com/csb-ric/eris/issues/2017)). `GET /api/v1/azure_subscriptions` exposes active Azure VM subscriptions (RITM, subscription ID, owner, fund) for rcfinops to poll daily. Authenticated via `API_KEY_FOR_RCFINOPS`. Producer side of [[RCS Metadata Sync from Eris]].
- [[Fund Expiry Enforcement]] — **completed** (master 2026-05-27, #1983). Strict `Fund#expired?` across every fund-attach path; removed the 6-month internal-fund grace. See [[Key Decisions]].
- [[Import Usage Information Decomposition]] — **active** ([eris#1811](https://github.com/csb-ric/eris/issues/1811)). Splitting monolithic `ImportUsageInformation` into per-vendor `Importers::*` objects + `MonthlyUsageImport` orchestrator; `rake import:usage_compare` parity harness diffs old vs new against prod before cutover. Legacy still live; branch `1811-refactor-invoice-generation-sending` unmerged. Parity harness already caught a subscriber double-email bug — see [[Gotchas]].
- [[RFA ServiceNow Provisioning Pipeline]] — **completed** (live in production 2026-04-16).
- [[AzureVM Import via Azure Export API]] — **completed** ([eris#1913](https://github.com/csb-ric/eris/issues/1913)).

## Decisions

- [[001-FreezerPro REDCap Integration Model]] — REDCap is system of record; RC Services consumes a minimal validated dataset for billing only.
- [[002-Fluent 2 Modal Design System]] — modal UI in eris adopts Microsoft's Fluent 2 as the visual / interaction baseline; mirrors in-repo `.claude/DECISION_LOG.md`.
- [[003-BriefCase Usage Billing Statistic]] — **proposed**. Which statistic to bill BriefCase usage on (avg vs 75th percentile); leaning p75 to match Chris's legacy scripts.

## Related
- [[Index]]
- [[Azure Usage Dashboard]] — separate app spun out of the eris Azure work (researcher-facing usage reporting; [[001-Standalone Azure Usage Dashboard App]])
