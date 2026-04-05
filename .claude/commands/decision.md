---
description: "Create an ADR in the right project's decisions/ folder with auto-numbering."
---

# Decision

Create an Architecture Decision Record scoped to a specific project.

## Usage

```
/decision <project name> <decision title>
```

If project name is omitted, ask the user which project this decision belongs to.

## Workflow

### 1. Find the Project

Search `work/projects/` for the project name. If not found, list available projects and ask.

### 2. Auto-Number

Scan `work/projects/<name>/decisions/` for existing ADRs. The next number is `max + 1`, zero-padded to 4 digits.

If no decisions exist yet, start at `0001`. Create the `decisions/` folder if needed.

### 3. Create ADR

Create at `work/projects/<name>/decisions/<number>-<slug>.md` where `<slug>` is a URL-safe version of the title.

Use the Decision Record template from `templates/Decision Record.md`:
- Fill `project:` with the project name
- Fill `date:` with today's date
- Set `status: proposed`
- Fill the title

### 4. Link It

- If there's a triggering work note or GitHub issue mentioned, add a wikilink in the Triggering Issue section
- Add a wikilink to the project README in the Related section
- Add a link from `work/Index.md` Decisions Log if one exists

### 5. Present

Show the user the created file path and open it for editing. Remind them to fill in Context, Options Considered, and Decision sections.

## Important

- ADRs start as `status: proposed`. The user changes to `accepted` when decided.
- Keep the numbering sequential within each project.
- Cross-project decisions should be noted in `brain/Key Decisions.md` as well.
