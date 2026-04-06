---
date: "2026-04-06"
description: "Automate AzureVM usage import via Azure Export API — build import, send sample CSV to stakeholders for review"
project: "rcservices"
github_issue: 1913
status: blocked
tags:
  - work-note
---

# AzureVM Import via Azure Export API

## Context

Automating the import of AzureVM usage data into [[RC Services (Eris)|rcservices]] via the Azure Export API. Currently on the `azure-api-access` branch (not yet pushed).

## Status

Code complete. PR open, pending decision from [[Rakesh Jain]] and [[Henry Ed Austin]] on which meter categories to filter out. Will merge once filtering is confirmed.

## Done

1. ~~Finish the AzureVM import implementation~~
2. ~~Export a sample CSV of 5-6 VMs~~
3. ~~Send to [[Michael Rogal]] and [[Alissa Scharf]] via Teams for review~~

## Waiting On

- [[Rakesh Jain]] and [[Henry Ed Austin]] — decide which Azure meter categories to filter out

## Related

- [[RC Services (Eris)|rcservices]]
- [[Alissa Scharf]]
