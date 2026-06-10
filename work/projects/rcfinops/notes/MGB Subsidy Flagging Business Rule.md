---
date: "2026-06-08"
description: "RC FinOps flags MGB-subsidized cost line items on import and filters/tints them across the dashboard and line-item index; affects what PIs see vs admins"
project: "rcfinops"
tags:
  - work-note
---

# MGB Subsidy Flagging Business Rule

## Context
Some cloud cost line items are subsidized by MGB rather than charged directly to a researcher's funding. The dashboard needs to make that distinction visible and filterable, because subsidized vs. unsubsidized spend reads very differently to a PI looking at their own costs versus an admin reviewing the whole picture.

## What / Why
- **Flagged on import**: line items are marked MGB-subsidized at import time (Azure import pipeline), so the flag is a property of the stored data, not a render-time guess.
- **Propagated as a filter**: the subsidy flag is a first-class filter across both the **dashboard** and the **line-item index** — you can scope a view to subsidized or unsubsidized spend.
- **Tinted in the table** with a legend, so subsidized rows are visually distinct without reading a column.

This sits on top of the role × funding-source visibility model ([[002-FundingSource as Cost-Ownership Authority]]) — subsidy is another axis layered over who-can-see-what.

## Compliance angle
Because the rule changes what different roles see (PIs vs. admins) and touches how subsidized institutional spend is surfaced, it's worth a deliberate compliance review — flagged as TBD in the [[RC FinOps|project README]]. Not yet reviewed.

## Links
- [[RC FinOps|RC FinOps — Cloud Cost Dashboard]]
- [[002-FundingSource as Cost-Ownership Authority]]
- [[RC FinOps Week-1 Build Log]]

## Related
- [[Research Computing Core]]
- [[Alissa Scharf]]
</content>
