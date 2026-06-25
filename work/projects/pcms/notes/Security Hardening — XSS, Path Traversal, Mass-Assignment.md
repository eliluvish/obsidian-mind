---
date: "2026-06-24"
description: "PCMS security hardening pass (2026-06-22 → 2026-06-24): XSS + path-traversal fixes via dependency upgrades, plus an account_id mass-assignment guard on user-facing service requests."
project: "pcms"
github_issue:
status: completed
tags:
  - work-note
  - compliance
---

# Security Hardening — XSS, Path Traversal, Mass-Assignment

## Context

Two security fixes landed in the 2026-06-22 → 2026-06-24 window alongside the [[PCMS Rails 8.1 Upgrade]]. Captured here for the audit trail — PCMS runs in a research-hospital context, so privilege-escalation and data-integrity guards are worth a durable record.

## What Changed

- **`e8ae7373`** — patches **XSS and path-traversal** vulnerabilities via dependency upgrades. Bundled with the broader dependency bumps from the Rails 8.1 cutover.
- **`12aa2c57`** — stops **`account_id` mass-assignment** on user-facing service requests. Previously a user-supplied `account_id` could be set through the public SR path; this closes a **privilege-escalation / data-integrity** gap (a user could associate a request with an account that isn't theirs).

## Why It Matters

- The `account_id` guard is the more consequential of the two: it's an authorization boundary, not just a dependency hygiene bump. Any path that mass-assigns account ownership on user-facing forms should be audited for the same pattern.
- Both shipped to master in the same window and are pushed.

## Action Items

- [x] Patch XSS + path traversal (`e8ae7373`)
- [x] Block `account_id` mass-assignment on user-facing SRs (`12aa2c57`)
- [ ] Deploy to production (rides with the Rails 8.1 cutover)

## Related

- [[PCMS]]
- [[PCMS Rails 8.1 Upgrade]] — shipped in the same window
- [[Index]]
