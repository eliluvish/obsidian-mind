---
description: "Freeform capture mode. Dump anything — conversations, decisions, wins, thoughts — and I'll route it all to the right notes with proper templates, frontmatter, and wikilinks."
---

Process the following freeform dump. For each distinct piece of information:

1. **Classify** it: decision, win/achievement, architecture, project update, person context, compliance note, deploy note, or general work note.
2. **Search first**: Use `qmd vsearch` (or `obsidian search` if QMD unavailable) to check if a related note already exists. Prefer appending to existing notes over creating new ones for small updates.
3. **Determine project**: If the content relates to a specific project, identify which `work/projects/<name>/` it belongs to.
4. **Create or update** the appropriate note following CLAUDE.md conventions:
   - Correct folder placement:
     - Work notes → `work/projects/<name>/notes/`
     - Decisions → `work/projects/<name>/decisions/`
     - People context → `org/people/`
     - Compliance/deploy info → `reference/compliance/` or `reference/ops/`
     - Cross-project brain knowledge → `brain/`
   - Full YAML frontmatter with date, description, tags, project, and type-specific fields
   - All relevant [[wikilinks]] to people, projects, other notes
5. **Update indexes** as needed (work/Index.md, org/People & Context.md)
6. **Cross-link**: Ensure every new note links to at least one existing note and is linked FROM at least one existing note.

After processing everything, provide a summary:
- What was captured and where each piece was filed
- Any new notes created (with paths)
- Any existing notes updated
- Any items you weren't sure how to classify (ask the user)

Content to process:
$ARGUMENTS
