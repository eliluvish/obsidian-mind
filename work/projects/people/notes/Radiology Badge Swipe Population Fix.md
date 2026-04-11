---
date: "2026-04-10"
description: "Fix Access Logs to show full Radiology/Martinos population — add missing department mappings for badge swipe reporting"
project: "people"
github_issue: 1180
status: active
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

## Next Steps

- [ ] Investigate how department mappings currently work in the People app
- [ ] Determine if the four departments above fully cover the ~405 population Stacey expects
- [ ] Implement the fix per #1180

## Related

- [[People|people]]
- [[Stacey Ladieu]]
