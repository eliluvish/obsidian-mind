---
date: "2026-05-18"
description: "Calendar focus area for PCMS — cross-core SR scoping fix shipped (PR #2338); Daniel proposed a larger calendar refactor for usability including drag/drop events"
project: pcms
github_issue:
status: active
tags:
  - work-note
---

# Calendar Refactor and Drag-Drop Proposal

## Context

The PCMS calendar surfaced as a focus area after the `calendar_events` API regression from commit `60b8ae3` (cross-core service requests returning 404 — see [[Gotchas#PCMS calendar_events API now scoped by core (commit 60b8ae3)]]). That regression is now **fixed and deployed**.

Off the back of that work, [[Daniel Guettler]] asked whether Eli would be interested in **refactoring the calendar** to make it more usable — explicitly raising **drag/drop events** as a desired feature.

## Notes

- **PR [#2338](https://github.com/csb-ric/pcms/issues/2338)** — calendar work begun. (Scope: started with the cross-core scoping fix; broader refactor TBD.)
- Daniel's ask is currently a verbal proposal, not a scoped ticket. Drag/drop event editing is the headline feature; full scope (recurring events, resource views, multi-core visibility) not yet defined.
- Decision point: treat as incremental improvement on PR #2338, or scope a dedicated calendar-refactor initiative with its own backlog.

## Action Items
- [ ] Confirm exact scope of PR #2338 (fix-only vs. refactor start)
- [ ] Scope Daniel's refactor ask — what "more usable" means concretely beyond drag/drop
- [ ] Decide whether this warrants an ADR (UI architecture) and/or a tracking issue
- [ ] Raise at next PCMS Weekly Sync with [[Daniel Guettler]]

## Related
- [[PCMS]]
- [[Daniel Guettler]]
- [[Gotchas#PCMS calendar_events API now scoped by core (commit 60b8ae3)]]
- [[2026-05-14 Meeting — pcms]]
- [[Index]]
