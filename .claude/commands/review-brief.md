# Generate Review Brief

Generate a performance review context transfer document from vault data. Supports manager version (manager-friendly) and peer version (project-focused).

## Usage

```
/review-brief <audience> [period]
```

Examples:
- `/review-brief manager "Q4 2025 + Q1 2026"`
- `/review-brief peers "Q4 2025 + Q1 2026"`

## Workflow

### 1. Gather Data

Read these vault sources:
- `perf/<cycle>/<cycle> Review Brief.md` (or current private brief) — full context
- `perf/Brag Doc.md` — quarterly highlights
- `perf/brag/Q*.md` — quarterly detail notes for the period
- `perf/evidence/<Your Name> PRs - *.md` — PR data
- `work/*.md` — project notes for the period
- `perf/competencies/*.md` — competency definitions
- Previous review notes for baseline comparison

### 2. Generate Content

**For manager audience:**
- Frame for a non-technical audience — outcome language, not technical jargon
- Include: The Arc (narrative), Impact at a Glance (table), Impact Details (per project), Competency Highlights (with baselines), Documentation Trail
- Replace technical terms: "deadlock" → "timing conflict", "data race" → "concurrency issue", etc.
- No wikilinks — use plain text or markdown links to external resources
- Include all documentation, issue tracker, source control, monitoring, and messaging references

**For peer audience:**
- Can be more technical but still manager-friendly (peers write reviews that go to your manager)
- Organize by project (matches your org's review tool structure)
- Include "Other things worth mentioning" for non-project work
- Casual tone — "jog your memory", "no pressure to cover everything"
- No competency section — that's for your manager

### 3. Create Files

- Markdown version in `perf/`
- HTML version with professional styling (blue theme, tables, responsive)
- PDF via Chrome headless: `--headless --no-pdf-header-footer --print-to-pdf`

### 4. Verify

- Check page breaks in PDF (render pages with pdftoppm)
- Ensure no content is cut mid-section
- Verify all links work
- Cross-check PR counts and dates against `reference/` data

## Important

- NEVER include: sensitive interpersonal details, private 1:1 talking points, peer selection strategy, personal strategic notes in shared versions
- Always maintain a private version with full context
- When updating, update BOTH private + shared versions
- Manager version: no wikilinks, non-technical language, professional formatting
- Peer version: project-focused, same manager-friendly language
