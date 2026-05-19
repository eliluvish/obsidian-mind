---
date: "2026-04-05"
description: "Biological sample transport between research hospital facilities — bills of lading for couriers"
project: "biolift"
status: active
rails_version: "8.1"
ruby_version: "3.4.4"
aliases:
  - BioLift
  - biolift
tags:
  - project
---

# BioLift

## Overview

Facilitates the transport of biological samples between research hospital facilities. Creates bills of lading for couriers.

## Repository & Deploy

- **Repo**: [csb-ric/biolift](https://github.com/csb-ric/biolift)
- **Production**: https://biolift.mgb.org
- **Staging**: https://biolift-stage.mgb.org
- **Deploy method**: Manual

## Tech Stack

- **Rails**: 8.1
- **Ruby**: 3.4.4
- **Database**: mySQL 8

## Stakeholders

- [[Kele Piper]] — Chief Research Compliance Officer
- [[Mirabella Daguerre]] — Research Integrity Program Manager
- [[Kathryn Holthaus]] — Director of Lab Safety and Research Subject Protection, BWH

## Compliance Notes

None currently.

## Architecture Notes

## Active Notes

- [[Refactor js.erb to Turbo]] — **priority, not started** ([biolift#20](https://github.com/csb-ric/biolift/issues/20)). Remove legacy `.js.erb` → Turbo; Rails 8.1 tech debt. Original ~2026-05-07 target slipped.

## Related

- [[work/Index|Work Index]]
- [[iLog]] — same stakeholders (Kele Piper, Mirabella Daguerre)
- [[Minor Intake Form|minr]] — same stakeholders
