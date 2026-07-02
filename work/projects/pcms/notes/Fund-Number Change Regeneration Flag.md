---
date: "2026-06-18"
description: "Proposal (declined, not planned) to split the single red 'regeneration required' invoice flag into two: total_mismatch (blocks journaling) and fund_changed (non-blocking). pcms#2356 closed not planned; PR #2362 closed unmerged."
project: "pcms"
github_issue: "https://github.com/csb-ric/pcms/issues/2356"
status: dropped
tags:
  - work-note
---

# Fund-Number Change Regeneration Flag

> [!failure] Not planned - we chose not to do this work (2026-06-29)
> [pcms#2356](https://github.com/csb-ric/pcms/issues/2356) was closed **not planned** by [[Jessica Cho]] (2026-06-25); the feature was considered but we decided not to pursue it. PR [#2362](https://github.com/csb-ric/pcms/pull/2362) was closed unmerged. The two-flag split described below is the proposal that was declined, not shipped work. Kept for context in case the requirement resurfaces; the action items below are void.

## Context

Invoices currently get a single red "regeneration required" flag when the **sent total ≠ calculated total** — this blocks the invoice from moving on to journal processing until it's regenerated and fixed.

This feature ([pcms#2356](https://github.com/csb-ric/pcms/issues/2356), all cores) adds a **second** regeneration signal: when a tracking's **fund number changes after the invoice was sent**, the invoice should be flagged for regeneration **but not blocked** from journaling — it has been (or will be) journaled/processed; regeneration + resend is still needed. Both flags surface in "Check for Issues" (`/shm/admin/billing`) and in the regeneration-required email.

## Proposed design (declined)

The proposal was to split the single flag into two distinct signals on `Invoice`, with different colors:

- **`:total_mismatch`** (red) — sent total differs from calculated total; **blocks** journal processing (existing behavior, preserved).
- **`:fund_changed`** (yellow) — a tracking was reassigned to a different fund after sending; **does not block** journaling, but needs eventual regenerate + resend.
- `Invoice#regeneration_reason` exposes the classification (memoized to avoid duplicate `to_invoice` builds during the check pass).
- Both would appear in "Check for Issues" and the regeneration-required email.

## Action Items

- [ ] Get PR [#2362](https://github.com/csb-ric/pcms/pull/2362) reviewed + merged
- [ ] Deploy + note for finance (behavior change: fund-change flag does **not** hold journaling)
- [ ] Confirm hover/email copy matches the issue's wording for each flag color

## Related

- [[PCMS]]
- [[Tera Morse]]
- [[Jessica Cho]]
- [[Yovani Edwards]]
