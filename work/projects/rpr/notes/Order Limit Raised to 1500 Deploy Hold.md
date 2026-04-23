---
date: "2026-04-17"
description: "Order limit raised from previous cap to $1500 — merged to master, deployed to production 2026-04-24 after Gala confirmed community was notified"
project: "rpr"
status: completed
github_pr:
  - 190
  - 191
event_date: "2026-04-24"
tags:
  - work-note
  - deploy
---

# Order Limit Raised to 1500 Deploy Hold

## Context

Order cap raised to **$1500** with over-cap merge refusal. Merged to master on 2026-04-17 (PR #190). Gala communicated the change to the participant study community before go-live.

## Deployed

- **Date**: 2026-04-24
- **Environment**: rprcore.mgb.org (production)
- **Gating signal**: [[Gala Laffey]] confirmed community notified ✅

## Changes Shipped

- PR #190 — `dc6faa2` — feat(orders): raise limits to $1500 and refuse over-cap merges
- PR #191 — `a1bc772` — perf(orders): add composite `(participant_study_id, status)` index
- PR #191 — `600a2dd` — perf(orders): add `(created_at, status)` composite index

## Related

- [[Research Participant Remuneration|rpr]]
- [[Gala Laffey]]
