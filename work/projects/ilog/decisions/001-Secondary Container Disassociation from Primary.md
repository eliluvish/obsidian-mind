---
date: "2026-04-21"
description: "Kele approved allowing secondary containers to be disassociated from their primary container. Implemented. Creates a known DEA reporting burden — the primary↔secondary chain is no longer enforced by the data model."
project: ilog
status: accepted
tags:
  - decision
---

# Decision: Secondary Container Disassociation from Primary

## Context

The accountability logbook models controlled substance containers as primary → secondary (a primary container can be drawn down into secondary containers for dispensing). Previously the model enforced that every secondary container was tied to its primary.

[[Kele Piper]] confirmed via email on **2026-04-21** that it is acceptable to allow secondary containers to be **disassociated** from their primary containers.

## Triggering Issue

Follow-up to [[Secondary Container Expiration Rules]] (shipped 2026-04-21). The expiration-rules work raised the adjacent question of whether the primary↔secondary link must be enforced at the data layer.

## Options Considered

1. **Keep primary↔secondary association enforced** — data model guarantees every secondary has a primary. Easier DEA reporting (chain of custody is a direct query). Less flexible for real-world workflows where secondaries get moved, merged, or outlive their primary.
2. **Allow disassociation** (chosen) — secondaries can exist independent of their primary. Matches actual lab practice and the SOP language around secondary containers being usable on their own. Moves chain-of-custody tracking from data-model enforcement to reporting-time reconstruction.

## Decision

Allow secondary containers to be disassociated from their primary container. Approved by [[Kele Piper]] via email 2026-04-21. Implementation is already shipped.

## Consequences

- **DEA reporting is harder.** The primary↔secondary chain is no longer guaranteed by the schema, so reports that need the full chain of custody must reconstruct it from history/audit records rather than traversing a direct association. Plan for this when building Form 41 / accountability reports.
- Matches real lab workflow — secondaries that survive their primary, get moved, or get consolidated are now representable without workarounds.
- Audit trail becomes load-bearing: if the live link is gone, the history table is the only place the primary↔secondary relationship persists. Any future schema change that touches container history needs to preserve this.

## Related

- [[iLog]]
- [[Kele Piper]]
- [[Secondary Container Expiration Rules]]
- [[Destruction Workflow and DEA Form 41 Process]]
- [[ARC Group iLog Demo]]
