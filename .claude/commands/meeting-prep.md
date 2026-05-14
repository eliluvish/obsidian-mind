---
description: "Prep for a recurring client meeting — gather shipped work, resolved items, and open issues since the last meeting in a client-facing four-bucket recap, then create a pre-filled meeting note."
---

# Meeting Prep

Prepare for a recurring client meeting by gathering activity since the last meeting window and creating a meeting note you can annotate live. The recap is structured to mirror what Eli typically sends the client ahead of the meeting.

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

### 6. Create the Meeting Note

- Path: `work/projects/<project>/notes/YYYY-MM-DD Meeting — <project>.md`
- Copy from `templates/Meeting Note.md`
- Fill placeholders: `{{date}}`, `{{project}}`, `{{meeting_name}}`, `{{date_range}}`, `{{name}}` for each attendee
- Pre-fill the `## Recap` subsections (Shipped this week / Resolved this week / Requires resolution) with the data from step 4
- Pre-fill `## Unresolved Questions from Vault Notes` with the data from step 5
- For **PCMS only**, insert a `### Waiting for RFCO review (work already in production for some time)` subsection between "Resolved this week" and "Requires resolution", linking to https://github.com/orgs/csb-ric/projects/7/views/1
- Leave `## Discussion`, `## Decisions`, and `## Action Items` empty for live annotation during the meeting
- Link to each attendee's person note and to the project README in `## Related`

### 7. Present the Briefing

Print a scannable summary to chat using the same four-bucket structure as the meeting note's `## Recap` section. This is the format Eli typically sends to the client:

- **Shipped this week** — merged PRs as a bulleted list, each linking to its PR and noting the issue it resolves when known
- **Resolved this week** — issues closed in the window (with or without a linked PR), noting who closed each
- **Waiting for RFCO review** (PCMS only) — link to the RFCO review board: https://github.com/orgs/csb-ric/projects/7/views/1
- **Requires resolution / finalization / clarification or closing** — open issues created before the window start, sorted by issue number, each as `[#N](url) — title`. This is the prunable list Eli edits before sending.

After the recap, surface internal context Eli may want before walking into the room (not part of the client-facing recap):

- **Unresolved Questions from Vault Notes** — from step 5, grouped by source note
- **Suggested Meeting Flow** — a numbered agenda Eli can skim into the meeting

End with the path to the created meeting note so Eli can open it and annotate live.

## Important

- **This creates a file.** Always include the created note path in your output.
- If `github_handle` is missing from any attendee's person note, **surface a warning** in the briefing — don't silently skip that person.
- Never modify existing notes during prep — only read and create the new meeting note.
- If a meeting note already exists for today, append ` (2)` to the filename rather than overwriting.
- The four-bucket recap is the source of truth for what gets sent to the client. The "Requires resolution" bucket will often be long — print it in full and let Eli prune before sending.
