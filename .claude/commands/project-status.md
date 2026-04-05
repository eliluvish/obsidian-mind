---
description: "Scan a project folder, summarize active work notes and open decisions, check for stale items."
---

# Project Status

Quick status check on a single project. Deeper than standup's per-project summary, shallower than a full audit.

## Usage

```
/project-status <project name>
```

## Workflow

### 1. Find the Project

Search `work/projects/` for the project name. If not found, list available projects and ask the user to clarify.

### 2. Read Project Context

- Read `work/projects/<name>/README.md` for full project context
- Note the repo URL, deploy target, stakeholders, compliance notes

### 3. Scan Work Notes

- List all notes in `work/projects/<name>/notes/` sorted by date (newest first)
- Read the 3-5 most recent notes
- Identify any with `status: active` (still in progress)
- Flag any notes older than 14 days that are still `status: active` (potentially stale)

### 4. Scan Decisions

- List all ADRs in `work/projects/<name>/decisions/`
- Identify any with `status: proposed` (not yet decided)
- Read the most recent decision

### 5. Check GitHub

If the project README has a repo URL:
- `gh issue list --repo <url> --limit 5` — check open issues
- `gh pr list --repo <url> --limit 5` — check open PRs

### 6. Present Summary

- **Project**: name, Rails version, deploy target
- **Recent Activity**: last 3-5 work notes summarized in one line each
- **Open Decisions**: any proposed ADRs awaiting resolution
- **Stale Items**: work notes still active but untouched for >14 days
- **GitHub**: open issues and PRs (if available)
- **Suggested Next Steps**: based on open items and recent momentum

## Important

- This is a read-only operation — don't modify anything
- Keep the output concise and scannable
- If the project folder is empty (new project), note that and suggest running `/context-switch` to set it up
