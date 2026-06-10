---
date: "2026-06-10"
description: "Open compliance review for RC FinOps — what cloud cost data is shown, whether any is sensitive, and whether role-scoped + MGB-subsidy visibility (PI vs admin) needs formal review"
project: "rcfinops"
status: proposed
tags:
  - compliance
---

# RC FinOps Cost Data Visibility Review

> [!question] Status: not yet reviewed
> Scaffolded 2026-06-10 from the [[repo-sync]] of [[RC FinOps|rcfinops]]. The app exposes researcher-facing cloud cost data with role-scoped visibility; this note holds the open questions until a review is done. Nothing here is a finding yet.

## Why this review
[[RC FinOps|RC FinOps]] is a **researcher-facing** surface (distinct from eris's internal/finance audience) that shows cloud cost line items. Two mechanisms control what a given user sees:
- **Role × funding source** — visibility scoped by user role against [[002-FundingSource as Cost-Ownership Authority|FundingSource]] (enriched from Insight).
- **MGB-subsidy flagging** — subsidized line items flagged/filtered/tinted, changing what PIs see vs. admins ([[MGB Subsidy Flagging Business Rule]]).

Because access differs by role and the data crosses funding/ownership boundaries, it warrants a deliberate check before the app is deployed to researchers.

## Requirements / Open Questions
_To be answered with the review. None resolved yet._

- [ ] **What data is actually displayed?** Enumerate the fields on `AzureCostLineItem` shown in the dashboard and line-item index (cost, resource/subscription IDs, `vm_name`, resource group, funding source, …).
- [ ] **Is any of it sensitive?** Does any displayed field constitute PHI, PII, or otherwise restricted data, or is cloud cost/usage metadata out of scope for HIPAA/IRB? (Confirm — don't assume.)
- [ ] **Is role-scoped visibility correct and enforced server-side?** Can a PI see only their own funding sources' line items? Verify the `visible_to` UNION scope can't be bypassed via direct URL/params (filter permit list is derived from `LineItemBrowser`).
- [ ] **PI vs. admin boundary** — is the subsidy view (what's subsidized vs. charged) appropriate to expose to PIs, or admin-only?
- [ ] **Insight dependency** — does pulling funding ownership from Insight introduce any data-handling obligation (data-use agreement, refresh/staleness, who can be enriched)?
- [ ] **Does this need IRB/privacy sign-off at all, or is it an operational/finance tool outside that scope?** Determine the right reviewer.

## Implementation
_How the controls are built (for the reviewer's reference). See [[RC FinOps Week-1 Build Log]] for detail._
- Role-based access control + site administration (groups, permissions matrix, users), all role-gated.
- `FundingSource` (from Insight) as the cost-ownership authority; dashboard scoped by role against it.
- `visible_to` query scope (rewritten as a UNION for covering-index performance) enforces row-level visibility.
- MGB-subsidy flag set at import, surfaced as a filter + row tint.

## Audit Trail
- 2026-06-10 — review scaffolded from repo-sync; no review conducted yet.

## Related
- [[RC FinOps|RC FinOps — Cloud Cost Dashboard]]
- [[002-FundingSource as Cost-Ownership Authority]]
- [[MGB Subsidy Flagging Business Rule]]
- [[Alissa Scharf]] — Manager, Research Computing Core
- [[Michael Oates]] — Director, Research Computing
</content>
