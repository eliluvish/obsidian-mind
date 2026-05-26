---
date: "2026-05-20"
description: "Taking over BriefCase storage usage billing from Chris Mow — pull pasxml from pan01 storage director nodes via sa4613 service account, retire legacy CentOS 6 ruby script."
project: "rcservices"
status: active
tags:
  - work-note
---

# Briefcase Billing Takeover

## Context

Third leg of the RC billing handoff from [[Chris Mow]], alongside [[Storage Usage Billing Pipeline Takeover]] (MAD3 via Isilon API) and [[RFA Billing Takeover and Powerscale Migration]] (RFA via Powerscale API). BriefCase is the remaining service.

Open question from the 2026-04-14 meeting was whether BriefCase usage could be pulled via API or whether the existing billing script needed to be handed off Chris → [[Richard Kenny]]. Richard's 2026-05-20 email answers it: **there is a pull path** (XML from the pan01 storage director nodes), but currently it still flows through a legacy ruby script on aged erisone infrastructure that needs to be retired.

## Current Workflow (legacy — to be replaced)

1. Legacy ruby script (CentOS 6.x VM on aged erisone infra) calls `pasxml volumes` against one of the pan01 storage director nodes → `BriefCASE_data.xml`
2. Same legacy script parses the XML and produces a daily `YYYY-MM-DD_storage_report.txt`
3. The storage report is fed into Chris Mow's code, which uploads to the RC billing MySQL DB

Stable but clunky; the CentOS 6 VM is a security risk and is scheduled to be retired in favor of the eris2-nucleus cluster later summer 2026.

## Access — provided 2026-05-20

- **Service account**: `sa4613` (set up by [[Richard Kenny]])
- **Login nodes** (eris2-nucleus): `eris2n7.research.partners.org`, `eris2n8.research.partners.org`
- **Initial credential**: `sa4613/sa4613.txt` (encrypted) + decryption key from Richard — used once to bootstrap key auth, no longer needed
- **Inner-hop key**: `~sa4613/.ssh/pan01_guest_rsa` — pre-provisioned by Richard, lives on the login node(s), authenticates `guest@pan01rm*`

### Storage director nodes (pan01)

| Node     | IP             |
| -------- | -------------- |
| pan01rm1 | 10.129.84.233  |
| pan01rm2 | 10.129.86.105  |
| pan01rm3 | 10.129.84.112  |

All three confirmed interchangeable as of 2026-05-20 — pick one as primary, fall back on connection failure.

## Verified Pull Path (2026-05-20)

End-to-end automated pull works from an outside EC2 host (private IP `10.122.80.126`) with **zero human intervention** after one-time key setup. This is the operational primitive the importer will sit on top of.

**The one-liner** (from any host with passwordless SSH to sa4613 + DNS for `*.research.partners.org` + network reachability to eris2n7/n8):

```bash
ssh sa4613@eris2n7.research.partners.org \
  "/usr/bin/ssh -i ~/.ssh/pan01_guest_rsa guest@10.129.84.112 'pasxml volumes'" \
  > BriefCASE_data.xml
```

Returns the same XML schema as Richard's sample `BriefCASE_data.xml`. Sample `2026-05-20_storage_report.txt` provided by Richard for the downstream comparison (XML → report → MySQL).

**One-time setup performed**:

- Dedicated ed25519 keypair `~/.ssh/sa4613_ed25519` on the originating host (workstation; same on EC2)
- Pubkey appended to `~sa4613/.ssh/authorized_keys` on eris2n7 (homes appear shared with n8 — confirm if/when needed)
- Host keys pinned in `~/.ssh/known_hosts` for eris2n7, eris2n8, and all three pan01 IPs (the pan01 keys captured via `ssh-keyscan` from inside eris2n7)
- SSH config alias `Host eris2n7 eris2n8` with `IdentityFile` + `IdentitiesOnly yes` so cron jobs never prompt

**Gotchas hit during setup**:

- `*.research.partners.org` may not resolve from arbitrary EC2 (internal MGB zone). Test `nc -vz eris2n7.research.partners.org 22` from any new host before assuming reachability.
- The eris2-nucleus `sa4613` user owns the inner `pan01_guest_rsa` key. **Don't copy it elsewhere** — keep the two-hop pattern so the key never leaves the login node.
- If the EC2 source IP changes (instance replacement, NAT gateway swap), the research network may stop accepting connections. Pin via Elastic IP / NAT gateway with EIP if this becomes the prod host.

## Goal

Bring BriefCase into the same shape as the MAD3 takeover: daily import directly into RC Services from the pan01 storage director nodes, skip the intermediate text report, skip Chris's upload step, retire the CentOS 6 VM. Cutover pattern likely mirrors the storage usage takeover — run alongside legacy for one billing cycle, validate, then switch.

## GitHub Issues

Parent + children tracking the implementation:

