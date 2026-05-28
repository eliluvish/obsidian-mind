---
date: "2026-04-27"
description: "PCMS chatbot — researcher-facing natural-language tool for equipment/core discovery. Originally scoped to Ragon; broadened to a general PCMS-wide initiative. SOW being drafted."
project: pcms
status: active
tags:
  - work-note
---

# PCMS Chatbot

## Context

Ongoing PCMS initiative: a natural-language chatbot to let researchers ask questions about equipment, services, and cores instead of clicking through PCMS or asking core staff. Original framing was Ragon-specific (equipment chatbot for the Ragon core). It's now a general PCMS chatbot — Ragon is just the first surface, with the same toolset reusable across cores and adjacent projects (e.g. iLog FAQ deflection, see [[2026-04-27 Meeting — ilog]]).

Listed as a medium-term goal in [[North Star]]. Aligns with the strategic ask [[Allison Moriarty]] raised in the stakeholder focus group ([[Stakeholder Focus Groups for User Feedback#AI-assisted core matching / chatbot]]): an AI surface where investigators describe a project and the system routes them to the right cores.

## Status

- **SOW sent to client (2026-05-28)** — [[Daniel Guettler]] sent the chatbot SOW to [[Andy Chitty]], [[Jessica Cho]], [[Yovani Edwards]], and [[Tera Morse]]. Awaiting client review/acceptance. Once accepted, the SOW becomes the active scoping document and the feature backlog below gets reconciled against it.
- Branch `rubyllm-v2` in `pcms` has 67 commits ahead of master: streaming chunks over Turbo, autoscroll, `SearchEquipment` capability filtering, composer textarea clear on send, i18n dedup, Turbo form wiring. Active dev, not near merge.
- Current tool surface returns equipment basics — `name`, `description`, `training_required`, `pre_requisites`, `status`, address fields — and searches across `street_address`, `city`, `building`, `floor`, `room`.
- Groundwork PRs shipped: tag system (#2314), multi-modality (#2312), support fields on equipment (#2311) — see [[2026-04-30 Meeting — pcms]].

## Feature Backlog — Questions the Chatbot Should Answer

### 1. "Is it available next Tuesday at 2pm?" — Scheduling / availability

**The #1 thing a researcher wants after "does it exist."** PCMS has a calendar engine, but the current tool can't answer "what's free this week" or "when can I book the SPE confocal."

- Build a new `CheckEquipmentAvailability` tool, or extend the existing one
- Needs to interpret natural-language times ("next Tuesday at 2pm", "tomorrow afternoon")
- Should respect existing reservations and equipment-level scheduling rules

### 2. "Do I need training, and have I had it?" — User-specific gating

Current tool returns `training_required: true/false` and `pre_requisites`, but doesn't know who's asking. A researcher seeing "training required" can't tell if it means "you specifically can't book this" vs. "you're already cleared."

- Flow `current_user` context into the tool
- Return `user_can_book: true/false` alongside the raw boolean
- Massive UX win for almost no model effort

### 3. "What can it actually do?" — Capabilities / specs

Currently `name` + `description` (prose). A query like "microscope with 100x objective" or "MRI above 3 Tesla" only works if those specs happen to land in the description text.

- **This is a data question, not a tool question.** Specs need structured fields before the tool can usefully filter on them.
- Ties into [[Equipment and Services Tag Taxonomy]] — that taxonomy work could surface the structured spec fields needed here. Worth coordinating.

### 4. "Show me what's nearby" — Location-aware filtering

Tool searches across address fields but doesn't expose `building` / `floor` as filters. A researcher in Building B who wants "any confocal in this building" goes through free-text instead of a clean filter.

- Low-priority but cheap to add — just expose existing fields as optional params.

### 5. "Has anyone used this for [my kind of experiment]?" — Track record

Tracking records exist (billable activity), but the model can't see usage volume. Can't say "this is the most-used confocal in the building" or "this one hasn't been used in 6 months."

- Probably out of scope for the equipment tool itself
- But a strong signal for ranking — worth a separate "popularity / recency" tool or a ranking layer

### 6. "What's the alternative if X is busy/broken?" — Substitutes

`status` is returned (so the model knows if something is down), but there's no notion of "similar equipment." Model can probably infer this loosely from category/modality.

- Flag only — not a build target. Common follow-up question to keep in mind.

### 7. "I have a project, who should I talk to?" — Core matching

Moriarty's blue-sky ask from the focus group: investigator describes project → system routes to the right cores. Requires structured `use_cases` / `example_projects` content on core pages so the model has prose to match against. Depends on the [[002-About Page as Auto-Populated Standardized Template]] ADR landing.

## Cross-Project Implications

If the chatbot pattern works for the first PCMS surface, two projects already want to inherit it:
- **iLog** — DEA 41 form help, FAQ deflection ([[Kele Piper]], 2026-04-27, see [[2026-04-27 Meeting — ilog]])
- **Possibly anything else with documentation-heavy user friction**

Design the chatbot's tool layer with reuse in mind from the start.

## Talking Points for Weekly Sync

- [ ] **Equipment information is scattered across cores** — some cores have a PDF flyer as the primary source, others (e.g. CCP core) have more detail on their website than anywhere else in PCMS. The chatbot needs to account for this; tool responses will only be as good as what's in the system. Worth flagging to stakeholders so they understand the data quality dependency.
- [ ] **CCMPC core has no findable location** — Eli spent significant time trying to locate it and couldn't. Their equipment will return no useful location data to the chatbot.
- [ ] **Catalog categorization is inconsistent** — some trainings are entered as equipment, and some equipment should be services. The chatbot will surface these mismatches to users. Worth aligning on whether to fix the data before a wider rollout, or accept that the chatbot handles the ambiguity.

## Open Questions

- Where does the chatbot UI live in PCMS? Per-page contextual widget, global modal, dedicated page?
- Where do `current_user` and authorization context flow through to tool calls?
- Does spec/capability structure need its own data modeling pass, or can it ride on the equipment/services tag taxonomy work?
- Once the SOW is signed, which surface ships first — Ragon (the original scope) or a broader equipment-search across cores?

## Related

- [[PCMS]]
- [[North Star]]
- [[Equipment and Services Tag Taxonomy]] — spec/tag taxonomy work that feeds into capabilities querying
- [[002-About Page as Auto-Populated Standardized Template]] — structured About content unlocks core-matching queries (#7 above)
- [[Stakeholder Focus Groups for User Feedback]] — focus-group signal from Moriarty/Jennings/Andy on chatbot direction
- [[2026-04-27 Meeting — ilog]] — Kele's interest in chatbot for iLog
