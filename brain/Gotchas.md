---
description: "Things that have bitten before and will bite again — pitfalls, edge cases, and testing traps"
tags:
  - brain
---

# Gotchas

Things that have bitten before and will bite again.

## PCMS

### PCMS calendar_events API now scoped by core (commit 60b8ae3)

`Api::CalendarEventsController#create` (pcms commit `60b8ae3`, 2026-05-11) added `before_action :load_service_request` that calls `ServiceRequest.find(params[:service_request_id])`. Because `ServiceRequest` includes `CoreScopable` (`default_scope { where(core_lab_id: Thread.current[:current_core].id) }`), the find only resolves SRs in the **current core** (e.g. `bic` when routed via `/api/bic/...`). Cross-core SRs raise `RecordNotFound` → 404.

**Why**: Pre-commit, the controller never loaded the SR — it just assigned `current_core.id` to `core_lab_id` and used `params[:service_request_id]` as a write-only field. So the bic-scoped time-tracking API accepted any SR ID. After the commit, only SRs already inside the bic core resolve. This silently broke the `recording-time` skill for projects whose tracking SR lives in a different core (PCMS SR `16131` was the symptom).

**How to apply**:
- Fix in pcms: `ServiceRequest.unscoped.find(params[:service_request_id])` in `load_service_request`. Add a spec covering a cross-core SR ID.
- When reviewing diffs that add `.find` calls on `CoreScopable` models, ask: is this lookup expected to cross core boundaries? If yes, `.unscoped`.
- The RCMS calendar API will return a bare `{}` with status 404 when the SR isn't visible — not 422 — so a 404 from `/api/bic/calendar_events` POST is most likely an SR-scope mismatch, not a route/auth issue.

## Stakeholder Communication

### Kele Piper doesn't always loop Eli in on iLog events

[[Kele Piper]] has at least once planned an iLog-related public event (the ARC demo on 2026-04-30 — see [[ARC Group iLog Demo]]) without telling Eli directly. Eli heard about it through the grapevine.

**Why**: Information about demos, audits, and compliance-facing events can reach Eli late — late enough to cause prep scrambles if he finds out close to the date.

**How to apply**:
- Don't wait to be told about upcoming iLog events. Assume gaps in the communication channel.
- **Eli prefers to track quietly rather than confront.** When grapevine intel lands, file it, prepare accordingly, but don't surface the source with Kele or other stakeholders. No "I heard you're doing X" conversations.
- Periodically (e.g. at weekly review), ask open-ended questions that invite Kele to volunteer upcoming plans — "anything coming up for iLog?" — without revealing what you already know.
- On iLog work, default to "demo-ready" quality earlier than you otherwise would, because a surprise event may land at any time.
