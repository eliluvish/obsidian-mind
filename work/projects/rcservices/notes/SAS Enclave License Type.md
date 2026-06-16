---
date: "2026-06-16"
description: "Alissa's request to add a SAS Enclave license type whose requests route to the Enclave team instead of the RCC software queue — new service vs SAS platform option is TBD (eris#1997)."
project: "rcservices"
status: active
github_issue: 1997
tags:
  - work-note
---

# SAS Enclave License Type

## Context

[[Alissa Scharf]] requested (2026-06-16, to discuss Wed 2026-06-17) a new **SAS Enclave** license type. When a user selects it, the request **ticket routes to the Enclave team** instead of the current RCC software queue. Her framing: *"We can either add to the current SAS Citrix/Server service or create a new one called SAS Enclave, whichever makes more sense — but the biggest piece is the ticketing is different."*

Tracked in [eris#1997](https://github.com/csb-ric/eris/issues/1997).

## How routing works today

The "ticket" is an email that spawns the downstream ServiceNow ticket. `SasSubscription` includes the `ServiceNowTicketing` concern → `SubscriptionMailer.new_subscription(user, self, mail_options)`. The destination is driven entirely by each subscription's **`mail_options[:to]`**.

- `SasSubscription#mail_options` currently routes to **`software-eris@partners.org`** — *not* `rcc@mgb.org`. The generic mailer defaults to `rcc@mgb.org`, but every subscription overrides via `mail_options`.
- **Flag for Alissa:** confirm "rcc@mgb.org" in her request is shorthand for the current software/RCC queue (`software-eris@partners.org`), so Enclave gets split from the *correct* current target.
- Net: the core ask is a **new `to:` address** for Enclave (the Enclave team's queue). Low-complexity either way — the decision is structural, not feasibility.

## The decision — new service vs. SAS platform option

> [!question] To be determined (Wed 2026-06-17)
> Implement Enclave as **(A)** a third platform option on the existing SAS service, or **(B)** a separate `SasEnclaveService` mirroring the existing `SasDesktopService`.

### Tradeoffs

| | **A — option on SAS Citrix/Server** | **B — new SAS Enclave service** |
|---|---|---|
| Routing | Branch `mail_options[:to]` on platform | Own `mail_options` → Enclave team (unconditional) |
| New code | Minimal — reuses SAS billing/proration/renewal | Duplicates SAS billing logic unless extracted to a shared concern |
| Selection UI | Add `Enclave` to `PLATFORMS` (third value) | New orderable service in the catalog |
| User instructions | `send_user_instructions` must stop `raise`-ing on Enclave; add a branch | Own instruction email (or none) — no branching |
| Precedent | — | **SAS Desktop is already its own service** because fulfillment differs |
| Cleanliness | `mail_options` + instructions become conditional | Keeps both unconditional |

### Lean

Leaning **B (separate service)** — Enclave's whole point is a *different fulfillment team*, which is a service-level distinction, and the codebase already precedents per-fulfillment-path services (Desktop). The one thing that flips it toward A: if Enclave is the **same $300/yr license** with identical billing terms, A's reuse wins. **Settle the billing question first** (below) — it's the deciding input.

### Decision criteria to settle Wed

- Is Enclave the **same license/price** as Citrix/Server ($300/yr, April-renewal proration → favors A) or a distinct offering (favors B)?
- What is the **Enclave team's ticket destination** (email/queue)?
- Should Enclave send the user an **instructions email**, or is fulfillment handled entirely by the Enclave team?

## Touchpoints (either approach)

- Routing: resolve `mail_options[:to]` to the Enclave team
- Selection UI: expose "Enclave" as selectable
- User instructions: handle/omit the Enclave instruction email (today SAS `raise`s on unknown platforms)
- Billing: confirm same terms or implement distinct
- Reporting: `to_csv` / `csv_headers` account for Enclave

## Related

- [[RC Services (Eris)|rcservices]]
- [[Alissa Scharf]]
- [[RFA ServiceNow Provisioning Pipeline]] — prior ticketing/provisioning work in eris
- [[Index]]
