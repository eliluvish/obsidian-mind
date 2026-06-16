---
date: "2026-06-16"
description: "Alissa's request to show prepaid accounts' remaining balance on their invoices (Prepaid / Remaining balance / Subtotal), updated monthly. Display change on the invoice. Deploy hold until after July 5 (eris#1998)."
project: "rcservices"
status: active
github_issue: 1998
tags:
  - work-note
---

# Prepaid Remaining Balance on Invoices

## Context

[[Alissa Scharf]] requested (2026-06-16) that prepaid accounts' **remaining balance** appear on their invoice and update each month. Her example invoice has a ~$47K balance. Desired layout:

```
Prepaid           = XX
Remaining balance = XX
Subtotal          = XX
```

Tracked in [eris#1998](https://github.com/csb-ric/eris/issues/1998).

> [!danger] Deploy hold — after July 5, 2026
> Alissa does not want this deployed until **after July 5**. Invoices post on the **3rd**, so the July run (~July 3) is *before* July 5 — the hold ensures July invoices go out in the current format and this change first affects the **August** cycle. Do not merge to production before the July billing run completes.

## How prepaid works today

- A `Subscription` can have a `PrepaidCard` (belongs to an `Account`). On `Tracking#after_save`, a negative-amount `Transaction` draws the card down and sets `tracking.prepaid`.
- `PrepaidCard#balance = deposit + Σ(transaction.amount)` — the running remaining balance (~$47K in the example).
- Prepaid trackings are **excluded from billable line items today** (`show.xls.rxls`), so the invoice surfaces none of this currently.
- Invoice rendering: `app/views/billing/show.pdf.prawn` + `show.html.erb`; total via `Invoice#total` (sum of `tracking_records.total_with_overhead`).

## Likely shape

Display-only change. Expose `prepaid_deposit` + `remaining_balance` on the `Invoice` PORO for prepaid accounts, then render the `Prepaid / Remaining balance / Subtotal` block conditionally in the PDF + HTML invoice templates. "Updated each month" is automatic — `balance` already reflects all transactions to date.

## Questions to confirm with Alissa

- **"Prepaid"** = original `PrepaidCard#deposit`, or the amount drawn this period? (Reading it as the original deposit.)
- **"Subtotal"** = this period's charges? For prepaid accounts those are drawn from the deposit, not separately billed — is Subtotal informational vs. an amount due?
- **Multiple prepaid cards per account** — sum into one line or show per-card? (Likely one per prepaid account in practice.)
- Applies to PDF only, or also HTML/XLS?

## Related

- [[RC Services (Eris)|rcservices]]
- [[Alissa Scharf]]
- [[Prawn UTF-8 Encoding Bug in Invoice PDFs]] — prior invoice-PDF work (pcms, same Prawn rendering family)
- [[Index]]
