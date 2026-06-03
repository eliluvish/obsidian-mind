---
date: "2026-05-27"
description: "Strict Fund#expired? semantics across every fund-attach path — removes the prior 6-month internal-fund grace period. Shipped to master via #1983 (closes #1981)."
project: "rcservices"
status: completed
github_issue: 1981
tags:
  - work-note
---

# Fund Expiry Enforcement

## Context

A fund could previously still back a subscription for up to **6 months after its `end_date`** for internal funds — the old `Fund#ineligible?` carried a grace period. #1981 asked to tighten this: a fund should be unusable the day its `end_date` passes, with no grace. Confirmed with the product owner as the intent of the ticket. Shipped to master 2026-05-27 via PR #1983 (commit `c3a27f66`, closes #1981).

## What Changed

Enforces strict `Fund#expired?` semantics across **every path that can attach a fund to a subscription** — not just the model validation, because two forms write `subscription_funds` directly and bypass subscription validation.

- **`Subscription#no_expiring_funding`** now blocks on `expired?` (was `ineligible?`). The now-dead `Fund#ineligible?` and its `SubscriptionFund` delegate were **removed**.
- **`CurrentFundChangeForm`** and **`ReplaceFundForm`** gained expired-fund guards — these write `subscription_funds` directly and would otherwise sidestep the model check.
- **Funding selects** (`assigned_funds_for_select`, and the admin branches of `_subscription_fund_form`, `_funding_information`, `subscription_funds/edit`) now use the `.active` scope, so expired funds never render as options.
- **New-funding-source modal** flags an expired grant after lookup; the create flows keep expired funds out of the select via a warning toast.

## Why It Matters

- **Behavioral change, not a bug fix.** The 6-month internal-fund grace is gone. Any subscription that was relying on it will now be blocked at the next fund-attach. Confirmed as intended with the product owner — recorded in [[Key Decisions]].
- The fix is **defense-in-depth across layers** (model validation + form guards + scoped selects + UI warnings) precisely because the model validation alone was bypassable by the two direct-write forms. If a future fund-attach path is added, it needs its own `expired?` guard — the model check is necessary but not sufficient.

## GitHub Issues

- [eris#1981](https://github.com/csb-ric/eris/issues/1981) — disallow subscriptions with expired funds
- [eris#1983](https://github.com/csb-ric/eris/pull/1983) — implementing PR (closes #1981)

## Related

- [[RC Services (Eris)|rcservices]]
- [[Alissa Scharf]] — RC Services stakeholder
- [[Key Decisions]] — behavioral-change record
