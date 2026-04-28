---
date: "2026-04-27"
description: "PCMS equipment chatbot for the Ragon core — answer researcher questions about what's available, where, when, and whether they can use it"
project: pcms
status: active
tags:
  - work-note
---

# Ragon Equipment Chatbot

## Context

In-progress chatbot for [[PCMS]] aimed at the Ragon core. Goal: let researchers ask natural-language questions about equipment instead of clicking through PCMS or asking core staff. Listed as a medium-term goal in [[North Star]]. Same toolset Eli mentioned to [[Kele Piper]] in [[2026-04-27 Meeting — ilog]] — Kele expressed interest in eventually applying it to iLog (DEA 41 form help, FAQ deflection).

Current tool surface returns equipment basics: `name`, `description`, `training_required`, `pre_requisites`, `status`, address fields. Searches across `street_address`, `city`, `building`, `floor`, `room`.

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

## Cross-Project Implications

If the chatbot pattern works for Ragon, two projects already want to inherit it:
- **iLog** — DEA 41 form help, FAQ deflection (Kele 2026-04-27, see [[2026-04-27 Meeting — ilog]])
- **Possibly anything else with documentation-heavy user friction**

Worth designing the chatbot's tool layer with reuse in mind from the start.

## Open Questions

- Where does the chatbot UI live in PCMS? Per-page contextual widget, global modal, dedicated page?
- Where do `current_user` and authorization context flow through to tool calls?
- Does spec/capability structure need its own data modeling pass, or can it ride on the equipment/services tag taxonomy work?

## Related

- [[PCMS]]
- [[North Star]]
- [[Equipment and Services Tag Taxonomy]] — spec/tag taxonomy work that feeds into capabilities querying
- [[2026-04-27 Meeting — ilog]] — Kele's interest in chatbot for iLog
