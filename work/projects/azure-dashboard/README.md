---
date: "2026-06-03"
description: "New standalone Rails app — a self-service dashboard for researchers to view their Azure cloud usage; pulls from Azure independently of eris billing"
project: "azure-dashboard"
status: active
rails_version:
ruby_version:
aliases:
  - Azure Usage Dashboard
  - azure-dashboard
tags:
  - project
---

# Azure Usage Dashboard

> [!note] Working name
> `azure-dashboard` is a placeholder slug. Rename the folder via `git mv` once the app/repo name is settled.

## Overview
A new, standalone Rails application giving researchers a self-service view of their Azure cloud usage. Decided 2026-06-03 (see [[001-Standalone Azure Usage Dashboard App]]). Spun out of the [[RC Services (Eris)|rcservices]] Azure work but built as a separate app — eris already *imports* Azure VM usage for billing ([[AzureVM Import via Azure Export API]]); this is the researcher-facing *reporting* surface.

## Repository & Deploy
- **Repo**: TBD — new app, not yet created
- **Production**: TBD
- **Staging**: TBD
- **Deploy method**: TBD

## Tech Stack
- **Rails**: TBD (eris is on 8.1)
- **Ruby**: TBD
- **Database**: TBD
- **Key gems**: TBD

## Stakeholders
- **Department**: [[Research Computing Core]]
- [[Alissa Scharf]] — Manager, Research Computing Core
- [[Michael Oates]] — Director, Research Computing
- **Audience**: researchers (self-service) — distinct from eris's internal/finance billing audience

## Compliance Notes
TBD — confirm what Azure usage data is shown and whether any of it is sensitive.

## Architecture Notes
- Pulls Azure usage data **independently** from the Azure Export API — does not read from eris's billing import pipeline. (Decided 2026-06-03.)

## Active Notes
-

## Decisions
- [[001-Standalone Azure Usage Dashboard App]] — researcher-facing dashboard built as a separate Rails app, pulling from Azure independently rather than extending eris.

## Related
- [[Index]]
- [[RC Services (Eris)|rcservices]]
- [[AzureVM Import via Azure Export API]]
