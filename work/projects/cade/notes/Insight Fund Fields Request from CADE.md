---
date: "2026-05-18"
description: "CADE (Rowan Potter) requested a set of fund/grant financial fields from Insight — blocked on the new Insight API project; near-term CSV-into-people workaround offered; escalation via Allison → Jane Murray"
project: cade
status: active
tags:
  - work-note
---

# Insight Fund Fields Request from CADE

## Context

[[Rowan Potter]] (CADE Senior Data Analyst) asked for a set of **fund/grant financial fields** to be available from Insight. This is distinct from the earlier space-data ask in [[Insight Square Footage Fields for CADE]] and the three Workday-only fields in [[Workday API Access for Missing Grant Fields]].

## Requested Fields (Insight)

Rowan has screenshots of where each is found in Insight; backend field names may differ.

- Current Actual IDC Rate
- Authorized Amount
- Award Amount
- Select Activity Type
- What is the proposal mechanism type?
- Immediate Sponsor Type (e.g. DHHS)
- Is this a Multi-PI proposal?
- Project Total Direct Costs
- Project Total Indirect Costs
- Project Total Costs
- Current GL Balance: Total Direct Costs & Total Costs

## Status & Eli's Response

- These fields **can be added to the list for the new Insight API**, but that is **not coming anytime soon**.
- **Why it's slow**: there is no existing documented Insight API. A project is **just starting to build a new API** — it is not a small add-on to an existing endpoint, it's a from-scratch build, which makes it a much bigger lift than CADE had hoped.
- **Near-term workaround offered**: if CADE can acquire the information in **CSV form**, Eli can ingest it into [[People|people]] (the lab_archives people app) in the near term.
- **Escalation**: [[Allison Moriarty]] was on board with CADE pursuing this and asked to be told of roadblocks. Eli advised Rowan to tell Allison there **is a roadblock** and that **Allison should talk to [[Jane Murray]]** about it.

## Action Items

- [ ] CADE/Rowan to escalate the roadblock to [[Allison Moriarty]] → [[Jane Murray]]
- [ ] If CADE provides a CSV, ingest the fund fields into [[People|people]] as the near-term path
- [ ] Add these fields to the requirements list for the new Insight API project

## Related

- [[CADE]]
- [[Rowan Potter]]
- [[Jane Murray]]
- [[Insight Square Footage Fields for CADE]]
- [[Workday API Access for Missing Grant Fields]]
- [[001-Insight vs Workday Data Source Scoping]]
- [[People|people]]
- [[Index]]
