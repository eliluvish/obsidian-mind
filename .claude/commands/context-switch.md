---
description: "Reload context for a project. Read README, recent notes, open decisions — rapid re-entry when jumping between projects."
---

# Context Switch

When jumping between projects, this command reloads the target project's full context so you can hit the ground running. This is the most important command for managing 5-7 concurrent projects.

## Usage

```
/context-switch <project name>
```

## Workflow

### 1. Find the Project

Search `work/projects/` for the project name. If not found, list available projects and ask the user to clarify.

### 2. Load Project Context

Read **everything** in the project folder:
- `work/projects/<name>/README.md` — full project context (repo, deploy, stakeholders, compliance, architecture)
- All files in `work/projects/<name>/decisions/` — scan for any `status: proposed`
- Last 3-5 notes in `work/projects/<name>/notes/` (by date, newest first)

### 3. Load Related Brain Context

Check `brain/` notes for project-specific knowledge:
- `brain/Gotchas.md` — any gotchas mentioning this project?
- `brain/Patterns.md` — any patterns specific to this project?
- `brain/Key Decisions.md` — any cross-project decisions affecting this one?

### 4. Load Related Reference Context

Check `reference/` for project-relevant info:
- `reference/ops/` — any deploy runbook for this project?
- `reference/compliance/` — any compliance notes relevant to this project?
- `reference/infrastructure/` — any infra notes relevant to this project?

### 5. Check GitHub (if repo URL in README)

- `gh issue list --repo <url> --assignee @me --limit 10` — your open issues
- `gh pr list --repo <url> --author @me --limit 5` — your open PRs

### 6. Present Context Briefing

Structure as a compact briefing:
- **Project**: name, Rails version, key stakeholders
- **Where You Left Off**: summary of the most recent work note
- **Open Items**: pending decisions, active work notes, assigned GitHub issues
- **Key Constraints**: compliance notes, gotchas, deploy considerations
- **Suggested Starting Point**: what to work on based on open items

## Important

- This is a read-only orientation — don't modify anything
- Speed matters here. The whole point is fast re-entry.
- If the project folder doesn't exist yet, offer to create it using the Project README template
- After presenting, you're ready to work. Don't ask "what would you like to do?" — the user knows.
