---
date: "2026-04-08"
description: "Accountability logbook secondary containers — expiration rules from Controlled Substances SOP, open text field for dates. Shipped 2026-04-21."
project: "ilog"
github_issue: 684
status: completed
completed_date: "2026-04-21"
tags:
  - work-note
---

# Secondary Container Expiration Rules

> [!success] Shipped 2026-04-21
> Expiration-rules work is complete. Kele also approved [[001-Secondary Container Disassociation from Primary|disassociating secondaries from primaries]] the same day.

## Context

[[Mirabella Daguerre]] provided guidance on how secondary containers work in the accountability logbook (2026-04-08). This informs how iLog handles the primary → secondary container workflow.

## Key Rules

- Once a secondary container is created, users **can dispense from it** the same way they can from a primary container
- Expiration dates must be an **open text field** — the expiration depends on what's in the secondary container
- **Powders don't expire**
- **Mixtures** are typically 28 days

## Controlled Substances SOP Language

> The expiration dates will change when the Controlled Substances are altered. Use packaging instructions to determine the expiration dates when possible, including storage requirements. If refrigeration is required, this must meet regulatory storage requirements and be approved by the DPH and DEA. Secondary containers must be sterile to be considered for later use. If there are no packaging instructions, use the following guidance:
>
> - **Reconstituted solutions** must be discarded per packaging instructions. Review storage requirements.
>   - Example: TELAZOL should be stored at controlled room temperature 20°–25°C (68°–77°F) prior to use. After initial use, discard unused solution after 7 days at room temperature or after 56 days when refrigerated.
> - **Mixtures** must be discarded 28 days after initial preparation, or sooner if the mixture becomes clouded or contaminated.
> - **Dilutions** must be discarded 28 days after the initial mixing date.

## Implementation Notes

- Expiration field: open text (not a date picker or calculated field) — too many variables
- Consider surfacing the SOP guidance as helper text or a callout near the expiration field so users know the rules

## Related

- [[iLog]]
- [[Mirabella Daguerre]]
- [[Kele Piper]]
- [[001-Secondary Container Disassociation from Primary]]
- [[Destruction Workflow and DEA Form 41 Process]]
