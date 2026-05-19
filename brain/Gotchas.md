---
description: "Things that have bitten before and will bite again — pitfalls, edge cases, and testing traps"
tags:
  - brain
---

# Gotchas

Things that have bitten before and will bite again.

## PCMS

### PCMS calendar_events API now scoped by core (commit 60b8ae3)

> [!success] Resolved & deployed (2026-05-18)
> Cross-core SR scoping fixed and shipped to production. Calendar is now an active focus area — see [[Calendar Refactor and Drag-Drop Proposal]].

`Api::CalendarEventsController#create` (pcms commit `60b8ae3`, 2026-05-11) added `before_action :load_service_request` that calls `ServiceRequest.find(params[:service_request_id])`. Because `ServiceRequest` includes `CoreScopable` (`default_scope { where(core_lab_id: Thread.current[:current_core].id) }`), the find only resolves SRs in the **current core** (e.g. `bic` when routed via `/api/bic/...`). Cross-core SRs raise `RecordNotFound` → 404.

**Why**: Pre-commit, the controller never loaded the SR — it just assigned `current_core.id` to `core_lab_id` and used `params[:service_request_id]` as a write-only field. So the bic-scoped time-tracking API accepted any SR ID. After the commit, only SRs already inside the bic core resolve. This silently broke the `recording-time` skill for projects whose tracking SR lives in a different core (PCMS SR `16131` was the symptom).

**How to apply**:
- Fix in pcms: `ServiceRequest.unscoped.find(params[:service_request_id])` in `load_service_request`. Add a spec covering a cross-core SR ID.
- When reviewing diffs that add `.find` calls on `CoreScopable` models, ask: is this lookup expected to cross core boundaries? If yes, `.unscoped`.
- The RCMS calendar API will return a bare `{}` with status 404 when the SR isn't visible — not 422 — so a 404 from `/api/bic/calendar_events` POST is most likely an SR-scope mismatch, not a route/auth issue.

## RPR

### Participant email is shared across all of a participant's studies

RPR stores **one email per participant**, not one per study-participant enrollment. A participant enrolled in two studies has a single email record. Editing the email from one study **silently mutates it for every other study** the participant is in.

**Why**: This caused a real incident — a non-BEHOLD user changed a shared participant's email, misrouting a gift card on study #2022P000780. A prior "additional email check" was believed to prevent cross-study changes but does not cover this path. See [[Cross-Study Email Mutation Incident]].

**How to apply**:
- Any change to participant email handling in `study_pay` affects all of that participant's studies — never assume edits are study-scoped.
- The proposed fix is email-per-study (per enrollment) while keeping records tied to one underlying participant — pending [[Gala Laffey]] decision and a future `rpr/decisions/` ADR.
- When auditing access: a user not on a study being able to edit that study's participant payment data is the access-scope question to chase, separate from the data-model fix.

## Stakeholder Communication

### Kele Piper doesn't always loop Eli in on iLog events

[[Kele Piper]] has at least once planned an iLog-related public event (the ARC demo on 2026-04-30 — see [[ARC Group iLog Demo]]) without telling Eli directly. Eli heard about it through the grapevine.

**Why**: Information about demos, audits, and compliance-facing events can reach Eli late — late enough to cause prep scrambles if he finds out close to the date.

**How to apply**:
- Don't wait to be told about upcoming iLog events. Assume gaps in the communication channel.
- **Eli prefers to track quietly rather than confront.** When grapevine intel lands, file it, prepare accordingly, but don't surface the source with Kele or other stakeholders. No "I heard you're doing X" conversations.
- Periodically (e.g. at weekly review), ask open-ended questions that invite Kele to volunteer upcoming plans — "anything coming up for iLog?" — without revealing what you already know.
- On iLog work, default to "demo-ready" quality earlier than you otherwise would, because a surprise event may land at any time.

## Vault Tooling

### Hook scripts assume project-root cwd — must `cd "$CLAUDE_PROJECT_DIR"`

The hooks in `.claude/settings.json` invoke scripts by **relative path** and the scripts themselves read by relative path (`session-start.sh`: `cat brain/North Star.md`, `for proj in work/projects/*/`, `find . -name "*.md"`). A hook does not necessarily run from the vault root — in a multi-working-directory session, `PostToolUse` fires from whatever cwd the edited file belongs to, producing `bash: .claude/scripts/find-python.sh: No such file or directory` (non-blocking, so frontmatter/wikilink validation silently stops running).

**Why**: Fixed 2026-05-18 (commit `8de602f`) by prefixing every hook with `cd "$CLAUDE_PROJECT_DIR" &&`. `pre-compact.sh` line 14 already used `${CLAUDE_PROJECT_DIR:-$(pwd)}` — evidence the intended contract was always "run from vault root," just not enforced uniformly.

**How to apply**:
- Any new hook added to `.claude/settings.json` must start with `cd "$CLAUDE_PROJECT_DIR" &&` (not just an absolute script path — the *scripts'* internal reads are cwd-relative, so an absolute launch path alone still produces silently-wrong output, not an error).
- A bare `find-python.sh: No such file or directory` from a hook is a cwd problem, not a missing file — check `.claude/scripts/` exists before assuming the script was deleted.
- The fix is invisible in the running session until settings reload (`/clear` or restart); changed hook commands may also prompt re-approval.
- See the Hooks table and the `cd "$CLAUDE_PROJECT_DIR"` rationale in [[CLAUDE]].
