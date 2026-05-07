---
date: "2026-04-07"
description: "Core facility finance team running user focus groups for general PCMS feedback — two sessions held, developer search/discovery signals captured"
project: "pcms"
status: active
tags:
  - work-note
---

# Stakeholder Focus Groups for User Feedback

## Context

[[Andy Chitty]], [[Tera Morse]], and the finance team are holding focus groups with PCMS users to gather general feedback on the system. Eli plans to get a transcription of each session.

## Sessions

| Date | Time | Notes |
|------|------|-------|
| 2026-04-08 (Wed) | 11:00am | First session — strong positive reception, users "gung ho", lots of actionable feedback captured live. Not transcribed. |
| 2026-04-30 (Thu) | 9:30am | Second session — full transcript (0:00–1:33:38). Developer signals below. |

## Takeaways from 2026-04-08

- Turnout was good — "a lot of people want to talk at the focus group" ([[Jessica Cho]])
- Users see PCMS as helpful and are engaged with the feedback process
- Finance team already learned a lot from the first session
- Process note: **sessions are not being transcribed**; rely on live note-taking by Tera/Jessica/Yovani. If future sessions need a record, decide up front whether to record or assign a scribe.

## Developer Signals from 2026-04-30 (Search & Discovery)

> [!info] Full transcript — 1h 33m
> Complete session captured. Attendees: Allison Moriarty (SVP Research Operations), Roy Soberman (molecular imaging), Charles Jennings (Neurotechnology Studio), Jessica Gerber (CTRU), Hope Taft (Martinos), Laura Seidman (McLean), Yemi Talabi (MGB Office of Clinical Research), Gray Arabasz (Martinos ops), Kelly Dakin (Autism Research Core / Laurie Center), Domenic Minicucci (Martinos/CTRU IT), Daniel Guettler, Eli.

### The core problem: discoverability, not search quality

The dominant theme across every speaker is that users don't know cores exist at all — they can't search for something they've never heard of. Several described investigators writing grants or signing CTO agreements without budgeting for a core, then arriving with no money. Hope Taft (Martinos) described how getting a single question added to the Insight/CTO questionnaire "completely changed" their ability to find new users.

**Developer lens**: This reframes the problem. Faceted search and tag taxonomy help users who already know to look. But the higher-leverage intervention is **proactive surfacing at institutional touchpoints** — grant submission, CTO agreements, IRB feasibility, postdoc onboarding. A PCMS search page won't reach users who never navigate to it. The Insight integration idea keeps coming up from multiple people independently — it's load-bearing.

### Intent-based routing via Insight / CTO agreements

Gerber (CTRU) and Taft (Martinos) both proposed routing users to relevant cores based on what they're submitting in Insight: clinical research → CTRU, biomarker research → relevant core, AI research → AI cores. The user never has to know the core exists — the system surfaces it at the point of grant/contract creation.

