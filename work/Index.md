---
description: "Central map of all projects, work notes, and decisions"
aliases:
  - Index
  - Work Index
tags:
  - index
  - moc
---

# Work Notes

Central map of content. All work notes and decisions link back here. For quick navigation, use [[Home]] or open `bases/Work Dashboard.base`.

**Folder structure**: `projects/<name>/` = one folder per Rails app with README, decisions, and notes. `archive/` = completed/sunset projects.

## Active Projects

Each project has its own folder in `work/projects/` with a README, decisions, and work notes.

- [[RC Services (Eris)|rcservices]] — Software reselling and pass-through billing for the research hospital community
- [[iLog]] — DEA controlled substances compliance, inventory, logbooks, Form 41 generation
- [[PCMS]] — Research Core Management System, core facility billing and operations
- [[CADE]] — Center for Academic Development and Enrichment (lab_archives repo, CADE label)
- [[Minor Intake Form|minr]] — Minor campus access requests with approval workflow (lab_archives repo, Minor intake form label)
- [[Research Participant Remuneration|rpr]] — Study participant payment tracking (study_pay repo), HIPAA-protected PII
- [[BioLift|biolift]] — Biological sample transport between facilities, bills of lading for couriers
- [[People|people]] — Employee data aggregation for deductions (lab_archives repo, excludes CADE/minr labels)
- [[Research Intake Survey|ris]] — Onboarding survey for new research hires (lab_archives repo, Research Intake Survey label)
- [[RC FinOps|rcfinops]] — Standalone Rails app: self-service cloud cost dashboard for researchers (Azure now, AWS later), role-scoped via FundingSource/Insight (spun out of eris Azure work)

## Recent Notes

