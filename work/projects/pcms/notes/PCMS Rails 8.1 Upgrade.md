---
date: "2026-06-24"
description: "Upgrade PCMS from Rails 7.2 to 8.1 — shipped to master 2026-06-24. Same jsonapi-resources keyword-arg breakage as lab_archives; CI modernized; backed by a large test-coverage push."
project: "pcms"
github_issue:
status: completed
rails_version: "8.1"
tags:
  - work-note
---

# PCMS Rails 8.1 Upgrade

## Context

PCMS was on **Rails 7.2**. Upgraded to **Rails 8.1** — closing the medium-term [[North Star]] goal. The upgrade was the anchoring event of the 2026-06-22 → 2026-06-24 work window and the single largest structural change in it.

This is the second app to make the 7.x/8.0 → 8.1 jump; [[lab_archives Rails 8.1 Upgrade]] went first and hit the **same `jsonapi-resources` keyword-arg breakage** — worth treating as a known gotcha for any remaining apps on that gem.

## Status

**Merged to master 2026-06-24** (`d98e4086`), pushed (`master`/`origin/main` in sync). Net for the window: 261 files, +8,218/−1,443 — dominated by the test push (below) rather than the upgrade diff itself.

What landed (non-obvious bits worth remembering):
- **`jsonapi-resources` positional-hash deprecation** (`3dcd9d96`) — Rails 8.1 flags the unmaintained gem passing a positional hash where keyword args are now expected. Same root cause as lab_archives' route-drawing break; here it was silenced/shimmed rather than left to warn.
- Dependency bumps landed alongside the cutover (`ed7f828a`, `830ea8d6`, `1ca21c04`).
- Repo `CLAUDE.md` updated to reflect the 8.1 stack (`c07cd37a`) — the upgrade was intentional and settled, not exploratory.
- **CI modernized** in the same window: new `bin/ci` pointing test DBs at a Docker host (`31d3ea65`), `ci.rb` adopted (`0dea915b`), rubocop step disabled (`e8aa9d1c`). Time frozen in calendar and `booking_release_time` specs (`1075b93b`, `12afc59a`) to kill midnight-UTC flakes.

## Backed by a large test-coverage push

~50+ commits in the same window covered nearly every controller and service across all engine namespaces (`Remunc`, `Mvvc`, `Svectr`, `Bpc`, `Camd`, `Mogi`, `Rsmg`, `Smorph`, `Vector`, `Cm`, `Mgbpm`, `SHM`, plus top-level `Admin::*` / `Pi::*`), plus a `should` → `expect` RSpec syntax sweep ([#2373](https://github.com/csb-ric/pcms/issues/2373)). Writing those tests surfaced and fixed several real latent bugs (e.g. `Vector::Plasmid.species` calling a nonexistent `Array#distinct`; multiple `head :not_found` / 404-contract fixes; a broken `DelayedJobsController` redirect symbol). The coverage is what made the version cutover safe to ship.

## Action Items

- [x] Bump Rails 7.2 → 8.1
- [x] Shim `jsonapi-resources` keyword-arg deprecation
- [x] Modernize CI (`bin/ci`, Docker test DB, time-frozen specs)
- [x] Promote → master (`d98e4086`, 2026-06-24)
- [ ] Deploy to production

## Related

- [[PCMS]]
- [[lab_archives Rails 8.1 Upgrade]] — prior app, same `jsonapi-resources` breakage
- [[Index]]
