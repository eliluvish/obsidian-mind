---
description: "Pull up the deploy runbook for a project, walk through pre/post-deploy checks."
---

# Deploy Checklist

Interactive deploy companion. Loads the project's deploy runbook and walks through each step.

## Usage

```
/deploy-checklist <project name>
```

## Workflow

### 1. Find the Project

Search `work/projects/` for the project name. Read its `README.md` for deploy info.

### 2. Find Runbook

Look for a deploy runbook in these locations (in order):
1. `reference/ops/<project-name>-deploy.md`
2. `reference/ops/<project-name>.md`
3. Deploy section in `work/projects/<name>/README.md`

### 3. If Runbook Exists

Present the checklist interactively:

**Pre-Deploy**:
- [ ] All tests passing?
- [ ] Migrations reviewed? (if any)
- [ ] Environment variables set?
- [ ] Project-specific pre-deploy steps from runbook

**Deploy**:
- Deploy command from runbook
- Expected deploy time

**Post-Deploy**:
- [ ] Smoke test URLs from runbook
- [ ] Check logs for errors
- [ ] Verify migrations ran
- [ ] Project-specific post-deploy steps from runbook

### 4. If No Runbook Exists

Offer to create one:
- Ask the user for deploy method (Capistrano, Docker, manual, etc.)
- Ask for production/staging URLs
- Ask for smoke test endpoints
- Ask for any special pre/post steps
- Create at `reference/ops/<project-name>-deploy.md`
- Link from the project README

### 5. Log the Deploy

After deployment, offer to create a brief work note in `work/projects/<name>/notes/YYYY-MM-DD-deploy.md` capturing:
- What was deployed (version, key changes)
- Any issues encountered
- Post-deploy verification status

## Important

- This is a guide, not automation. The user runs the actual deploy commands.
- If the project has compliance notes (HIPAA, IRB), surface them prominently before deploy.
- Always check for pending migrations — they're the #1 source of deploy issues.