- [[Fund-Number Change Regeneration Flag]] — pcms [pcms#2356](https://github.com/csb-ric/pcms/issues/2356) (PR #2362); two-color regeneration flag — `total_mismatch` (red, blocks journaling) vs `fund_changed` (yellow, non-blocking)
- [[MAD3 Billing Basis — Average vs Month-End Snapshot]] — rcservices [eris#2010](https://github.com/csb-ric/eris/issues/2010); MAD3 import temporarily bills the month-end snapshot during the physical→logical cutover; revert to monthly average in July 2026 before August billing
- [[2026-06-17 Meeting — rcservices]] — rcservices biweekly sync; **SAS Enclave settled as a standalone service** (custom messaging the deciding factor, ticket routes to Enclave team, #1997); **GraphPad Prism to be dropped from the catalog after next year** (~$1M renewal); cadence moving to weekly
- [[2026-06-11 Meeting — pcms]] — pcms weekly sync; quiet shipping week. Agreed PCMS needs a UI facelift (Eli demoed rcfinops dashboard as the bar; outdated look confirmed across all focus groups); Eli to mock up MGB-branded options. Cache-drift monitor still clean. Finance to file small focus-group tickets soon.
- [[PCMS UI Facelift]] — pcms, MGB-branded UI refresh; dated look flagged across all focus groups; AI mockups make redesign cheap. Direction agreed at 6/11 sync; mockups-vs-agency-design path undecided.
- [[RC FinOps Week-1 Build Log]] — rcfinops, greenfield build arc Jun 4–10 (116 commits): Azure import, RBAC + site admin, FundingSource/Insight scoping, MGB subsidy, faceted browser; `main` 16 ahead of origin
- [[MGB Subsidy Flagging Business Rule]] — rcfinops, MGB-subsidized line items flagged on import + filtered/tinted across dashboard and index; affects PI vs admin visibility; compliance review TBD
- [[ServiceNow Ticket Analysis for Alissa]] — rcservices, ✅ completed 2026-06-10. Analysis delivered to [[Alissa Scharf]].
- [[2026-05-28 Meeting — pcms]] — pcms weekly sync, quiet shipping week (no merged PRs), 1 issue closed (#2267), 31 requiring resolution; no outcomes from the meeting itself
- [[BriefCase Unbilled Volume Triage]] — rcservices, first triage list sent to [[Rolf Fabre]] (2026-05-22) — Group A ended subs + Group B unmatched (internal/template paths, pcpgm outlier); awaiting response
- [[BriefCase Volume Matching Logic]] — rcservices [eris#1972](https://github.com/csb-ric/eris/issues/1972), four-iteration design path for matching pasxml volumes to subscriptions; importer's bucket taxonomy
- [[PRISM-48686 Expired Fund Order Investigation]] — rcservices [eris#1963](https://github.com/csb-ric/eris/issues/1963), investigate how an order was placed against an expired fund — guardrail bypass or fund-state ambiguity
- [[Cached Total Resync on SR Cancel-Uncancel]] — pcms PR #2337, after_commit + RecalculateServiceRequestTrackingsJob closes the cancel/uncancel staleness vector; auditor PR #2307 is the audit companion (deferred to next week)
- [[lab_archives Rails 8.1 Upgrade]] — people/cade/minr/ris, shared app 8.0.5 → 8.1.3 **merged to master 2026-06-10** (PR #1189, dual-boot validated, `bin/ci` added, cookie serializer →`:json`); deploy + Bootstrap 5 still pending
- [[Cross-Study Email Mutation Incident]] — rpr, shared participant email across studies misrouted a gift card (#2022P000780); no PII exposed; proposed fix email-per-study, awaiting [[Gala Laffey]]
- [[Approvals by Institution]] — minr #1187, Kele wants approvals routed by institution; blocked waiting on [[Kele Piper]] for the institution → approver mapping
- [[Refactor js.erb to Turbo]] — biolift #20, **in progress** (2026-06-10); `turbo-rails` installed (Drive off, opt-in per element), specimen transport deletes migrated as PoC; gated on shared Site plugin UJS conversion
- [[Insight Fund Fields Request from CADE]] — cade, Rowan Potter requested fund/grant fields from Insight; blocked on new Insight API build; near-term CSV→people; escalate Allison → [[Jane Murray]]
- [[Accountability Logbook Testing Feedback]] — ilog, open testing-feedback tickets (compliance #718–724); the Kele/Mirabella set, in progress, current North Star goal
- [[Calendar Refactor and Drag-Drop Proposal]] — pcms, cross-core SR scoping bug fixed & deployed; PR #2338 opened; Daniel proposed a larger calendar refactor (drag/drop), scope TBD
- [[2026-05-21 Meeting — pcms]] — pcms weekly sync, three shipped items (equipment schedule filter #2291, FundPricingTier rename #2339, cached_total cancel/uncancel #2337), 3 issues closed
- [[2026-05-14 Meeting — pcms]] — pcms weekly sync, four-bucket client recap sent (1 PR shipped, 2 issues closed, 8 RFCO-pending, 8 requiring resolution)
- [[002-About Page as Auto-Populated Standardized Template]] — pcms, ADR 2026-05-08 **proposed**, replace free-text core About page with standardized template; services/equipment are source of truth
- [[Stakeholder Focus Groups for User Feedback]] — pcms, third / final focus group captured (2026-05-08); cores building external front ends, About-page architecture debate
- [[2026-04-30 Meeting — pcms]] — pcms weekly sync prep, chatbot questions, stakeholder focus group follow-up, stale PR flagged
- [[Core Browse UI Design]] — pcms, filterable card grid to replace the flat 130-core list; design ready for schema feasibility review
- [[PCMS Chatbot]] — pcms, general chatbot initiative (formerly Ragon-only); **SOW sent to client 2026-05-28** by [[Daniel Guettler]] to Andy/Jessica/Yovani/Tera, awaiting acceptance
- [[2026-04-27 Meeting — ilog]] — ilog stakeholder sync, ARC demo postponed by Kele, schedule logic clarified, chatbot interest opened
- [[Equipment and Services Tag Taxonomy]] — pcms, define tags for equipment and services, Eli owns the list
- [[Order Limit Raised to 1500 Deploy Hold]] — rpr PR #190, order cap raised to $1500, ✅ deployed to production 2026-04-24
- [[Radiology Badge Swipe Population Fix]] — people #1180, Access Logs showing 23 instead of 400+ for Radiology/Martinos, department mapping fix needed
- [[ARC Group iLog Demo]] — ilog, grapevine intel that Kele is demoing at ARC 2026-04-30, unconfirmed, tracking quietly
- [[2026-04-23 Meeting — pcms]] — pcms weekly sync, 5 PRs shipped, PI fund assignments, AR fix, invoice preview fix
- [[2026-04-09 Meeting — pcms]] — pcms weekly sync, Insight/Workday scoping accepted, general upload behavior confirmed
- [[General Upload Template Service Request Sync]] — pcms, uploads will mutate service requests, percentage-based split funding, retraining needed
- [[Secondary Container Expiration Rules]] — ilog, ✅ shipped 2026-04-21, SOP-based expiration rules for secondary containers
- [[001-Secondary Container Disassociation from Primary]] — ilog, ADR 2026-04-21, Kele approved disassociation, known DEA reporting tradeoff
- [[Registration Onboarding Workflow Redesign]] — ilog, smart form to reduce registration errors, mock-up pending
- [[Insight Square Footage Fields for CADE]] — cade, contacting Insight team re: square footage data availability
- [[Briefcase Billing Takeover]] — rcservices, third leg of the Chris Mow billing handoff; two-hop SSH pull verified from EC2 ([eris#1969](https://github.com/csb-ric/eris/issues/1969) parent + 4 children); blocked on legacy ruby parser source from Richard
- [[RFA Billing Takeover and Powerscale Migration]] — rcservices, billing code in production; usage importer in progress ([eris#1962](https://github.com/csb-ric/eris/issues/1962), started 2026-06-10)
- [[Storage Usage Billing Pipeline Takeover]] — rcservices, MAD3 takeover from Chris Mow restarted; Isilon API path in production; June parallel-run, July full cutover
- [[RFA ServiceNow Provisioning Pipeline]] — rcservices, ✅ complete, live in production 2026-04-16
- [[AzureVM Import via Azure Export API]] — rcservices #1913, ✅ complete, live in production 2026-04-10
- [[FreezerPro RedCap Integration]] — rcservices PR #1854, active; schema + report-API delivery agreed 2026-06-11, importer gated on Svetlana's API tokens

## Decisions Log

Cross-project decisions. Project-specific ADRs live in each project's `decisions/` folder.

| Date | Decision | Project | Status | Link |
|------|----------|---------|--------|------|
| 2026-06-08 | FundingSource (from Insight) as cost-ownership authority | rcfinops | accepted | [[002-FundingSource as Cost-Ownership Authority]] |
| 2026-06-03 | Azure usage dashboard as a standalone app | rcfinops | accepted | [[001-Standalone Azure Usage Dashboard App]] |
| 2026-05-27 | BriefCase usage billing statistic (avg vs p75) | rcservices | proposed | [[003-BriefCase Usage Billing Statistic]] |
| 2026-05-25 | Fluent 2 as modal design system | rcservices | accepted | [[002-Fluent 2 Modal Design System]] |
| 2026-05-08 | About page as auto-populated standardized template | pcms | proposed | [[002-About Page as Auto-Populated Standardized Template]] |
| 2026-04-21 | Secondary container disassociation from primary | ilog | accepted | [[001-Secondary Container Disassociation from Primary]] |
| 2026-04-09 | Insight vs Workday data source scoping | pcms | accepted | [[001-Insight vs Workday Data Source Scoping]] |
| 2026-04-06 | FreezerPro REDCap integration model | rcservices | accepted | [[001-FreezerPro REDCap Integration Model]] |

## Open Questions

-

## Archive

Completed or sunset projects moved from `work/projects/` to `work/archive/`.

-
