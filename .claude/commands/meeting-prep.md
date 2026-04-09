---
description: "Prep for a recurring client meeting — gather shipped work, open issues, stale PRs, and unresolved questions since the last meeting, then create a pre-filled meeting note."
---

# Meeting Prep

Prepare for a recurring client meeting by gathering activity since the last meeting window and creating a meeting note you can annotate live.

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
- Convert to ISO date (`YYYY-MM-DD`) for the `since` cutoff used in `gh` queries and git log

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

- **Merged PRs**: `gh pr list --repo <repo> --state merged --search "merged:>=<since>" --limit 30 --json number,title,mergedAt,author`
- **Closed issues**: `gh issue list --repo <repo> --state closed --search "closed:>=<since>" --limit 30 --json number,title,closedAt,author`
- **New open issues**: `gh issue list --repo <repo> --state open --search "created:>=<since>" --limit 30 --json number,title,createdAt,author,labels`
- **Open issues assigned to stakeholders**: for each `github_handle`, `gh issue list --repo <repo> --state open --assignee <handle> --json number,title,createdAt,assignees`
- **Stale PRs**: `gh pr list --repo <repo> --state open --json number,title,createdAt,updatedAt,author`, then filter client-side to PRs with `updatedAt` older than 14 days

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
- Pre-fill the `## Since Last Meeting` subsections with the data gathered in steps 4 and 5
- Leave `## Discussion`, `## Decisions`, and `## Action Items` empty for live annotation during the meeting
- Link to each attendee's person note and to the project README in `## Related`

### 7. Present the Briefing

Print a scannable summary to chat in the style of `/standup`:

- **Shipped This Week** — merged PRs table with "For" column attributing each to the reporter when known
- **Closed Without Code** — issues closed without a linked PR
- **New on the Plate** — newly opened issues, flag ones assigned to Eli
- **Waiting on Stakeholders** — open issues grouped by attendee
- **Stale PRs** — open PRs older than 14 days, sorted by age
- **Unresolved Questions** — from vault notes, grouped by source note
- **Suggested Meeting Flow** — a numbered agenda Eli can skim into the meeting

End with the path to the created meeting note so Eli can open it and annotate live.

## Important

- **This creates a file.** Always include the created note path in your output.
- If `github_handle` is missing from any attendee's person note, **surface a warning** in the briefing — don't silently skip that person.
- If no stakeholders have `github_handles` at all, still generate the note but omit the "Waiting on Stakeholders" section and note why.
- Never modify existing notes during prep — only read and create the new meeting note.
- If a meeting note already exists for today, append ` (2)` to the filename rather than overwriting.
