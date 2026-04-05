🌐 **English** | [日本語](README.ja.md) | [中文](README.zh-CN.md) | [한국어](README.ko.md)

# 🧠 Obsidian Mind

[![Claude Code](https://img.shields.io/badge/claude%20code-required-D97706)](https://docs.anthropic.com/en/docs/claude-code)
[![Obsidian](https://img.shields.io/badge/obsidian-1.12%2B-7C3AED)](https://obsidian.md)
[![Python](https://img.shields.io/badge/python-3.8%2B-3776AB)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> **An Obsidian vault that makes Claude Code remember everything.** Start a session, talk about your day, and Claude handles the rest — notes, links, indexes, project context. Every conversation builds on the last.

---

## 🔴 The Problem

Claude Code is powerful, but it forgets. Every session starts from zero — no context on your goals, your projects, your patterns, your wins. You re-explain the same things. You lose decisions made three conversations ago. The knowledge never compounds.

## 🟢 The Solution

Give Claude a brain.

```
You: "start session"
Claude: *reads North Star, checks active projects, scans recent memories*
Claude: "You have 5 active projects. patient-registry has a pending ADR
         on Stimulus migration. lab-inventory hasn't had activity in 12 days.
         Your deploy runbook for sample-tracker needs updating."
```

---

## ⚡ See It In Action

**Morning kickoff:**

```bash
/standup
# → loads North Star, active projects, open tasks, recent git changes
# → "You have 5 active projects. patient-registry had 3 commits yesterday.
#    lab-inventory has a stale work note from 2 weeks ago."
```

**Context switch between projects:**

```bash
/context-switch patient-registry
# → reads project README (Rails 7.1, deploys to research-app01, PI is Dr. Smith)
# → loads last 3 work notes and open decisions
# → "You left off on the bulk CSV import timeout fix. There's a pending
#    decision on whether to switch to Stimulus for the form validation."
```

**Capture a GitHub issue as a work note:**

```bash
/issue-capture https://github.com/hospital/patient-registry/issues/47
# → fetches issue via gh CLI
# → creates work/projects/patient-registry/notes/2026-04-05-bulk-import-timeout.md
# → pre-fills frontmatter with project, github_issue, description
```

**Brain dump after a meeting:**

```bash
/dump Met with Dr. Smith about the patient registry. She wants bulk import
to handle 50k rows by end of month. Also, IT security said we need to add
audit logging for all PHI access — that's a HIPAA requirement. Decision:
use Active Job for the import instead of inline processing.
```

```
→ Created work/projects/patient-registry/notes/2026-04-05-bulk-import-requirements.md
→ Created decision record: "Use Active Job for bulk imports"
→ Updated reference/compliance/hipaa-audit-logging.md with PHI access requirement
→ Updated org/people/Dr Smith.md with meeting context
```

**End of day:**

```
You: "wrap up"
# → verifies all notes have links
# → updates indexes
# → suggests improvements
```

---

## ⚙️ How It Works

**Folders group by purpose. Links group by meaning.** A note lives in one folder (its home) but links to many notes (its context). Claude maintains this graph — linking work notes to projects, decisions, and people automatically. A note without links is a bug.

**Project-centric organization.** Each of your Rails apps gets its own folder under `work/projects/` with a README (repo URL, deploy target, stakeholders, compliance notes), a `decisions/` folder for ADRs, and a `notes/` folder for work notes. When you `/context-switch`, Claude reads the whole project folder to reload context.

**Vault-first memory** keeps context across sessions and machines. All durable knowledge lives in `brain/` topic notes (git-tracked, Obsidian-browsable, linked). Claude Code's `MEMORY.md` (`~/.claude/`) is an auto-loaded index that points to vault locations — never the storage itself. This means memories survive machine changes and are part of the graph.

**Sessions have a designed lifecycle.** The `SessionStart` hook auto-injects your North Star goals, active projects, recent changes, open tasks, and the full vault file listing — Claude starts every session with context, not a blank slate. At the end, say "wrap up" and Claude runs `/wrap-up` — verifying notes, updating indexes, and spotting gaps. The `CLAUDE.md` governs everything in between: where to file things, how to link, when to split a note, what to do with decisions and deploys.

### Hooks

Five lifecycle hooks handle routing automatically:

| Hook | When | What |
|------|------|------|
| 🚀 SessionStart | On startup/resume | QMD re-index, inject North Star, projects, recent changes, tasks, file listing |
| 💬 UserPromptSubmit | Every message | Classifies content (decision, win, architecture, person, project, deploy, compliance) and injects routing hints |
| ✍️ PostToolUse | After writing `.md` | Validates frontmatter, checks for wikilinks, verifies folder placement |
| 💾 PreCompact | Before context compaction | Backs up session transcript to `thinking/session-logs/` |
| 🏁 Stop | End of session | Checklist: archive completed projects, update indexes, check orphans |

> [!TIP]
> You just talk. The hooks handle the routing.

---

## 📅 Daily Workflow

**Morning**: Run `/standup`. Claude loads your North Star, active projects, open tasks, and recent changes. You get a structured summary and suggested priorities.

**Switching projects**: Run `/context-switch <project>`. Claude reads the project README, recent notes, open decisions, and related reference material. This is the most important command for managing multiple projects.

**Throughout the day**: Talk naturally. Mention a decision you made, a deploy you're doing, a compliance issue. The classification hook nudges Claude to file each piece correctly. For bigger brain dumps, use `/dump` and narrate everything at once.

**End of day**: Say "wrap up" and Claude invokes `/wrap-up` — verifies notes, updates indexes, checks links.

**Weekly**: Run `/weekly` for cross-project synthesis — North Star alignment, patterns, uncaptured wins, and next-week priorities. Run `/vault-audit` to catch orphan notes, broken links, and stale content.

---

## 🛠️ Commands

Defined in `.claude/commands/`. Run them in any Claude Code session.

| Command | What It Does |
|---------|-------------|
| `/standup` | Morning kickoff — loads context, reviews yesterday, surfaces tasks, suggests priorities |
| `/dump` | Freeform capture — talk naturally about anything, Claude routes it all to the right notes |
| `/wrap-up` | Full session review — verify notes, indexes, links, suggest improvements |
| `/humanize` | Voice-calibrated editing — makes Claude-drafted text sound like you wrote it |
| `/weekly` | Weekly synthesis — cross-project patterns, North Star alignment, uncaptured wins |
| `/weekly-review` | Lighter cross-project review — what shipped, what's stuck, update Index.md |
| `/context-switch` | Reload context for a project — README, recent notes, open decisions |
| `/project-status` | Deep status check on a single project — notes, decisions, stale items, GitHub issues |
| `/issue-capture` | Scaffold a work note from a GitHub Issue URL with pre-filled frontmatter |
| `/decision` | Create an ADR in the right project's `decisions/` folder with auto-numbering |
| `/deploy-checklist` | Pull up deploy runbook, walk through pre/post-deploy checks |
| `/project-archive` | Move a completed project from `work/projects/` to `work/archive/`, update indexes |
| `/vault-audit` | Audit indexes, links, orphans, stale context |
| `/vault-upgrade` | Import content from an existing vault — version detection, classification, migration |

---

## 🤖 Subagents

Specialized agents that run in isolated context windows. They handle heavy operations without polluting your main conversation.

| Agent | Purpose | Invoked by |
|-------|---------|------------|
| `context-loader` | Loads all vault context about a person, project, or concept | Direct |
| `cross-linker` | Finds missing wikilinks, orphans, broken backlinks | `/vault-audit` |
| `vault-librarian` | Deep vault maintenance — orphans, broken links, stale notes | `/vault-audit` |
| `vault-migrator` | Classify, transform, and migrate content from a source vault | `/vault-upgrade` |

> [!NOTE]
> Subagents are defined in `.claude/agents/`. You can add your own for domain-specific workflows.

---

## 📋 Bases

The `bases/` folder contains database views that query your notes' frontmatter properties. They update automatically as notes change.

| Base | Shows |
|------|-------|
| Projects | All project READMEs with status, Rails version, last updated |
| Work Dashboard | Active work notes grouped by project |
| People Directory | Everyone in `org/people/` with role, team |
| Templates | Quick access to all templates |

`Home.md` embeds these views, making it the vault's dashboard.

---

## 🔄 Upgrading

Already using an older version of obsidian-mind (or any Obsidian vault)? The `/vault-upgrade` command migrates your content into the latest template:

```bash
# 1. Clone the latest obsidian-mind
git clone https://github.com/breferrari/obsidian-mind.git ~/new-vault

# 2. Open it in Claude Code
cd ~/new-vault && claude

# 3. Run the upgrade pointing to your old vault
/vault-upgrade ~/my-old-vault
```

Claude will:
1. **Detect** your vault version (v1–v3.3, or identify it as a non-obsidian-mind vault)
2. **Inventory** every file — classify as user content, scaffold, infrastructure, or uncategorized
3. **Present a migration plan** — you see exactly what will be copied, transformed, and skipped
4. **Execute** after your approval — transforms frontmatter, fixes wikilinks, rebuilds indexes
5. **Validate** — checks for orphans, broken links, missing frontmatter

Your old vault is **never modified**. Use `--dry-run` to preview the plan without executing.

> [!NOTE]
> Works with any Obsidian vault, not just obsidian-mind. For non-obsidian-mind vaults, Claude reads each note and classifies it semantically — routing work notes, people, decisions, and reference material to the right folders.

---

## 🚀 Quick Start

1. Clone this repo (or use it as a **GitHub template**)
2. Open the folder as an **Obsidian vault**
3. Enable the **Obsidian CLI** in Settings → General (requires Obsidian 1.12+)
4. Run **`claude`** in the vault directory
5. Fill in **`brain/North Star.md`** with your goals — this grounds every session
6. Create your first project folder in `work/projects/` using the Project README template
7. Start talking about work

### Optional: QMD Semantic Search

For semantic search across the vault (find "what did we decide about caching" even if the note is titled "Redis Migration ADR"):

```bash
npm install -g @tobilu/qmd
qmd collection add . --name vault --mask "**/*.md"
qmd context add qmd://vault "Developer's work vault: projects, decisions, deploys, compliance, people"
qmd update && qmd embed
```

> [!NOTE]
> If QMD isn't installed, everything still works — Claude falls back to the Obsidian CLI and grep.

---

## 📁 Vault Structure

```
Home.md                 Vault entry point — embedded Base views, quick links
CLAUDE.md               Operating manual — Claude reads this every session
vault-manifest.json     Template metadata — version, structure, schemas
CHANGELOG.md            Version history
CONTRIBUTING.md         Template development checklist
README.md               Product documentation
LICENSE                 MIT license

bases/                  Dynamic database views (Projects, Work Dashboard, People, Templates)

work/
  projects/
    <project-name>/     One folder per Rails app
      README.md         Project context: repo, deploy, tech stack, stakeholders, compliance
      decisions/        ADRs scoped to this project
      notes/            Dated work notes for this project
  archive/<name>/       Completed/sunset project folders
  Index.md              Map of Content for all work

org/
  people/               One note per person — PIs, IT contacts, collaborators
  teams/                One note per team — members, scope
  People & Context.md   MOC for organizational knowledge

perf/
  Brag Doc.md           Flat running log of wins, linked to work notes

brain/
  North Star.md         Goals and focus areas — read every session
  Memories.md           Index of memory topics
  Key Decisions.md      Significant decisions and their reasoning
  Patterns.md           Recurring patterns observed across work
  Gotchas.md            Things that have gone wrong and why
  Skills.md             Custom workflows and slash commands

reference/
  compliance/           HIPAA, IRB, and regulatory notes
  ops/                  Deploy runbooks and operational procedures
  infrastructure/       Network, server, and environment notes
thinking/               Scratchpad for drafts — promote findings, then delete
templates/              Obsidian templates with YAML frontmatter

.claude/
  commands/             14 slash commands
  agents/               4 subagents
  scripts/              Hook scripts
  skills/               Obsidian + QMD skills
  settings.json         5 hooks configuration
```

---

## 📝 Templates

Templates with YAML frontmatter, each including a `description` field for progressive disclosure:

- **Work Note** — date, description, project, github_issue, status, tags
- **Decision Record** — date, description, project, status (proposed/accepted/deprecated), context
- **Thinking Note** — date, description, context, tags (scratchpad — delete after promoting)
- **Project README** — date, description, project, status, rails_version, ruby_version, stakeholders, compliance

---

## 🔧 What's Included

### Obsidian Skills

[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) pre-installed in `.claude/skills/`:

- **obsidian-markdown** — Obsidian-flavored markdown (wikilinks, embeds, callouts, properties)
- **obsidian-cli** — CLI commands for vault operations
- **obsidian-bases** — Database-style `.base` files
- **json-canvas** — Visual `.canvas` file creation
- **defuddle** — Web page to markdown extraction

### QMD Skill

A custom skill in `.claude/skills/qmd/` that teaches Claude to use [QMD](https://github.com/tobi/qmd) semantic search proactively — before reading files, before creating notes (to check for duplicates), and after creating notes (to find related content that should link to it).

---

## 🎨 Customize It

This is a starting point. Adapt it to how you work:

| What | Where |
|------|-------|
| Your goals | `brain/North Star.md` — grounds every session |
| Your projects | `work/projects/` — one folder per app with README |
| Your contacts | `org/` — add PIs, IT contacts, collaborators |
| Your compliance | `reference/compliance/` — HIPAA, IRB, audit requirements |
| Your runbooks | `reference/ops/` — deploy procedures per project |
| Your tools | `.claude/commands/` — edit for your GitHub org |
| Your conventions | `CLAUDE.md` — the operating manual, evolve it as you go |
| Your domain | Add folders, subagents in `.claude/agents/`, or classification rules in `.claude/scripts/` |

> [!IMPORTANT]
> `CLAUDE.md` is the operating manual. When you change conventions, update it — Claude reads it every session.

---

## 📋 Requirements

- [Obsidian](https://obsidian.md) 1.12+ (for CLI support)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- Python 3 (for hook scripts)
- Git (for version history)
- [QMD](https://github.com/tobi/qmd) (optional, for semantic search)

---

## 🙏 Design Influences

- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) — Official Obsidian agent skills
- [James Bedford](https://x.com/jameesy) — Vault structure philosophy, separation of AI-generated content
- [arscontexta](https://github.com/agenticnotetaking/arscontexta) — Progressive disclosure via description fields, session hooks

---

## 📄 License

MIT
