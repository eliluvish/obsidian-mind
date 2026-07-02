---
date: "2026-07-02"
description: "Splitting the monolithic ImportUsageInformation service into per-vendor Importers::* objects with a MonthlyUsageImport orchestrator and a parity harness that diffs old vs new against production before cutover."
project: "rcservices"
status: active
github_issue: 1811
tags:
  - work-note
---

# Import Usage Information Decomposition

## Context

The monolithic `ImportUsageInformation` service handles usage import for every vendor at once. [eris#1811](https://github.com/csb-ric/eris/issues/1811) breaks it apart into per-vendor importer objects so each can be reasoned about, spec'd, and cut over independently. This is the plumbing beneath the billing-takeover arc — the same import path that [[Storage Usage Billing Pipeline Takeover]] and [[Briefcase Billing Takeover]] feed into.

Work is mid-flight on branch `1811-refactor-invoice-generation-sending` (pushed to origin, ~8 commits ahead of `master`, **not merged**). The legacy service still runs in production; the new path is parity-testing only.

## What's being built

- **Per-vendor `Importers::*` objects over a shared base** (`b82aff34`, `a1b56108`, `0f05f2ef`, `9f4b8aad`, `1267c4b6`) — Context, Biorender, Zoom, Jmp, Chemdraw, then the license-renewal and storage-usage families. Each is a faithful port of the legacy logic with full spec coverage added alongside. The legacy service is left untouched to run in parallel during the transition.
- **`MonthlyUsageImport` orchestrator** (`987f15f8`) — a thin successor that sequences the new importers in one transaction, preserving the legacy `service_only` option and rollback semantics. Quietly wires in ChemDraw, which the legacy import never actually ran.
- **`rake import:usage_compare` parity harness** (`435e3c9b`) — runs old and new importers each in a rolled-back transaction and diffs the resulting `meta_trackings`, to verify parity against real production data before cutover.

## Cutover strategy

Parallel-run, not big-bang: legacy stays live in production while `import:usage_compare` proves the new path produces identical `meta_trackings` against real data. Cutover only after parity holds. No cutover date yet.

## Bug caught by the parity harness

Running the compare against production would have **double-emailed every eligible SAS Desktop subscriber**: `deliver_email: false` only suppressed the completion summary email, not subscriber renewal/failure/no-usage notices. Fixed (`5c93bb4e`, 2026-07-02) by threading `deliver_email` through `Importers::Context` and gating every mailer on it in both the legacy and new paths. Generalized in [[Gotchas#Transaction rollback doesn't undo email side-effects — gate mailers in shadow/compare paths]].

## Related

- [[RC Services (Eris)|rcservices]]
- [[Storage Usage Billing Pipeline Takeover]] — one of the importer families this decomposition covers
- [[Briefcase Billing Takeover]]
- [[Gotchas]]
- [[Index]]
