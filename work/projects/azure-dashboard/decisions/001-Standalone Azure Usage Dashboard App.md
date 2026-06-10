---
date: "2026-06-03"
description: "Build the researcher-facing Azure usage dashboard as a separate Rails app pulling from Azure independently, rather than extending eris"
project: "azure-dashboard"
status: accepted
tags:
  - decision
---

# 001 — Standalone Azure Usage Dashboard App

## Context

[[RC Services (Eris)|rcservices]] (eris) already imports Azure VM usage data for **billing** via the Azure Export API ([[AzureVM Import via Azure Export API]]). There's now a need to give **researchers** a self-service view of their own Azure cloud usage — a different audience (researchers, not finance) and a different purpose (reporting/visibility, not pass-through billing).

The question was whether to build this reporting surface into eris or stand up a separate application.

## Options Considered

1. **Extend eris** — add a researcher-facing usage dashboard inside the existing rcservices app, reusing the Azure usage data it already imports.
2. **New standalone Rails app** — a dedicated application that pulls Azure usage from the Azure Export API independently.

## Decision

Build a **new, standalone Rails application** (option 2). It will pull Azure usage data **independently** from the Azure Export API, separate from eris's billing import pipeline.

> [!question] Rationale to confirm
> Capture *why* a separate app was chosen over extending eris (audience separation, deploy/access boundaries, billing-vs-reporting concerns, etc.) — recorded as the decision but the reasoning wasn't detailed at capture time.

## Consequences

- A new app to scaffold, deploy, and maintain — repo, Rails/Ruby versions, DB, and deploy target all TBD.
- Two independent Azure Export API consumers (eris for billing, this app for researcher reporting). Watch for duplicated import logic and potential API rate/quota overlap.
- Researcher-facing audience implies different auth/access and possibly different compliance review than eris's internal billing surface.

## Related

- [[Azure Usage Dashboard]] — project README
- [[RC Services (Eris)|rcservices]]
- [[AzureVM Import via Azure Export API]] — eris's existing Azure billing import
