---
date: "2026-04-08"
description: "Smart onboarding workflow for iLog registration — gatekeeping questions to reduce errors, skip irrelevant sections for practitioner licenses"
project: "ilog"
github_issue: 683
status: active
tags:
  - work-note
---

# Registration Onboarding Workflow Redesign

## Context

Chat with [[Mirabella Daguerre]] on 2026-04-08. Investigators are confused by the current registration flow — gatekeeping mechanisms aren't clear enough, leading to errors. Eli and Mirabella agreed to redesign the onboarding experience. [[Kele Piper]] has been thinking along the same lines — a "smart form" that guides users to the right form and eliminates irrelevant questions.

## Problem Areas

### Schedule Selection by Registration Type

- Practitioner registrations **do not allow** Schedule I drugs — but the UI currently lets users select them
- Each registration type should only show the schedules it's eligible for

### Practitioner License (IND Registration) — Pharmacy Storage

- A PI with a practitioner license = someone with only an **IND (Investigational New Drug)** registration
- If they store drugs in the **research pharmacy**, they don't need to answer questions about:
  - Location of drugs
  - Dispensing
  - Disposal
  - Inventory
- For this population, iLog is only used to **document their registration** — the pharmacy handles everything else

### Gatekeeping Question: Human vs. Animal Research

- Splitting the registration into tabs creates an opportunity to ask upfront: **human subject research or animal research?**
- This answer determines which schedules and license types are available

## Proposed Solution: Onboarding Workflow

A step-by-step "smart form" approach (similar to how [[Research Intake Survey|ris]] works — the form cuts off when the user doesn't need to complete further sections).

- First step in the "new registration" modal: select institution
- Gatekeeping questions early to route users to the right form
- Skip entire sections that don't apply (e.g., pharmacy-stored practitioner registrations skip location/dispensing/disposal/inventory)

## Action Items

- [ ] Eli to write up detailed table explaining the logic for each registration type and send to [[Mirabella Daguerre]]
- [ ] Eli to mock up the onboarding workflow

## Related

- [[iLog]]
- [[Mirabella Daguerre]]
- [[Kele Piper]]
- [[Authorized User Log Rules and Training Changes]]
- [[Research Intake Survey|ris]] — onboarding workflow pattern inspiration
