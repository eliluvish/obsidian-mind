---
date: "2026-05-21"
description: "Investigate how PRISM-48686 was able to place an RC Services order against an expired fund — guardrail bypass or fund-state ambiguity (eris#1963)"
project: rcservices
github_issue: 1963
status: active
tags:
  - work-note
---

# PRISM-48686 Expired Fund Order Investigation

## Context

Eris issue [#1963](https://github.com/csb-ric/eris/issues/1963) — investigate how project **PRISM-48686** managed to place an RC Services order against a fund that should have been expired. Opened 2026-05-20.

This is a guardrail question: ordering against an expired fund is exactly the case the system is supposed to prevent. Two broad possibilities:

1. **Real bypass** — a validation/check is missing or wrong on a code path (modal create, API, admin edit, account-picker, copy-from-prior, etc.). If so, this is a billing-correctness bug with compliance overtones (charges accrued against a closed fund).
2. **Fund-state ambiguity** — the fund was technically not yet "expired" in Eris's view (timezone edge, end-date inclusive vs exclusive, Workday sync lag, manual override flag, draft → active transition) even though it presented as expired to the user. If so, the fix is to align Eris's "expired" definition with the source of truth.

## Notes

- The Eris issue body is empty — the investigation hasn't been scoped yet.
- Worth checking in parallel: the recent `fix(projects): wire admin project funding row controller to form scope` commit (`11ae721a`, 2026-05-20) — close in time to when the issue was filed; possible the funding-row UX exposed this or that this commit changes how fund expiry surfaces in admin.
- The "additional funding source button doesn't work" report (eris#1964, same day) is in the same area of the UI — may be related, may be coincidence.

## Investigation Plan

- [ ] Pull the order record for PRISM-48686 — find created_at, the user who placed it, the entry-point controller, and the fund's expiry as seen by Eris at that moment
- [ ] Map every code path that creates an order/charge and audit each for an expired-fund guardrail (account-picker modal, admin/projects, API, copy-from-prior, recurring/auto-generated)
- [ ] Confirm what "expired" means in Eris — column, derived from Workday sync, time-zoned, inclusive/exclusive of end date
- [ ] Decide: missing validation (add it + spec) vs. definition mismatch (align with source of truth)

## Compliance Note

If charges did accrue against a closed fund, there may be a downstream billing reversal / re-allocation needed. Flag to [[Alissa Scharf]] once root cause is known so RC Services finance has a heads-up.

## Action Items

- [ ] Run the investigation plan above
- [ ] If a guardrail bypass, write a regression spec and patch
- [ ] If a definition mismatch, propose an ADR for what counts as "expired" in Eris
- [ ] Update this note as findings land

## Related

- [[RC Services (Eris)]]
- [[Alissa Scharf]]
- [[Index]]
