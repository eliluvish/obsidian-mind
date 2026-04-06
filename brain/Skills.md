---
description: "Vault-specific workflows and slash commands — project management, context switching, deploy checklists, and vault maintenance"
tags:
  - brain
  - index
---

# Skills

Custom slash commands, subagents, and reusable workflows. Defined in `.claude/commands/` and `.claude/agents/`.

## Slash Commands

### Daily Workflow

| Command | Purpose |
|---------|---------|
| `/standup` | Morning kickoff — load context, review yesterday, surface tasks, identify priorities |
| `/dump` | Freeform capture — dump anything, gets routed to the right notes automatically |
| `/wrap-up` | Full session review — verify notes, indexes, links, suggest improvements. Auto-triggered on "wrap up". Offers to record time via `/recording-time`. |
| `/recording-time` | Record work hours to RCMS calendar API — parse project, date, times, description, submit entries |

### Editing & Synthesis

| Command | Purpose |
|---------|---------|
| `/humanize` | Voice-calibrated editing — makes Claude-drafted text sound like you wrote it |
| `/weekly` | Weekly synthesis — cross-project patterns, North Star alignment, uncaptured wins |
| `/weekly-review` | Lighter cross-project review — what shipped, what's stuck, update Index.md |

### Project Management

| Command | Purpose |
|---------|---------|
| `/context-switch` | Reload context for a project — README, recent notes, open decisions. Key command for multi-project work. |
| `/project-status` | Deep status check on a single project — notes, decisions, stale items, GitHub issues |
| `/issue-capture` | Scaffold a work note from a GitHub Issue URL with pre-filled frontmatter |
| `/decision` | Create an ADR in the right project's `decisions/` folder with auto-numbering |
| `/deploy-checklist` | Pull up the deploy runbook for a project, walk through pre/post-deploy checks |
| `/project-archive` | Move completed project from `work/projects/` to `work/archive/`, update all indexes |

### Vault Maintenance

| Command | Purpose |
|---------|---------|
| `/vault-audit` | Deep structural audit — indexes, frontmatter, links, Bases, folder placement, stale context |
| `/vault-upgrade` | Import content from an existing vault — detects version, classifies notes, transforms frontmatter, rebuilds indexes |

## Usage Notes

**Daily:**
- `/standup` replaces the manual session start — reads North Star, projects, tasks, git log
- `/dump` processes freeform text and routes each piece to the correct note type and folder
- `/wrap-up` is auto-triggered when you say "wrap up" — runs full session review

**Editing & Synthesis:**
- `/humanize` calibrates against your actual writing samples. Run after drafting any note to make it sound human.
- `/weekly` is the full North Star analysis — run at end of week for cross-project patterns and drift detection.
- `/weekly-review` is the lighter version — focused on per-project status and updating Index.md.

**Project Management:**
- `/context-switch` is the most important command for multi-project work. Run it before starting work on a different project.
- `/issue-capture` only creates notes for significant issues — bug investigations, architectural decisions, not routine fixes.
- `/decision` auto-numbers ADRs within each project's `decisions/` folder.
- `/deploy-checklist` loads or creates a deploy runbook from `reference/ops/`.

**Maintenance:**
- `/vault-audit` should be run at the end of substantial sessions
- `/vault-upgrade` handles importing from other Obsidian vaults

## Subagents

| Agent | Purpose | Invoked by |
|-------|---------|------------|
| `context-loader` | Loads all vault context about a person, project, team, or concept | Direct — "load context on X" |
| `cross-linker` | Finds missing wikilinks, orphans, broken backlinks across the vault | `/vault-audit` |
| `vault-librarian` | Deep vault maintenance — orphan detection, broken links, frontmatter validation, stale notes | `/vault-audit` |
| `vault-migrator` | Classify, transform, and migrate content from a source vault | `/vault-upgrade` |

Subagents run in isolated context windows via `.claude/agents/`. They don't pollute the main conversation.

## Hooks

| Hook | When | What |
|------|------|------|
| SessionStart | On startup/resume | QMD re-index, inject North Star, projects, recent changes, tasks, file listing |
| UserPromptSubmit | Every message | Classify content (decision, win, architecture, person, project update, deploy, compliance) and inject routing hints |
| PostToolUse (Write/Edit) | After file writes | Validate frontmatter, check for wikilinks, verify folder placement |
| PreCompact | Before context compaction | Back up session transcript to `thinking/session-logs/` |
| Stop | End of session | Checklist: archive, update indexes, check orphans |

## Semantic Search (QMD)

If QMD is installed (`npm install -g @tobilu/qmd`), the vault has semantic search:

- `qmd query "..."` — hybrid BM25 + vector + LLM reranking (best quality)
- `qmd search "..."` — fast BM25 keyword search
- `qmd vsearch "..."` — semantic vector search (exploratory)
- `qmd update && qmd embed` — refresh index after bulk changes

SessionStart hook runs `qmd update` automatically. See `.claude/skills/qmd/SKILL.md` for full reference.

## Workflow: Weekly Review

1. **`/weekly`** — synthesize the week's activity, check alignment, find patterns
2. Promote any uncaptured wins to brag doc
3. Update North Star if focus shifted
4. **`/wrap-up`** — close the session cleanly

## Workflow: Project Ramp-Up

1. **`/context-switch <project>`** — load all project context
2. **`/project-status <project>`** — deep dive on current state
3. Create work notes for significant items
4. **`/vault-audit`** — ensure everything links properly

## Workflow: New Project Setup

1. Create project folder: `work/projects/<name>/`
2. Create README from template: `templates/Project README.md`
3. Create `decisions/` and `notes/` subfolders
4. Add project to `work/Index.md`
5. Capture the first decision or work note
