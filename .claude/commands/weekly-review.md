---
description: "Cross-project review: what shipped, what's stuck, pending decisions. Update Index.md."
---

# Weekly Review

Lighter than `/weekly` (which does full North Star analysis). This is a focused project-by-project review that updates `work/Index.md`.

## Usage

```
/weekly-review
```

## Workflow

### 1. Scan All Projects

For each folder in `work/projects/`:
- Count notes created/modified in the last 7 days
- List open decisions (`status: proposed`)
- Check for stale active notes (>14 days untouched)
- Check GitHub if repo URL is in README: `gh issue list --repo <url> --limit 5`

### 2. Compile Per-Project Summary

For each active project:
- **Shipped**: work notes marked completed this week
- **In Progress**: active work notes
- **Stuck**: stale items, blocked issues
- **Pending Decisions**: proposed ADRs
- **Open Issues**: from GitHub (if available)

### 3. Cross-Project View

- Total notes created this week
- Projects with zero activity (may need attention or may be intentionally paused)
- Any cross-project patterns (same gem upgrade needed, same compliance change)

### 4. Update Index

Update `work/Index.md`:
- Ensure all active projects are listed with current status
- Move any completed projects to archive section
- Update any stale descriptions

### 5. Present

- Per-project table: project name, notes this week, open decisions, open issues
- Flagged items: stale notes, projects with no activity
- Suggested actions for next week

## Important

- This modifies `work/Index.md` — other files are read-only
- Keep output scannable. Tables over paragraphs.
- If a project has been quiet for 2+ weeks, flag it but don't assume it's a problem — the user may be intentionally pausing it.
