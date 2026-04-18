---
date: "2026-04-17"
description: "Order limit raised from previous cap to $1500 — merged to master, production deploy held until 2026-04-24 per Gala's request so the change can be announced to the community first"
project: "rpr"
status: active
github_pr:
  - 190
  - 191
event_date: "2026-04-24"
tags:
  - work-note
  - deploy
---

# Order Limit Raised to 1500 Deploy Hold

> [!danger] Production deploy hold: do not deploy rpr to production before 2026-04-24
> [[Gala Laffey]] asked that this change not hit production until the community has been told. Merged to master, but production ship is on hold until **2026-04-24**. Staging is unaffected.

## Context

Order cap raised to **$1500** with over-cap merge refusal. Merged to master on 2026-04-17 (PR #190). Gala needs time to communicate the change to the participant study community before it goes live.

## Changes on master (awaiting deploy)

- PR #190 — `dc6faa2` — feat(orders): raise limits to $1500 and refuse over-cap merges
- PR #191 — `a1bc772` — perf(orders): add composite `(participant_study_id, status)` index
- PR #191 — `600a2dd` — perf(orders): add `(created_at, status)` composite index

## Deploy Plan

- **Hold until**: 2026-04-24
- **Environments**: rpr **production only** (rprcore.mgb.org). Staging unaffected.
- **Gating signal**: Gala confirms the community has been informed

## Open Items

- [ ] Confirm with [[Gala Laffey]] on or after 2026-04-24 that community has been notified
- [ ] Deploy to production once cleared

## Related

- [[Research Participant Remuneration|rpr]]
- [[Gala Laffey]]