**Developer lens**: This is out of scope for PCMS alone (requires Insight integration), but it points to what PCMS search would need to support it: cores need to be categorized by research type / modality in a machine-readable way. The tag taxonomy work (#2314) is a prerequisite. If we ever build an Insight touchpoint or a referral landing page, the taxonomy is what powers the matching.

### AI-assisted core matching / chatbot

Moriarty (SVP Research Operations) opened the session by naming this as an MGB strategic goal and laying out her blue-sky target: an AI chatbot where an investigator describes their project and the system routes them to the right cores. She specifically said: *"let's use AI here so that people can actually go in and have a chat bot essentially, say 'this is the type of project I'm doing, here's what I need,' and actually have AI generated content that directs them to the resources."* She acknowledged the backend data model is what needs solving.

Jennings ran a live experiment during the call — tried ChatGPT to find MGB cores offering specific equipment. It found the Magnus 3T scanner but missed the Minflux (Roy's, not yet listed). His takeaway: LLMs are already being used for this, but only return what's indexed. If our data is sparse, the chatbot fails.

Andy mentioned that NYU's microscopy core has an effective chatbot already — equipment-specific, lets you describe what you want and returns options and contacts.

Daniel mentioned during the session that Eli had already demoed something the day before using the data we have. *"I was like, wow, this is great."*

**Developer lens**: The chatbot is already in motion and addresses one specific user intent — "I know roughly what I need, help me find the right core." It does not solve browse (people who don't know what to search for), institutional touchpoints (people who never navigate to PCMS at all), or content staleness. Data quality — use case descriptions, service details, equipment specs, freshness — matters for the chatbot but also for any other interface. Treat it as one tool, not the umbrella solution.

### Cross-core awareness (core directors need to know each other)

Talabi raised that investigators come to one core asking about services that belong to another core, and core directors can't always refer them because they don't know what their peers offer. She explicitly asked for a notification mechanism when new services are added.

**Developer lens**: A "what's new at cores" feed or digest for core directors — this is a simpler version of the newsletter idea Jennings raised later in the session. Could be a scheduled email or an in-app notification. Would need a `published_at` or `updated_at` on services/cores to power it.

### Training / "what is a core" onboarding

Seidman (Laura) and Jennings (Charles) both pushed for a 15-minute onboarding overview — not how to use the system, but what a core even is and why you'd use one. Seidman suggested surfacing it at the top of the core listing page before any search. Jennings emphasized new postdocs and junior researchers as the target: they're planning projects and have no idea what's available.

**Developer lens**: Not a search feature per se, but informs the landing page design — an educational entry point before search may reduce the "zero results because I didn't know what to search" problem. Could be a callout/banner on the cores listing with a link to a short explainer.

### Tag-based discovery / topic filtering

Jennings (Charles G.) proposed a newsletter where users could subscribe by topic ("I want updates on microscopy, not human MRI"). The desire isn't really about newsletters — it's that users don't have a good way to find cores relevant to their research interests. They want to filter by topic/modality, not browse everything.

**Developer lens**: This is the same underlying problem the [[Equipment and Services Tag Taxonomy]] work addresses. The tag vocabulary we're building for equipment capabilities (modality, technique, application domain) is the right foundation. If search lets users filter by those same tags, the newsletter idea becomes less necessary — users can bookmark a search rather than subscribe to an email.

### Search analytics

Minicucci (Domenic) explicitly called out: *"analytics from core site users would be super helpful — we know what they're searching, where they click afterwards."* He framed this in the context of budget allocation — leadership wants data to justify investment.

**Developer lens**: Zero-result queries and click-through rates are the highest-signal analytics. A lightweight `SearchEvent` model (query, results_count, clicked_result_id) would cover both. Worth a GitHub issue even if it's backlog for now.

### Geographic grouping / location filtering

Gray Arabasz (Martinos ops) raised this directly at 1:22:34 — cluster cores by physical building, not just by institution. His example: Martinos Center, CTRU, and Roy's lab are all co-located at the Charlestown Navy Yard. An investigator planning a complex study could choose all three services without crossing campus. Andy confirmed this has come up in other conversations too, especially for flow cytometry where sample transport is a real constraint.

Jennings endorsed it: *"that's hugely important, not just for flow cytometry, but for the majority of core services — most people are not going to travel from Longwood to MGH and back."*

**Developer lens**: Need a `location` or `building` field on cores. Faceted filter by location. For the chatbot, location would be a relevant signal ("I'm at Brigham, what's closest?"). Gray is the source of this idea; Minicucci echoed it at the end.

### Search vs. browse (two distinct user modes)

Dakin (Kelly, Autism Research Core) drew a sharp distinction at 47:48: **search** is when you know what you need (I need flow cytometry); **browse** is serendipitous discovery — "I'm a scientist, I want to do cool research, what's out there?" Browse surfaces things you didn't know to search for. Seidman reinforced: browse should be visual (icons, cards), not text-heavy paragraphs.

Dakin's concrete example: their core offers a behavior specialist who helps patients tolerate blood draws. Nobody would search for this, but it's broadly applicable across clinical populations. It needs to be discoverable by browsing.

**Developer lens**: Two UX modes with different information architectures. Browse = category cards with icons and a one-line hook; Search = keyword input + facet filters. The current flat alphabetical list of 130 cores serves neither. Seidman literally said *"I don't even know what keyword to search for"* when looking at the list.

### Fuzzy / typo-tolerant search

Jennings ran a live test at 54:49 during the call. Equipment made by "RareCyte" (spelled C-Y-T-E) — searching "RareCite" (C-I-T-E) returned zero results. Current search is exact-match only. *"We're all accustomed to searching with Google or Bing and it corrects for error, you know, it's intelligent in a way that this search is not."*

**Developer lens**: ~~Not fixing the existing search~~ — this is moot. A chatbot/LLM-based replacement handles typos and natural language inherently. The signal here is that the bar for the new interface is Google-like tolerance, not exact-match. Keep in mind when evaluating the chatbot UX.

### Service-level data richness (not a search index problem)

Talabi raised this at 46:30 — search should surface individual services within a core, not just the core itself. If you search "phlebotomy" it should return the specific service, not require you to know which core offers it.

Daniel confirmed this on the call: *"we especially talked about services being included in the search, but we haven't implemented yet."*

**Developer lens**: Not fixing existing search, so this isn't an indexing problem — it's a **data modeling and content problem**. Services need to exist as first-class, well-described records regardless of what interface surfaces them (browse cards, chatbot, or a future search replacement). If a service is just a line item with no description, nothing can surface it meaningfully.

### "What problems do we solve" / use-case framing

Soberman at ~22:00 surfaced something important: *"about 70% of the time, people who come through our office don't know what the right tool to use for the right experiment is."* He and Chitty discussed the "10mm drill vs. 10mm hole" analogy — users come in with a preconceived tool in mind, but what they actually need is an outcome.

Roy's proposal: core pages should lead with "these are the research problems we solve" and examples of past work, not just a list of instruments and services. Users can match problems to their needs more easily than they can match specs.

**Developer lens**: This is a content modeling question. A `use_cases` or `example_projects` field on core pages (structured or rich text) that's indexed for search would let someone search "identify protein markers in blood" and surface the right core even if they don't know the instrument name. This also feeds the chatbot — use cases are exactly the kind of prose an LLM needs.

### Stale content / last-updated timestamps

Jennings (36:27) gave a concrete example: he discovered a piece of equipment at MGH by word of mouth, mentioned to the core that it wasn't listed on PCMS, and a month later it still wasn't there. His own core website auto-timestamps the "last updated" date on each page — if a page hasn't been updated in 3 years, that's visible. *"It helps with accountability as well as encouraging."* Andy confirmed he'd mentioned this at the intro meeting.

**Developer lens**: A `content_updated_at` timestamp on core pages, displayed publicly. Could trigger an email nudge to core contacts after N months of inactivity. Low lift, high accountability signal. Also directly relevant to chatbot data quality — stale content degrades results.

### Turnaround time on services

Soberman (1:21:00) proposed publishing expected turnaround time per service. Users have no sense of whether a process takes 15 minutes or two months. Daniel immediately flagged it as easy: *"That's actually a very easy improvement — allow cores to specify expected turnaround time on a service, and then also measure it when completed, and you could rank cores based on it."*

**Developer lens**: Add `expected_turnaround` to services (freeform text or structured range). Measure actual turnaround from order creation → completion timestamps. Daniel already called this easy — it's a good quick win.

### Zero-result / unmet demand capture

Dakin (1:24:24) made a sharp point: when the chatbot or search returns nothing, that's the most valuable signal. *"We want to know about that."* She wanted it captured organically — not a survey, but automatic logging of what people searched for and didn't find.

**Developer lens**: Log zero-result queries to the same `SearchEvent` model proposed above. A dashboard showing top zero-result queries tells you exactly what services to add or how to improve metadata. This also answers "what do users want that we don't offer?"

## Action Items

- [x] ~~Get transcription of 2026-04-08 focus group~~ (not transcribed)
- [ ] Confirm whether future sessions should be recorded or scribed
- [ ] Roll feedback themes into [[Proposed Feature Prioritization from Finance]] as they surface
- [ ] Open GitHub issue for search analytics (`SearchEvent` model — query, results_count, clicked_result_id; log zero-result queries separately)
- [ ] Check whether cores have `location`/`building` field — needed for geographic filtering
- [ ] Audit service content richness — services need descriptions good enough for a chatbot to match on (data quality problem, not a search index problem)
- [ ] Open GitHub issue for turnaround time on services — Daniel said it's easy, `expected_turnaround` field + measure actuals
- [ ] Explore `content_updated_at` timestamp on core pages + stale content nudge

## Related

- [[PCMS]]
- [[Andy Chitty]]
- [[Tera Morse]]
- [[Jessica Cho]]
- [[Yovani Edwards]]
- [[Daniel Guettler]]
- [[Core Browse UI Design]]
- [[Proposed Feature Prioritization from Finance]]
