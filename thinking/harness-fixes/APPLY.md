---
date: "2026-06-10"
description: "Staged .claude/ harness fixes from the 6/10 harness evaluation — review, apply with cp, then delete this folder"
tags:
  - thinking
---

# Harness Fixes — Staged for Review

Claude Code's permission layer blocks the agent from editing `.claude/` (self-modification requires your explicit approval per file). These are the ready-to-apply replacement files from the [[2026-06-10]] harness evaluation. Review the diffs, apply, commit, delete this folder.

## Review

```bash
diff -u .claude/settings.json        thinking/harness-fixes/settings.json
diff -u .claude/settings.local.json  thinking/harness-fixes/settings.local.json
diff -u .claude/scripts/session-start.sh  thinking/harness-fixes/scripts/session-start.sh
diff -u .claude/agents/repo-scanner.md    thinking/harness-fixes/agents/repo-scanner.md
diff -u .claude/commands/wrap-up.md       thinking/harness-fixes/commands/wrap-up.md
diff -u .claude/commands/vault-audit.md   thinking/harness-fixes/commands/vault-audit.md
```

## What each change does

| File | Change |
|---|---|
| `settings.json` | Registers `classify-message.py` as the UserPromptSubmit hook — written, tested, documented in CLAUDE.md's "five hooks" table, but never wired up. Makes the table true. |
| `settings.local.json` | Fixes `additionalDirectories` ↔ repo-map drift: removes `~/dev/people` (doesn't exist — the repo dir is `pi_app`), adds `pi_app`, `cloud_costs`, `pcms-api`, `pcms-islands` so `/standup` sweeps and `/repo-sync` run prompt-free for every mapped repo. |
| `scripts/session-start.sh` | Adds a detached background `qmd embed` after `qmd update` so vector search stops silently going stale; bumps the North Star injection from `head -30` to `head -60` so growing goals aren't truncated. |
| `agents/repo-scanner.md` | Map now covers every vault project: `pi_app`/lab_archives → `minr`+`cade`+`ris`+`people` (label-scoped, per each README), `study_pay` → `rpr`. Adds multi-project attribution guidance. |
| `commands/wrap-up.md` | Step 8 referenced a `/time-entry-writing` skill that doesn't exist; now uses the installed `recording-time` skill. |
| `commands/vault-audit.md` | Step 10 becomes a real harness-hygiene pass: hooks table ↔ settings.json, repo map ↔ additionalDirectories ↔ projects three-way check, stale skill/command references, empty folder dependencies. Step 1 learns about `daily/`. |

## Apply

```bash
cd ~/dev/obsidian-mind
cp thinking/harness-fixes/settings.json              .claude/settings.json
cp thinking/harness-fixes/settings.local.json        .claude/settings.local.json
cp thinking/harness-fixes/scripts/session-start.sh   .claude/scripts/session-start.sh
cp thinking/harness-fixes/agents/repo-scanner.md     .claude/agents/repo-scanner.md
cp thinking/harness-fixes/commands/wrap-up.md        .claude/commands/wrap-up.md
cp thinking/harness-fixes/commands/vault-audit.md    .claude/commands/vault-audit.md
git add .claude && git commit -m "fix(harness): apply staged harness fixes (hooks, repo map, stale refs)"
git rm -r thinking/harness-fixes && git commit -m "chore(vault): remove applied harness-fixes staging"
```

## After applying

- Settings changes take effect on session restart (`/clear` or new session); the new UserPromptSubmit hook may prompt for approval once — see [[Gotchas#Vault Tooling]].
- One manual step Claude can't do (`.obsidian/` is off-limits): **Obsidian → Settings → Daily notes → New file location → `daily`**, so new dailies stop landing at the vault root.
