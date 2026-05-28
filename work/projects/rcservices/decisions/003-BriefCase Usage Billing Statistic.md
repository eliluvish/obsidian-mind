---
date: "2026-05-27"
description: "Which statistic to bill BriefCase/HPC storage usage on — average vs 75th percentile — when collapsing the importer's daily usage samples into one monthly number."
project: "rcservices"
status: proposed
tags:
  - decision
---

# 003 — BriefCase Usage Billing Statistic

## Context

The new BriefCase importer ([[Briefcase Billing Takeover]]) records **one storage-usage sample per day** per volume. Monthly billing needs a **single number** per volume, so we must choose how to collapse the daily samples into that figure. The choice is material — it directly sets the billed amount and the size of the diffs during the parallel run against Chris Mow's legacy scripts.

Chris's legacy scripts bill on the **75th percentile** of the period's samples.

## Triggering Issue

Surfaced in Eli's 2026-05-27 stakeholder status update (captured in [[Briefcase Billing Takeover#Status update — RCS stakeholders (2026-05-27)]]). No GitHub issue yet; relates to the BriefCase monthly aggregator ([eris#1974](https://github.com/csb-ric/eris/issues/1974)).

## Options Considered

1. **75th percentile** — matches Chris's existing scripts. Keeps parallel-run diffs clean: any remaining differences then reflect real matching/scope bugs rather than a methodology change. Slightly forgiving of short usage spikes.
2. **Average (mean)** — simpler to explain; smooths spikes more than p75. Diverges from the legacy number, so the parallel-run comparison would mix methodology drift with genuine discrepancies, making validation harder.
3. **Other** (max, median, end-of-period snapshot) — not seriously on the table; noted only to bound the space.

## Decision

_Pending._ Leaning **75th percentile** to match Chris during cutover validation, revisiting only if it demonstrably over/under-bills relative to what cores expect.

## Consequences

_To be filled once decided._ If p75 is chosen: the aggregator (#1974) computes the 75th percentile of daily samples per volume per billing period; parallel-run diffs against Chris's scripts should trend toward zero, isolating real bugs.

## Related

- [[Briefcase Billing Takeover]] — parent work; cutover validation depends on this
- [[BriefCase Volume Matching Logic]] — produces the matched volumes this statistic is applied to
- [[RC Services (Eris)|rcservices]]
- [[Chris Mow]] — owns the legacy p75 implementation being compared against
