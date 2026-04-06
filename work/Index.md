---
description: "Central map of all projects, work notes, and decisions"
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

## Recent Notes

- [[AzureVM Import via Azure Export API]] — rcservices #1913, code complete, blocked on meter category filtering
- [[FreezerPro RedCap Integration]] — rcservices PR #1854, on hold pending REDCap schema

## Decisions Log

Cross-project decisions. Project-specific ADRs live in each project's `decisions/` folder.

| Date | Decision | Project | Status | Link |
|------|----------|---------|--------|------|
| 2026-04-06 | FreezerPro REDCap integration model | rcservices | accepted | [[001-FreezerPro REDCap Integration Model]] |

## Open Questions

-

## Archive

Completed or sunset projects moved from `work/projects/` to `work/archive/`.

-
