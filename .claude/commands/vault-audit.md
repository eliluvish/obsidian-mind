# Vault Audit

Deep structural audit of the vault. Checks indexes, folder placement, frontmatter, links, Bases, and consistency. Fix what can be fixed, flag what needs user input.

**When to use**: After substantial sessions, after reorganization, or periodically to maintain vault health. For lighter end-of-session checks, use `/wrap-up` instead.

## Usage

```
/vault-audit
```

## Subagents

This command orchestrates two subagents for deep analysis:
- **`vault-librarian`** — orphan detection, broken links, frontmatter validation, stale notes, index consistency
- **`cross-linker`** — finds missing wikilinks, orphan notes, broken backlinks

Launch `vault-librarian` first for the structural audit, then `cross-linker` for link quality.

## Workflow

### 1. Check Folder Structure

Verify the vault matches the expected layout:
- `Home.md` exists at vault root
- `bases/` contains all `.base` files (none scattered elsewhere)
- `work/projects/` contains project folders, each with `README.md`, `decisions/`, `notes/`
- `work/archive/` contains completed/sunset project folders
- `org/people/` contains only notes tagged `person`
- `org/teams/` contains only notes tagged `team`
- `reference/compliance/`, `reference/ops/`, `reference/infrastructure/` exist
- `templates/` contains only template files (with `{{placeholders}}`)
- `thinking/` is clean (no leftover drafts that should have been promoted)
- Nothing unexpected at vault root (allowed: `Home.md`, `CLAUDE.md`, `vault-manifest.json`, `CHANGELOG.md`, `CONTRIBUTING.md`, `README.md`, `LICENSE`, `.gitignore` — no user notes)

### 2. Check Indexes

Read and verify each index file:
- `Home.md` — do embedded Base views reference existing Bases? Are quick links valid?
- `work/Index.md` — are active projects listed? Are archived projects in the right section? Any missing notes?
- `brain/Memories.md` — any stale claims?
- `org/People & Context.md` — are roles and contacts current?
- `perf/Brag Doc.md` — do entries match reality?
- `brain/Skills.md` — are all slash commands registered? Workflows still valid?

### 3. Check Frontmatter Completeness

For each note type, verify required properties:

**Project READMEs** (`work/projects/*/README.md`):
- Required: `date`, `project`, `description`, `status`, `tags: [project]`
- Recommended: `rails_version`, `ruby_version`

**Work notes** (`work/projects/*/notes/`):
- Required: `date`, `description`, `project`, `status`, `tags: [work-note]`
- Optional: `github_issue`

**Decision records** (`work/projects/*/decisions/`):
- Required: `date`, `description`, `project`, `status`, `tags: [decision]`

**Person notes** (`org/people/`):
- Required: `date`, `title`, `description`, `tags: [person]`
- Optional: `team`

**Team notes** (`org/teams/`):
- Required: `date`, `description`, `tags: [team]`

**Brain notes** (`brain/`):
- Required: `description`, `tags: [brain]`

### 4. Check for Duplicate Tags

Scan all notes for duplicate entries in the `tags` array. Fix any found.

### 5. Check Status/Folder Alignment

- Projects in `work/projects/` should have `status: active`
- Projects in `work/archive/` should have `status: completed`

### 6. Check Bases

For each `.base` file in `bases/`:
- Do filters still match the expected notes?
- Are templates excluded where relevant?
- Do referenced properties exist in the target notes?

### 7. Check for Orphans

- Are there work notes not linked from their project's README or `work/Index.md`?
- Are there people notes not linked from `org/People & Context.md`?
- Are there notes without any inbound links at all?
- Are there thinking notes that should have been promoted or deleted?

### 8. Check Links

- Scan for wikilinks that reference notes that don't exist (broken links)
- Check that bidirectional links exist where expected
- Verify `## Related` sections aren't empty on work notes

### 9. Check for Stale Context

- Read `brain/Memories.md` — is anything outdated?
- Read `org/People & Context.md` — any contacts that changed?
- Check `brain/Key Decisions.md`, `brain/Patterns.md`, `brain/Gotchas.md` for outdated claims
- Check `brain/North Star.md` — does Current Focus reflect reality?

### 10. Check Claude Config

- `.claude/settings.json` — are hooks well-formed and referencing correct paths?
- `.claude/commands/` — do all commands reference correct folder structure?
- `CLAUDE.md` — any stale instructions that contradict current vault state?

### 11. Fix and Report

- Fix what's clearly wrong (broken links, missing frontmatter, duplicate tags, wrong folder)
- For ambiguous issues, list them and ask the user
- Summarize:
  - **Fixed**: issues resolved
  - **Flagged**: needs user input
  - **Suggested**: improvements for the vault

## Important

- Don't delete anything without asking
- Don't create new notes during audit — just fix existing ones
- Preserve existing frontmatter when editing
- If a note is in the wrong folder, move it with `git mv`
- Use parallel agents for large audits
