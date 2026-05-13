---
date: "2026-04-07"
description: "Three stakeholder focus groups on PCMS — researcher-user signals (discoverability, browse, chatbot) + operator-side signals (external front ends, About page architecture)"
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
| 2026-05-08 (Fri) | 2:30pm | Third / final session — full transcript (1h 17m). Core-operator perspective. Developer signals below. |

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

## Developer Signals from 2026-05-08 (Workflow & Architecture)

> [!info] Full transcript — 1h 17m
> Final session. Audience shift: this group was **core operators**, not researcher-users. Attendees: [[Andy Chitty]] (chair), [[Tera Morse]] (co-moderator), [[Yovani Edwards]] (co-moderator), Teresa "Terry" Bowman (specialized histopathology core, BWH, 18yr), Linda Nieman (Tumor Cartography Core, MGH→Jackson), Domenic Minicucci (Martinos Center / CTRU IT), David Drew (Dept of Medicine core, MGH — *not yet in RCMS*), Lynelle Cortellini (TCRC admin director; Harvard Catalyst grant POC), Meini "Amy" Shin (Exec Director, Personalized Medicine & GCTI — manages biobank, LMM, RNA therapeutic core, gene editing core), Jessica Gerber (Ops Director, CTRU), [[Daniel Guettler]], Eli.

### The dominant new theme: cores have built their own front ends

Multiple cores have stood up external intake/scheduling systems outside RCMS and only feed RCMS at billing time. The pattern is consistent across at least three cores:

- **CTRU / Martinos** (Gerber + Minicucci): users fill a REDCap form to scope a project, then book individual events (nurse practitioner, blood draw, room) in **EMS** — the MGB-wide scheduling system. Trevor manually re-enters the resulting orders into RCMS. Gerber: *"we don't direct our users there right now."*
- **GCTI / biobank / LMM cores** (Shin): users never touch RCMS. The core handles order entry internally; RCMS is the billing back end. *"Once you're in, if it's MGB, it's all automatic journal and everything, which is like amazing."*
- **Dept of Medicine core** (Drew): not yet on RCMS but plans to be. Uses REDCap as a triage form before consult. Concerned about activation energy if users have to create RCMS accounts: *"the perceived activation energy to use the core may be higher."*

**Why they did this**:
- Gerber: RCMS "screams outdated" and ordering complex clinical services isn't like ordering a pizza. They also want **gatekeeping** — *"we don't want people just going into the core and signing up for an account and all of a sudden ordering like neuropsychological testing."*
- Drew: REDCap is familiar to investigators and nimble for the core to modify. *"It's easy enough for us and nimble enough for us to make changes."*
- Cortellini: their own intake "is super complicated, it's a whole other thing developed that, ironically, Daniel is now managing as well."

Eli's response on the call: *"I'm not thrilled that our functionality is insufficient that you've built another front end."* But also opened the door: *"if EMS can expose an API to us, we can integrate with that."* Past attempt with "Misha" stalled (Gerber/Minicucci recall it was a phone-number-digits issue).

Daniel reinforced that RCMS already supports per-service intake surveys on the service request form, and admins can edit submitted requests before activating them — addressing the gatekeeping concern.

**Developer lens**: Three architectural options surface:

