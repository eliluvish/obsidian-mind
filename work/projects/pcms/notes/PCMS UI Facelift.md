---
date: "2026-06-11"
description: "MGB-branded UI refresh for PCMS — focus groups flagged the dated look as a usability barrier; AI-generated mockups make a redesign cheap. Direction agreed; mockups-vs-agency-design path undecided."
project: pcms
github_issue:
status: active
tags:
  - work-note
---

# PCMS UI Facelift

## Context

PCMS's interface looks dated, and that came up as feedback **across all three stakeholder focus groups** (see [[Stakeholder Focus Groups for User Feedback]]). At the [[2026-06-11 Meeting — pcms|2026-06-11 weekly sync]], Eli demoed the [[RC FinOps|rcfinops]] Azure cost dashboard — MGB-branded (blue/teal/white), with a month switcher and faceted filters — as a concrete bar for what PCMS could look like. [[Jessica Cho]] agreed PCMS needs a refresh.

**Why now:** the old blocker for UI work is gone. Billing apps historically never get UI budget ("the billing just needs to work"), and a redesign used to mean hiring a design agency and hand-implementing their comps. AI now generates branded mockups in minutes, so the cost of producing and iterating on options is low. The focus-group feedback is the evidence that the dated UI is a real usability barrier, not a cosmetic nice-to-have.

## Notes

- **Open decision — two paths:**
  1. Mock up ~5 MGB-branded PCMS design options (~1–1.5 hrs of prompt/assembly work) and present at a future weekly sync for the group to choose from.
  2. Implement the agency design Jessica already has (she showed it in the meeting; "not super in love with it").
  - Path (1) is Eli's recommendation given how cheap mockups now are; awaiting Jessica's call before investing the time.
- The rcfinops dashboard is the reference aesthetic: MGB palette, familiar Microsoft-environment framing, minimal, faceted filtering, month switcher.
- **Likely supersedes the earlier design proposals.** This is not a parallel track — an AI-driven, whole-app MGB-branded refresh would most likely take the place of [[Core Browse UI Design]] (filterable card-grid browse UI) and the [[002-About Page as Auto-Populated Standardized Template|About-page template ADR]] rather than coexist with them. Those predate the cheap-mockup approach; fold their intent (browsable cores, standardized About content) into the facelift instead of building them separately.
- Scope is undefined: whole-app reskin vs. high-traffic pages first. To be narrowed once a direction is picked.

## Action Items

- [ ] [[Jessica Cho]] — decide: fresh AI mockups vs. implement the existing agency design
- [ ] Eli — if mockups: produce ~5 MGB-branded options and present at a future weekly sync
- [ ] Fold the intent of [[Core Browse UI Design]] and the About-page template into the facelift; if it supersedes them, mark those notes/ADR superseded
- [ ] Define scope once a direction is chosen (full reskin vs. priority pages)

## Related

- [[PCMS]]
- [[2026-06-11 Meeting — pcms]]
- [[Stakeholder Focus Groups for User Feedback]]
- [[Core Browse UI Design]]
- [[002-About Page as Auto-Populated Standardized Template]]
- [[RC FinOps]]
- [[Index]]
