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

## Prefer Request Specs over System Specs

Default to **request specs** for controller/endpoint coverage; reserve system (Capybara/browser) specs for flows that genuinely need a real browser (JS-driven interactions, Turbo/Stimulus behavior). Request specs are faster and less flaky — no browser automation, no headless-driver fragility — and authenticate by actually POSTing to the login path rather than stubbing auth methods.

- **Greenfield example**: [[RC FinOps|rcfinops]] (`cloud_costs`) was built request-spec-first — the RBAC/permissions-matrix and line-item-browser coverage is request specs, with system specs only where the dashboard's interactive affordances require a browser.
- **Conversion example**: [[BioLift|biolift]] converted its existing Capybara system specs (dropped_off, missing_specimen, received) to request specs (`5482673`), citing speed and reliability and shifting auth from mocked methods to real POST login. The same tradeoff applies across the Rails apps.
