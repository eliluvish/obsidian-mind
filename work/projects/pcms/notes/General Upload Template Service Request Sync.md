---
date: "2026-04-09"
description: "Planned behavior for the general upload template — uploads will update service requests with a change message; split funding uses percentage format; existing users need retraining"
project: pcms
status: backburner
tags:
  - work-note
---

# General Upload Template Service Request Sync

## Context

Working session on 2026-04-09 with [[Jessica Cho]] and [[Daniel Guettler]]. Jessica confirmed that the Finance team (including [[Yovani Edwards]]) met and decided on the behavior they want when the new general upload template lands.

## Planned Behavior

- **Uploads update the service request.** When the general upload is processed, the service request will be updated to reflect the new values.
- **Change message on the service request.** The service request should display some form of message indicating that a change was made via upload, so users can see the history and understand why their SR looks different.
- **Split funding via percentage.** The general upload template will support split funding using a percentage format (e.g. `50%`, `30%`) in whatever column represents the split.
- **User retraining required.** Users who currently use upload need to be informed that uploads will now mutate their service requests. Jessica flagged retraining (or at least a broadcast) as a prerequisite before turning this on.

## Open Questions

- What does the "change message" look like on the service request — a banner, an event log entry, an email notification, or all three?
- Is the retraining owned by Finance ([[Tera Morse]] / [[Jessica Cho]] / [[Yovani Edwards]]) or by Eli?
- Is there a new GitHub issue for this, or does it roll under #2225 "New General Tracking Upload Template"?

## Related

- [[PCMS]]
- [[2026-04-09 Meeting — pcms]] — planning discussion happened here
- [[Proposed Feature Prioritization from Finance]]
- [[Jessica Cho]]
- [[Daniel Guettler]]
- [[Yovani Edwards]]
