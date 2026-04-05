# Obsidian Mind

Personal Obsidian vault -- an external brain for a solo Rails developer at a research hospital. Tracks 5-7 concurrent projects, technical decisions, deploy runbooks, compliance notes, and Claude context.

## Skills & Capabilities

This vault has [obsidian-skills](https://github.com/kepano/obsidian-skills) installed in `.claude/skills/`. Follow these skill conventions:

- **obsidian-markdown**: Obsidian-flavored markdown -- wikilinks, embeds, callouts, properties. See `references/` for callout types, embed syntax, and property specs. Always prefer `[[wikilinks]]` over markdown links.
- **obsidian-cli**: CLI commands for vault operations when Obsidian is running. See CLI section below.
- **json-canvas**: Create `.canvas` files with nodes, edges, and visual layouts. See `references/EXAMPLES.md`.
- **obsidian-bases**: Create `.base` files with views, filters, and formulas. Bases core plugin is enabled. See `references/FUNCTIONS_REFERENCE.md`.
- **defuddle**: Extract clean markdown from web pages via `defuddle parse <url> --md`.
- **qmd**: Semantic search across the vault via [QMD](https://github.com/tobi/qmd). Use PROACTIVELY before reading files -- `qmd query "..."` for hybrid search, `qmd search "..."` for keyword, `qmd vsearch "..."` for semantic. Falls back to grep/glob if QMD not installed.

### Custom Slash Commands

Defined in `.claude/commands/`. See [[Skills]] for full documentation.

| Command | Purpose |
|---------|---------|
| `/standup` | Morning kickoff -- load context, review yesterday, surface tasks, priorities |
| `/dump` | Freeform capture -- dump anything, gets routed to the right notes |
| `/wrap-up` | Full session review -- verify notes, indexes, links, suggest improvements |
| `/humanize` | Voice-calibrated editing -- make notes sound like you, not AI |
| `/weekly` | Weekly synthesis -- cross-project patterns, North Star alignment, uncaptured wins |
| `/project-status` | Scan a project folder, summarize active work and open decisions, flag stale items |
| `/context-switch` | Reload context for a project -- README, recent notes, open decisions, rapid re-entry |
| `/issue-capture` | Scaffold a work note from a GitHub Issue URL with pre-filled frontmatter |
| `/decision` | Create an ADR in the right project's `decisions/` folder with auto-numbering |
| `/deploy-checklist` | Pull up deploy runbook for a project, walk through pre/post-deploy checks |
| `/weekly-review` | Cross-project review -- what shipped, what's stuck, pending decisions |
| `/vault-audit` | Audit indexes, links, orphans, stale context |
| `/vault-upgrade` | Import content from an existing vault into this obsidian-mind instance |
| `/project-archive` | Move completed project from `work/projects/` to `work/archive/`, update indexes |

## Vault Structure

| Folder | Purpose | Key Files |
|--------|---------|-----------|
| `Home.md` | **Vault entry point** -- embedded Base views, quick links | Open this first |
| `vault-manifest.json` | **Template metadata** -- version, infrastructure vs user content boundaries, frontmatter schemas, version fingerprints | Used by `/vault-upgrade` for migration |
| `CHANGELOG.md` | **Version history** -- tracks template releases with what changed | Reference for upgrade paths |
| `bases/` | **All Bases centralized** -- dynamic views for navigation | `Work Dashboard`, `Projects`, `People Directory`, `Templates` |
| `work/` | Work notes index | `Index.md` (detailed MOC) |
| `work/projects/<name>/` | **One folder per active project** -- self-contained with README, decisions, notes | `README.md`, `decisions/`, `notes/` |
| `work/archive/<name>/` | Completed project folders | Moved here via `/project-archive` |
| `perf/` | Performance tracking | `Brag Doc.md` (flat running log) |
| `brain/` | Claude's operational knowledge | `Memories.md`, `Key Decisions.md`, `Patterns.md`, `Gotchas.md`, `Skills.md`, `North Star.md` |
| `org/` | Organizational knowledge index | `People & Context.md` (MOC) |
| `org/people/` | Person notes -- PIs, IT contacts, collaborators | One note per person |
| `org/teams/` | Team notes as graph nodes | One note per team |
| `reference/` | Technical reference material | Architecture docs, flow docs |
| `reference/compliance/` | HIPAA, IRB, and regulatory notes | Compliance checklists, policies |
| `reference/ops/` | Deploy runbooks and operational procedures | Per-project or shared runbooks |
| `reference/infrastructure/` | Network, server, and environment notes | Server inventory, network maps |
| `thinking/` | Scratchpad for drafts and reasoning | Named `YYYY-MM-DD-topic.md` |
| `templates/` | Obsidian templates | `Work Note.md`, `Decision Record.md`, etc. |
| `.claude/commands/` | 14 slash commands | See command table above |
| `.claude/agents/` | 4 subagents | See subagents table below |
| `.claude/scripts/` | Hook scripts | `session-start.sh`, `classify-message.py`, `validate-write.py`, `pre-compact.sh` |
| `.claude/skills/` | Obsidian + QMD skills | Loaded automatically via Skill tool |

## Obsidian CLI

When Obsidian is running, prefer CLI over raw filesystem. It provides vault-aware search, backlink discovery, and property management. Fall back to filesystem when Obsidian is not running.

```bash
obsidian read file="Note Name"                    # Read a note
obsidian create name="Name" content="..." silent   # Create without opening
obsidian append file="Name" content="..."          # Append to note
obsidian search query="text" limit=10              # Vault-aware search
obsidian backlinks file="Name"                     # Discover connections
obsidian tags sort=count counts                    # List all tags
obsidian tasks daily todo                          # Open tasks
obsidian daily:read                                # Today's daily note
obsidian property:set name="status" value="done" file="Name"
obsidian orphans                                   # Unlinked notes
```

`file=` resolves like a wikilink (by name). `path=` for exact path from root. Use `silent` to prevent files from opening. Run `obsidian help` for full reference.

## Session Workflow

### Starting a Substantial Session

The `SessionStart` hook automatically injects rich context: vault file listing, North Star goals, project list, recent git changes, open tasks, and triggers a QMD re-index. Most context is already loaded -- you don't need to manually read files.

**Shortcut**: Run `/standup` for a structured morning kickoff that reads everything and presents a summary with suggested priorities.

If doing it manually:

1. Read `Home.md` -- vault entry point with embedded dashboards
2. Read `brain/North Star.md` -- ground suggestions in current goals
3. Check `work/Index.md` -- see active projects and recent notes
4. Scan `brain/Memories.md` -- index of memory topics, then read relevant topic notes
5. `obsidian tasks daily todo` -- see pending items

### Context Switching

**`/context-switch` is the most important command.** When jumping between projects, it reloads all relevant context: the project README, recent notes, open decisions, and any linked reference material. Use it every time you switch projects mid-session.

### Ending a Substantial Session

**When the user says "wrap up", "let's wrap", "wrapping up", or similar -- invoke `/wrap-up` automatically.** This runs a full review of the session.

If `/wrap-up` is not invoked, at minimum do these before wrapping up:

1. **Archive completed projects**: `git mv` from `work/projects/<name>/` to `work/archive/<name>/`, update `status: completed` (or use `/project-archive`)
2. Update `work/Index.md` if new notes or decisions were created
3. Update the relevant brain topic note (`brain/Key Decisions.md`, `brain/Patterns.md`, `brain/Gotchas.md`) with key learnings
4. Update `org/People & Context.md` if org knowledge changed
5. Update `perf/Brag Doc.md` if wins or impact were achieved
6. Offer to update `brain/North Star.md` if goals shifted or new focus emerged
7. Verify all new notes link to at least one existing note (orphans are bugs)
8. Run `/vault-audit` if the session created many notes

Skip steps that don't apply. The goal is transferring durable knowledge from conversation to vault state.

### Thinking Workflow

Use `thinking/` for drafts, reasoning, and analysis before writing final notes. **Thinking notes are scratchpads, not storage.** They exist to help you reason -- once the reasoning produces durable knowledge, promote it to proper notes and delete the scratchpad.

1. Create a thinking note: `thinking/YYYY-MM-DD-descriptive-name.md`
2. Use the Thinking Note template
3. Reason through the problem, analyze options, draft content
4. Promote findings to atomic notes in the correct folder (not one monolith -- one note per distinct concept)
5. Delete the thinking note -- it served its purpose
6. If the thinking process itself is worth preserving (unusual), keep it but link to the promoted notes

### Creating Notes

1. **Always use YAML frontmatter** with at minimum `date`, `description` (~150 chars), `tags`, and type-specific fields. Work notes also need `project` and optionally `github_issue`. Deploy notes need `project`. Reference notes may include `rails_version` or `ruby_version`.
2. **Use templates** from `templates/`. Fill `{{placeholders}}` with real values.
3. **Place files correctly**:
   - **Project work notes** -- `work/projects/<name>/notes/`
   - **Project decisions** -- `work/projects/<name>/decisions/`
   - **Project README** -- `work/projects/<name>/README.md`
   - **Completed projects** -- `work/archive/<name>/` (entire folder)
   - **Performance / brag entries** -- `perf/Brag Doc.md` (append to running log)
   - **People** -- `org/people/`
   - **Teams** -- `org/teams/`
   - **Claude operational context** -- `brain/`
   - **Compliance reference** -- `reference/compliance/`
   - **Deploy runbooks** -- `reference/ops/`
   - **Infrastructure notes** -- `reference/infrastructure/`
   - **Drafts** -- `thinking/`
   - Vault root: `Home.md`, `CLAUDE.md`, `vault-manifest.json`, `CHANGELOG.md`, `CONTRIBUTING.md`, `README.md`, `LICENSE`, `.gitignore`. No user notes at root.
4. **Name files descriptively.** Use the note title as filename.

### Note Types

| Type | Location | Naming | Key Sections |
|------|----------|--------|--------------|
| Project README | `work/projects/<name>/README.md` | `README.md` | Overview, Stack, Status, Links, Key Decisions |
| Work note | `work/projects/<name>/notes/` | Descriptive title | Context, What/Why, Links, Related |
| Decision record | `work/projects/<name>/decisions/` | `NNN-descriptive-title.md` (auto-numbered) | Context, Decision, Consequences, Related |
| Deploy note | `work/projects/<name>/notes/` or `reference/ops/` | Descriptive title | Pre-deploy, Steps, Post-deploy, Rollback |
| Person note | `org/people/` | Full name | Role & Team, Relationship, Key Moments, Notes |
| Team note | `org/teams/` | Team name | Members, Scope, Interactions |
| Compliance note | `reference/compliance/` | Descriptive title | Requirements, Implementation, Audit Trail |
| Infrastructure note | `reference/infrastructure/` | Descriptive title | Specs, Access, Maintenance, Related |
| Brain note | `brain/` | Topic name | Topic-specific content |

### Linking -- This Is Critical

**Graph-first, not folder-first.** Folders help browse in the sidebar. Links help discover through connections. Both matter, but links are the primary organizational tool.

**A note without links is a bug.** When creating a note, the FIRST thing to do after writing content is add wikilinks. Every new note must link to at least one existing note.

**Atomicity rule**: Before writing or appending to any note, ask: "Does this cover multiple distinct concepts that could be separate nodes?" If a note has or would have 3+ independent sections that don't need each other to make sense, split into atomic notes that link to each other.

Note types have graph roles:
- **Evidence nodes** (work notes, deploy notes): add outbound links to concepts they relate to
- **Concept nodes** (patterns, compliance rules): stay definitional -- evidence arrives via backlinks
- **Index nodes** (Index, Brag Doc, Memories, People & Context): actively curate links -- they're navigational
- **Person nodes** (org/people/): link to projects, teams. Receive backlinks from work notes.
- **Project READMEs**: hub nodes -- link to all decisions, key notes, people, and reference material for that project

Link syntax:
- `[[Note Title]]` -- standard wikilink
- `[[Note Title|display text]]` -- aliased link
- `[[Note Title#Heading]]` -- deep link to section
- `![[Note Title]]` -- embed content inline
- `[[Note Title#^block-id]]` -- link to specific block

#### When to Link

- **Work note <-> Decision**: bidirectional links
- **Work note -> Project README**: every work note links back to its project README
- **Work note -> Team**: in `## Related`, link to team(s) involved
- **Work note -> Person**: link people involved (PIs, collaborators, IT contacts)
- **Project README -> Reference**: link to relevant compliance, ops, or infrastructure notes
- **Brag Doc -> Work note**: every entry links to evidence
- **Memories -> Source**: every memory links to where it was learned
- **Index -> Everything**: `work/Index.md` links to all project READMEs
- **North Star -> Projects**: active focus areas link to project READMEs

### Maintaining Indexes

Update these when creating or archiving notes:

- **`work/Index.md`** -- add to Active Projects or Recent Notes, move completed to Archive
- **`brain/Memories.md`** -- index of memory topics. Add new memories to the relevant topic note, not here.
- **`brain/Skills.md`** -- register vault-specific workflows and slash commands
- **`org/People & Context.md`** -- update when people, teams, or org structure changes
- **`perf/Brag Doc.md`** -- append wins with links to evidence (flat running log, no sub-notes)

### Decision Records

1. Create in `work/projects/<name>/decisions/` using the Decision Record template (use `/decision` for auto-numbering)
2. Link from the work note(s) that led to the decision
3. Link from the project README
4. Add to the Decisions Log table in `work/Index.md`
5. If significant, note in `brain/Key Decisions.md`

### Wins & Achievements

When significant work is completed, append to `perf/Brag Doc.md` with links to the work note(s). Keep it a flat running log -- no quarterly sub-notes.

## North Star

`brain/North Star.md` is a living document of goals and focus areas.

- **Read it** at the start of substantial sessions
- **Reference it** when suggesting priorities or trade-offs
- **Update it** when the user signals a shift in goals
- Both the user and Claude write to it

## Tags Convention

Use tags in frontmatter (not inline):

- **Type**: `work-note`, `decision`, `project`, `deploy`, `compliance`, `thinking`, `brain`, `reference`, `person`, `team`
- **Index**: `index`, `moc`
- **Status** (frontmatter field): `active`, `completed`, `archived`, `proposed`, `accepted`, `deprecated`
- **Team** (frontmatter field on people + work notes): your team names, e.g. `Research IT`, `Lab Systems`
- **Project** (frontmatter field): project name, matching the folder name in `work/projects/`

## Properties for Querying

Beyond tags, use these frontmatter properties to enable search and Bases views:

- `project: "my-project"` -- find all notes for a project (matches folder name in `work/projects/`)
- `github_issue: 123` -- link vault note to a GitHub issue number. Not every issue needs a note -- only significant ones.
- `status: active` -- find active projects and notes
- `team: "Research IT"` -- find all notes related to a team
- `rails_version: "8.0"` -- Rails version relevant to a note or project
- `ruby_version: "3.3"` -- Ruby version relevant to a note or project

## Memory System

**All project memories live in the vault.** The `~/.claude/` MEMORY.md is an auto-loaded index that points to vault locations. The `~/.claude/` MEMORY.md is the only file that should exist there -- it is an auto-loaded index. Never create additional memory files in that directory.

| System | Location | Purpose |
|--------|----------|---------|
| **MEMORY.md** | `~/.claude/projects/.../memory/MEMORY.md` | Auto-loaded index only. Pointers to vault notes. |
| **Vault memories** | `brain/` topic notes | Git-tracked, Obsidian-browsable, linked. All durable knowledge lives here. |

When asked to "remember" something:
1. Find or create the appropriate `brain/` topic note (Gotchas, Patterns, Key Decisions, etc.)
2. Add the knowledge there with a wikilink to context
3. Update `brain/Memories.md` index if a new topic note was created
4. Do NOT create additional files in `~/.claude/projects/.../memory/` beyond MEMORY.md -- they are not version-controlled

## Agent Guidelines

### Graph-First Thinking

- **Folders group by purpose, links group by meaning.** A note lives in ONE folder (its home) but links to MANY notes (its context).
- When creating a note, add wikilinks FIRST. A note without links is a bug.
- Prefer bidirectional links: if A links to B, B should link back to A (unless B is a concept node that receives backlinks passively).
- Before creating a new subfolder, ask: "Can I solve this with a tag, a property, or a link instead?" Folders are for browsing convenience, not for categorization.
- After every substantial session, verify new notes have at least one inbound link.

### Project-Centric Organization

Everything revolves around `work/projects/<name>/`. Each project is a self-contained folder:

```
work/projects/my-app/
  README.md          # Project overview, stack, status, links
  decisions/         # ADRs: 001-choice.md, 002-choice.md, ...
  notes/             # Work notes, deploy notes, issue captures
```

When starting a new project, create the folder structure and README first. The README is the hub node -- it links to everything related to the project.

### Where to Put Things

- **Writing about a person?** -- `org/people/` (PIs, IT contacts, collaborators -- not direct reports)
- **Writing about a team?** -- `org/teams/`
- **Writing about how the codebase works?** -- `brain/` (Patterns, Gotchas, Key Decisions)
- **Writing about what Claude should remember?** -- `brain/Memories.md` topic notes
- **Tracking active project work?** -- `work/projects/<name>/notes/`
- **Recording a technical decision?** -- `work/projects/<name>/decisions/` (use `/decision`)
- **Capturing a GitHub issue?** -- `work/projects/<name>/notes/` (use `/issue-capture`)
- **Writing deploy procedures?** -- `reference/ops/` for shared runbooks, project `notes/` for project-specific
- **Writing compliance notes?** -- `reference/compliance/` (HIPAA, IRB, regulatory)
- **Writing infrastructure notes?** -- `reference/infrastructure/` (servers, networks, environments)
- **Dumping unstructured info?** -- use `/dump` to auto-classify and route everything

### Don't Mix Contexts

When capturing information from different sources:
- **Project work** (code decisions, deploys, issue resolution) -- goes to the relevant `work/projects/<name>/` folder
- **Compliance and regulatory** (HIPAA, IRB, audit requirements) -- goes to `reference/compliance/`
- **Operational knowledge** (deploy steps, server access, environment setup) -- goes to `reference/ops/` or `reference/infrastructure/`
- **People and stakeholders** (PI preferences, IT contacts, collaborator notes) -- goes to `org/people/`
- **Cross-project patterns** (recurring technical decisions, gotchas) -- goes to `brain/`

### GitHub Issues Integration

The `github_issue` frontmatter property links vault notes to GitHub issues. Guidelines:

- **Not every issue needs a vault note.** Only create notes for significant issues -- ones involving design decisions, compliance implications, or multi-session work.
- Use `/issue-capture` to scaffold a note from a GitHub Issue URL with pre-filled frontmatter.
- The `github_issue` property stores the issue number (not the full URL) for Bases queries.

## Subagents

Specialized agents in `.claude/agents/` for heavy operations. They run in isolated context windows.

| Agent | Purpose | Invoked by |
|-------|---------|------------|
| `context-loader` | Loads all vault context about a person, project, or concept | `/context-switch`, Direct |
| `cross-linker` | Finds missing wikilinks, orphans, broken backlinks | `/vault-audit` |
| `vault-librarian` | Deep vault maintenance -- orphans, broken links, stale notes | `/vault-audit` |
| `vault-migrator` | Classifies, transforms, and migrates content from a source vault | `/vault-upgrade` |

## Hooks

Five lifecycle hooks in `.claude/settings.json`:

| Hook | When | What |
|------|------|------|
| SessionStart | On startup/resume | QMD re-index, inject North Star, project list, recent changes, tasks, file listing |
| UserPromptSubmit | Every message | Classifies content (decision, win, architecture, person context, project update, project switch, deploy, compliance) and injects routing hints |
| PostToolUse | After writing `.md` | Validates frontmatter, checks for wikilinks, verifies folder placement, validates `project:` in frontmatter for `work/projects/` notes |
| PreCompact | Before context compaction | Backs up session transcript to `thinking/session-logs/` |
| Stop | End of every session | Lightweight checklist reminder: archive, update indexes, check orphans. For thorough review, use `/wrap-up` instead. |

## Rules

- Never modify `.obsidian/` config files unless explicitly asked.
- Preserve existing frontmatter when editing notes.
- Git sync is handled by the user's preferred method (obsidian-git, manual commits, etc.) -- don't configure git hooks or auto-commit.
- When asked to "remember" something, write to the relevant `brain/` topic note with a link to context. Never create memory files in `~/.claude/` -- they are not git-tracked.
- Prefer Obsidian CLI over filesystem when Obsidian is running.
- **Always invoke Obsidian skills via the Skill tool** before doing vault work. Load `obsidian-markdown` when creating/editing `.md` files. Load `obsidian-cli` when running vault commands. Load `obsidian-bases` or `json-canvas` when working with those file types.
- Always check for and suggest connections between notes.
- Every note must have a `description` field (~150 chars). Claude fills this automatically.
- **Zero data loss**: when reorganizing, always use `git mv`. Never delete without explicit user confirmation.
