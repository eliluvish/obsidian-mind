---
date: "2026-06-10"
description: "RC FinOps greenfield build arc, Jun 4–10 2026 — Azure import, RBAC + site admin, FundingSource/Insight scoping, MGB subsidy, faceted line-item browser, tooling"
project: "rcfinops"
tags:
  - work-note
---

# RC FinOps Week-1 Build Log

## Context
RC FinOps (`csb-ric/rcfinops`, local `~/dev/cloud_costs`) went from `initial commit` to a multi-feature Rails app in roughly a week — **116 commits, Jun 4–10 2026, all solo**. Captured via [[repo-sync]] on 2026-06-10. The vault project had only the planning-stage [[001-Standalone Azure Usage Dashboard App|ADR]] before this; this note records what actually shipped.

## What shipped

1. **Azure cost import pipeline** (Jun 4–5) — bootstrapped the app (rspec, FactoryBot, credentials, seeds, Tailwind) and built the Azure cost import with a design doc + implementation plan committed alongside. `AzureCostLineItem` schema slimmed after the first pass; DB indexes added for dashboard and admin queries.

2. **Role-based access control + site administration** (Jun 7) — site groups (full CRUD, Turbo Streams), a site-permissions matrix with live privilege toggle, and a site-users view, all role-gated and tested with permission-gated affordances.

3. **FundingSource model + MGB subsidy** (Jun 7–8) — added `FundingSource` enriched from Insight, scoped the dashboard by role against it, and built an import flow. Flagged MGB-subsidized line items on import and propagated the filter across dashboard + line-item index, tinting subsidized rows with a legend. → [[002-FundingSource as Cost-Ownership Authority]], [[MGB Subsidy Flagging Business Rule]].

4. **Faceted line-item browser** (Jun 8–9) — role-based facets, free-text search, `visible_to` scope rewritten as a UNION for covering-index performance, filter defs as value objects, permit list + URL keys derived from `LineItemBrowser`. Added `vm_name` to the schema and search scope.

5. **Dashboard polish + UX hardening** (Jun 9–10) — chart bar-width caps for sparse charts, "no prior spend" instead of blank percent, group-by dimension preserved across month switches, top-3 spend chart with aligned labels, conditional legend entries, responsive tablet/phone layout, SVG chrome icons, `aria-expanded` on dropdowns.

6. **Tooling + hygiene** (Jun 8–10) — rubocop, i18n-tasks, simplecov, `config/ci.rb`; removed dead `UserRitm` references and unused `FundingSource` associations; extracted `breakdown_rows` helper; moved seed data to `db/seeds/*.yml`.

## Stack (as built)
Rails 8.1.3 · Ruby 3.4.4 · MySQL/Trilogy · Tailwind + Turbo Streams.

## State as of capture (2026-06-10)
- `main` is **16 commits ahead of `origin/main`** — today's refactor/UX burst not yet pushed.
- Branch **`add-vm-name`** adds resource group to the free-text search scope; one commit, appears ready to merge.

## Links
- [[RC FinOps|RC FinOps — Cloud Cost Dashboard]]
- [[001-Standalone Azure Usage Dashboard App]]
- [[002-FundingSource as Cost-Ownership Authority]]
- [[MGB Subsidy Flagging Business Rule]]

## Related
- [[RC Services (Eris)|rcservices]] — origin of the Azure work
- [[AzureVM Import via Azure Export API]] — eris's existing Azure billing import
</content>
