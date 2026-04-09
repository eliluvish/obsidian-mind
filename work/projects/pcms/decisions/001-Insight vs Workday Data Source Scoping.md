---
date: "2026-04-09"
description: "Scope the PCMS Insight Integration — Insight for expenses/revenue, Workday optional for internal funding. Resolved 2026-04-09 with Jessica Cho and Daniel Guettler."
project: pcms
status: accepted
tags:
  - decision
---

# Decision: Insight vs Workday Data Source Scoping

## Context

The [[Proposed Feature Prioritization from Finance|Insight Integration]] feature was proposed by Finance as a single line item: "Integrate RCMS with Insight/Workday for expense data and budgeting." During a working session on 2026-04-09 with [[Jessica Cho]] and [[Daniel Guettler]], the scope was clarified and split into two separate data flows with different systems of record.

Two related concerns overlapped in the original proposal:

1. Pulling **expense and revenue** data into PCMS for core-facility budgeting
2. Pulling **internal grant funding information** so PCMS can enrich funds with data that Insight is missing

These are distinct needs with different source-of-truth systems and different urgency levels.

## Triggering Issue

- [[Proposed Feature Prioritization from Finance]]
- #2241 "Change source of internal funding information from Workday instead of Insight" (assigned to [[Yovani Edwards]])
- [[Workday API Access for Missing Grant Fields]] (CADE, ticket INC4967792 — parallel ask)

## Options Considered

1. **Workday for both** — treat Workday as the sole source of truth for all expense, revenue, and funding data. Most accurate but gated on Workday API access, which has been the longest-standing blocker.
2. **Insight for both** — stay on Insight for everything, use the existing pipeline. Fastest but inherits Insight's data gaps (grant funding fields are missing for a meaningful number of funds).
3. **Split the scope** — Insight for expenses/revenue (where it is already authoritative), Workday only for internal funding when easy. Accept duplication temporarily; consolidate later if Insight closes its gaps.

## Decision

**Option 3 — split the scope.**

- **Expenses and revenue → Insight.** Insight is now under Digital and the team has been responsive on Teams/email. [[Jessica Cho]] will send [[Daniel Guettler]] the list of Insight columns PCMS needs. Daniel will request those columns from the Insight team in parallel with any Workday work.
- **Internal grant funding information → Workday (optional).** Jessica's position: "if it's easy, we're totally fine with pulling that... not a huge necessity right now." Eli already pulls cost-center information from Workday, so adding internal funding is low marginal effort. Eli will first compare the Savient → Insight pipeline against Workday to see how many fund numbers Insight is actually missing for PCMS before committing to the Workday path.
- **Cost centers → not needed** in PCMS.
- **Long-term principle**: Workday remains the source of truth; it is better to depend on one system than two. If Insight eventually closes its data gaps, the Workday fallback can be removed.

## Consequences

- **Unblocks the expense/revenue half of the Insight Integration** without waiting on Workday API access.
- **Keeps #2241 alive** but deprioritized — it is now "nice to have if easy," not the primary path.
- **Two parallel asks**: Jessica/Daniel to Insight team (columns); Eli to Workday for internal funding as a comparison/backfill.
- **Cross-project synergy**: the Workday API access request can still be bundled with [[Workday API Access for Missing Grant Fields|CADE's ask]] (INC4967792) — the combined case is stronger.
- The Insight discrepancy may shrink on its own — Daniel noted the Insight team is aware of the fund-number gap and working on a solution.

## Action Items

- [ ] [[Jessica Cho]] sends the list of Insight columns PCMS needs to [[Daniel Guettler]]
- [ ] [[Daniel Guettler]] files the column request with the Insight team
- [ ] Eli compares Savient → Insight output against Workday to quantify the missing-fund gap
- [ ] Revisit Workday internal-funding pull once the comparison is done
- [ ] Coordinate with [[CADE]] on the shared Workday API access ask

## Related

- [[PCMS]]
- [[2026-04-09 Meeting — pcms]] — the meeting where this was accepted
- [[Proposed Feature Prioritization from Finance]]
- [[Workday API Access for Missing Grant Fields]] — CADE's parallel ask
- [[Jessica Cho]]
- [[Daniel Guettler]]
- [[Yovani Edwards]]
