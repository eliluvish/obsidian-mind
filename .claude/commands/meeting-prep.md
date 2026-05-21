---
description: "Prep for a recurring client meeting — translate shipped work into a non-technical, client-facing recap (new features, bug fixes, what needs resolution) with internal work summarized vaguely at the bottom, then create a pre-filled meeting note."
---

# Meeting Prep

Prepare for a recurring client meeting by gathering activity since the last meeting window and creating a meeting note you can annotate live. The recap is structured for a non-technical audience — PIs, lab managers, finance partners — and mirrors what Eli sends the client ahead of the meeting. Behind-the-scenes engineering work (refactors, test updates, internal cleanups) is acknowledged but kept high-level at the bottom.

## Usage

```
/meeting-prep <project> [timerange] [--with "Name1, Name2"]
```

Examples:
- `/meeting-prep pcms` — past 7 days, all stakeholders from the README
- `/meeting-prep ilog 2w` — past 14 days
- `/meeting-prep rcservices 1m` — past month
- `/meeting-prep pcms --with "Tera Morse, Jessica Cho"` — subset of attendees

## Workflow

### 1. Validate Project

Check `work/projects/<project>/` exists. If not, list available projects in `work/projects/` and stop.

### 2. Parse Timerange

- Default: `7d`
- Accepted: `Nd` (days), `Nw` (weeks), `Nm` (months) — e.g. `14d`, `2w`, `1m`
- Convert to ISO date (`YYYY-MM-DD`) for the `since` cutoff used in `gh` queries

### 3. Load Meeting Metadata

- Read `work/projects/<project>/README.md`
- Pull stakeholders from `## Stakeholders` section
- Pull `meetings:` from frontmatter if present — use `meetings[0].name` as the meeting title, otherwise default to `<Project> Weekly Sync`
- **Attendee schema** — the `attendees:` list under a meeting supports two forms:
  - Flat list: `- Jessica Cho`
  - Structured list with frequency: `- name: Jessica Cho` / `frequency: always|sometimes`
  - Always include `sometimes` attendees in the prep — they may show up. Mark them as "occasional" in the briefing so Eli knows not to block on them.
- If `--with "..."` is passed, filter attendees to that subset
- For each attendee, read `org/people/<Name>.md` and grab `github_handle` from frontmatter
- **Warn** in the output if any attendee is missing a `github_handle` — surface it so Eli can add it

### 4. Gather GitHub Activity (parallel)

Use the repo URL from the project README. Run these `gh` queries in parallel:

- **Shipped this week** (merged PRs): `gh pr list --repo <repo> --state merged --search "merged:>=<since>" --limit 30 --json number,title,mergedAt,author`
- **Resolved this week** (closed issues): `gh issue list --repo <repo> --state closed --search "closed:>=<since>" --limit 30 --json number,title,closedAt,author`
- **Requires resolution** (all open issues created before window start): `gh issue list --repo <repo> --state open --search "created:<<since>" --limit 50 --json number,title,createdAt,author,labels`

For shared-repo projects (e.g. lab_archives-hosted projects), scope issue queries with the project's GitHub label from the README.

### 5. Scan Vault for Unresolved Questions

- Grep `work/projects/<project>/notes/` for `## Open Questions` headings
- **Skip notes with `status: completed`** in frontmatter
- Extract the bullets under each `## Open Questions` heading verbatim
- Attribute each question to its source note as a wikilink

### 6. Classify Merged PRs

Before writing anything, sort the merged PRs from step 4 into three buckets:

- **New features** — users can now do something they couldn't before, or a workflow has materially changed. Example: cancel-and-refund for software services, tabbed project edit page, email preview modal.
- **Bug fixes & improvements** — a visible problem was resolved, or an existing feature got cleaner / faster / more correct. Example: "additional funds won't attach" fixed, expired-fund visibility, refund flow now covers pre-billed software.
- **Behind-the-scenes** — no user-visible change. Refactors, test updates, dependency bumps, controller rewrites, encoding fixes, scheduled-job cleanups, dead-code removal, internal investigations.

When in doubt about a borderline item, ask: *"Would the client notice this if I didn't tell them?"* If no → behind-the-scenes.

### 7. Create the Meeting Note

- Path: `work/projects/<project>/notes/YYYY-MM-DD Meeting — <project>.md`
- Copy from `templates/Meeting Note.md`
- Fill placeholders: `{{date}}`, `{{project}}`, `{{meeting_name}}`, `{{date_range}}`, `{{name}}` for each attendee
- Pre-fill the `## Recap` subsections using the buckets from step 6:
  - **New features** — bullets, plain language, see Tone Guide below
  - **Bug fixes & improvements** — bullets, plain language
  - **Resolved this week** — issues closed in the window, noting who closed each
  - **Requires resolution / finalization / clarification or closing** — open issues created before window start, sorted by issue number, each as `[#N](url) — title`
  - **Behind-the-scenes work** — one short paragraph (2–4 sentences), no issue numbers, no library/framework names. Group similar internal work together at a high level.
