---
description: "Morning kickoff. Load today's context, review yesterday, surface open tasks, and identify priorities."
---

Run the morning standup:

1. Read `Home.md` for current dashboard state
2. Read `brain/North Star.md` for current goals
3. Scan `work/projects/` — list each project folder and read its `README.md` for current state
4. Read `work/Index.md` for the active projects overview
5. Read yesterday's and today's daily notes if they exist: `obsidian daily:read`
6. List open tasks: `obsidian tasks daily todo`
7. Check recent git activity: `git log --oneline --since="24 hours ago" --no-merges`
8. Check for any unlinked notes or inbox items needing processing

Present a structured standup summary:
- **Yesterday**: What got done (from git log and daily note)
- **Projects**: Status of each active project in `work/projects/`, noting recent notes and open decisions
- **Open Tasks**: Pending items
- **North Star Alignment**: How active work maps to current goals
- **Suggested Focus**: What to prioritize today based on goals + open items

Keep it concise. This is a quick orientation, not a deep dive.
