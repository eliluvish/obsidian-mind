# Obsidian Mind

An Obsidian vault template for engineers who use Claude Code as a thinking partner. Your external brain for work notes, decisions, performance tracking, and persistent AI context.

## What This Is

A ready-to-use vault structure that makes Claude Code productive from session one. Every conversation builds on the last because Claude has persistent context in the vault -- your goals, your decisions, your patterns, your wins.

The vault is built around **wikilinks**. Every note links to related notes, building a knowledge graph that compounds over time. Claude maintains the indexes and links as notes are created, so the graph stays navigable without manual effort.

## What's New in V2

V2 is a significant expansion of the original template, adding structured workflows for performance tracking, incident management, and organizational knowledge.

- **`Home.md` dashboard** -- vault entry point with embedded Base views for active work, incidents, 1:1 history, and people
- **`bases/`** -- 7 centralized dynamic database views (Work Dashboard, Incidents, People Directory, 1-1 History, Review Evidence, Competency Map, Templates)
- **`work/active/` + `work/archive/`** -- explicit project lifecycle. Active projects live in `active/`, completed ones move to `archive/YYYY/`
- **`work/incidents/`** -- structured incident tracking with root cause analysis, timelines, and deep dives
- **`org/`** -- organizational knowledge with `org/people/` for person notes and `org/teams/` for team context
- **8 slash commands** -- `/peer-scan`, `/slack-scan`, `/capture-1on1`, `/vault-audit`, `/review-brief`, `/incident-capture`, `/project-archive`, `/wrap-up`
- **3 hooks** -- SessionStart (injects vault file listing), PreToolUse (validates frontmatter on writes), Stop (end-of-session checklist)
- **Enhanced `CLAUDE.md`** -- full session workflow, note type reference, graph-first linking rules, index maintenance, and agent guidelines

## Quick Start

1. **Clone** this repo (or use it as a GitHub template)
2. **Open** the folder as an Obsidian vault
3. **Enable Bases** in Settings > Core plugins
4. **Enable the Obsidian CLI** in Settings > Core plugins (requires Obsidian 1.12+)
5. **Run** `claude` in the vault directory
6. **Fill in** `brain/North Star.md` with your current goals -- this grounds every session

Claude will read `CLAUDE.md` automatically and understand the full vault structure, conventions, and workflows.

## Vault Structure

```
Home.md                    Vault entry point -- embedded dashboards
CLAUDE.md                  Operating manual for Claude (loaded every session)

bases/                     Centralized dynamic database views
  Work Dashboard.base        Active and recent work
  Incidents.base             All incidents with severity and status
  People Directory.base      People organized by team
  1-1 History.base           Meeting notes timeline
  Review Evidence.base       PR scans and evidence for reviews
  Competency Map.base        Competency definitions and levels
  Templates.base             Available note templates

work/                      Work notes index
  Index.md                   Map of Content -- central hub for all work notes
  active/                    Current projects (1-3 files)
  archive/                   Completed work organized by year
    2025/
    2026/
  incidents/                 Incident docs (main note + RCA + deep dive)
  1-1/                       1:1 meeting notes (Person YYYY-MM-DD.md)

perf/                      Performance framework
  Brag Doc.md                Running log of wins, linked to evidence
  brag/                      Quarterly brag notes (Q1 2025.md, etc.)
  competencies/              One note per competency (link targets)
  evidence/                  PR deep scans and data extracts for reviews

brain/                     Claude's operational knowledge
  Memories.md                Index of memory topics
  Key Decisions.md           Significant technical and architectural decisions
  Patterns.md                Recurring patterns and approaches
  Gotchas.md                 Known pitfalls and workarounds
  Skills.md                  Custom workflows and slash command docs
  North Star.md              Goals and focus areas (read every session)

org/                       Organizational knowledge
  People & Context.md        Index of people, teams, and org structure
  people/                    One note per person
  teams/                     One note per team

reference/                 Codebase knowledge, architecture maps
thinking/                  Scratchpad for drafts and reasoning
templates/                 Obsidian templates with YAML frontmatter
```

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
| `/wrap-up` | Full session review -- verify notes, indexes, links, suggest improvements |

Commands are defined in `.claude/commands/` and can be invoked directly in Claude Code with the slash prefix.

## Bases

The vault includes 7 Obsidian Base files in `bases/` that provide dynamic database views over your vault content.