- Pre-fill `## Unresolved Questions from Vault Notes` with the data from step 5
- For **PCMS only**, insert a `### Waiting for RFCO review (work already in production for some time)` subsection between "Resolved this week" and "Requires resolution", linking to https://github.com/orgs/csb-ric/projects/7/views/1
- Leave `## Discussion`, `## Decisions`, and `## Action Items` empty for live annotation during the meeting
- Link to each attendee's person note and to the project README in `## Related`

### 8. Tone Guide (for New features / Bug fixes / Behind-the-scenes prose)

Write for a non-technical reader — a PI, lab manager, or finance partner. The recap is what Eli sends to the client.

**Do:**
- Lead with what the user can now do, or what problem they no longer have
- Use plain verbs: "added", "fixed", "now shows", "no longer breaks", "is faster", "is clearer"
- Put issue references at the end of the bullet in brackets: `… [#1899]` linked to the issue URL
- Group multiple small related improvements into one bullet when they share a theme (e.g. "Several improvements to the fund picker: …")
- Keep the **Behind-the-scenes** paragraph vague and reassuring — the client should know work happened, not what the work was

**Don't:**
- Use engineering vocabulary: Stimulus, controller, refactor, schema, migration, jQuery, encoding, collation, importer, snapshot, rake, validation, scrubbing, branch, rescue, jbuilder, turbo, partial
- Chain issue numbers inline mid-sentence (`… (#1885, #1902, #1916)`)
- Describe implementation ("rewrote the inline jQuery as a Stimulus controller") — describe outcome ("the billing page is more responsive")
- Use commit-style verbs ("feat:", "chore:", "refactor")
- List behind-the-scenes items with issue numbers — they're internal and should be summarized as one paragraph

**Example translations:**
| Engineering description | Client-facing |
|---|---|
| "Replaced new-account overlay with modal + select2 picker (#1885)" | "Adding a new fund mid-project is now a cleaner picker and no longer breaks the page [#1885]" |
| "Rewrote BillingController inline jQuery as Stimulus controller" | *(behind-the-scenes paragraph)* |
| "Converted free-text tables to utf8mb4_0900_ai_ci" | *(behind-the-scenes paragraph)* |
| "Tabbed nav for project edit page (#1934)" | "The project edit page is now organized into tabs, making fields easier to find [#1934]" |

### 9. Present the Briefing (Teams-paste-clean)

Print the same content as the meeting note's `## Recap` section to chat, but formatted so Eli can copy/paste straight into Microsoft Teams. Teams only renders a subset of markdown — the chat printout must follow these rules even though the saved meeting note keeps full Obsidian formatting:

**Teams-paste rules for the chat printout:**
- **No `###` / `##` / `#` headers.** Use a bold line instead: `**New features**` on its own line, blank line below, then bullets.
- **No wikilinks `[[Name]]`.** Strip them. For person attribution (e.g. who closed an issue), use the attendee's `github_handle` as `@handle` if available in their person note, otherwise plain text (`Daniel Guettler`). Never print `[[Daniel Guettler]]` to chat.
- **No markdown tables.** If you need a table, render as bullets instead.
- **No footnotes.**
- **Keep markdown links as `[text](url)`** — these paste correctly.
- **Nested bullets: max 1 level deep.** Teams flakes on deeper nesting.
- **Behind-the-scenes:** a single plain paragraph, no bullets needed, no issue numbers.

Same five subsections, same plain-language tone, same Tone Guide rules from step 8 — just the formatting above.

After the client-facing recap, print a separator (`---`) then surface internal context Eli may want before walking into the room (not part of what gets sent to the client). This part is for chat only; format however reads best:

- **Unresolved Questions from Vault Notes** — from step 5, grouped by source note (wikilinks OK here — internal only)
- **Suggested Meeting Flow** — a numbered agenda Eli can skim into the meeting

End with the path to the created meeting note so Eli can open it and annotate live.

## Important

- **This creates a file.** Always include the created note path in your output.
- If `github_handle` is missing from any attendee's person note, **surface a warning** in the briefing — don't silently skip that person.
- Never modify existing notes during prep — only read and create the new meeting note.
- If a meeting note already exists for today, append ` (2)` to the filename rather than overwriting.
- The recap is the source of truth for what gets sent to the client. The "Requires resolution" bucket will often be long — print it in full and let Eli prune before sending.
- **The client-facing tone is non-negotiable.** If you find yourself writing "Stimulus", "controller", "refactor", "encoding", or any other engineering term in the New features / Bug fixes sections, stop and rewrite the bullet around what the user experiences. If a PR has no user-facing effect, it belongs in the Behind-the-scenes paragraph — never in the top buckets.
- **Two outputs, two formats.** The saved meeting note (step 7) uses full Obsidian markdown — wikilinks, `###` headers, the whole vocabulary. The chat printout (step 9) is Teams-paste-clean — bold lines instead of headers, no wikilinks, no tables, no footnotes. Don't mix the two.
