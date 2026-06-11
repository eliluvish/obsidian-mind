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

**Merged to master 2026-06-10** (PR [#1189](https://github.com/csb-ric/lab_archives/pull/1189), `f39c535e`). Rails **8.0.5 → 8.1.3**, validated with `next_rails` dual-boot (suite green on both versions before cutover). Net 30 files, +461/−563. Repo-wide upgrade — one effort covers all four projects since they share the codebase. Deploy to production still pending.

What landed (non-obvious bits worth remembering):
- All six 8.1 `load_defaults` adopted; stale `new_framework_defaults_7_0/7_1.rb` retired. The 7.0 file had been silently overriding `cookies_serializer` to `:hybrid` via load order — that shadow behavior is gone.
- **Cookie serializer `:hybrid` → `:json`**, closing the Marshal deserialization vector open since the 7.0 upgrade.
- **`jsonapi-resources` shim** (`config/initializers/jsonapi_resources.rb`) — 8.1 changed `Resource#initialize` to keyword args; the unmaintained gem passes a positional hash and broke all route drawing. Compatibility layer prepended.
- `database.yml`: `pool:` → `max_connections:` per 8.1 deprecation.
- New **`bin/ci`** pipeline (`config/ci.rb`, 6 steps): i18n-tasks, rubocop `--fail-level warning`, zeitwerk:check, bundler-audit, yarn audit, brakeman — all green.
- Bundled security bumps: puma 8.0.2, httparty 0.24, turbo-rails 8. Bootstrap 4 CVE-2024-6531 deferred to the open `bootstrap-5` branch (fingerprinted in `.bundler-audit.yml`).

## Action Items

- [x] Bump Rails 8.0 → 8.1, update `Gemfile` / dependencies
- [x] Reconcile framework defaults / cookie serializer / `jsonapi-resources` compat
- [x] Full test suite green (dual-boot) + `bin/ci` pipeline added
- [x] Promote → master (PR #1189, merged 2026-06-10)
- [ ] Smoke-test each project surface (people, cade, minr, ris) before deploy
- [ ] Deploy to production
- [ ] Update `rails_version` in cade / minr / ris READMEs once shipped
- [ ] Bootstrap 5 migration (open `bootstrap-5` branch) — closes deferred CVE-2024-6531

## Related

- [[People|people]]
- [[CADE]]
- [[Minor Intake Form|minr]]
- [[Research Intake Survey|ris]]
- [[Index]]
