---
date: "2026-04-28"
description: "Morning briefing — picking up PCMS work today. Handoff doc + capabilities table plan."
tags:
  - thinking
---

# PCMS Continuation — 2026-04-28

> [!important] First thing this morning
> Read the handoff before starting: `~/dev/pcms/.claude/handoffs/2026-04-27-2157-equipment-search-launch-prep.md`

## What You Said You'd Do Today

**Create a capabilities table for equipment in PCMS, then populate it core-by-core.**

This is the structured-spec data work. It's what unblocks chatbot feature #3 from [[Ragon Equipment Chatbot]] — capability-based queries like:

- "microscope with 100x objective"
- "MRI above 3 Tesla"
- "confocal with two-photon"

Right now those queries can only succeed if the relevant specs happen to land in the equipment `description` text. A structured capabilities model fixes that.

## Why It Matters

- **Direct blocker** for Ragon chatbot capability questions
- **Likely overlap** with [[Equipment and Services Tag Taxonomy]] — Andy + Daniel asked you to own the tag list. Worth deciding upfront whether tags and capabilities are the same model or two different things.
- Ties to North Star: PCMS chatbot for Ragon core (medium-term)

## Suggested Order of Operations

1. Read the handoff doc (above) — has yesterday's specific design direction
2. Decide: capabilities = tags, or capabilities ≠ tags? (data modeling question)
3. Sketch the table schema
4. Pick one core to populate first (probably Ragon, since it's the chatbot target)

## Related

- [[Ragon Equipment Chatbot]]
- [[Equipment and Services Tag Taxonomy]]
- [[PCMS]]
