# Wrap Up

Full session review before ending. Review context, ways of working, files modified, consistency, and suggest improvements.

## Usage

```
/wrap-up
```

Triggered when the user says "wrap up", "let's wrap", "wrapping up", or similar. Claude should invoke this automatically.

## Workflow

### 1. Review What Was Done

Scan the conversation for:
- Notes created or modified (list them all with paths)
- Indexes updated
- Brain notes updated (Patterns, Gotchas, Key Decisions, Memories)
- Project READMEs updated
- PRs merged today completed today across all projects
- Github issues completed today across all projects

### 2. Verify Note Quality

For each note created or modified this session:
- Frontmatter complete? (`date`, `description`, `tags`, `project`, type-specific fields)
- At least one wikilink to another note?
- In the correct folder? (`work/projects/<name>/notes/` vs `work/projects/<name>/decisions/` etc.)
- Description accurate and ~150 chars?
- Status field correct?

### 3. Check Index Consistency

- `work/Index.md` — are new notes linked? Are completed projects in the right section?
- `brain/Memories.md` — does it reflect what happened this session?
- `org/People & Context.md` — any new people or relationship changes to capture?
- `Home.md` — are embedded Bases still valid?

### 4. Check for Orphans

- Any new notes not linked from at least one other note?
- Any thinking notes that should be promoted or deleted?

### 5. Archive Check

- Are there projects in `work/projects/` that should be moved to `work/archive/`?
- Any status fields still `active` that should be `completed`?

### 6. Ways of Working Review

Check if this session revealed:
- A new pattern that should be in `brain/Patterns.md`?
- A new gotcha that should be in `brain/Gotchas.md`?
- A workflow improvement for `brain/Skills.md`?
- A CLAUDE.md update needed (new convention, stale reference)?
- A new or improved slash command?
- A hook that should be added or modified?

### 7. Suggest Improvements

Based on how the session went:
- Were there friction points in the workflow?
- Did we do something manually that could be automated?
- Did we repeat a pattern that should be a skill?
- Are there Bases that should be created or updated?
- Any frontmatter properties that would help future queries?

### 8. Offer to Record Time

Review the session's completed work across all projects — issues closed, PRs merged, notes written, decisions made, meetings captured — and offer to record time entries. Use the `/time-entry-writing` skill to generate administrator-friendly descriptions from the session's git activity and conversation context, then present the proposed entries via the `recording-time` skill for confirmation and submission.

### 9. Report

Present a concise summary:
- **Done**: what was captured this session
- **Fixed**: issues found and resolved
- **Flagged**: things that need user input
- **Suggested**: improvements for next time

## Important

- This is a READ + VERIFY pass, not a creation pass. Fix small issues (broken links, missing frontmatter), but flag larger changes for user approval.
- Be honest about what's missing — the goal is leaving the vault in a better state than you found it.
- If North Star goals shifted during the session, suggest updating it.
