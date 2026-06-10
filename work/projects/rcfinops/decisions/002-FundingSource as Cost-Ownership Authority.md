---
date: "2026-06-08"
description: "Use a FundingSource model enriched from Insight as the authority for who owns a cloud cost line item; scope dashboard visibility by user role against it"
project: "rcfinops"
status: accepted
tags:
  - decision
---

# 002 — FundingSource as Cost-Ownership Authority

## Context

The dashboard shows cloud cost line items (currently Azure, via [[001-Standalone Azure Usage Dashboard App|the independent Azure import]]). A researcher-facing surface needs a defensible answer to "whose costs are these, and who is allowed to see them?" Raw Azure line items carry resource/subscription identifiers but not the funding ownership the hospital reasons about.

The question: what is the authoritative source for cost ownership, and how does visibility get scoped?

## Decision

Introduce a **`FundingSource` model enriched from Insight** as the authority for who owns a cost line item. Dashboard visibility is **scoped by user role against `FundingSource`** — what a user sees is derived from the funding sources their role grants them, not from the raw Azure data alone.

This was built out alongside the role-based access control and site-administration layer (site groups, permissions matrix, site users) — see [[RC FinOps Week-1 Build Log]].

## Consequences

- Insight becomes an upstream dependency for this app's ownership model — consistent with [[PCMS]]'s existing reliance on Insight as a data source ([[001-Insight vs Workday Data Source Scoping]]), and worth watching for the same staleness/availability concerns.
- Visibility is now a function of role × funding source, which is the mechanism the [[MGB Subsidy Flagging Business Rule]] and the `visible_to` query scope build on. The `visible_to` scope was rewritten as a UNION for covering-index performance.
- Establishes a clear authority boundary: cost data comes from Azure, *ownership and access* come from `FundingSource`/Insight. Any future cloud source (AWS) plugs into the same ownership model rather than inventing its own.
- Possible compliance review implication — role-scoped visibility determines what PIs see vs. admins.

## Related

- [[RC FinOps|RC FinOps — Cloud Cost Dashboard]] — project README
- [[001-Standalone Azure Usage Dashboard App]]
- [[MGB Subsidy Flagging Business Rule]]
- [[RC FinOps Week-1 Build Log]]
- [[001-Insight vs Workday Data Source Scoping]] — pcms's Insight-as-source decision
</content>
