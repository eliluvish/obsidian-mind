---
description: "Architectural and workflow decisions worth recalling across sessions — each links to its source work note"
tags:
  - brain
---

# Key Decisions

Architectural or workflow decisions worth recalling. Link to the full [[Decision Record]] when one exists.

## Accepted

- **iLog secondary containers disassociated from primaries 2026-04-21** — [[Kele Piper]] approved allowing secondaries to exist without a primary link. Implemented. Known cost: DEA chain-of-custody reporting must reconstruct the relationship from history/audit records rather than a live association. See [[001-Secondary Container Disassociation from Primary]].
- **PCMS Insight Integration scoped 2026-04-09** — Insight for expenses/revenue, Workday optional for internal funding backfill. Workday is source-of-truth in principle but Insight is the practical primary. Jessica sends columns to Daniel; Eli compares Savient→Insight against Workday to quantify gaps. See [[001-Insight vs Workday Data Source Scoping]].

## Pending

- **Workday API access** — [[CADE]] still has the harder ask (3 grant fields not in Insight, INC4967792). PCMS's need is now optional after the 2026-04-09 scoping decision. CADE's case is the one pushing this forward. See [[Workday API Access for Missing Grant Fields]].
- **Extracting apps from lab_archives** — [[Research Intake Survey|ris]] confirmed standalone (Mirabella/Kelé approved 2026-04-07). [[Minor Intake Form|minr]] also approved to extract after busy season. Pattern: standalone apps like [[BioLift|biolift]] over modules in lab_archives. Eli considering a multi-app consolidation approach. **No setup fee** for either extraction (decided 2026-04-08 with [[Daniel Guettler]]). See [[RIS Revival and Platform Decision]] and [[Plan to Extract minr from lab_archives]].
