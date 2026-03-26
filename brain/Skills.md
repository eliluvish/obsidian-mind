---
description: "Vault-specific workflows and slash commands — reusable patterns for review prep, project tracking, and vault maintenance"
tags:
  - brain
  - index
---

# Skills

Custom slash commands and reusable workflows. Defined in `.claude/commands/`.

## Slash Commands

| Command | Purpose |
|---------|---------|
| `/peer-scan` | Deep scan a peer's GitHub PRs for review prep |
| `/slack-scan` | Deep scan Slack channels/DMs for evidence |
| `/capture-1on1` | Capture 1:1 meeting transcript into structured vault note |
| `/vault-audit` | Audit indexes, links, orphans, stale context |
| `/review-brief` | Generate review brief (manager or peer version) |
| `/incident-capture` | Capture incident from Slack channels/DMs into structured vault notes |
| `/project-archive` | Move completed project from active/ to archive/, update indexes |
| `/wrap-up` | Full session review — verify notes, indexes, links, suggest improvements |

## Usage Notes

- `/peer-scan` works best when launched as parallel agents (one per person)
- `/slack-scan` should be run AFTER `/peer-scan` to add context beyond code
- `/capture-1on1` handles transcripts, raw notes, or summaries
- `/vault-audit` should be run at the end of substantial sessions
- `/review-brief` needs the private brief to exist first — it generates filtered versions
- `/incident-capture` takes Slack URLs and produces structured incident documentation
- `/project-archive` handles the active/ → archive/ move with index updates
- `/wrap-up` is auto-triggered when you say "wrap up" — runs full session review

## Workflow: Full Review Cycle Prep

1. **`/review-brief manager`** — generate the manager context transfer doc
2. **`/review-brief peers`** — generate the peer context transfer doc
3. **`/peer-scan`** (parallel, one per peer) — deep scan each peer's PRs
4. **`/slack-scan`** — scan relevant channels for your own evidence + peer context
5. **`/capture-1on1`** — capture the review 1:1 with your manager
6. **`/vault-audit`** — tidy up after all the new data

## Workflow: Project Ramp-Up

1. **`/slack-scan`** — scan project channels for history and decisions
2. **`/peer-scan`** (if needed) — understand what teammates have already built
3. Create work note from gathered context
4. **`/vault-audit`** — ensure everything links properly
