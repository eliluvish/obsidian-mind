---
date: "2026-05-08"
description: "Proposed: replace free-text core About page with a standardized template auto-populated from structured services, equipment, location, and contacts. Source of truth = services/equipment."
project: pcms
status: proposed
tags:
  - decision
---

# Decision: About Page as Auto-Populated Standardized Template

## Context

Each core in PCMS has an **About page** — a free-text HTML region the core administrator edits to describe their core externally. The implementation is 15+ years old and is reused across so many surfaces inside RCMS that it cannot be modernized incrementally.

Two problems have compounded over time:

1. **It is not searchable.** The About page is free HTML — services, equipment, location, contacts mentioned there are invisible to RCMS search and to any future chatbot / browse interface. Admins regularly put service lists, equipment lists, location, and contact info there expecting it to surface in search. It does not.
2. **It absorbs effort that should go into structured data.** Because admins can put anything on the About page, many treat it as the canonical description of their core — and skip filling out the structured service and equipment records that the rest of the system actually uses. The About page becomes a crutch that suppresses the data quality the system needs.

Surfaced in three focus-group sessions ([[Stakeholder Focus Groups for User Feedback]]):

- **2026-04-30** — researchers want browse, filter, freshness signals; About-page text is opaque to all of those.
- **2026-05-08** — explicit operator-side debate. [[Meini Shin]]'s core director uses the About page for scientific marketing (graphs comparing circular RNA to mRNA). [[Lynelle Cortellini]] noted cores still showing "work temporarily paused due to COVID." [[Linda Nieman]] articulated the four questions a user needs answered to evaluate a core: *"Where's the core? What does it do? Can I use it? And who do I contact?"* — none of which the current About page answers reliably.
- Same session: [[Daniel Guettler]] confirmed the About page was never meant to list services. *"It became a dumping ground."*

## Triggering Issue

- [[Stakeholder Focus Groups for User Feedback]] — 2026-05-08 session, About page debate
- [[Core Browse UI Design]] — design depends on structured `building` / `institution` / modality / freshness fields, none of which live on the About page today

## Options Considered

1. **Status quo.** Free HTML About page, no enforcement, no search. Continues to absorb effort that should go to structured data; continues to leave cores unfindable to anyone not already in PCMS. Rejected.

2. **Searchable About page.** Index the HTML content and surface About-page text in search results. Rejected by Eli on the call: indexing a free-text HTML document is expensive at query time, and surfacing About-page text would *reward* the anti-pattern of dumping unstructured data there instead of filling in structured fields. *"If we use it for searching, then we are taking away from functionality the system already does, which is services and equipment."*

3. **Standardized auto-populated About page.** All cores share the same About-page template. Structured sections — service list, equipment list, location, contacts, freshness — are auto-rendered from the underlying records. Admins keep editorial control over a **narrative region** (marketing copy, images, scientific differentiation graphs like circular-RNA-vs-mRNA). Search indexes the structured fields. (**Chosen direction.**)

## Decision

**Option 3 — standardized auto-populated About page.**

- **Structured sections render from data**: service list, equipment list, location (`building` / `institution` / `street_address` / `city`), contacts, "last updated X months ago" from `content_updated_at`. These cannot be edited as free text on the About page; they come from the canonical records.
- **Narrative region**: admin-editable rich text + image upload for the core's differentiation, scientific positioning, etc. Not indexed for search, not the source of truth for any structured field. This preserves the legitimate marketing use case ([[Meini Shin]]'s circular RNA example).
- **Source of truth is the services/equipment records.** Search and browse never consult the About page for facts.
- **About page narrative does NOT need to be removed retroactively.** Existing content stays where it is; new cores get the template; existing cores migrate when convenient.

This decision is **proposed**, not yet accepted. It requires:

- Schema changes per [[Core Browse UI Design]] (location fields, `content_updated_at`, core-level modality join).
- A migration story for the long-tail of existing About-page content that contains both narrative *and* structured data (services, equipment, contacts) mixed together.
- Stakeholder confirmation from [[Andy Chitty]] and at least one operator who currently uses the About page heavily for marketing (Shin offered to introduce a GCTI director who is the strongest critic of current About-page editing UX — useful design-review voice).

## Consequences

- **Unlocks search and browse over core descriptions.** The [[Core Browse UI Design]] cards, the [[Ragon Equipment Chatbot]], and any future Insight/CTO touchpoint can rely on structured data being present and current.
- **Removes the crutch.** Once the structured sections are mandatory and visible, cores can't hide thin service/equipment data behind a rich About page.
- **Migration cost.** Long-tail About pages mix narrative and structured data. Extracting the structured parts (services, equipment, location) into the canonical records is per-core manual work — or an AI-assisted backfill, which Eli has already been doing informally for equipment.
- **Some admins will resist.** [[Meini Shin]] flagged that her director invested heavily in the current About page as marketing. The narrative region preserves that use case, but the editing UX needs to be meaningfully better than today's 15-year-old editor or the change feels like a downgrade.
- **Cleanup target**: 15-year-old About page implementation is reused across many surfaces, which has prevented incremental modernization. A standardized template gives a clean line to deprecate the old editor behind.

## Action Items

- [ ] Confirm with [[Andy Chitty]] and Meini's GCTI director that the narrative region adequately preserves the marketing use case
- [ ] Ship the [[Core Browse UI Design]] schema (location fields, modality join, `content_updated_at`) — prerequisite
- [ ] Design the migration path: per-core review of current About-page content, extract structured parts into canonical records
- [ ] Mock the standardized template before committing to implementation
- [ ] Decide enforcement: do existing About pages still render as-is until migrated, or is there a deadline?

## Related

- [[PCMS]]
- [[Stakeholder Focus Groups for User Feedback]] — the focus-group note where this surfaced (2026-04-30 + 2026-05-08)
- [[Core Browse UI Design]] — provides the structured location/modality/freshness fields this decision depends on
- [[Equipment and Services Tag Taxonomy]] — tag vocabulary that powers structured search
- [[Ragon Equipment Chatbot]] — downstream consumer of the structured data this unlocks
- [[Andy Chitty]]
- [[Daniel Guettler]]
