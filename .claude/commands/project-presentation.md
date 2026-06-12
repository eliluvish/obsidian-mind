---
description: "Generate a minimal HTML status presentation for a project — stakeholder-ready summary of shipped work, in-progress items, decisions, and risks — saved to the project's presentations/ folder."
---

# Project Presentation

Generate a polished, self-contained HTML status report for a project, written for stakeholders and managers (PIs, lab managers, finance partners, IT leadership). Saved to `work/projects/<name>/presentations/` so reports accumulate over time and the latest can be shared directly — attached to an email, opened from a file share, or screen-shared in a meeting.

## Usage

```
/project-presentation <project> [timerange]
/project-presentation all
```

Examples:
- `/project-presentation pcms` — status presentation for PCMS, default 30-day window for "recent" work
- `/project-presentation ilog 2w` — recent window of 14 days
- `/project-presentation all` — generate one presentation per active project in `work/projects/`

## Workflow

### 1. Validate Project

Check `work/projects/<project>/` exists. If not, list available projects and stop. For `all`, run steps 2–6 for each project folder under `work/projects/` (skip `work/archive/`).

### 2. Gather Content

- Timerange: default `30d`; accepts `Nd`/`Nw`/`Nm` like `/meeting-prep`. "Recent" means a note's frontmatter `date` falls inside the window.
- Read `work/projects/<project>/README.md` — overview, stack, status, stakeholders, links
- List notes in `work/projects/<project>/notes/` sorted by frontmatter date; read the ones inside the window (minimum the latest 5). **Also read any note the README flags as active or current regardless of date** — old-but-active work is often the context behind open decisions.
- List ADRs in `work/projects/<project>/decisions/` — note any with `status: proposed` (decisions awaiting stakeholders). ADRs accepted inside the window can appear under highlights; older accepted ones are history, leave them out.
- If the README has a repo URL and `gh` is available, pull merged PRs in the window for "recently shipped": `gh pr list --repo <repo> --state merged --search "merged:>=<since>" --limit 30 --json number,title,mergedAt`. If `gh` fails or there's no repo, rely on vault notes alone — don't block.

### 3. Classify for a Stakeholder Audience

Sort everything into the presentation sections:

- **Highlights / Recently shipped** — user-visible features and fixes from the window
- **In progress** — active work notes, what's currently being built and why it matters
- **Decisions needed** — proposed ADRs and open questions that need stakeholder input, each phrased as the question a manager would answer
- **Risks & blockers** — anything stalled, waiting on access/approvals, or flagged stale
- **What's next** — near-term plan, drawn from README status and recent notes

**Follow the Tone Guide in `/meeting-prep` (step 8) — and apply its spirit to every section**, including Decisions, Risks, and What's next (which meeting-prep doesn't cover). Plain language, lead with outcomes, no engineering vocabulary (refactor, controller, migration, Stimulus, schema, ADR…). Plain business terms are fine: "statement of work", "the decision record", "vendor quote". Internal-only work gets one reassuring sentence, not a list. The test for every line: *would a PI or finance manager understand and care?*

### 4. Audience Safety — Non-Negotiable

This file may leave the vault. Before writing:

- **No PHI, ever.** No patient or subject identifiers, even in examples.
- **No internal-only vault content** — nothing from `org/people/` notes, `brain/Gotchas.md`, or anything about individuals beyond name + role as project stakeholders.
- **No credentials, server names, or internal URLs.** GitHub issue/repo links are fine when the stakeholders demonstrably use that repo (they file or comment on issues there) — that's the normal case for project repos. Otherwise strip the links and keep plain `[#N]` references.
- When unsure whether a detail is shareable, leave it out.

### 5. Generate the HTML

- Path: `work/projects/<project>/presentations/YYYY-MM-DD-status.html` (create the `presentations/` folder if missing). If a file already exists for today, overwrite it — same-day regeneration is a revision, not a new report.
- **Fully self-contained**: inline CSS, no external fonts, scripts, or CDN requests. It must render offline and inside the hospital network. No JavaScript needed.

**Design spec — minimal but pleasant:**

- Light theme: warm off-white page (`#faf9f6`-ish), near-black text, one muted accent color per project (e.g. a desaturated blue, green, or rust). **Before picking, check existing files in that project's `presentations/` folder and reuse their accent color** — reports for the same project should look like a series.
- System font stack: `-apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`; generous line-height (1.6+)
- Single centered column, max-width ~780px, generous whitespace between sections
- **Header**: project display name, a small status badge mapped from the README's `status:` frontmatter (`active` → "Active", `completed` → "Completed", `archived` → "Archived"), report date, "Prepared by Eli Luvish — Research Computing"
- **At a glance**: 2–4 sentence executive summary right under the header — if a manager reads nothing else, this is enough
- **Sections** in step-3 order, each with a small uppercase letter-spaced label in the accent color and a thin rule
- Bullets for shipped/in-progress items; decisions and risks may use simple bordered cards or a two-column definition layout — whatever reads cleanest, no heavy boxes or shadows
- Optional **milestones** strip if the project has real dates (simple labeled dots on a line — pure CSS)
- **Footer**: the names + roles from the README's `## Stakeholders` section (other people may appear in body text by name, but the footer is just the README list), the project repo link per the step-4 rule, and "Questions? eluvish@mgb.org"
- `@media print` styles so it prints to a clean one-to-two page PDF (no backgrounds bleeding, sensible margins)
- No animations, no dark theme, no slide deck — this is a document, not a pitch

### 6. Wrap Up

- Print the file path(s) created
- Give a 2–3 line summary of what the presentation says (so Eli can sanity-check without opening it)
- Offer to open it: `open <path>`

## Important

- **This creates files.** Always print the created path(s).
- Read-only on all vault notes — only the new HTML file is written. Don't update indexes; presentations are artifacts, not notes (no frontmatter, no wikilinks — the `.md` note rules don't apply).
- Old presentations are history — never delete or rewrite previous dates' files.
- **The audience-safety rules in step 4 override completeness.** A thinner report is always better than a leaked detail.
- If the project has almost no recent activity, say so honestly in "At a glance" ("steady state, no major changes this period") rather than padding the report.
