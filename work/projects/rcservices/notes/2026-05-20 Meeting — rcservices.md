---
date: "2026-05-20"
description: "RC Services weekly sync — recap and prep covering 2026-05-06 → 2026-05-20"
project: "rcservices"
meeting_type: weekly
attendees:
  - Alissa Scharf
  - Laura Brown
tags:
  - work-note
  - meeting
---

# RC Services Weekly Sync — 2026-05-20

## Attendees

- [[Alissa Scharf]]
- [[Laura Brown]]

## Recap

_Window: 2026-05-06 → 2026-05-20._

### Shipped this week

Storage billing moved forward on the Powerscale/MAD3 side: the MAD3 usage importer is live, building on the StorageUsageSnapshot model, and Isilon quotas are now matched to MAD3 subscriptions by stored path so unmatched shares get escalated rather than silently dropped ([#1941](https://github.com/csb-ric/eris/issues/1941), [#1939](https://github.com/csb-ric/eris/issues/1939)). On the Azure side, AzureVmSubscription validation was loosened to handle real-world `lun_name` collisions, PH2776 is now correctly flagged unbillable on import, and the empty-RITM investigation was closed out ([#1919](https://github.com/csb-ric/eris/issues/1919), [#1922](https://github.com/csb-ric/eris/issues/1922), [#1907](https://github.com/csb-ric/eris/issues/1907)). Daily jobs are now enqueued via a rake task with a `recurring.yml` schedule, so the storage importers and other periodic work run on their own ([#1925](https://github.com/csb-ric/eris/issues/1925)).

For end users, the refund flow now covers pre-billed software services — previously refunds weren't surfacing for software subscriptions at all ([#1899](https://github.com/csb-ric/eris/issues/1899)). The fund/funding-source UX was rebuilt: the new-account overlay was replaced with a modal + select2 picker, adding a new fund mid-project no longer breaks, and creating a new funding source now reloads the page so it's searchable immediately ([#1885](https://github.com/csb-ric/eris/issues/1885), [#1902](https://github.com/csb-ric/eris/issues/1902)). The DIPR fund forms were removed and the "edit current funding" styling was fixed ([#1916](https://github.com/csb-ric/eris/issues/1916), [#1917](https://github.com/csb-ric/eris/issues/1917)). The project edit page was reorganized into tabs ([#1934](https://github.com/csb-ric/eris/issues/1934)), the services edit page got markdown support and renewability information ([#1928](https://github.com/csb-ric/eris/issues/1928), [#1930](https://github.com/csb-ric/eris/issues/1930)), sent emails can now be previewed in a lazy-loaded modal ([#1678](https://github.com/csb-ric/eris/issues/1678)), and users can choose how many records they see per page ([#1752](https://github.com/csb-ric/eris/issues/1752)). Smaller polish: input scrubbing for copy/pasted formatting from Word ([#1698](https://github.com/csb-ric/eris/issues/1698)), reactivation limited to subscriptions without an existing cancelled sub of the same type ([#1731](https://github.com/csb-ric/eris/issues/1731)), and a data-retention attestation on cloud/storage cancellation in place of the old reason field ([#1799](https://github.com/csb-ric/eris/issues/1799)).

Internal improvements: tables holding free-text fields were converted to `utf8mb4_0900_ai_ci` to fix encoding errors on pasted Unicode (resolving an `ActiveRecord::StatementInvalid` from `use_case`); the `BillingController` inline jQuery was rewritten as a Stimulus controller; the funds-create path replaced rescue-for-control-flow with explicit guards; a dead JSON branch in `FundsController#lookup` was removed; Workday cost-center sync was confirmed to be on a schedule; and the long-standing `charges` vs `cached_charges` question was investigated and closed ([#1947](https://github.com/csb-ric/eris/issues/1947), [#1687](https://github.com/csb-ric/eris/issues/1687), [#1937](https://github.com/csb-ric/eris/issues/1937), [#1935](https://github.com/csb-ric/eris/issues/1935), [#1915](https://github.com/csb-ric/eris/issues/1915), [#1704](https://github.com/csb-ric/eris/issues/1704)).

### Resolved this week

[[Daniel Guettler]] closed several items on his side: cached-charge display for software services, instrumentation around reactivation, the user-lookup input clearing on `/admin/funds/new`, the EndNote user-agreement overlay exit, and his PAS keygiver course ([#1665](https://github.com/csb-ric/eris/issues/1665), [#1664](https://github.com/csb-ric/eris/issues/1664), [#1673](https://github.com/csb-ric/eris/issues/1673), [#1683](https://github.com/csb-ric/eris/issues/1683), [#1669](https://github.com/csb-ric/eris/issues/1669)).

### Requires resolution / finalization / clarification or closing

- [#1680](https://github.com/csb-ric/eris/issues/1680) — Convert stimulus controllers that use templates from the DOM to instead use an endpoint (Tech Debt; [[Daniel Guettler]])
- [#1682](https://github.com/csb-ric/eris/issues/1682) — Update stimulus subscription_users controller to take in a template (Tech Debt; [[Daniel Guettler]])
- [#1811](https://github.com/csb-ric/eris/issues/1811) — Refactor invoice generation / sending
- [#1812](https://github.com/csb-ric/eris/issues/1812) — Split invoices into sent and unsent tabs
- [#1844](https://github.com/csb-ric/eris/issues/1844) — Add `FreezerProService` service (Waiting — REDCap schema)
- [#1863](https://github.com/csb-ric/eris/issues/1863) — When cancelled within the month, mark tracking record unbillable
- [#1926](https://github.com/csb-ric/eris/issues/1926) — Create a mock-up for ordering where the requester enters their finance person

## Unresolved Questions from Vault Notes

From [[FreezerPro RedCap Integration]]:

- SR asked whether Eli knows of billing scenarios not contemplated in the 2026-02-03 meeting notes. Need to think through edge cases (mid-year user count changes crossing tier boundaries, PI departure mid-cycle, fund expiration before renewal).
- SR asked whether Eli has worked with REDCap before — pending response.

## Discussion

### Transition to PowerScale API for MAD usage data

[[Chris Mow]]'s script currently pulls MAD usage into a database for RC Services. The team is moving to direct API pulls from PowerScale. For June, invoices will still use Chris's script, but the results will be compared against the API data to confirm accuracy before fully cutting over.

[[Alissa Scharf]] raised a recurring issue: some accounts haven't been showing up in RC Services. Rolf attributed those to internal accounts, but Alissa has been surfacing this in management meetings — the gap reflects manual processes that don't reliably feed the system. Eli has previously offered Rolf an API to automate the data entry, but Rolf continues to manage it manually. The group agreed automation is needed, and Alissa will set up a working session with Rolf and Kevin.

Billing methodology was also discussed: should MAD usage bill on average usage across the month, or the last day's snapshot? Edge cases like mid-month cancellations and data-retention timing complicate both. Eli suggested aligning deletion schedules to simplify the math; Alissa will follow up with Rolf and Kevin and decide after the June 1st data is in.

Ties into [[Storage Usage Billing Pipeline Takeover]] and [[RFA Billing Takeover and Powerscale Migration]].

### SAS subscription process for Enclave access

The current path for an Enclave user to get SAS is convoluted: multiple manual steps and coordination between Ken, Randy, Will, and Kristine. Confusing for users, inefficient for everyone.

Eli proposed surfacing an "Enclave" option on the SAS service request form so users declare Enclave usage at order time. That would let tickets route directly to the Analytics Enclave team for confirmation, collapsing several handoffs. Alissa will dig into the current user instructions and coordinate with Eli on adding the third option.

Tangentially: RC Services supports automatic integration for some products but isn't using it for SAS. Worth revisiting for the Enclave path.

### Azure / MTM / Demo subscription cleanup

[[Laura Brown]] confirmed Jane's fund no longer appears for Azure — recent fund-tracking updates landed correctly. Alissa noted the MTM investigation is closed.

Demo is migrating off shared environments and onto its own subscriptions; some legacy subscriptions are still in RC Services during the transition and will need cleanup.

### Cancel-and-refund for software services ([#1899](https://github.com/csb-ric/eris/issues/1899))

Demoed the new flow on a March tracking record — running cancel-and-refund now produces a negative $65 entry on the June journal, giving a cleaner audit trail than asking users to journal corrections on their end. Alissa recalled the old Misha-era guidance ("they should do it on their end with their grants manager") and explicitly endorsed flipping that for the new feature: "I think that's worth doing, Laura."

Important caveats Eli walked through:

- **Refund and cancel are independent actions** — you can refund without cancelling.
- **Be careful which services you cancel.** For SCIM/Okta-provisioned products (Zoom is the canonical example), cancellation removes the user from the access group and they lose product access immediately. For non-SCIM products like BioRender and In Vivo, cancellation does *not* remove access — that's a manual step.
- **Historical refunds work** — negative tracking records can be created for previous months.

### Project edit / funding source management

The project and services edit pages now use tabbed navigation ([#1934](https://github.com/csb-ric/eris/issues/1934)), with markdown support for descriptions ([#1928](https://github.com/csb-ric/eris/issues/1928)) and clearer download / Okta SSO information.

**Bug — can't add additional funds to a project.** Laura shared her screen on a project split between two funds. After using "add new funding source" the new fund displays, but clicking "additional funds" doesn't let her attach it. Alissa confirmed she hit the same thing on the SAS project — at least the second occurrence. Eli will investigate. Distinct from [#1885](https://github.com/csb-ric/eris/issues/1885) (create-project flow), which was already fixed.

**Expired funds.** Alissa asked for better visibility on expired or inactive funds in the UI — current display doesn't make their state obvious. Related: an expired fund was apparently used for a new order, which shouldn't be possible. Eli will investigate the verification gap and how expired funds should be surfaced and gated.

### Order page and external service integration

Demoed the external order URL feature on the order page — services can now redirect users to external systems like ServiceNow directly from the RC Services order page, instead of duplicating the order flow. Reviewed markdown editing for service descriptions and how services are categorized / made visible on the order page. Alissa adjusted visibility settings for Azure and RFA live during the demo.

### AI tangent (closing)

Brief exchange at the close: Laura's reservation about AI is specifically about infrastructure electricity and water usage, not the technology itself. Eli acknowledged the concern is legitimate.

## Decisions

- **June MAD billing strategy** — continue using Chris's script for June invoices while running the PowerScale API pull in parallel for comparison. Final cutover follows once the two reconcile.
- **Cancel-and-refund is endorsed for RC Services use** — overturning the prior Misha-era guidance that users should always journal their own corrections. [[Laura Brown]] is cleared to use it going forward, with discretion. Caveat: avoid cancelling SCIM-provisioned services (Zoom, etc.) unless removing access is intended; refund-only is safer in those cases.
- **Add an "Enclave" option to the SAS service request form** so Enclave orders route directly to the Analytics Enclave team for confirmation, removing several manual handoffs.
- [[Alissa Scharf]] will promote the markdown editing on the services edit page — feature accepted as-is.

## Action Items

- [ ] [[Alissa Scharf]] — compare June MAD billing output from [[Chris Mow]]'s script against the new PowerScale API pull; confirm accuracy before next cutover step.
- [ ] [[Alissa Scharf]] — reach out to Rolf to ensure all relevant accounts are properly entered for MAD usage tracking (including the "internal accounts" gap).
- [ ] [[Alissa Scharf]] — decide between average-usage vs. last-day-of-month MAD billing methodology after reviewing the June 1st data.
- [ ] [[Alissa Scharf]] — set up a working session with Kevin and Rolf to plan automation of storage data entry and reduce manual intervention.
- [ ] [[Alissa Scharf]] — pull the current user instructions for SAS Enclave orders and coordinate with Eli on adding the third "Enclave" option to the SAS service request form.
- [ ] [[Eli Luvish]] — investigate the "additional funds won't attach" bug on the project edit page (reproduces on Laura's project and Alissa's SAS project). Distinct from [#1885](https://github.com/csb-ric/eris/issues/1885); open a new issue.
- [ ] [[Eli Luvish]] — investigate how an expired fund was used for a new order; close the verification gap and improve visibility of expired/inactive funds in the project edit UI.
- [ ] [[Alissa Scharf]] — start using markdown for live service descriptions on the services edit page.

## Open Questions

- Laura reports that fund financial contacts most often reach out to her *after* invoices land. She confirmed it's the fund-level fin contact (not a project- or subscription-level contact) doing the outreach. **Ask Alissa**: should fund fin contacts be given access to all of the grant's subscriptions, so they can self-serve on invoice questions instead of routing through Laura?

## Related

- [[RC Services (Eris)|rcservices]]
- [[Alissa Scharf]]
- [[Laura Brown]]
- [[RFA Billing Takeover and Powerscale Migration]]
- [[Storage Usage Billing Pipeline Takeover]]
- [[FreezerPro RedCap Integration]]
