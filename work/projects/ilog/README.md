---
date: "2026-04-05"
description: "DEA controlled substances compliance — inventory, logbooks, accountability, Form 41 generation"
project: ilog
status: active
rails_version: "8.1"
ruby_version: "3.4.4"
aliases:
  - iLog
  - ilog
tags:
  - project
---

# iLog

## Overview
DEA controlled substances compliance application. Handles inventory tracking, accountability logbooks, and regulatory form generation (e.g., DEA Form 41).

## Repository & Deploy
- **Repo**: https://github.com/csb-ric/compliance
- **Default branch**: master
- **Production**:
- **Staging**:
- **Deploy method**: Manual

## Tech Stack
- **Rails**: 8.1
- **Ruby**: 3.4.4
- **Database**:
- **Key gems**:

## Stakeholders
- **Department**: [[Compliance, Audit & Business Integrity]]
- [[Kele Piper]] — Chief Research Compliance Officer
- [[Mirabella Daguerre]] — Research Integrity Program Manager
- [[Kathryn Holthaus]] — Director of Lab Safety and Research Subject Protection, BWH

## Compliance Notes
DEA-regulated application. Handles controlled substance inventory and accountability records.

## Architecture Notes

- Row-level authorization is centralized in shared concerns — `PermissionScopable#permission_scope` (controller) and `Ownable#owned_by` (model), extracted from 21 controllers in `777e6318` (2026-06). `ContainerAuditScopable` intentionally keeps an inline copy due to different tenant semantics. See [[Patterns#Row-Level Authorization as a Shared Concern]].
- **Unmerged feature work** (as of Jun 2026): `development` branch carries ModalFormComponent conversions (DEA visits, buildings, tenant contacts, missing substances), Bootstrap→esbuild migration, and date-field modernization; `reg-group-ui-fix` carries registration-group UI fixes. Not yet on `master`.

## Active Notes

- [[Accountability Logbook Testing Feedback]] — **active**. Open testing-feedback tickets (compliance #718–724); the Kele/Mirabella set, current North Star goal. Beta path unchanged (no movement).
- [[Container Disposition Balance Fix]] — correctness fix shipped on `master` (`fa274dcf`, 2026-06-22): disposition balance now subtracts recorded losses; DEA accountability implication, no historical review needed (feature not yet in production)
- [[2026-04-27 Meeting — ilog]] — stakeholder sync: ARC demo postponed, schedule logic clarified, chatbot interest opened
- [[Registration Onboarding Workflow Redesign]] — wireframes **complete**; implementation deferred until after the logbook ships (wireframe branch `experiment-1-onboarding-workflow-no-pdf-processing` still seeing iteration as of Jun 2026)
- [[Authorized User Log Rules and Training Changes]]
- [[Destruction Workflow and DEA Form 41 Process]]
- [[ARC Group iLog Demo]] — ✅ resolved 2026-04-27 (Kele postponed)

## Decisions

- [[001-Secondary Container Disassociation from Primary]] — 2026-04-21, Kele approved; DEA reporting cost noted

## Related
- [[Index]]
