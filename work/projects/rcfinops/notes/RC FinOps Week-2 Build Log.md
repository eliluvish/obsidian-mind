---
date: "2026-06-22"
description: "RC FinOps build arc Jun 10–22 2026 — observability (Ahoy + Honeybadger), daily engagement digest mailer, line-item sort + filter-preserving CSV export, VM cost breakdown (unmerged)"
project: "rcfinops"
tags:
  - work-note
---

# RC FinOps Week-2 Build Log

## Context
Continuation of the [[RC FinOps Week-1 Build Log]] (Jun 4–10). This window — **Jun 10–22 2026, 14 non-merge commits, +4,725/−858 across 58 files, all solo** — shifts from greenfield feature build to observability, a digest mailer, and line-item UX. Captured via [[repo-sync]] on 2026-06-22.

## What shipped

1. **Engagement telemetry (Ahoy)** (`3f5129a`, PR #2) — integrated the Ahoy gem to record visits and track filter-change events on the line-item browser. Added a `UserEngagement` model wrapping Ahoy's visit/event tables with `total_visits` / `active_users` aggregates. This is the telemetry layer the digest mailer depends on.

2. **Daily engagement digest mailer** (`9da88b1`, PR #5) — `DailySummaryMailer#previous_day` renders a prior-day digest (total visits, unique active users) from `UserEngagement`, through the MGB SMTP relay (letter_opener in dev), MGB-branded layout. Invoked via a `daily_summary:send` rake task designed for **external cron** (not an in-app scheduler).

3. **Line-item browser: sort + CSV export** (`d3e38f2`, `c436b15`, `41303b0`, PR #3) — sortable column headers; a CSV export button that **preserves active filter state** at export time, with a timestamped filename.

4. **Honeybadger error reporting** (`c3de55d`) — added the gem + `config/honeybadger.yml`; exception monitoring in place before production.

5. **Asset + hygiene** (`1fde5e9`, `1f34998`, `431fab1`, `972738a`, `c9f9715`, `744fee8`, `8752ba8`) — proper MGB logo image asset (replacing the SVG), Brakeman warnings resolved, gem/yarn bumps, unused i18n key cleanup, request specs DRY'd into shared support, seed data extracted to `db/seeds/*.yml`, `icon_tag` moved to `IconHelper`.

## In progress / unmerged
Branch **`add-vm-name`** off `main`, two commits not yet merged:
- `6a22d6c feat(costs): add VM name tracking and breakdown` — adds a `vm_name` column sourced from the Azure `Description` resource tag at import, a "Spend by VM" dashboard chart (visible to **all** roles, unlike the admin-only user breakdown), two covering indexes for the breakdown queries, and a backfill of existing rows.
- `220dc9f feat(line-items): search by resource group in free-text` — adds `resource_group_name` to the free-text search scope.

> [!note] Decisions to capture on merge
> `add-vm-name` encodes real design choices worth ADRs once merged: VM name sourced from the `Description` tag (not `additionalInfo`); covering indexes rather than a search index (leading-wildcard LIKE can't use a B-tree); "Spend by VM" visible to all roles. Telemetry-via-Ahoy + external-cron digest is a second candidate.

## State as of capture (2026-06-22)
`origin/main` is now in sync with local `main` — the Week-1 "16 commits ahead" gap is cleared. `add-vm-name` is the only in-flight branch.

## Links
- [[RC FinOps|RC FinOps — Cloud Cost Dashboard]]
- [[RC FinOps Week-1 Build Log]]
- [[002-FundingSource as Cost-Ownership Authority]]

## Related
- [[RC Services (Eris)|rcservices]] — origin of the Azure work
- [[Index]]
