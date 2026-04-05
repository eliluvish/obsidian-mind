---
description: "Recurring patterns and conventions discovered across work — architecture, naming, tooling, and implementation patterns"
tags:
  - brain
---

# Patterns

Recurring patterns discovered across work.

## Shared Repo with Label Scoping (lab_archives)

The [csb-ric/lab_archives](https://github.com/csb-ric/lab_archives/) repo hosts multiple projects, each scoped by GitHub issue label:

- [[CADE]] — "CADE" label
- [[Minor Intake Form|minr]] — "Minor intake form" label
- [[Research Intake Survey|ris]] — "Research Intake Survey" label
- [[People|people]] — everything else (no specific label)

All deploy to https://people.mgh.harvard.edu. The direction is to **extract standalone apps** (like [[BioLift|biolift]]) rather than adding more modules. [[Minor Intake Form|minr]] extraction approved by [[Kele Piper]], pending after busy season. [[Research Intake Survey|ris]] will be standalone from the start.