1. **Build the workflows inside RCMS** — service-request intake surveys + admin review queues (Daniel's framing). Already supported but underused; opportunity to document and evangelize.
2. **Integrate with external front ends** — REDCap data pull (already supported but Eli flagged the data-shape risk: REDCap is unstructured), EMS API (worth resurrecting the Misha thread).
3. **Cortellini's pragmatic reframing** — *"should the focus then be more of building some sort of API to just have a more streamlined transfer of that data from everyone else's front door into the system?"* Treat RCMS as a billing/data sink; let cores keep their bespoke front ends. Lower scope, accepts current reality.

This is significant enough to be its own decision — see Open Questions for ADR promotion.

### About page vs services page — architectural debate (extensive)

Triggered by Shin reporting that her core director (GCTI / circular RNA) finds the About page editor painful but considers it critical for marketing the core's differentiation. Eli pushed back hard on the About page as architecture:

- *"The landing page and its existence is the biggest problem in RCMS because it has no structured data. You can put whatever you want and then it's completely not searchable."*
- *"The About page is up to the administrator to keep current. Whereas the services page is what people actually order. The source of truth is the services page."*
- *"The About page was a crutch that prevented people from using good descriptions for their services and equipment."*
- *"We're talking about 15-year-old technology because it's used in so many different ways in our CMS that we can't update it."*

Eli's proposal (already pitched to Andy & team): **standardized About pages auto-populated from underlying structured data** (services, equipment, location, contacts). Cores can still upload an image and a short narrative, but service/equipment lists, location, contacts come from the structured fields automatically.

Shin's concern: her director uses the About page for scientific marketing — graphs comparing circular RNA vs mRNA, demonstrating the core's differentiation. *"He believe all the scientists understand that... that's like how we can attract our client to use our service."*

Eli's concession: *"I'm not saying we're going to take it away. You can still put an image up. You can still put whatever text you want up. You just have to remember that you can make that page as nice as possible, and if no one finds it, it's meaningless."*

Daniel reinforced from history: *"The About page was never meant to list your services. People just ended up doing it because it was possible... It's really meant for description, not meant for okay, this is the list of services that I'm providing."*

**Developer lens**: This is the same data-quality theme from 2026-04-30 surfaced through a different lens. The About page as it exists today is the **anti-pattern** that absorbs effort that should be going into structured service/equipment metadata. The proposed direction — auto-populated standardized template — is a clear architectural decision worth promoting to an ADR. Crucially: it does *not* remove free narrative/imagery; it changes the boundary between "structured data the system uses" and "narrative the admin curates."

### External discoverability — the Harvard Catalyst use case

Cortellini opened with a problem we hadn't heard framed this way before: she's been trying for **two years** to give Harvard Catalyst a comprehensive, accurate list of MGB cores for their resource compendium. Cores not on RCMS are invisible; cores on RCMS have inconsistent external presentation; URLs go stale; one core's page still had a "work temporarily paused due to COVID" notice (Andy confirmed he'd seen it too). *"Our marketing of the cores is basically a detriment just in terms of how many more people we could get using them if it was easier to figure out what we had."*

**Developer lens**: Reinforces the discoverability theme from 2026-04-30 but extends it to **outside MGB entirely**. The audience isn't just MGB investigators — it's Harvard-wide researchers using Catalyst. The standardized About page proposal addresses this directly: consistent external-facing presentation, machine-readable structured fields, ability to flag stale content.

### The required-fields-per-core ask (reinforcement)

Nieman, when asked what works well: scheduler/calendar/auto-bill flow is great *for equipment cores after user training* — minimal friction once users are in. But for the *finding* step she echoed Cortellini: *"having a form that all core directors fill out that have things like the key services that are offered, who are their service communities, where they're located."* Her four user questions: **"Where's the core? What does it do? Can I use it? And who do I contact?"**

**Developer lens**: This is exactly the shape of the [[Core Browse UI Design]] proposal — `building` / `institution` / `street_address` / `city` on the core model, modality tags, contacts. Multiple sessions now converge on the same fields. Strengthens the case for shipping browse + the supporting schema changes.

### Service catalog structure — packages, billable_name, budget tie-in

Gerber and Cortellini both thought menu items had to match the budget exactly. Daniel/Eli clarified: the **billable_name** must match the budget (for audit/compliance), but the **display name** in RCMS is flexible. Shin had built a workflow assuming the catalog had to be at the lowest-billable level — leading CTRU to list 5 sub-services where it could have been one "CTRU Resources Fee" package.

Daniel surfaced **service packages** — a service can appear in multiple packages, packages can mix and match. Shin didn't know this existed. Tera confirmed: as long as the sub-service rates tie to the approved budget, audit-compliant.

**Developer lens**: A real **discoverability-of-features** problem inside RCMS itself. Multiple admins have built workarounds because they didn't know existing functionality. Gerber explicitly asked: *"I think there's like opportunity to learn the functionality more, maybe even have some sort of like crash course in what it does offer."* Worth: short feature documentation, admin onboarding, or an in-app callout for underused features. Likely the cheapest single improvement on the table.

### Bill splitting — feature gap

Cortellini surfaced a concrete unsupported case: a research visit has 5 services billed together. Current behavior: you can split the invoice by **percentage** across grants, but you can't allocate **specific services** to **specific grants** (e.g., "the extra blood draw goes on grant B, the other four services go on grant A"). They do manual math on the side as a workaround.

**Developer lens**: This is a real feature gap, not a workflow misunderstanding. The data model already has per-service line items on invoices; the splitting UI just doesn't expose per-line allocation. Worth a GitHub issue. Adjacent users: Shin confirmed her core hits the same workaround.

### Invoice reply-to routing — operational pain + unsolved mystery

Cortellini in the admin-group session (Tuesday) raised that Tera fields a huge volume of invoice reply emails she has to forward to the right core. Suggestion: when an invoice email goes out, include the **core's billing contact** as a CC/Reply-To so users' replies land directly at the core.

But Gerber and Shin both report that **their** cores already receive replies directly — and neither knows how that was configured. Tera's hypothesis: the billing contact is BCC'd on send; if the user hits "Reply All" it goes to everyone, if they hit "Reply" it goes only to the sender (Tera).

