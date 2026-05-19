---
description: "Scan an external code repo's git history over a window, summarize what was accomplished, and tie it back into the matching vault project."
---

# Repo Sync

Look at a code repository outside this vault (e.g. `~/dev/eris`), figure out what's been accomplished since a given point, and connect that work to the right vault project — README status, open notes, candidate decisions.

## Usage

```
/repo-sync <repo> [since <date | commit | last-sync>]
```

Examples:
- `/repo-sync eris since 2026-05-11`
- `/repo-sync pcms since last-sync` — uses the date of the last `chore(vault): … pcms sync` commit
- `/repo-sync ~/dev/biolift` — no window given; agent defaults to 14 days and says so

## Workflow

### 1. Resolve the window

- Explicit date or commit ref → pass it straight through.
- `last-sync` → run `git log --oneline -20` in **this vault** and find the most recent `chore(vault): … <project> sync` commit; pass its date as the `since` argument.
- Nothing given → let the agent default to 14 days (it will flag that it defaulted).

### 2. Dispatch the repo-scanner agent

Invoke the `repo-scanner` subagent with the repo and the resolved window. It runs in its own context, reads the external repo's git history (read-only), maps it to a vault project via its config table, and returns a briefing.

### 3. Tie it back into the vault

With the agent's briefing and your full vault context:

- Confirm or correct the mapped project (the agent flags inferred/unknown mappings; confirmed ones like `eris → rcservices` pass through).
- Cross-check against open notes and decisions in `work/projects/<project>/` — does the shipped work resolve, advance, or contradict anything tracked there?
- Surface concrete, specific suggestions: README status bumps, work notes to write, decisions to record, North Star items affected.

### 4. Offer, don't auto-apply

Present the tie-in as suggestions. Only write vault notes if the user confirms — then follow normal note conventions (frontmatter, wikilinks, correct folder).

## Important

- The agent is **read-only on the external repo and writes nothing**. All vault writes happen here, in the main context, only after user confirmation.
- If the repo isn't in the agent's config map, it will report candidates and ask you to confirm the mapping before going further.
- Speed matters — this is meant for quick "what happened in eris lately, and where does it land in the vault" checks.
