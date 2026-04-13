---
date: "2026-04-05"
description: "RESOLVED — External fund PI field UX fixes shipped: unlock/edit, input format, missing PI backfill — GitHub #2273"
project: "pcms"
github_issue: 2273
status: completed
tags:
  - work-note
---

# External Fund PI Field Issues

## Status

**Completed 2026-04-10.**

## Context

End user Michael Waring reported to [[Yovani Edwards]] that the PI field on external funds has multiple UX problems. Filed as GitHub issue #2273.

## Problems Reported

1. **PI field locks after fund creation** — Michael Waring was set as PI on an Actus Bio fund by mistake (the actual PI should be Christine Palmer, cpalmer@actusbio.com). The field is now locked and can't be edited.
2. **Unclear PI input format** — Is it name and email? Just name? Should users type `Palmer, Christine (cpalmer@actusbio.com)`?
3. **PI Statement delivery** — Should the PI receive the PI Statement when invoices are sent out if entered as an external?
4. **Missing PI on existing fund** — Another external user (Nish Reddy) created a funding source with no PI, so the field is blank. Can that be fixed?
5. **Default fund side effect** — The incorrectly-assigned fund became Michael Waring's default fund when booking, which is disruptive.

## Open Questions

- Can the PI field be edited/unlocked after fund creation?
- If not, do users need to create a new fund? What's the workaround?
- What's the correct PI entry format for external funds?
- Can blank PI fields be backfilled?

## Related

- [[PCMS]]
- [[Yovani Edwards]]
