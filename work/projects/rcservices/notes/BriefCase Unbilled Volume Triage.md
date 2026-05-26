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

First-pass triage from the new BriefCase importer ([[Briefcase Billing Takeover]], branch `1971-briefcase-usage-importer`). The matching logic ([[BriefCase Volume Matching Logic]]) bucketed pasxml volumes that aren't billing today into two groups. Sent to [[Rolf Fabre]] 2026-05-22; **Rolf replied same day** — dispositions captured inline below.

The dispositions feed the importer's permanent behavior — which paths to ignore, which to bill via internal unbillable subscriptions, which to escalate.

## Group A — Directory still on pan01, subscription ended

These matched a subscription whose end date had passed (importer's **ended-sub bucket** — suppressed from billing, not alerted). All resolved by Rolf 2026-05-22:

| Volume | Sub ID | Ended | Rolf's disposition |
|---|---|---|---|
| `/hpc/groups/miket` | 3347 | 2019-06-30 | Cancelled long ago. Directory still appears because `/hpc/groups/miket` is a **bind mount of `/data/talkowski`** (volume was renamed in `groups_lab.yml` ~10y ago). No subscription needed. |
| `/hpc/groups/awad1` | 8840 | 2025-03-31 | Definition commented out since end date; **volume deleted 2026-05-22**. Resolved. |
| `/hpc/groups/adsleepeeg` | 5038 | 2023-11-30 | No ticket received; **Rolf will delete next week**. |
| `/hpc/groups/shahlab` | 18389 | 2024-04-30 | No ticket received; **Rolf will delete next week**. |
| `/hpc/groups/scottcarter1` | 9496 | 2024-10-31 | No ticket received; **Rolf will delete next week**. |
| `/hpc/groups/best-trial` | 24027 | 2024-10-31 | No ticket received; **Rolf will delete next week**. |
| `/hpc/groups/aanand` | 16169 | 2024-12-31 | No ticket received; **Rolf will delete next week**. |
| `/hpc/groups/cteu_imaging` | 25765 | 2025-01-31 | No ticket received; **Rolf will delete next week**. |
| `/hpc/groups/bml` | 28451 | 2025-01-31 | No ticket received; **Rolf will delete next week**. |
| `/hpc/groups/epi-gen-share` | 19525 | 2025-01-31 | No ticket received; **Rolf will delete next week**. |
| `/hpc/groups/insomnia` | 8243 | 2025-01-31 | No ticket received; **Rolf will delete next week**. |
| `/hpc/groups/bass1` | 10503 | 2026-01-31 | No ticket received; **Rolf will delete next week**. |
| `/hpc/groups/thakurelaLab` | 26488 | 2026-04-30 | No ticket received; **Rolf will delete next week**. (Implicitly answers the "30 day hold" question.) |

**Importer behavior**: ended-sub bucket stays as-is — directories drop out of pasxml when Rolf deletes them. No code change required, but `miket`-style bind mounts mean **a volume's continued presence in pasxml is not by itself proof of a billable share** — see gotcha below.

## Group B — Directory exists, no subscription history

These were in the importer's **unmatched bucket** (escalated via Honeybadger). Original proposal: create unbillable subscriptions with **PH2776** as the funding source. Rolf's 2026-05-22 reply categorizes each:

### Cluster-internal — opt out

Rolf: _"All the other volumes are used by the cluster."_ These should be filtered before they reach the unmatched bucket. Candidates for the [[BriefCase Volume Matching Logic|opt-out prefix filter]]:

- `/hpc/groups/appstest`
- `/hpc/groups/buildtree`
- `/hpc/groups/erisxdl`
- `/hpc/groups/released`
- `/hpc/groups/slurm-warewulf`
- `/hpc/groups/slurm-warewulf1`
- `/hpc/groups/slurm-warewulf2`
- `/hpc/groups/slurm-warewulf3`
- `/hpc/groups/testsuite`
- `/hpc/groups/virt4eris2`

Decision needed: filter as an explicit exact-path allowlist (safer) vs. by prefix (e.g. `slurm-*`). Filter as explicit paths for now — too few to justify a prefix rule, and a `slurm-*` regex would mask the day a real `slurm-…` lab subscription appears.

### Prepaid — needs internal-sub pattern decision

- `/hpc/groups/ccr` — prepaid
- `/hpc/groups/cctm` — prepaid

Rolf identified these as prepaid but did **not** explicitly endorse the PH2776 unbillable-subscription pattern. Open question: do prepaid shares already have a representation in RC Services, or is this the moment to standardize? **See [[BriefCase Prepaid Volume Handling]] (TBD) — Eli to decide pattern.**

### In transition — keep flagged

- `/hpc/groups/bwh-comppath-img3` — created during a corruption issue in `img`; user is migrating data from `img` → `img3`. Once migration completes, Rolf will tell us whether to create a new subscription for `img3`. **Action: leave in unmatched bucket; revisit when Rolf signals migration is done.**

### Resolved

- `/hpc/groups/rftest` — deleted by Rolf

### Unknown — still open

- `/hpc/groups/whaas` — Rolf doesn't know. **Eli to investigate** (lab match? abandoned?). Stays in unmatched bucket until classified.

### `/hpc/scratch/*` — opt out (with one exception)

Rolf: _"We do plan in converting `/hpc/scratch/pcpgm`. Otherwise, `/hpc/scratch/<letter>` and home are free and can be ignored."_

- **Single-letter `/hpc/scratch/{a..z}` and `/hpc/scratch/home`**: confirmed never billable → add to opt-out filter.
- **`/hpc/scratch/pcpgm` (BriefCASE-2994)**: transitional. Rolf plans to convert it (presumably to `/hpc/groups/pcpgm`). **Action: keep matching for now via the existing path; when Rolf signals the conversion, update the subscription's `share_path` and the matching will follow.**

## Gotcha — Bind mounts in pasxml

`/hpc/groups/miket` continues to appear in pasxml even though its subscription ended in 2019, because the path is a **bind mount of `/data/talkowski`** (the lab was renamed in `groups_lab.yml` ~10 years ago). Pasxml reports the mount, not the underlying ownership. The importer cannot distinguish a bind mount from a real share by looking at pasxml alone — this is one of the reasons the matching ladder ([[BriefCase Volume Matching Logic]]) has multiple buckets rather than a single match/no-match decision.

## Follow-ups

- [ ] Add cluster-internal paths to the opt-out filter (exact paths, not prefix)
- [ ] Add `/hpc/scratch/{a..z}` + `/hpc/scratch/home` to the opt-out filter
- [ ] Decide on prepaid-share representation (ccr, cctm) — possibly a new ADR
- [ ] Investigate `/hpc/groups/whaas` — what is it?
- [ ] Watch for Rolf to confirm Group A deletions next week — re-run importer, the ended-sub bucket should shrink by 11
- [ ] Watch for Rolf to signal `bwh-comppath-img3` migration completion → possibly new subscription for `img3`
- [ ] Watch for Rolf to signal `/hpc/scratch/pcpgm` → `/hpc/groups/pcpgm` conversion → update subscription `share_path`

## Related

- [[Briefcase Billing Takeover]] — parent work
- [[BriefCase Volume Matching Logic]] — bucket taxonomy that produced this list
- [[Rolf Fabre]] — escalation contact
- [[RC Services (Eris)|rcservices]]
