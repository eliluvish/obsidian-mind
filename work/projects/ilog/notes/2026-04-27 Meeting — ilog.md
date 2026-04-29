---
date: "2026-04-27"
description: "iLog stakeholder sync with Kele and Mirabella — feedback on accountability logbook, brief demo of registration onboarding redesign, ARC demo prep (3 days out)"
project: "ilog"
meeting_type: stakeholder-sync
attendees:
  - "Kele Piper"
  - "Mirabella Daguerre"
tags:
  - work-note
  - meeting
---

# iLog Stakeholder Sync — 2026-04-27

> [!info] Meeting goal
> **Primary: gather feedback** on the accountability logbook from Kele and Mirabella. Let them drive.
> **Secondary: brief demo** of [[Registration Onboarding Workflow Redesign]] — keep it short, hand back for feedback.
>
> ⚠️ Don't surface the ARC demo grapevine intel directly. See [[ARC Group iLog Demo]].

## Attendees

- [[Kele Piper]] — Chief Research Compliance Officer
- [[Mirabella Daguerre]] — Research Integrity Program Manager

## Since Last Meeting

_Auto-filled by `/meeting-prep`. Window: 2026-04-20 → 2026-04-27 (7 days)._

### Shipped

| # | Title | For |
|---|-------|-----|
| — | _No PRs merged in window._ Secondary container work shipped 2026-04-21 (just outside window) — see [[Secondary Container Expiration Rules]] and [[001-Secondary Container Disassociation from Primary]] | Kele / Mirabella |

### Closed Without Code

- _None._

### New Bugs / Issues

- _None opened in csb-ric/compliance in window._

### Open Items Waiting on Stakeholders

- **[[Kele Piper]]** — DEA follow-up on whether signatures must be Adobe/DocuSign or if text signatures are acceptable (see [[Destruction Workflow and DEA Form 41 Process]])
- **[[Mirabella Daguerre]]** — review/feedback on registration onboarding redesign mock-up (Eli still owes the detailed logic table — see [[Registration Onboarding Workflow Redesign]])

### Stale PRs

