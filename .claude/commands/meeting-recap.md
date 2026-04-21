---
description: "Capture a meeting transcript — parse speakers, decisions, and action items into a meeting note with optional ADR and work note extraction."
---

# Meeting Recap

Turn a raw meeting transcript into a structured meeting note. Companion to `/meeting-prep` — that command preps *before* a meeting, this one captures *after*.

## Usage

```
/meeting-recap <project> [--with "Name1, Name2"]
```

The transcript is passed as the dump content after the command. Supports auto-generated transcripts (Teams, Zoom, Otter) and manual notes.

Examples:
- `/meeting-recap pcms` then paste the transcript
- `/meeting-recap ilog --with "Kele Piper, Mirabella Daguerre"` then paste

## Workflow

### 1. Validate Project

Check `work/projects/<project>/` exists. If not, list available projects and stop.

### 2. Load Meeting Context

- Read `work/projects/<project>/README.md` — pull stakeholders and `meetings:` metadata
- If `--with` passed, use that attendee list. Otherwise infer from speakers in the transcript + the README's meeting metadata.
- For each attendee, read `org/people/<Name>.md` for context on their role and relationship
- Read the last 3-5 notes in `work/projects/<name>/notes/` for recent project context

### 3. Parse the Transcript

Identify from the raw text:
- **Speakers** — match against known people in `org/people/`. Flag unknown speakers.
- **Topics discussed** — cluster related exchanges into coherent topics
- **Decisions made** — anything where the group reached agreement ("we decided", "let's go with", "that works", consensus moments)
- **Action items** — anything someone committed to doing ("I'll", "can you", "we need to", task assignments)
- **Open questions** — unresolved items, things deferred to next meeting
- **Wins / positive signals** — user satisfaction, positive feedback, things going well

### 4. Search for Related Notes

For each identified topic:
- Grep `work/projects/<project>/notes/` for related existing notes
- Check if a decision already has an ADR in `work/projects/<project>/decisions/`
- Prefer **appending** to existing notes over creating new ones for small updates

### 5. Create the Meeting Note

- Path: `work/projects/<project>/notes/YYYY-MM-DD Meeting — <project>.md`
- Use `templates/Meeting Note.md`
- Fill in:
  - **Attendees** with wikilinks to person notes; mark absent regulars if identifiable
  - **Since Last Meeting** — leave empty or link to the `/meeting-prep` note if one exists for today
  - **Discussion** — synthesized summary of each topic, NOT a verbatim transcript dump. Write it like meeting minutes: what was discussed, what positions were taken, what was resolved. Link to relevant existing notes.
  - **Decisions** — each decision as a bullet with enough context to understand it standalone
  - **Action Items** — checklist with assignee wikilinks and specific deliverables
- Add `## Open Questions` if unresolved items were identified

### 6. Promote Significant Decisions

If a decision is architecturally significant (changes how systems interact, sets a precedent, has compliance implications):
- Offer to create an ADR via `/decision`
- Link the ADR from the meeting note
- Add to `brain/Key Decisions.md` if cross-project

### 7. Promote Work Items

If a new feature or task was discussed that doesn't already have a work note:
- Offer to create a work note in `work/projects/<project>/notes/`
- Pre-fill with context from the transcript discussion
- Link from the meeting note

### 8. Update Indexes

- Add the meeting note to `work/Index.md` Recent Notes
- Add any new ADRs to `work/Index.md` Decisions Log
- Update existing notes if new information emerged (e.g., status changes, new context)
- Update person notes in `org/people/` if new Key Moments or relationship context surfaced

### 9. Cross-Link

Ensure:
- Meeting note links to all notes referenced in discussion
- Meeting note links to all attendees and the project README
- Any new notes created link back to the meeting note
- No orphans

### 10. Present Summary

Report to the user:
- **Topics captured** — bulleted list of what was discussed
- **Decisions** — with status (accepted, proposed, deferred)
- **Action items** — with assignees
- **Notes created or updated** — paths
- **Promotions offered** — decisions or work items that could become standalone notes/ADRs
- **Unknown speakers** — names from the transcript not in `org/people/`

## Important

- **Synthesize, don't transcribe.** The meeting note should be readable as minutes, not a copy-paste of the raw transcript. Strip filler words, timestamps, and repetition.
- **Attribute decisions and action items.** Every decision should say who was involved. Every action item needs an assignee wikilink.
- **Respect the grapevine.** If the user says information is unconfirmed or heard secondhand, mark it accordingly in the notes (see `brain/Gotchas.md` for precedent).
- If a meeting note for today already exists (from `/meeting-prep`), **merge into it** rather than creating a duplicate. Fill in the Discussion/Decisions/Action Items sections that `/meeting-prep` left empty.
- **Ask before creating ADRs or work notes.** Offer to promote, don't auto-create. The user decides what's worth a standalone note.
