---
date: "2026-04-05"
description: "Center for Academic Development and Enrichment — multi-project Rails 8.1 app (lab_archives repo, CADE label)"
project: "cade"
status: active
rails_version: "8.0"
ruby_version: "3.4.4"
aliases:
  - CADE
  - cade
tags:
  - project
---

# CADE

Center for Academic Development and Enrichment.

## Overview

CADE is one of several projects served by the lab_archives application. Work is tracked via GitHub Issues with the **CADE** label.

**Billing**: CADE is now billed **directly** (as of 2026-05-18).

## Repository & Deploy

- **Repo**: [csb-ric/lab_archives](https://github.com/csb-ric/lab_archives/)
- **Issues**: [CADE-labeled issues](https://github.com/csb-ric/lab_archives/issues?q=label%3ACADE)
- **Production**: https://people.mgh.harvard.edu
- **Staging**: N/A
- **Deploy method**: Manual

## Tech Stack

- **Rails**: 8.0 (upgrade to 8.1 pending — see [[lab_archives Rails 8.1 Upgrade]])
- **Ruby**: 3.4.4
- **Database**: mySQL 8.0

## Stakeholders

- [[Karan Patel]] — Director of Administration
- [[Rowan Potter]] — Senior Data Analyst
- [[Matthew Crowson]] — Director
- [[Allison Moriarty]] — Senior VP, Research Operations (Insight data sponsor, escalation point)

## Architecture Notes

Shared codebase with other projects in lab_archives. CADE-specific work is scoped by the CADE GitHub label.

## Active Notes

- [[Insight Fund Fields Request from CADE]] — **active**. Rowan Potter requested fund/grant fields from Insight; blocked on the new Insight API build. Near-term: CSV → people. Escalation: [[Allison Moriarty]] → [[Jane Murray]].
- [[Insight Square Footage Fields for CADE]] — **active**. Square footage / wet-vs-dry lab data; formal request to Insight helpdesk pending ([[Andrew Chase]] as sponsor).
- [[Workday API Access for Missing Grant Fields]] — ongoing. 3 grant fields not in Insight; ticket INC4967792, awaiting Workday API access.

## Related

- [[Index]]
- [[Minor Intake Form|minr]] — also in the lab_archives repo
- [[People|people]] — also in the lab_archives repo
- [[Research Intake Survey|ris]] — also in the lab_archives repo
