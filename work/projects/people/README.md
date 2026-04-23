---
date: "2026-04-05"
description: "Employee data aggregation from multiple sources for deductions processing"
project: "people"
status: active
rails_version: "8.1"
ruby_version: "3.4.4"
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

- **Rails**: 8.1
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

- **Week of 2026-04-28**: investigate why Active Directory sync is slow — benchmark it.

## Related

- [[work/Index|Work Index]]
- [[CADE]] — also in the lab_archives repo
- [[Minor Intake Form|minr]] — also in the lab_archives repo
- [[Research Intake Survey|ris]] — also in the lab_archives repo
