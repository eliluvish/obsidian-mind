---
description: "Weekly synthesis — cross-project review of vault activity, North Star alignment, patterns, and forward priorities."
---

Cross-session synthesis of the past week. Bridges daily standup (lightweight) and long-term planning. This is ANALYSIS, not verification — find patterns, surface drift, detect uncaptured work.

## Workflow

### 1. Gather Week's Activity

Automated — no user input needed:

- `git log --since="7 days ago" --oneline --no-merges` — all vault changes
- List all notes modified in the past 7 days (git + filesystem)
- Scan each `work/projects/*/notes/` for new or updated work notes
- Scan each `work/projects/*/decisions/` for new ADRs
- Read today's daily note if it exists: `obsidian daily:read`

### 2. North Star Alignment

Read `brain/North Star.md` and compare actual activity against stated focus:

- **Aligned work**: which Current Focus items got attention this week?
- **Drift**: work that doesn't map to any stated goal (not necessarily bad — flag it)
- **Silent goals**: focus items with zero commits, zero note updates, zero mentions
- **Emerging themes**: work patterns suggesting a focus shift that hasn't been written down yet

### 3. Cross-Project Patterns

Look across the week's notes for:
- Recurring themes (same topic in multiple projects)
- Multiple issues touching the same system or library
- Context that evolved across sessions (decisions that shifted, understanding that deepened)
- Deployment activity or production issues

### 4. Per-Project Summary

For each active project in `work/projects/`:
- What shipped this week?
- What's stuck or blocked?
- Any pending decisions?
- Any compliance or deploy concerns flagged?

### 5. Uncaptured Win Detection

Check:
- Were completed items logged in `perf/Brag Doc.md`?
- Any significant bug fixes, feature deliveries, or firefighting not captured?
- Any wins from git log that don't have corresponding work notes?

### 6. Forward Look

- Blocked items or upcoming deadlines from active work notes
- North Star goals that need attention next week
- Suggested priority ordering for next week based on goals + momentum + gaps
- Any projects that have been quiet and may need attention

### 7. Present Synthesis

Structure the output as:

- **This Week**: 3-5 bullet summary of what actually happened
- **North Star Check**: alignment status — what's on track, what drifted, what's silent
- **Per Project**: compact status for each active project
- **Patterns**: cross-project themes worth noting
- **Uncaptured Wins**: anything that should be in the brag doc
- **Next Week**: suggested priorities and attention areas

After presenting, offer:
- "Want me to add any of these wins to the brag doc?"
- "Should I update North Star with any focus shifts?"
- "Want me to update `work/Index.md`?"
- "Want me to save this as `thinking/weekly-YYYY-MM-DD.md`?"

## Important

- This is transient analysis by default — do NOT create a file unless the user asks.
- Keep the tone analytical, not cheerful. This is a status check, not a celebration.
- Be honest about drift and silent goals — the value is in surfacing what's NOT happening, not just what is.
- Don't duplicate standup (daily, what's next) or wrap-up (session, verify quality). This is SYNTHESIS across days.
- If it was a light week (few commits, no new notes), say so. Don't pad the analysis.
