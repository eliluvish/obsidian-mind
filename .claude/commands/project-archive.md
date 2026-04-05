# Project Archive

Move a completed project from `work/projects/` to `work/archive/` and update all indexes.

## Usage

```
/project-archive <project name>
```

## Workflow

### 1. Find the Project

Search `work/projects/` for the project name. Confirm with the user before proceeding.

### 2. Update Frontmatter

- Set `status: completed` on the project's `README.md`
- Verify `description` reflects the final state
- Update status on any remaining active work notes and decisions

### 3. Move the Project

```bash
git mv "work/projects/<project-name>" "work/archive/<project-name>"
```

### 4. Update Indexes

- **`work/Index.md`**: Move from Active Projects to Archive section
- **`brain/North Star.md`**: Mark as completed in Current Focus if listed there
- **`perf/Brag Doc.md`**: Verify the project's key accomplishments are captured
- **`brain/Memories.md`**: Update if the project is mentioned as "in progress"

### 5. Verify

- Run a quick check that no wikilinks are broken (Obsidian resolves by name, so moves shouldn't break links)
- Confirm the Projects Base shows the project with `status: completed`
- Confirm the Work Dashboard Base no longer shows the project's notes in "Active Work"

## Important

- Always use `git mv` — never copy+delete
- Don't archive without user confirmation
- The entire project folder moves together (README, decisions, notes)
