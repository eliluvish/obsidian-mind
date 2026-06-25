---
date: "2026-06-25"
description: "Daily sync of RCServices Azure subscription attribution (RITM → researcher/fund) from eris into rcfinops — replaces static seeds, adds PaperTrail audit trail."
project: "rcfinops"
github_issue:
status: active
tags:
  - work-note
---

# RCS Metadata Sync from Eris

## Context

`RcsMetaDatum` in rcfinops was previously populated from **static seeds**, meaning RITM-to-researcher/fund attribution drifted whenever subscriptions were created, refunded, or transferred in RCServices. This makes cost line-item attribution stale — the cost shows up against the right RITM but the wrong PI or fund.

The fix is a live sync from the eris API. This is a **cross-repo integration**: eris exposes a feed (producer), rcfinops consumes it (consumer).

## Implementation (branch `feature/rcs-meta-data-eris-sync`, unmerged as of 2026-06-25)

**Consumer side (rcfinops):**
- `Rcservices::MetaDataSync` service — pulls the current Azure subscription mapping from the eris JSON feed and upserts one `RcsMetaDatum` per RITM (upsert-in-place, not snapshot)
- Funding/owner changes overwrite the row; cancelled subscriptions whose RITM has dropped from the feed are left in place so historical cost line items still attribute correctly
- Blank-RITM subscriptions are skipped
- Exposed as `rcs_meta_data:sync` rake task, intended for **daily cron**
- PaperTrail added to `RcsMetaDatum`; sync stamps versions with `whodunnit: "rcservices_sync"` to distinguish automated rewrites from manual edits
- 119-line spec in `spec/models/rcservices/meta_data_sync_spec.rb`

**Producer side (eris):** `GET /api/v1/azure_subscriptions` — see [[RC Services (Eris)|rcservices]] and [eris#2017](https://github.com/csb-ric/eris/issues/2017). Authenticated via `API_KEY_FOR_RCFINOPS`.

## Pending

- [ ] Merge `feature/rcs-meta-data-eris-sync` to main
- [ ] Configure daily cron for `rcs_meta_data:sync` (deploy step)
- [ ] Verify `API_KEY_FOR_RCFINOPS` is provisioned in production environment

## Related

- [[RC FinOps — Cloud Cost Dashboard|rcfinops]]
- [[RC Services (Eris)|rcservices]] — eris#2017 is the producer side of this integration
- [[Index]]
