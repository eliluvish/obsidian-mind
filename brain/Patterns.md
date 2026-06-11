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

## A Polished Build Doubles as a Design Proof-Point

AI-generated, brand-aligned UI is cheap enough now that a finished app in one project becomes the sales pitch for redesigning another. The old blocker for UI work — hire a design agency, then hand-implement their comps — is gone; asking AI for ~5 MGB-branded options and picking one is minutes of work, not a budget line.

- **Source**: at the [[2026-06-11 Meeting — pcms|2026-06-11 PCMS sync]], demoing the MGB-branded [[RC FinOps|rcfinops]] dashboard ("a consultancy failed us — AI does the design now") sold [[Jessica Cho]] on a PCMS facelift on the spot. Outdated UI had been flagged across all three focus groups but never actioned because UI never gets budget. The live demo turned a known-but-parked complaint into an agreed direction → [[PCMS UI Facelift]].
- **Why it matters**: ships toward the [[North Star]] "manager of agents / AI-first" aspiration. Practically — keep a polished reference build handy; it's more persuasive than a deck, and it reframes "we can't afford a redesign" as "redesign is now cheap."