- [eris#1969](https://github.com/csb-ric/eris/issues/1969) — **parent**: Add BriefCase usage importing
- [eris#1970](https://github.com/csb-ric/eris/issues/1970) — pasxml XML parser for BriefCase
- [eris#1971](https://github.com/csb-ric/eris/issues/1971) — BriefCase usage importer (`import_briefcase_storage`)
- [eris#1972](https://github.com/csb-ric/eris/issues/1972) — Match BriefCase volumes to RC Services subscriptions
- [eris#1973](https://github.com/csb-ric/eris/issues/1973) — Shadow run + cutover from legacy CentOS 6 pipeline
- [eris#1974](https://github.com/csb-ric/eris/issues/1974) — BriefCase monthly billing aggregator

## Status (2026-05-22)

Importer code is **complete on branch `1971-briefcase-usage-importer`** (20 commits ahead of master), awaiting merge. The parser, SSH fetcher, daily `LogStorageUsageJob` (with error bucketing), volume-matching logic, and daily-enqueue scheduling are all in. Only `share_path` migration + README have landed on master so far. Next gates: merge → shadow run (#1973) → monthly aggregator (#1974).

The legacy ruby parser source from Richard never arrived, but it stopped being a blocker — the pasxml schema was clear enough to build a parser fresh. See [[BriefCase Volume Matching Logic]] for the matching iterations.

## Next: Rerun checklist (2026-05-26)

Holding the merge of `1971-briefcase-usage-importer` until a fresh run confirms Rolf's promised deletions landed (see [[BriefCase Unbilled Volume Triage]] Group A — 11 directories he said he'd remove "next week" from 5/22). A clean rerun validates the importer on real recent pasxml and shrinks the ended-sub bucket without any code change.

- [ ] Pull fresh `BriefCASE_data.xml` via the two-hop one-liner — confirms the operational primitive still works
- [ ] Run `LogStorageUsageJob` against the fresh XML on the branch
- [ ] Diff buckets vs. the 5/22 run:
  - Ended-sub: expect **11 → fewer** (Rolf's deletions)
  - Unmatched: Group B paths still present (opt-out filter not yet added) — confirms nothing new appeared
- [ ] Spot-check for any **new** unmatched paths not on the 5/22 list — those are the interesting signal
- [ ] If clean: proceed with merge + opt-out filter follow-ups below

## Action Items

**Done**

- [x] Receive decryption key from [[Richard Kenny]] for `sa4613/sa4613.txt` _(2026-05-20)_
- [x] SSH into eris2n7/eris2n8 as `sa4613`, set up SSH keys from workstation _(2026-05-20)_
- [x] Replicate SSH setup from EC2 (`10.122.80.126`); confirm passwordless two-hop pull _(2026-05-20)_
- [x] Pull a sample `BriefCASE_data.xml` end-to-end from EC2 _(2026-05-20)_
- [x] Document operational primitive in `eris/README.md` (BriefCase Storage Usage section) _(2026-05-20)_
- [x] Scaffold GitHub issues for the remaining work _(2026-05-20)_
- [x] pasxml XML parser with contract specs (#1970) _(2026-05-21)_
- [x] pasxml SSH fetcher with isilon director fallback _(2026-05-21)_
- [x] `LogStorageUsageJob` happy path + error buckets (unmatched, missing-name, missing-usage, duplicate `lun_name`, active-no-volume, ended-sub) (#1971) _(2026-05-21–22)_
- [x] Schedule `LogStorageUsageJob` in the daily enqueue _(2026-05-22)_
- [x] Add `share_path` column to `hpc_meta` via migration (on master) _(2026-05-22)_
- [x] SSH `BatchMode` + `ConnectTimeout` hardening to prevent hangs _(2026-05-22)_

**Next**

- [ ] Merge `1971-briefcase-usage-importer` → master
- [ ] Diff EC2 pull against Richard's sample `BriefCASE_data.xml` — schema (root element, per-volume fields), not values
- [ ] Test all three pan01 nodes return the same volume count; document failover order
- [ ] Time 3–5 pulls; record baseline runtime + variance
- [ ] Shadow run alongside legacy CentOS 6 pipeline (#1973)
- [ ] Build monthly billing aggregator (#1974)
- [ ] Request Chris's uploader source from [[Chris Mow]] (`storage_report.txt` → MySQL billing tables) — for cutover validation only
- [ ] Confirm with Richard: can prod RC Services host reach `10.129.84.0/24` directly? If yes, drop the sa4613 hop entirely

**Open prod-deploy decisions** (resolve before merging #1971)

- [ ] Decide where the importer runs in prod (RC Services host vs. dedicated job runner) and which OS user owns the keypair
- [ ] Determine prod outbound IP stability and whether it needs to be allowlisted by the research network

## Key People

- [[Richard Kenny]] — set up the sa4613 service account and pull path; sending decryption key
- [[Chris Mow]] — owns the final-stage upload to RC billing MySQL DB; handing off
- [[Alissa Scharf]] — manager, RC Services stakeholder

## Related

- [[RC Services (Eris)|rcservices]]
- [[Storage Usage Billing Pipeline Takeover]] — sibling MAD3 takeover; same cutover pattern likely applies
- [[RFA Billing Takeover and Powerscale Migration]] — sibling RFA/Powerscale takeover; BriefCase was the open third item from the 2026-04-14 meeting
- [[Chris Mow]]
- [[Richard Kenny]]
- [[Alissa Scharf]]