- [#717 Serve Bootstrap 5.3 via esbuild instead of Sprockets](https://github.com/csb-ric/compliance/pull/717) — opened 2026-04-22 (5 days). Eli's own; infra cleanup, not stakeholder-blocking.

### Unresolved Questions from Vault Notes

From [[ARC Group iLog Demo]] — items to surface (carefully):
- Confirmation the ARC demo is happening 2026-04-30
- Which features Kele plans to show
- Whether Eli should attend, support prep, or stay out of the way
- Whether a rehearsal/walkthrough is wanted before Thursday
- Any messaging constraints for the ARC audience

## Recently Shipped (broader context for the demo)

Both shipped 2026-04-21, candidates for ARC demo:
- [[Secondary Container Expiration Rules]] — SOP-based expiration rules
- [[001-Secondary Container Disassociation from Primary]] — Kele approved disassociation

## Discussion

> [!note] Transcript gap
> ~24 minutes of the wireframe walkthrough (0:42 → 24:31) were not captured. Recap below covers the back half: the registration logic discussion, beta testing plan, ARC demo postponement, and the chatbot tangent.

### Registration Onboarding — Schedule Logic Across Animal vs. Human

Walking through the wireframe table, Eli asked whether the schedule selection logic was specific to the human-research branch. **[[Kele Piper]] clarified that IND is the only field specific to human research — everything else (schedules, license types) is universal across animal and human registrations.** This collapses the gatekeeping: the human/animal split doesn't need to drive most of the form, only the IND question.

→ Reduces complexity in [[Registration Onboarding Workflow Redesign]]. Whole step removed from the animal branch.

### Beta Testing Plan

Kele laid out the rollout sequence:
1. Finish current build
2. Push to the **Controlled Substance Work Group** (members from Mass Eye and Ear, McLean, Brigham) as the next testing layer
3. Then pick a lab or two for live pilot

### Wireframes in Test Environment

Kele asked if the wireframes Eli demoed could be put into the test environment so the group can give feedback on order-of-steps, wording, and layout (e.g. the "submitted" step ordering she'd want changed). Eli said he'd try, but if it's painful (since it's a wireframe, not real implementation), he'll send screenshots + a video walkthrough as a fallback.

### ARC Demo — Postponed ✅

> [!success] Resolved without needing to ask
> **Kele postponed the ARC demo on her own.** Told the ARC group "we're not ready" and that they had a full agenda anyway. She'd rather demo the whole thing once the key pieces are in place than rush it with screenshots. **No deploy freeze pressure on 2026-04-30.** No need to surface the grapevine intel — it resolved itself.

### Chatbot Possibility for iLog

Eli mentioned the [[PCMS]] chatbot work in his toolset. Initially said he didn't see iLog application (not search-heavy), but Kele pushed back — DEA 41 form is where they get the most user questions, and a contextual help chatbot on specific pages (disposal, DEA 41, power of attorney) could deflect 80% of inquiries. Mirabella raised whether the chatbot could surface specific timestamped video segments from the quarterly discussions (chopped by topic).

**Eli confirmed:**
- Page-specific chatbot placement is doable
- Timestamped video links work if the video has a public link (YouTube timestamp, SharePoint link, etc.)
- Chatbot can link to videos but the video files still live wherever they're hosted

Kele plans to have **Irina** review past audit findings to identify the FAQ patterns worth building in.

### Multilingual Support — Deferred

Brief tangent on Mandarin/Cantonese support given the lab demographics. Kele parked it as "iLog 3.0" — not now, future problem. Eli flagged political sensitivity as something to be aware of when the time comes. Kele's view: match whatever languages the hospital already prints materials in.

## Decisions

- **ARC demo postponed** by Kele — no rushed demo on 2026-04-30 ([[ARC Group iLog Demo]] now resolved)
- **Schedule selection logic is universal** across animal and human registrations — only IND is human-specific. Simplifies [[Registration Onboarding Workflow Redesign]].
- **Beta testing path**: Controlled Substance Work Group → selected pilot lab(s)
- **Multilingual support deferred** to "iLog 3.0" — not on the current roadmap

## Action Items

- [ ] [[Eli Luvish|Eli]] — Go through all the tickets Kele/Mirabella added: #721 (destruction modal bug), #720 (DEA 41 text cut off), #719 (language: Adjustment → Bottle Variance), #718 (secondary container modal: add Substance Name field, rename "mixed with" → "formulary")
- [ ] [[Eli Luvish|Eli]] — Take screenshots and a video walkthrough of the wireframes; send to Kele + Mirabella
- [ ] [[Eli Luvish|Eli]] — Try to push the wireframes into the test environment so the group can give in-context feedback on wording / step order / layout
- [ ] [[Mirabella Daguerre]] — Think about "the tree" (decision logic for registration onboarding). Yes/no is fine; **keep it out of Excel** — text/if-then format works for programmatic processing
- [ ] [[Kele Piper]] — Have Irina review past audit findings to identify recurring questions that could become chatbot content (future, not blocking)

## Open Questions

- ~~Which specific tickets did Kele/Mirabella add?~~ Resolved 2026-04-29: #718, #719, #720, #721 (all opened 2026-04-27).
- Should videos for the chatbot live in the new SharePoint repository the team created? File-type constraints unclear (Mirabella asked about MP4).

## Wins

- 🎉 Kele: "It's looking amazing"
- ARC demo deadline pressure dissolved on its own
- Schedule logic clarification meaningfully simplifies the onboarding redesign

## Related

- [[iLog]]
- [[Kele Piper]]
- [[Mirabella Daguerre]]
- [[ARC Group iLog Demo]]
- [[Registration Onboarding Workflow Redesign]]
- [[Secondary Container Expiration Rules]]
- [[Authorized User Log Rules and Training Changes]]
- [[Destruction Workflow and DEA Form 41 Process]]
