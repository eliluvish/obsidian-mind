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

✅ Shipped. Department mapping fix deployed to production. Issue #1180 closed 2026-04-23.

Landed via **PR #1182** (`2ab24d19`, 2026-04-14): the flat exact-match department hash in `DepartmentMappable` was replaced with a `DeptMapping` lookup supporting ordered fallback rules (String / Regexp / Proc via `===`). The first rule added — `/\ARad Rsch\b/i → "Radiology"` — is what pulls the `Rad Rsch *` departments back into the Radiology population. The pattern-based approach means future department-normalization gaps can be fixed by adding a rule rather than enumerating every variant.

## Follow-on: PIs Missing from Report

Stacey (or the team) now asking why PIs aren't appearing on the report. New open question — unclear if this is a separate mapping gap, a role/type filter, or a different data source issue.

## Next Steps

- [ ] Investigate why PIs are excluded from the badge swipe report
- [ ] Determine if it's a department mapping issue, a role-based filter, or something else
- [ ] Fix and ship

## Related

- [[People|people]]
- [[Stacey Ladieu]]
