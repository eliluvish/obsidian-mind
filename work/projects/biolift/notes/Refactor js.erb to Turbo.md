---
date: "2026-05-18"
description: "biolift#20 — remove legacy .js.erb views and move to Turbo (Streams/Frames). Rails 8.1 tech-debt cleanup; not started, original ~May 7 target slipped"
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

**Not started.** Original target (~2026-05-07, per the README) has slipped. Still flagged priority.

## Notes

- Approach: replace each `respond_to { |f| f.js }` / `*.js.erb` path with a Turbo Stream response (or Turbo Frame where a frame-scoped update fits better).
- Inventory the `.js.erb` files first to scope the work and sequence the migration (lowest-risk views first).

## Action Items

- [ ] Inventory all `.js.erb` views and the controller actions that render them
- [ ] Migrate each to Turbo Stream / Turbo Frame responses
- [ ] Remove dead JS helpers / `format.js` blocks left orphaned by the migration
- [ ] Verify forms and dynamic updates still work end-to-end (system specs)

## Related

- [[BioLift]]
- [biolift#20](https://github.com/csb-ric/biolift/issues/20)
- [[Index]]
