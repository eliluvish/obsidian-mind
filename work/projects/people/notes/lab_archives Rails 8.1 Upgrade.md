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

**In progress (on `development`, not yet on master/deployed).** Discovered via repo-sync 2026-06-10: the `upgrade-rails-8` branch has been merged into `development` — includes an Oracle `DESC` error fix and a webpacker → esbuild swap (`11fda816`). Not yet promoted to master, so nothing has deployed. Repo-wide upgrade — one effort covers all four projects since they share the codebase.

## Action Items

- [x] Bump Rails 8.0 → 8.1, update `Gemfile` / dependencies — on `development`
- [x] Reconcile framework defaults / asset pipeline (webpacker → esbuild) — on `development`
- [ ] Full test suite green on `development`
- [ ] Promote `development` → master
- [ ] Smoke-test each project surface (people, cade, minr, ris) before deploy
- [ ] Update `rails_version` in cade / minr / ris READMEs once shipped

## Related

- [[People|people]]
- [[CADE]]
- [[Minor Intake Form|minr]]
- [[Research Intake Survey|ris]]
- [[Index]]
