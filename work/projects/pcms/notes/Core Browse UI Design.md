---
date: "2026-04-30"
description: "Design spec for a filterable core browse UI — card grid with modality, institution, and location filters replacing the flat 130-item list"
project: "pcms"
status: active
tags:
  - work-note
---

# Core Browse UI Design

## Problem

The current core listing is a flat alphabetical list of ~130 cores with short text descriptions. It serves neither of the two primary user modes:

- **Search** — "I need flow cytometry." Being addressed separately via chatbot.
- **Browse** — "I'm a scientist, what's out there?" Users don't know what to search for and need to discover cores serendipitously.

Feedback from a stakeholder focus group (2026-04-30) was consistent: the list is overwhelming, not visual enough, and gives no way to narrow by what matters most to investigators — modality and location.

## Design Decision

**A filterable card grid.** All cores on one page as cards. Filters narrow the grid in place. No separate category landing pages, no duplicating cores that span multiple modalities.

Cores appear **once** regardless of how many modalities or categories they belong to.

## Filters

| Filter | Source | Notes |
|--------|--------|-------|
| Modality | Core-level modality join (see below) | Multi-select |
| Institution | `institution` field on core | BWH, MGH, McLean, Mass Eye and Ear, etc. |
| Building | `building` field on core | Charlestown Navy Yard, Longwood, MGH Main, etc. |

## Core Card

Each card displays:

- Core name
- Short description (~150 chars) — one-liner, distinct from full description
- Location — building + institution
- Modality tags
- "Last updated X months ago" — from `content_updated_at`, not `updated_at`

## Data Model Changes

### 1. Location fields on cores

Add structured location fields directly to the core model:

```
building        string
street_address  string
city            string
institution     string
```

`institution` drives one filter dimension. `building` drives another. `street_address` and `city` are for display and future map view.

### 2. Core-level modality join

Cores need their own association to the modality vocabulary — separate from equipment modalities. This is necessary because some cores are service-heavy (clinical research units, behavioral specialists, phlebotomy) and have no equipment records to derive modalities from. Equipment-only derivation leaves service cores invisible when any modality filter is active.

The modality vocabulary should be **the same table** already used for equipment modalities — no new concepts, just a new join:

```
core_modalities: core_id, modality_id
```

Equipment-centric cores: tag via admin using existing modality records.
Service-centric cores: tag the same way; no equipment required.

### 3. `content_updated_at` on cores

A datetime field set intentionally via admin when content is meaningfully refreshed — distinct from `updated_at`, which changes on any model touch. Displayed on the card as a freshness signal ("Updated 3 months ago"). Stale threshold TBD (6 or 12 months).

### 4. Short description on cores

A ~150-char one-liner for the card view, enforced separately from the long description. If the existing description field is already short in practice, this may not be needed.

## What This Does Not Include

- A separate `categories` table — modalities serve this purpose
- Map view — location fields lay the groundwork but map rendering is out of scope
- Core director self-service — all editing goes through admin
- Chatbot integration — separate effort; this is browse only

---

## Agent: Things to Confirm Against Code and Schema

Before implementing, verify the following. If any assumption is wrong, the design may need adjustment.

### Schema

- [ ] What is the core model called? (`Core`, `Lab`, `Facility`, something else?)
- [ ] Does a `modalities` table already exist? What are its columns?
- [ ] How are modalities associated to equipment — join table, has_many through, or something else? What are the table/column names?
- [ ] Does a `capabilities` table exist separately from modalities? If so, are they two distinct concepts or synonyms?
- [ ] Does the core model already have any location-related fields (`location`, `address`, `building`, `institution`)?
- [ ] Does the core model have a `description` field? Is it short in practice or long-form?
- [ ] Does the core model have `updated_at` (standard Rails)? Is there already a `content_updated_at` or similar?
- [ ] Does an `institution` lookup table exist, or is institution currently a string on related models?

### Associations

- [ ] What is the equipment → core relationship? (`belongs_to :core`? `has_many :equipment`? Through a join?)
- [ ] Do equipment records currently have modality associations? What does that query look like?
- [ ] Is there already any core → modality association, or is this new?

### Admin

- [ ] Is there an existing admin interface for cores (`/admin/cores` or similar)?
- [ ] Which fields are currently editable via admin?
- [ ] Is admin built with a specific framework (ActiveAdmin, custom controllers, etc.)?

### Existing UI

- [ ] Where is the current core listing page? What controller and view?
- [ ] Is there any existing filtering or search on the listing page?
- [ ] What does the current core card/row look like in the listing — what fields are displayed?

## Related

- [[PCMS]]
- [[Ragon Equipment Chatbot]]
- [[Equipment and Services Tag Taxonomy]]
- [[Stakeholder Focus Groups for User Feedback]]
