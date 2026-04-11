---
date: "2026-04-06"
description: "Automate AzureVM usage import via Azure Export API — build import, send sample CSV to stakeholders for review"
project: "rcservices"
github_issue: 1913
status: completed
tags:
  - work-note
---

# AzureVM Import via Azure Export API

## Context

Automating the import of AzureVM usage data into [[RC Services (Eris)|rcservices]] via the Azure Export API. Currently on the `azure-api-access` branch (not yet pushed).

## Status

**Completed 2026-04-10.** Meter category filtering implemented and merged.

## Meter Category Exclusions (2026-04-08)

Exclude these categories from the usage import (decided by [[Rakesh Jain]]):
- Virtual Networking
- Bandwidth
- Azure DNS
- Networking

## Done

1. ~~Finish the AzureVM import implementation~~
2. ~~Export a sample CSV of 5-6 VMs~~
3. ~~Send to [[Michael Rogal]] and [[Alissa Scharf]] via Teams for review~~
4. ~~Get meter category filtering decision from Rakesh/Ed Austin~~

## Related

- [[RC Services (Eris)|rcservices]]
- [[Alissa Scharf]]