**Developer lens**: Worth verifying the actual SMTP/header behavior. If billing contact is BCC'd, a quick fix is to put them in `Reply-To` so plain `Reply` lands at the core, not Tera. Low-effort if true.

### Branding / "outdated" feel

Gerber: *"the first word that comes to mind is just outdated when I look at it."* *"It does not scream to me 'we do cutting edge research here.' I think it is a total disservice to the cutting edge research that we're actually doing."* She'd welcome a quarterly mandatory update cadence and help with searchable keywords.

Shin reinforced: *"It would be amazing if our website also can help us with basically market all of our service."*

**Developer lens**: The look-and-feel point matters but is downstream of structural decisions (standardized About template, browse UI, data freshness display). Once those land, the visual refresh has real surfaces to apply to. Don't lead with skinning; lead with the structured templates.

### Data quality = search quality (Eli reinforcing)

Eli returned to his consistent position: *"We can only do as good as the data you give us. And it has to be current."* Mentioned the new **capabilities** and **modalities** tags on equipment ([[Equipment and Services Tag Taxonomy]], [pcms#2314](https://github.com/csb-ric/pcms/pull/2314)) and plans to extend the same to services. Also flagged he's been using AI to fill equipment descriptions himself for cores that haven't.

Stated the enforcement model bluntly: *"I'm going to be the bad guy and say that the cores that don't provide it, they're not going to appear in the search."*

Andy proposed templates / outreach to cores in a uniform way. Eli's counter: *"It's in the system, right? It's tagging. So everything is done in the system. I don't want to send you all an Excel file to fill out."*

**Developer lens**: Consistent with prior sessions. The enforcement model ("if you don't tag, you don't surface") is the right stance, but needs to be paired with **(a)** clear admin UX for adding tags, **(b)** outreach explaining the consequence, and **(c)** ideally a visible "completeness score" so admins can see what they're missing before users notice it. The AI-assisted backfill Eli mentioned could become a tool exposed to admins ("suggest tags for this equipment based on its description") rather than something only Eli runs.

## Action Items

- [x] ~~Get transcription of 2026-04-08 focus group~~ (not transcribed)
- [ ] Confirm whether future sessions should be recorded or scribed
- [ ] Roll feedback themes into [[Proposed Feature Prioritization from Finance]] as they surface
- [ ] Open GitHub issue for search analytics (`SearchEvent` model — query, results_count, clicked_result_id; log zero-result queries separately)
- [ ] Check whether cores have `location`/`building` field — needed for geographic filtering
- [ ] Audit service content richness — services need descriptions good enough for a chatbot to match on (data quality problem, not a search index problem)
- [ ] Open GitHub issue for turnaround time on services — Daniel said it's easy, `expected_turnaround` field + measure actuals
- [ ] Explore `content_updated_at` timestamp on core pages + stale content nudge

### From 2026-05-08

- [x] ~~Promote About-page architectural decision to ADR~~ → [[002-About Page as Auto-Populated Standardized Template]] (proposed, 2026-05-08)
- [ ] **Promote to ADR or work note**: External front-end integration pattern (REDCap intake, EMS scheduling) — when to integrate vs. when to build inside RCMS. Resurrect Misha-era EMS API thread.
- [x] ~~Open GitHub issue: bill splitting by specific service → specific grant~~ → [pcms#2336](https://github.com/csb-ric/pcms/issues/2336)
- [ ] Investigate invoice reply-to routing — why does CTRU/GCTI receive user replies directly while Tera fields most? Likely Reply-All vs Reply-To behavior; consider setting `Reply-To: <billing contact>` so plain Reply lands at the core.
- [ ] Document underused features (service packages, quote tool, intake surveys on service requests) — multiple admins built workarounds because they didn't know these existed. Form: short "what RCMS already does" doc + admin onboarding callouts.
- [ ] Roll out capabilities/modalities tags from equipment to services (already planned per [pcms#2314](https://github.com/csb-ric/pcms/pull/2314)).
- [ ] Consider an admin-facing "AI suggest tags" tool — currently Eli runs this manually for cores that haven't tagged.
- [ ] [[Andy Chitty]] / Eli: Meini offered to swap her seat for a GCTI/RTC director who has strong opinions on About page UX — willing to introduce him to Eli for a direct conversation.

## Related

- [[PCMS]]
- [[Andy Chitty]]
- [[Tera Morse]]
- [[Jessica Cho]]
- [[Yovani Edwards]]
- [[Daniel Guettler]]
- [[Core Browse UI Design]]
- [[Proposed Feature Prioritization from Finance]]