| Base | What It Shows |
|------|---------------|
| Work Dashboard | Active projects filtered by status and quarter |
| Incidents | All incidents with severity, role, and ticket number |
| People Directory | People organized by team with roles |
| 1-1 History | Timeline of all 1:1 meeting notes |
| Review Evidence | PR scans and evidence linked to people and cycles |
| Competency Map | Competency definitions with level criteria |
| Templates | Available note templates for quick reference |

Bases require the Bases core plugin (Obsidian 1.8+). They query frontmatter properties like `status`, `quarter`, `team`, `person`, and `cycle`.

## Hooks

Three hooks in `.claude/settings.json` automate vault hygiene:

### SessionStart
Runs on startup, resume, and clear. Injects the full vault file listing into Claude's context so it immediately knows what exists -- no wasted turns on file discovery. Also prints a quick-reference reminder of vault conventions.

### PreToolUse
Triggers before any file write. Reminds Claude to include proper frontmatter (`date`, `quarter`, `description`, `tags`), add at least one wikilink, and place the file in the correct folder per `CLAUDE.md`.

### Stop
Triggers at the end of every session. Prints a checklist: archive completed projects, update indexes, verify new notes are linked, and optionally run `/vault-audit`.

## Key Files

Start by customizing these files for your situation:

| File | What to Do |
|------|------------|
| `brain/North Star.md` | Write your current goals and focus areas |
| `perf/competencies/` | Create notes for your organization's competency framework |
| `org/People & Context.md` | Add your team, manager, and key collaborators |
| `org/teams/` | Create notes for teams you work with |
| `work/Index.md` | Will grow as you add work notes |
| `perf/Brag Doc.md` | Will grow as you log wins |

## Customization

This is a starting point, not a straitjacket. Adapt it to how you work:

- **Teams**: Replace the generic team names in `CLAUDE.md` tags convention with your actual team names
- **Competencies**: Create notes in `perf/competencies/` matching your organization's framework (IC3/IC4/IC5 levels, or whatever your org uses)
- **Properties**: Add custom frontmatter properties and update `CLAUDE.md` Properties for Querying section
- **Templates**: Modify templates in `templates/` or add new ones
- **Slash commands**: Edit commands in `.claude/commands/` to match your tools (GitHub org, Slack workspace, etc.)
- **Bases**: Customize the `.base` files in `bases/` to add filters, columns, or new views
- **Reference**: Add codebase architecture docs, flow diagrams, or domain knowledge to `reference/`
- **Review cycles**: Create `perf/<cycle>/` folders as review periods come up (e.g., `perf/h1-2026/`)

## Migrating from V1

If you used the original Obsidian Mind template (V1), here is what changed:

1. **Rename `claude/` to `brain/`** -- `git mv claude/ brain/`
2. **Create new folders**: `bases/`, `org/`, `org/people/`, `org/teams/`, `work/active/`, `work/archive/`, `work/incidents/`, `work/1-1/`, `perf/brag/`, `perf/evidence/`, `reference/`
3. **Move active work notes** from `work/` to `work/active/`
4. **Move completed work notes** from `work/` to `work/archive/YYYY/`
5. **Create `Home.md`** in vault root with embedded Base views
6. **Copy Base files** from the V2 template into `bases/`
7. **Add new commands**: copy missing `.claude/commands/` files from V2
8. **Update `CLAUDE.md`**: replace with the V2 version, then re-add any custom conventions
9. **Update `.claude/settings.json`**: add PreToolUse and Stop hooks from V2
10. **Update tags**: `claude` tag becomes `brain`, add `person` and `team` tags

All V1 content is preserved -- V2 only adds structure around it.

## Requirements

- [Obsidian](https://obsidian.md) 1.12+ (for CLI support and Bases)
- [Claude Code](https://claude.ai/claude-code)
- Bases core plugin enabled (Settings > Core plugins)
- Git (for version history; sync via git, [Obsidian Sync](https://obsidian.md/sync), or your preferred method)

## Design Influences

- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) -- Official Obsidian agent skills
- [James Bedford](https://x.com/jameesy) -- Vault structure philosophy, separation of AI-generated content
- [arscontexta](https://github.com/agenticnotetaking/arscontexta) -- Progressive disclosure via description fields, session hooks, kernel primitives

## License

MIT
