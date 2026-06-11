---
date: "2026-06-11"
description: "PCMS Weekly Sync — recap and prep covering 2026-06-04 → 2026-06-11. Quiet shipping week (no merged PRs); focus on open backlog and stakeholder questions."
project: "pcms"
meeting_type: weekly
attendees:
  - "Jessica Cho"
  - "Tera Morse"
  - "Daniel Guettler"
  - "Yovani Edwards"
tags:
  - work-note
  - meeting
---

# PCMS Weekly Sync — 2026-06-11

## Attendees

- [[Jessica Cho]]
- [[Tera Morse]]
- [[Daniel Guettler]]
- [[Yovani Edwards]] (occasional)

## Recap

_Window: 2026-06-04 → 2026-06-11._

### New features

- _Nothing new shipped this week._

### Bug fixes & improvements

- _No production changes this week._

### Resolved this week

- _No issues closed this week._

### Waiting for RFCO review (work already in production for some time)

See the review board: https://github.com/orgs/csb-ric/projects/7/views/1

### Requires resolution / finalization / clarification or closing

- [#1845](https://github.com/csb-ric/pcms/issues/1845) — RIIFC: not respecting limit 1 per day per person equipment booking between 12pm–5pm
- [#1848](https://github.com/csb-ric/pcms/issues/1848) — Include link to filtered invoice page
- [#1849](https://github.com/csb-ric/pcms/issues/1849) — Kraft about page links do not open in a new page
- [#1851](https://github.com/csb-ric/pcms/issues/1851) — Add link to "Modified Invoice" email pointing to the filtered invoice page
- [#1856](https://github.com/csb-ric/pcms/issues/1856) — Downloading invoices doesn't respect filters
- [#1911](https://github.com/csb-ric/pcms/issues/1911) — Cores with auto approval, when regenerated after 15th, should remain approved
- [#1935](https://github.com/csb-ric/pcms/issues/1935) — Export Core with all settings, users and services
- [#1936](https://github.com/csb-ric/pcms/issues/1936) — Import Core with all settings, users and services
- [#1945](https://github.com/csb-ric/pcms/issues/1945) — Remove all whitespace from invoice number field when entering checks
- [#2043](https://github.com/csb-ric/pcms/issues/2043) — RSMG copier: before importing check if the file is open
- [#2049](https://github.com/csb-ric/pcms/issues/2049) — Upgrade `jsonapi-resources` (tech debt — internal)
- [#2080](https://github.com/csb-ric/pcms/issues/2080) — Invoice isn't flagged for regeneration _(ask: do we still need this?)_
- [#2086](https://github.com/csb-ric/pcms/issues/2086) — Error message formatting
- [#2164](https://github.com/csb-ric/pcms/issues/2164) — Restore data-protection functionality
- [#2169](https://github.com/csb-ric/pcms/issues/2169) — `_resend` or manually resending, option to skip report
- [#2170](https://github.com/csb-ric/pcms/issues/2170) — Double click adding fund still exists somewhere
- [#2220](https://github.com/csb-ric/pcms/issues/2220) — Updating setting results in `ActiveModel::ForbiddenAttributesError`
- [#2223](https://github.com/csb-ric/pcms/issues/2223) — Speeding up the External Payment logging Process — BPC
- [#2224](https://github.com/csb-ric/pcms/issues/2224) — P&L Reporting — PeopleSoft to Workday
- [#2225](https://github.com/csb-ric/pcms/issues/2225) — New General Tracking Upload Template
- [#2226](https://github.com/csb-ric/pcms/issues/2226) — Search Feature for Core Services & Equipment
- [#2263](https://github.com/csb-ric/pcms/issues/2263) — BPC Service Request blocked reopening for invoiced records
- [#2272](https://github.com/csb-ric/pcms/issues/2272) — Working Potential Enhancement List
- [#2292](https://github.com/csb-ric/pcms/issues/2292) — Reduce Schedule view for Services if Filtered
- [#2306](https://github.com/csb-ric/pcms/issues/2306) — Editable Document Page Core
- [#2317](https://github.com/csb-ric/pcms/issues/2317) — `/cm/checks/edit` is 247 queries per row (internal performance)
- [#2331](https://github.com/csb-ric/pcms/issues/2331) — Usage Analytics causing a crash
- [#2333](https://github.com/csb-ric/pcms/issues/2333) — Remove noise from unknown funds
- [#2336](https://github.com/csb-ric/pcms/issues/2336) — Allow splitting an invoice by service-to-grant, not just by percentage
- [#2340](https://github.com/csb-ric/pcms/issues/2340) — Replace string name link between PricingTier and assignments with a FK (internal)
- [#2344](https://github.com/csb-ric/pcms/issues/2344) — Ragon Flow Cytometry — Schedule Event editing early completion _(waiting on external resolution)_
- [#2345](https://github.com/csb-ric/pcms/issues/2345) — Equipment Filter on Schedule does not remain when switching calendar day
- [#2346](https://github.com/csb-ric/pcms/issues/2346) — Filter Services View to Selected Services and Equipment
- [#2347](https://github.com/csb-ric/pcms/issues/2347) — Remunc: when SR status changed from completed/cancelled to active, unarchive in RPR
- [#2353](https://github.com/csb-ric/pcms/issues/2353) — Bad grant list

### Behind-the-scenes work

_Internal improvements with no user-visible change. Kept high-level on purpose._

- No production changes landed in PCMS this week; engineering time went to other projects. PCMS work continues on the open items above.

## Unresolved Questions from Vault Notes

**From [[External Fund PI Field Issues]]**
- Can the PI field be edited/unlocked after fund creation?
- If not, do users need to create a new fund? What's the workaround?
- What's the correct PI entry format for external funds?
- Can blank PI fields be backfilled?

**From [[Equipment and Services Tag Taxonomy]]**
- Some equipment entries appear to actually be services (Proposal Assistance, Post-Award Management, Financial Analysis, Overall Project Management, Clinical Trial Invoicing — all "Consultant"). Are these mislabeled in the source, or do we need a tag/flag to distinguish service-type entries living in the equipment model?

**From [[PCMS Chatbot]]**
- Where does the chatbot UI live — per-page contextual widget, global modal, dedicated page?
- Where do `current_user` and authorization context flow through to tool calls?
- Does spec/capability structure need its own data-modeling pass, or can it ride on the equipment/services tag taxonomy work?
- Once the SOW is signed, which surface ships first — Ragon (original scope) or a broader equipment-search across cores?

**From [[General Upload Template Service Request Sync]]**
- What does the "change message" look like on the service request — a banner, an event-log entry, an email, or all three?
- Is retraining owned by Finance ([[Tera Morse]] / [[Jessica Cho]] / [[Yovani Edwards]]) or by Eli?
- New GitHub issue for this, or does it roll under [#2225](https://github.com/csb-ric/pcms/issues/2225)?

**From [[Proposed Feature Prioritization from Finance]]**
- PET / LMM cores — do they have interfacing data into the system, or stay manual entry? (PET has had past automation conversations.)

## Discussion

Short meeting (~9 min). Quiet shipping week, so the substance was a UI direction conversation plus two status updates.

### PCMS needs a UI facelift

Eli demoed the new [[RC FinOps|rcfinops]] Azure cloud-cost dashboard — MGB-branded (blue/teal/white), with a month switcher and faceted filters — built by asking AI for ~5 branding-based design options and picking the best. The point landed as a contrast with PCMS's dated look. [[Jessica Cho]] confirmed "outdated look" was feedback heard **across all three focus groups** (see [[Stakeholder Focus Groups for User Feedback]]), and agreed PCMS needs a refresh.

Eli's framing: UI redesign is cheap now — AI generates branded mockups in minutes, so the old blocker (hiring a design agency, then hand-implementing) is gone. Offered two paths: (a) mock up ~5 MGB-branded PCMS options (~1–1.5 hrs) and present at a future meeting, or (b) implement the agency design Jessica showed. Tracked in [[PCMS UI Facelift]]. Eli noted these billing apps historically never get UI budget because "the billing just needs to work" — but the focus groups are evidence the dated UI is a real usability barrier.

### Incoming focus-group tickets

[[Jessica Cho]] flagged Finance may file a few **small tickets** from focus-group feedback over the next couple of weeks rather than batching them — so expect those to appear.

### CachedTotalAuditor drift monitor — still clean

Eli reported the [[CachedTotalAuditor — Cache Drift Audit System|cache-total drift checker]] continues to run with **no drift detected** ("haven't heard a peep"). Not ready to flip the change yet — wants more evidence first. Will report drift status at each weekly sync going forward.

## Decisions

- **Agreed PCMS needs a UI refresh** (Eli + Jessica; backed by all-focus-group feedback). Direction set; exact path (fresh AI mockups vs. implement the agency design) not yet decided.
- **Hold on the cached-total change** until the drift monitor has accumulated more clean evidence. Status reviewed each weekly meeting.

## Action Items

- [ ] [[Jessica Cho]] / Finance — file the small focus-group tickets over the next couple of weeks
- [ ] Eli — continue monitoring cached-total drift; report status at each weekly sync
- [ ] Eli — (pending Jessica's call) mock up ~5 MGB-branded PCMS design options for a future meeting

## Related

- [[PCMS]]
- [[Stakeholder Focus Groups for User Feedback]]
- [[CachedTotalAuditor — Cache Drift Audit System]]
- [[RC FinOps]]
- [[Jessica Cho]]
- [[Tera Morse]]
- [[Daniel Guettler]]
- [[Yovani Edwards]]
- [[Index]]
