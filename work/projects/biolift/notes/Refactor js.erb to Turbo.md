---
date: "2026-05-18"
description: "biolift#20 — remove legacy .js.erb / UJS and move to Turbo. In progress: turbo-rails installed (Drive off), specimen transports migrated as proof-of-concept, opt-in coexistence strategy established"
project: biolift
github_issue: 20
status: active
tags:
  - work-note
---

# Refactor js.erb to Turbo

## Context

[biolift#20](https://github.com/csb-ric/biolift/issues/20) (opened 2026-04-21, label `feature`). Important refactor: **remove the `.js.erb` code and swap it to Turbo**.

**Driver**: Rails 8.1 tech debt. `.js.erb` server-generated JavaScript responses are legacy; moving to Turbo (Streams/Frames) aligns biolift with a Turbo-first Hotwire architecture and removes a class of brittle, hard-to-test view code.

## Status

**In progress** — kicked off 2026-06-10 (6 commits, merged to master). `turbo-rails` installed and the migration pattern is validated; the bulk of the `.js.erb`/UJS surface still remains.

### Coexistence strategy (the key constraint)

Turbo is installed but **Turbo Drive is disabled globally** (`Turbo.session.drive = false`). The shared **Site plugin's admin pages still depend on `jquery_ujs`** for remote deletes and permission toggles — dropping UJS site-wide would break them. So the approach is **opt-in per element** via `data: { turbo: true }`, with full Drive enablement deferred until the shared plugin is converted. This pattern is documented in the repo's `CLAUDE.md`. Candidate for an ADR.

### Done (`623fea4`, `52d9950`, `62d8f9c`, `d2ba74d`, `14f46e6`, `d19e42c`, `4ed8d33`)

- [x] `turbo-rails` added + wired into importmap, Drive disabled globally
- [x] **Specimen transport deletes** migrated UJS → Turbo (proof-of-concept): 303 See Other redirect, `turbo_method`/`turbo_confirm`, flash auto-hide on `turbo:load`, Sprockets `DoubleLinkError` fixed; request + system specs added
- [x] Nav masquerade link replaced with proper `button_to` (was faking POST via UJS)
- [x] Receiver autocomplete switched to JSON LDAP lookup endpoint (system spec added)
- [x] Coexistence pattern documented in repo `CLAUDE.md`; `Gemfile.lock` committed

## Action Items

- [ ] Inventory remaining `.js.erb` views / `format.js` blocks and the actions that render them
- [ ] Migrate each remaining feature to Turbo (opt-in per element until Drive can be enabled)
- [ ] Convert the shared **Site plugin** off UJS — the gate for enabling Turbo Drive globally
- [ ] Remove dead JS helpers / `format.js` blocks orphaned by the migration

## Related

- [[BioLift]]
- [biolift#20](https://github.com/csb-ric/biolift/issues/20)
- [[Index]]
