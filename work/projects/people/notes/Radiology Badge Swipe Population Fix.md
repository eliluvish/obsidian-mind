---
date: "2026-04-10"
description: "Fix Access Logs to show full Radiology/Martinos population — add missing department mappings for badge swipe reporting"
project: "people"
github_issue: 1180
status: in-progress
tags:
  - work-note
---

# Radiology Badge Swipe Population Fix

## Context

[[Stacey Ladieu]] (Martinos Center PM) reported that the Access Logs page at people.mgh.harvard.edu only shows 23–24 people for Radiology/Martinos, down from the ~405 it previously showed. The issue is not permissions — it's how the People app identifies group membership using pre-Workday department mappings.

## Problem

The system relies on imperfect, pre-Workday department mappings and can't definitively answer "show me everyone in Radiology" or "everyone at the Martinos Center." The population dropped because the mapping no longer covers all the relevant departments.

## Target Departments

From the issue, the departments to include:

- NMR Physicians
- NMR Center
- Rad Rsch ResAdm
- Rad Rsch Mart

## Status

✅ Shipped. Department mapping fix deployed to production.

## Follow-on: PIs Missing from Report

Stacey (or the team) now asking why PIs aren't appearing on the report. New open question — unclear if this is a separate mapping gap, a role/type filter, or a different data source issue.

## Next Steps

- [ ] Investigate why PIs are excluded from the badge swipe report
- [ ] Determine if it's a department mapping issue, a role-based filter, or something else
- [ ] Fix and ship

## Related

- [[People|people]]
- [[Stacey Ladieu]]
