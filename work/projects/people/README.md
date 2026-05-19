---
date: "2026-04-05"
description: "Employee data aggregation from multiple sources for deductions processing"
project: "people"
status: active
rails_version: "8.0"
ruby_version: "3.4.4"
aliases:
  - People
  - people
tags:
  - project
---

# People

## Overview

Aggregates employee information from various data sources to make deductions.

## Repository & Deploy

- **Repo**: [csb-ric/lab_archives](https://github.com/csb-ric/lab_archives/)
- **Issues**: [All lab_archives issues](https://github.com/csb-ric/lab_archives/issues) excluding CADE and Minor intake form labels
- **Production**: https://people.mgh.harvard.edu
- **Staging**:
- **Deploy method**:

## Tech Stack

- **Rails**: 8.0 (upgrade to 8.1 pending — see [[lab_archives Rails 8.1 Upgrade]])
- **Ruby**: 3.4.4
- **Database**:
- **Key gems**:

## Stakeholders

- [[Stacey Ladieu]] — Project Manager, Martinos Center (badge swipe access logs)

## Compliance Notes

None currently.

## Architecture Notes

Shared codebase with [[CADE]] and [[Minor Intake Form|minr]] in the lab_archives repo. Each project is scoped by GitHub issue labels.

## Active Notes

- [[lab_archives Rails 8.1 Upgrade]] — **active**. Upgrade the shared lab_archives app (people/cade/minr/ris) from Rails 8.0 → 8.1.
- **Week of 2026-04-28**: investigate why Active Directory sync is slow — benchmark it. _(still open)_

## Related

- [[work/Index|Work Index]]
- [[CADE]] — also in the lab_archives repo
- [[Minor Intake Form|minr]] — also in the lab_archives repo
- [[Research Intake Survey|ris]] — also in the lab_archives repo
