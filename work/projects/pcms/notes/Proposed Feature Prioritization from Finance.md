---
date: "2026-04-05"
description: "Jessica Cho's email proposing initial PCMS feature priorities — needs feasibility assessment and answers to data questions"
project: "pcms"
tags:
  - work-note
---

# Proposed Feature Prioritization from Finance

## Context

[[Jessica Cho]] emailed [[Daniel Guettler]] and Eli on 2026-04-05 with a proposed list of initial projects to prioritize. Finance is presenting tomorrow (2026-04-06) and wants to be conscientious of feasibility and workload.

## Open Questions from Finance (Answered)

1. **How much of a lift will these projects be?** — [[Daniel Guettler]]: None seem like a major lift. Biggest challenge will be getting access to Workday APIs for the Insight Integration.
2. **Do the PET core and LMM Core have interfacing data into the system?** — PET core does manual data entry (there have been past conversations about automating it). LMM does manual data entry.

## Proposed Features

| Feature | Description |
|---------|-------------|
| Insight Integration | Integrate RCMS with Insight/Workday for expense data and budgeting |
| Enhanced Search | Improved search across services/equipment |
| Email Listserv | System-wide communication capability (all user accounts, by roles: admin, technician, etc.) |
| BCC General Inbox | BCC a general inbox for all outgoing emails from the system |
| Certify Refund is Not a Transfer | Popup certification for refunds — user, time, and date stamped |
| Individual Dana Farber Payment Source | Custom payment source for invoicing |
| Question/Problem Ticketing System | Centralized issue tracking |

## SOW Packaging — 2026-06-18

At the [[2026-06-18 Meeting — pcms|6/18 sync]], the conversation turned to how to package these requests as SOWs:

- Much of Finance's list is small (e.g. the email-address change is ~1 hour) — not worth a standalone SOW each.
- ~4 SOWs total ([[Daniel Guettler]]'s framing): one Finance already has + three more.
- **Decision**: RIC delivers a document with the **cost of every line item**, broken into sections; **Finance groups it themselves** into project SOWs to present to [[Allison Moriarty]] for budget approval (allocating to Finance vs. digital department budget). RIC owns the costing, not the grouping.
- Finance's rationale for grouping: a single larger project number budgets/approves more cleanly than many small line items.
- Eli to deliver the costed breakdown in a day or two.

## Related

- [[PCMS]]
- [[2026-06-18 Meeting — pcms]] — SOW packaging discussion + decision
- [[Allison Moriarty]] — budget approver Finance presents the grouped SOWs to
- [[001-Insight vs Workday Data Source Scoping]] — the Insight Integration line item was split 2026-04-09 into Insight (expenses/revenue) and Workday (optional internal funding)
- [[General Upload Template Service Request Sync]] — related behavior decisions for the upload template
- [[Jessica Cho]]
- [[Daniel Guettler]]
- [[Andy Chitty]]
