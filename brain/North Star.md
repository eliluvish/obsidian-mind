---
date:
description: "Living document of goals, focus areas, and aspirations — read at session start, updated when direction shifts"
tags:
  - brain
  - north-star
aliases:
  - Goals
  - Focus
---

# North Star

A living document of goals, aspirations, and current focus areas. Both you and Claude write to this. Claude reads it at the start of meaningful work sessions and references it when making suggestions.

## Current Focus

_What am I working toward right now?_

- RCS: compare [[Chris Mow]] billing implementation to my own for HPC briefcase and MAD3
- Keep PCMS cached charges at top of mind. First cron report 2026-06-16: 99.92% accuracy; the 2 overstating mismatches were **root-caused + fixed** ([pcms#2360](https://github.com/csb-ric/pcms/issues/2360) / #2361 — overlapping cancelled-reservation rebook gap, merged 2026-06-16). Clock restarts: if the cron stays clean through ~2026-07-16 we can fully switch to caching. See [[CachedTotalAuditor — Cache Drift Audit System]].
- RCS: determine billing structure for new RFA

## Goals

### Short-term (This Quarter)

- RCservices Freezerpro integration

### Medium-term (This Half)

- complete all accountability logbook tickets (the set Kele/Mirabella added — tracked in [[Accountability Logbook Testing Feedback]]; origin [[2026-04-27 Meeting — ilog]])
- iLog accountability logbook — wireframes complete (implementation deferred until after logbook ships); beta testing path through Controlled Substance Work Group → pilot lab(s)

### Long-term (This Year+)

- Create a better autonomous workflow as a solo Ruby on Rails developer

## Aspirations

_What kind of engineer/person am I becoming?_

- One that is fully in to AI and recognizes my new role as manager of agents

## Anti-goals

_What am I explicitly NOT optimizing for?_

-

## Shifts Log

Record when focus changes, with date and reason.

| Date | Shift | Reason |
|------|-------|--------|
|      | Created North Star | Initial setup |
| 2026-04-05 | Initial vault population | Scaffolded 4 new projects (rpr, biolift, people, ris), 25 people, 1 team, 10 work notes across 7 projects. Added PCMS #2271 and minr updates as high priority. |
| 2026-04-09 | Added ARC iLog demo to Current Focus | Grapevine intel that [[Kele Piper]] is demoing iLog at ARC on 2026-04-30. Unconfirmed; tracking quietly. Creates a soft deadline for in-flight iLog features. |
| 2026-04-17 | Added rpr deploy hold to Current Focus | rpr PR #190 ($1500 order cap) merged to master but production deploy held until 2026-04-24 per [[Gala Laffey]]. Remove once deployed. |
| 2026-04-24 | Removed rpr deploy hold | ✅ Deployed to production 2026-04-24. |
| 2026-04-27 | Removed ARC iLog demo from Current Focus | Kele postponed the ARC demo on her own ("we're not ready, no point rushing"). Deploy freeze 2026-04-30 no longer needed. See [[2026-04-27 Meeting — ilog]]. |
| 2026-06-04 | Cached-charges goal resolved | PR #2307 (CachedTotalAuditor + `audit:cached_totals` cron) merged, closing #2280. Both drift vectors fixed (#2337 + `update_columns`); ongoing monitoring now in place. See [[CachedTotalAuditor — Cache Drift Audit System]]. |
| 2026-06-24 | PCMS Rails 8.1 upgrade shipped | Medium-term goal complete — Rails 7.2 → 8.1 merged to master. Same `jsonapi-resources` kwarg breakage as lab_archives. See [[PCMS Rails 8.1 Upgrade]]. |
