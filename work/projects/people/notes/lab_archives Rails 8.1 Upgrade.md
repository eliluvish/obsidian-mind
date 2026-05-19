---
date: "2026-05-18"
description: "Upgrade the shared lab_archives Rails app (serves people, cade, minr, ris) from Rails 8.0 to 8.1"
project: people
github_issue:
status: active
tags:
  - work-note
---

# lab_archives Rails 8.1 Upgrade

## Context

The `csb-ric/lab_archives` repo is **one Rails app** that serves four vault projects — [[People|people]], [[CADE]], [[Minor Intake Form|minr]], and [[Research Intake Survey|ris]] — scoped by GitHub issue labels. It is currently on **Rails 8.0** and needs to be upgraded to **Rails 8.1**.

> [!note] Vault correction
> The people/cade/minr READMEs previously listed `rails_version: 8.1` — that was inaccurate. The shared app is on 8.0; 8.1 is the upgrade target. people README corrected 2026-05-18; cade/minr/ris pending.

## Status

**Not started.** Repo-wide upgrade — one PR/effort covers all four projects since they share the codebase.

## Action Items

- [ ] Bump Rails 8.0 → 8.1, update `Gemfile` / dependencies
- [ ] Run `rails app:update`, reconcile framework defaults
- [ ] Full test suite green
- [ ] Smoke-test each project surface (people, cade, minr, ris) before deploy
- [ ] Update `rails_version` in cade / minr / ris READMEs once shipped

## Related

- [[People|people]]
- [[CADE]]
- [[Minor Intake Form|minr]]
- [[Research Intake Survey|ris]]
- [[Index]]
