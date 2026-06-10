---
date: "2026-06-03"
description: "Standalone Rails app — researcher-facing dashboard for cloud cost usage (Azure now, AWS later); pulls from Azure independently of eris billing, role-scoped via FundingSource/Insight"
project: "rcfinops"
status: active
rails_version: "8.1"
ruby_version: "3.4.4"
aliases:
  - RC FinOps
  - Azure Usage Dashboard
  - cloud_costs
  - rcfinops
  - azure-dashboard
tags:
  - project
---

# RC FinOps — Cloud Cost Dashboard

> [!note] Naming
> Slug settled as `rcfinops` (was the `azure-dashboard` placeholder) — the repo is `csb-ric/rcfinops` (dir `cloud_costs`), named broader than Azure to leave room for AWS usage later. "Azure Usage Dashboard" kept as an alias.

## Overview
A standalone Rails application giving researchers a self-service view of their cloud usage (Azure today; AWS is a possible later addition). Decided 2026-06-03 (see [[001-Standalone Azure Usage Dashboard App]]). Spun out of the [[RC Services (Eris)|rcservices]] Azure work but built as a separate app — eris already *imports* Azure VM usage for billing ([[AzureVM Import via Azure Export API]]); this is the researcher-facing *reporting* surface, with its own role-based access scoped against funding ownership.

## Repository & Deploy
- **Repo**: [csb-ric/rcfinops](https://github.com/csb-ric/rcfinops) (local dir `~/dev/cloud_costs`)
- **Production**: TBD — not yet deployed
- **Staging**: TBD
- **Deploy method**: TBD

## Tech Stack
- **Rails**: 8.1
- **Ruby**: 3.4.4
- **Database**: MySQL via Trilogy adapter
- **Key gems**: rspec, FactoryBot, rubocop, i18n-tasks, simplecov; Tailwind + Turbo Streams for the UI

## Status
Greenfield app, ~1 week old — went from `initial commit` (2026-06-04) to a multi-feature Rails app by 2026-06-10. See [[RC FinOps Week-1 Build Log]] for the full arc. Built so far:
- Azure cost import pipeline (`AzureCostLineItem`)
- Role-based access control + site administration (groups, permissions matrix, users)
- `FundingSource` model enriched from Insight, scoping the dashboard by role — see [[002-FundingSource as Cost-Ownership Authority]]
- MGB-subsidy flagging + filtering across dashboard and line-item index — see [[MGB Subsidy Flagging Business Rule]]
- Faceted line-item browser (role-based facets, free-text search, `visible_to` UNION scope)

> [!warning] Unpushed work
> As of 2026-06-10, `main` is **16 commits ahead of `origin/main`** (today's refactor/UX burst) and branch **`add-vm-name`** (resource group in search scope) sits off `main`, ready to merge. Push before treating this as the source of truth.

## Stakeholders
- **Department**: [[Research Computing Core]]
- [[Michael Rogal]] — Senior Project Specialist, Research Computing Core
- [[Alissa Scharf]] — Manager, Research Computing Core
- [[Michael Oates]] — Director, Research Computing
- **Audience**: researchers (self-service) — distinct from eris's internal/finance billing audience

## Compliance Notes
Open review: [[RC FinOps Cost Data Visibility Review]] — what data is shown, whether any is sensitive, and whether role-scoped + MGB-subsidy visibility (PI vs. admin) needs formal sign-off. Not yet reviewed.

## Architecture Notes
- Pulls Azure usage data **independently** from the Azure Export API — does not read from eris's billing import pipeline. (Decided 2026-06-03.)
- `FundingSource` (enriched from Insight) is the authority for who owns a cost line item; dashboard visibility is scoped by user role against it. (See [[002-FundingSource as Cost-Ownership Authority]].)

## Active Notes
- [[RC FinOps Week-1 Build Log]] — greenfield build arc, Jun 4–10
- [[MGB Subsidy Flagging Business Rule]] — subsidized line-item flagging + role-scoped filtering

## Decisions
- [[001-Standalone Azure Usage Dashboard App]] — researcher-facing dashboard built as a separate Rails app, pulling from Azure independently rather than extending eris.
- [[002-FundingSource as Cost-Ownership Authority]] — `FundingSource` enriched from Insight defines who owns a cost line item; dashboard scoped by role against it.

## Related
- [[Index]]
- [[RC Services (Eris)|rcservices]]
- [[AzureVM Import via Azure Export API]]
