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
7. Check recent **vault** git activity: `git log --oneline --since="24 hours ago" --no-merges`
8. Check recent **code** activity not yet in the vault. For each repo in the config map in `.claude/agents/repo-scanner.md` (single source of truth for repo→project mapping), run a cheap inline sweep — `git -C ~/dev/<repo> log --oneline --no-merges --since=<date of that project's last `chore(vault): … sync` commit, else "7 days ago">`. This is a lightweight signal only — do **not** dispatch the `repo-scanner` subagent here.
9. Check for any unlinked notes or inbox items needing processing
10. Check open pull requests across all projects
11. Check **new issues** created in the lookback window across the mapped project repos. Pick the window from today's weekday: **Monday → 72h**, **Sunday → 48h**, **Tue–Sat → 24h**. Compute the cutoff date, then for each repo in the config map in `.claude/agents/repo-scanner.md` run `gh issue list -R <remote> --state open --json number,title,createdAt,assignees --search "created:>=<cutoff>"`, using the GitHub remote from that map's table (the `csb-ric/…` column) and attributing issues to the mapped project. Surface **all** new issues regardless of assignee; mark which are assigned to you.

Present a structured standup summary:
- **Yesterday**: What got done (from vault git log and daily note)
- **Projects**: Status of each active project in `work/projects/`, noting recent notes and open decisions
- **Uncaptured code work**: per-project, the count + one-line gist of code commits not yet reflected in vault notes. For any project with meaningful activity, suggest `/repo-sync <repo> since last-sync` to synthesize and tie it in. Don't capture it here — just flag it.
- **New issues**: new issues in the lookback window, grouped by project, each with number/title and an "(assigned to you)" marker where applicable. For significant ones (design decisions, compliance, multi-session work) suggest `/issue-capture <url>` to scaffold a note. State the window used (e.g. "72h — Monday").
- **Open Tasks**: Pending items
- **North Star Alignment**: How active work maps to current goals
- **Suggested Focus**: What to prioritize today based on goals + open items

Keep it concise. This is a quick orientation, not a deep dive — the sweeps are flags; `/repo-sync` and `/issue-capture` are the drill-downs.
