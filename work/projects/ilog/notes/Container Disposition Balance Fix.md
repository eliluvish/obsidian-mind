---
date: "2026-06-22"
description: "iLog correctness fix — disposition balance ignored recorded losses, letting containers with losses accept over-dispensation and go negative; DEA accountability implication. Shipped on master; feature not yet in production."
project: "ilog"
github_issue:
status: active
tags:
  - work-note
---

# Container Disposition Balance Fix

> [!info] Status
> Fix **shipped on `master`** (`fa274dcf`, captured via [[repo-sync]] 2026-06-22). No historical-record review needed — the disposition feature is **not yet in production**, so no real records were created under the old logic.

## Context

The `DispositionRecord` amount validation guards how much can be dispensed/disposed from a container against the available balance. It was computing available balance as `effective_start_amount − prior dispensations` — **ignoring recorded losses**.

## What broke

A container with recorded losses would compute too high a remaining balance, so it would **accept additional dispensations that drove the true balance negative**. In a DEA-regulated app, that means accountability records could show phantom remaining amounts — a correctness bug with direct regulatory implications, not a cosmetic one.

## The fix

`fix(dispositions): subtract losses from remaining` (`fa274dcf`) — available balance now subtracts recorded losses alongside prior dispensations. Shipped with a regression test proving the previously-accepted over-dispensation is now rejected.

## Related

- [[iLog]]
- [[Destruction Workflow and DEA Form 41 Process]] — loss/disposal accounting feeds the Form 41 process
- [[Index]]
