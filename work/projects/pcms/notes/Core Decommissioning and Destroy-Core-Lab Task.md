---
date: "2026-06-30"
description: "Decommissioning retired PCMS cores (PST, MVVC, CCIBDNA) by removing bespoke per-core namespaces, plus a generic destroy-core-lab rake task generalizing the pattern."
project: pcms
status: active
tags:
  - work-note
---

# Core Decommissioning and Destroy-Core-Lab Task

## Context

PCMS carried bespoke per-core customization namespaces for individual core labs. As cores retire, that dead code needs removing — and the removal had been hand-rolled as a one-off PR per core. This window (2026-06-30) both cleared three retired cores and started generalizing the process so future decommissions are a rake task, not a bespoke PR.

## What shipped (merged to master)

Three core decommissions, each removing the core's dead/bespoke customization namespace:

- **PST** — [#2376](https://github.com/csb-ric/pcms/pull/2376) (`e599bad2`)
- **MVVC** — [#2374](https://github.com/csb-ric/pcms/pull/2374) (`b81e627e`)
- **CCIBDNA** — [#2375](https://github.com/csb-ric/pcms/pull/2375) (`676b8ea4`)

Followed by a DB schema regen for Rails 8.1 (`0c16be33`) to reflect the removals.

## In progress (unmerged)

- **`chore/destroy-core-lab-task`** branch (3 commits, `a6febd1c` → `f1df77b2`, 2026-06-30) — a generic rake task to fully destroy a core lab, with orphan-menu sweep hardening. This is the generalization of the three manual removals above: rather than a bespoke PR per retired core, a single task that tears a core down cleanly. Not yet merged to `master`/`development`.

## Why it matters

Removing dead per-core namespaces reduces the surface area that every future refactor (e.g. the [[PCMS Rails 8.1 Upgrade]]) has to carry. The destroy-core-lab task turns a recurring manual chore into a repeatable operation — worth watching whether it lands and becomes the standard decommission path.

## Related

- [[PCMS]]
- [[PCMS Rails 8.1 Upgrade]] — the schema regen (`0c16be33`) rode on the 8.1 work
- [[Index]]
