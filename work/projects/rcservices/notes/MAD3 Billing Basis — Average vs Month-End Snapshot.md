---
date: "2026-06-18"
description: "MAD3 import temporarily bills the month's final daily snapshot during the physical→logical cutover; revert to monthly average in July 2026 before August billing once a full month of logical snapshots exists. eris#2010."
project: "rcservices"
github_issue: "https://github.com/csb-ric/eris/issues/2010"
status: active
tags:
  - work-note
---

# MAD3 Billing Basis — Average vs Month-End Snapshot

## Context

Part of the physical→logical billing fix ([eris#2008](https://github.com/csb-ric/eris/issues/2008) / PR [#2009](https://github.com/csb-ric/eris/issues/2009)) — see [[Storage Usage Billing Pipeline Takeover]]. Two **temporary** cutover changes were made:

1. **Dropped the physical-based MAD3/OLD_MAD3 snapshots** (rake `eris:mad3:delete_physical_snapshots`) so the corrected `fslogical` collector rebuilds daily snapshots forward in logical units. Result: months before the cutover have **no daily snapshots**, and the cutover month has only a **partial** set (from the fix date onward).
2. **Switched `Isilon::Mad3SubscriptionUsageImport` from monthly *average* to the month's *final daily snapshot*.** With early-month days missing, an average would understate usage; the last-day value is a clean point-in-time logical figure and matches how #2008 was validated against the live quota.

## Decision: month-end is a transitional stand-in; average is the long-term basis

Storage drifts within a month; the monthly average smooths daily fluctuation and is what the legacy pipeline (Chris Mow's scripts) billed. The month-end snapshot is only a stand-in while logical history is incomplete. This mirrors the avg-vs-statistic question in [[003-BriefCase Usage Billing Statistic]].

## Action Items

Do this in **July 2026**, before the **August billing run** (July 1 onward is the first full month of logical daily snapshots):

- [ ] Confirm July has a complete set of daily logical snapshots (no missing days that would skew the average)
- [ ] Revert `Isilon::Mad3SubscriptionUsageImport` to averaging `StorageUsageSnapshot.bytes` across the month (restore `average_bytes` / `.average(:bytes)`)
- [ ] Restore the class / `ImportMad3UsageJob` comments describing averaging
- [ ] Restore the importer spec expectations to the averaged values

## Related

- [[RC Services (Eris)|rcservices]]
- [[Storage Usage Billing Pipeline Takeover]] — the MAD3 takeover this billing-basis question lives inside
- [[RFA Billing Takeover and Powerscale Migration]] — RFA aligned to the same `fslogical` logical-usage treatment
- [[003-BriefCase Usage Billing Statistic]] — sibling billing-statistic decision (avg vs p75)
- [[Chris Mow]] — legacy pipeline billed the monthly average
