---
date: "2026-06-17"
description: "RC Services Biweekly Sync — recap and prep covering 2026-06-03 to 2026-06-17"
project: "rcservices"
meeting_type: weekly
attendees:
  - "Alissa Scharf"
  - "Laura Brown"
tags:
  - work-note
  - meeting
---

# RC Services Weekly Sync — 2026-06-17

## Attendees

- [[Alissa Scharf]]
- [[Laura Brown]]

## Recap

_Window: 2026-06-03 to 2026-06-17._

### New features

- Users now have a **My Applications** menu where they can see and launch the services they have access to [[#1992](https://github.com/csb-ric/eris/pull/1992)].
- RC Services now collects RFA storage usage automatically every day, so it can be billed without anyone running the old manual scripts — a key step in taking RFA billing fully in-house [[#1994](https://github.com/csb-ric/eris/pull/1994)].

### Bug fixes & improvements

- BioRender purchases now set a clear expectation that access can take up to 24 hours, and fixed gaps where access wasn't granted correctly on purchase or renewal [[#1990](https://github.com/csb-ric/eris/issues/1990)].
- BioRender purchase confirmations now include the portal link and login instructions [[#1989](https://github.com/csb-ric/eris/issues/1989)].
- The login form now explains more clearly what to enter as the username [[#1988](https://github.com/csb-ric/eris/issues/1988)].
- ChemDraw subscriptions now bill on their anniversary date [[#1982](https://github.com/csb-ric/eris/issues/1982)].
- Fixed an error that could occur when editing a project without an account selected; the project keeps its owner [[#1985](https://github.com/csb-ric/eris/issues/1985)].

### Resolved this week

- [#1962](https://github.com/csb-ric/eris/issues/1962) — RFA usage collection is now in place
- [#1982](https://github.com/csb-ric/eris/issues/1982) — ChemDraw billing moved to anniversary date
- [#1985](https://github.com/csb-ric/eris/issues/1985) — Project edit error fixed
- [#1987](https://github.com/csb-ric/eris/issues/1987) — Renewed the five May-2025 ChemDraw subscriptions
- [#1988](https://github.com/csb-ric/eris/issues/1988) — Clearer login form language
- [#1989](https://github.com/csb-ric/eris/issues/1989) — BioRender login instructions in confirmation
- [#1990](https://github.com/csb-ric/eris/issues/1990) — BioRender provisioning expectation + entitlement fixes

_(All closed by Eli.)_

### Requires resolution / finalization / clarification or closing

- [#1680](https://github.com/csb-ric/eris/issues/1680) — Convert stimulus controllers that use templates from the DOM to instead use an endpoint
- [#1682](https://github.com/csb-ric/eris/issues/1682) — Update stimulus subscription_users controller to take in a template
- [#1811](https://github.com/csb-ric/eris/issues/1811) — Refactor invoice generation / sending
- [#1812](https://github.com/csb-ric/eris/issues/1812) — Split invoices into sent and unsent tabs
- [#1844](https://github.com/csb-ric/eris/issues/1844) — Add `FreezerProService` service
- [#1863](https://github.com/csb-ric/eris/issues/1863) — When cancelled within the month, mark tracking record unbillable
- [#1926](https://github.com/csb-ric/eris/issues/1926) — Mock up for ordering where they enter their finance person
- [#1952](https://github.com/csb-ric/eris/issues/1952) — Retire legacy MAD3 import path after the new Isilon job goes live
- [#1955](https://github.com/csb-ric/eris/issues/1955) — Add settings tab to services
- [#1968](https://github.com/csb-ric/eris/issues/1968) — Admin chatbot list
- [#1973](https://github.com/csb-ric/eris/issues/1973) — BriefCase shadow run + cutover from legacy CentOS 6 pipeline
- [#1974](https://github.com/csb-ric/eris/issues/1974) — Add BriefCase monthly billing aggregator
- [#1984](https://github.com/csb-ric/eris/issues/1984) — MAD3/BriefCase: make share path and full path searchable in the subscriptions admin index

### Behind-the-scenes work

_Internal improvements with no user-visible change. Kept high-level on purpose._

Continued the groundwork to move the storage billing pipelines off the older legacy scripts — validation and parallel runs so the eventual cutover is safe before anything changes for users. Also some internal cleanup to make subscription funding logic easier to maintain.

## Unresolved Questions from Vault Notes

**From [[2026-05-20 Meeting — rcservices]]:**
- Laura reports fund financial contacts most often reach out to her *after* invoices land — confirmed it's the fund-level fin contact (not project- or subscription-level). **Ask Alissa**: should fund fin contacts get access to all of the grant's subscriptions, so they can self-serve on invoice questions instead of routing through Laura?

**From [[FreezerPro RedCap Integration]]:**
- [[Svetlana Rojevsky]] asked whether Eli knows of billing scenarios not contemplated in the 2026-02-03 meeting notes. Edge cases to think through: mid-year user-count changes crossing tier boundaries, PI departure mid-cycle, fund expiration before renewal.
- SR asked whether Eli has worked with REDCap before — pending response.

## Discussion

### GraphPad Prism — sunsetting after next year

[[Alissa Scharf]] reported that GraphPad is offering only **one more year of the legacy model**, after which the cost jumps to **~$1,000,000** — beyond what RCC can fund. Her read: **RCC likely cannot offer Prism after this coming year.** She'll keep the legacy model for the upcoming year while she does the work to figure out alternatives. Researchers who still need it would likely have to **purchase on their own**. Alternatives noted: BioRender now has graphing, plus other statistical tools; GraphPad itself stays relatively cheap with student rates. She also flagged general price creep on the software catalog (e.g. a license that was ~$35 when she started is now $110 and rising another $100+).

### Storage usage report

Walked through the storage usage view together. Units are in **bytes** by design — Eli stores the lowest common unit so values can be converted later. One subscription showed by far the largest storage; another was **not yet started**. Alissa had "create monthly report" / discrepancy view on her list; Eli offered to add it to the existing view.

### SAS Enclave — settled (see Decisions)

[[Alissa Scharf]] confirmed the need: SAS for the enclave needs a differentiator so that submitting a request creates a **separate ticket routed to Eli's (the Enclave) team**, getting RCC out of the manual-email loop. Eli explained that making it a **new service** unlocks custom messaging, downloads, and the rest of the per-service extras. Alissa confirmed they **want custom messaging** — which settled it as a new service. Resolves the open question in [[SAS Enclave License Type]].

### Cadence

Agreed the biweekly slot is too infrequent — moving to **weekly** (or a 45-minute slot), scheduled before Eli's 1:1 with [[Daniel Guettler]].

## Decisions

- **SAS Enclave will be its own new service** (Option B), not a platform option on the existing SAS Citrix/Server service — chosen because RCC wants custom messaging, which a standalone service provides. Mirrors SAS Citrix except the request ticket routes to the **Enclave team** instead of the RCC software queue. Same billing terms; the major difference is ticketing only. [[Alissa Scharf]] + Eli, 2026-06-17. Resolves [eris#1997](https://github.com/csb-ric/eris/issues/1997).
- **GraphPad Prism to be discontinued from the RCC catalog after the upcoming legacy year** (Alissa's call) — cost becomes unsustainable (~$1M); researchers steered toward alternatives or self-purchase.
- **Meeting cadence → weekly** (or 45 min), scheduled before Eli's Daniel 1:1.

## Action Items

- [ ] [[Alissa Scharf]] — write up the SAS Enclave service page / content (modeled on SAS Citrix)
- [ ] Eli — confirm the SAS Enclave service fields, then build it as a new standalone service routing to the Enclave team ([eris#1997](https://github.com/csb-ric/eris/issues/1997))
- [ ] Eli — add the discrepancy / monthly report to the storage usage view
- [ ] Eli — set up a weekly (or 45-min) RC Services meeting before the Daniel 1:1

## Open Questions

- Will researchers who lose RCC-provided Prism need to self-purchase, and does RCC actively steer them to BioRender graphing / other stats tools? (Alissa: "probably.")
- Not covered this meeting (still open from prep): fund-contact self-serve access ([[2026-05-20 Meeting — rcservices]]), FreezerPro billing edge cases + REDCap-experience reply ([[FreezerPro RedCap Integration]]), and the prepaid-balance ask ([[Prepaid Remaining Balance on Invoices]], deploy hold until after July 5).

## Related

- [[RC Services (Eris)|rcservices]]
- [[Alissa Scharf]]
- [[Laura Brown]]
- [[SAS Enclave License Type]]
- [[Prepaid Remaining Balance on Invoices]]
- [[Storage Usage Billing Pipeline Takeover]]
- [[Daniel Guettler]]
