---
date: "2026-05-22"
description: "Triage email to Rolf Fabre listing pasxml volumes not billing today — Group A (ended subs, directory still on pan01) and Group B (no subscription history, including internal shares and /hpc/scratch placeholders)."
project: "rcservices"
status: active
tags:
  - work-note
---

# BriefCase Unbilled Volume Triage

## Context

First-pass triage from the new BriefCase importer ([[Briefcase Billing Takeover]], branch `1971-briefcase-usage-importer`). The matching logic ([[BriefCase Volume Matching Logic]]) bucketed pasxml volumes that aren't billing today into two groups. Sent to [[Rolf Fabre]] on 2026-05-22 for disposition. Awaiting his response.

The dispositions Rolf gives back will feed into the importer's permanent behavior — which paths to ignore, which to bill via internal unbillable subscriptions, which to escalate.

## Group A — Directory still on pan01, subscription ended

These match a subscription, but the subscription's end date has passed. They live in the importer's **ended-sub bucket** (suppressed from billing, not alerted). Question to Rolf: decommission the directory or re-open a subscription?

| Volume | Sub ID | Ended |
|---|---|---|
| `/hpc/groups/miket` | 3347 | 2019-06-30 |
| `/hpc/groups/adsleepeeg` | 5038 | 2023-11-30 |
| `/hpc/groups/shahlab` | 18389 | 2024-04-30 |
| `/hpc/groups/scottcarter1` | 9496 | 2024-10-31 |
| `/hpc/groups/best-trial` | 24027 | 2024-10-31 |
| `/hpc/groups/aanand` | 16169 | 2024-12-31 |
| `/hpc/groups/cteu_imaging` | 25765 | 2025-01-31 |
| `/hpc/groups/bml` | 28451 | 2025-01-31 |
| `/hpc/groups/epi-gen-share` | 19525 | 2025-01-31 |
| `/hpc/groups/insomnia` | 8243 | 2025-01-31 |
| `/hpc/groups/awad1` | 8840 | 2025-03-31 |
| `/hpc/groups/bass1` | 10503 | 2026-01-31 |
| `/hpc/groups/thakurelaLab` | 26488 | 2026-04-30 — held 30 days? |

## Group B — Directory exists, no subscription history

These are in the importer's **unmatched bucket** (currently escalated via Honeybadger). Proposal in the email: create unbillable subscriptions programmatically with **PH2776** as the funding source so RCS admins have a place to see them.

### Likely labs / internal / unknown — needs triage

- `/hpc/groups/appstest`
- `/hpc/groups/buildtree`
- `/hpc/groups/bwh-comppath-img3`
- `/hpc/groups/ccr`
- `/hpc/groups/cctm`
- `/hpc/groups/erisxdl`
- `/hpc/groups/released`
- `/hpc/groups/rftest`
- `/hpc/groups/slurm-warewulf`
- `/hpc/groups/slurm-warewulf1`
- `/hpc/groups/slurm-warewulf2`
- `/hpc/groups/slurm-warewulf3`
- `/hpc/groups/testsuite`
- `/hpc/groups/virt4eris2`
- `/hpc/groups/whaas`

### Single-letter `/hpc/scratch/*` (template / placeholder?)

`/hpc/scratch/{a..z}` plus `/hpc/scratch/pcpgm`. Proposal: ignore `/hpc/scratch/*` entirely **if Rolf confirms it's never a real billing path**.

### The pcpgm outlier

`/hpc/scratch/pcpgm` maps to BriefCASE-2994 — an older subscription that looks misplaced. Question to Rolf: should this be `/hpc/groups/pcpgm` instead? If not, the importer can keep it as a one-off, but it's the reason a blanket `/hpc/scratch/*` ignore can't ship blind.

## Decisions blocked on Rolf's response

- [ ] Per-row disposition for Group A (decommission vs. re-open)
- [ ] Confirm PH2776 + unbillable-subscription pattern for Group B internal shares
- [ ] Confirm `/hpc/scratch/*` is never a real billing path → add to opt-out prefix filter ([[BriefCase Volume Matching Logic]])
- [ ] Resolve `/hpc/scratch/pcpgm` — relocate or one-off allow

## Related

- [[Briefcase Billing Takeover]] — parent work
- [[BriefCase Volume Matching Logic]] — bucket taxonomy that produced this list
- [[Rolf Fabre]] — escalation contact
- [[RC Services (Eris)|rcservices]]
