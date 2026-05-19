---
date: "2026-04-05"
description: "Minor Intake Form — staff request permission for minors on campus with approval workflow (lab_archives repo, Minor intake form label)"
project: "minr"
status: active
rails_version: "8.0"
ruby_version: "3.4.4"
aliases:
  - Minor Intake Form
  - minr
tags:
  - project
---

# Minor Intake Form

## Overview

Allows staff at a research hospital to request permission for a minor to be on campus for a set period of time. Requests go through an approval workflow.

## Repository & Deploy

- **Repo**: [csb-ric/lab_archives](https://github.com/csb-ric/lab_archives/)
- **Issues**: [Minor intake form issues](https://github.com/csb-ric/lab_archives/issues?q=label%3A%22Minor+intake+form%22)
- **Production**:
- **Staging**:
- **Deploy method**:

## Tech Stack

- **Rails**: 8.0 (upgrade to 8.1 pending — see [[lab_archives Rails 8.1 Upgrade]])
- **Ruby**: 3.4.4
- **Database**:
- **Key gems**:

## Stakeholders

- [[Kele Piper]] — Chief Research Compliance Officer
- [[Mirabella Daguerre]] — Research Integrity Program Manager

## Compliance Notes


## Architecture Notes

Shared codebase with other projects in lab_archives. Minr-specific work is scoped by the "Minor intake form" GitHub label.

## Active Notes

- [[Approvals by Institution]] — **active, blocked** ([lab_archives#1187](https://github.com/csb-ric/lab_archives/issues/1187)). Kele wants approvals routed by institution; waiting on the institution → approver mapping.
- [[Plan to Extract minr from lab_archives]] — plan to split minr into its own app out of the shared lab_archives repo.

## Related

- [[Index]]
- [[CADE]] — also in the lab_archives repo
- [[People|people]] — also in the lab_archives repo
- [[Research Intake Survey|ris]] — also in the lab_archives repo
