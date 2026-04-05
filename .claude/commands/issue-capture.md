---
description: "Scaffold a work note from a GitHub Issue URL with pre-filled frontmatter."
---

# Issue Capture

Create a vault work note from a GitHub issue. Fetches issue details via `gh` CLI and scaffolds a note with pre-filled frontmatter in the correct project folder.

## Usage

```
/issue-capture <github issue URL or owner/repo#number>
```

## Workflow

### 1. Fetch Issue Details

```bash
gh issue view <url> --json title,body,labels,assignees,number,url,repository
```

### 2. Determine Project

- Check if a project in `work/projects/` matches the repository name
- If no match, ask the user which project this belongs to
- If the project folder doesn't exist, offer to create it using the Project README template

### 3. Create Work Note

Create the note at `work/projects/<project>/notes/YYYY-MM-DD-<slug>.md` where:
- `YYYY-MM-DD` is today's date
- `<slug>` is a URL-safe version of the issue title (lowercase, hyphens, truncated to ~50 chars)

Frontmatter:
```yaml
---
date: "YYYY-MM-DD"
description: "<issue title — truncated to ~150 chars>"
project: <project name>
github_issue: "<full issue URL>"
status: active
tags:
  - work-note
---
```

Body:
```markdown
# <Issue Title>

## Context
<Issue body, cleaned up for readability. Convert GitHub markdown to Obsidian markdown where needed.>

## Notes

## Action Items
- [ ]

## Related
- [[<Project README>]]
```

### 4. Update Index

- Add a link to the new note in `work/Index.md` under the project's section

### 5. Cross-Link

- Add a link from the project README's Related section to this note (if the Related section exists)

## Important

- Not every GitHub issue needs a vault note. This is for issues that involve decisions, debugging discoveries, or architectural thinking worth preserving.
- If the issue body is very long, summarize it in the Context section rather than pasting everything.
- Preserve the GitHub issue URL in frontmatter — it's the link back to the source of truth.
