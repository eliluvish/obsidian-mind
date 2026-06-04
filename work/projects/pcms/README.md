---
date: "2026-04-05"
description: "Research Core Management System — core facility management, billing, and operations for a research hospital"
project: pcms
status: active
rails_version: "7.2"
ruby_version: "3.4.4"
meetings:
  - name: "PCMS Weekly Sync"
    cadence: weekly
    day: thursday
    attendees:
      - name: Jessica Cho
        frequency: always
      - name: Tera Morse
        frequency: always
      - name: Daniel Guettler
        frequency: always
      - name: Yovani Edwards
        frequency: sometimes
aliases:
  - PCMS
  - pcms
tags:
  - project
---

# PCMS

## Overview
Research Core Management System. Manages core facility operations, billing, and services for a research hospital.

## Repository & Deploy
- **Repo**: https://github.com/csb-ric/pcms
- **Default branch**: master
- **Production**:
- **Staging**:
- **Deploy method**: Manual

## Tech Stack
- **Rails**: 7.2
- **Ruby**: 3.4.4
- **Database**:
- **Key gems**:

## Stakeholders
- **Department**: [[Research Core Facilities]]
- [[Andy Chitty]] — Director
- [[Tera Morse]] — Finance Specialist
- [[Jessica Cho]] — Finance Specialist
- [[Yovani Edwards]] — Finance Specialist

## Compliance Notes
None currently.

## Architecture Notes

## Active Notes

- [[Calendar Refactor and Drag-Drop Proposal]] — **active**. Cross-core SR scoping bug **fixed & deployed**; PR [#2338](https://github.com/csb-ric/pcms/issues/2338) opened. Daniel proposed a larger calendar refactor (drag/drop events) — scope TBD.
- [[2026-05-14 Meeting — pcms]] — weekly sync; four-bucket client recap sent
- [[Core Browse UI Design]] — design spec for filterable card grid browse UI; ready for agent feasibility review against schema
- [[PCMS Chatbot]] — in progress. General PCMS chatbot initiative (formerly scoped to Ragon only); **SOW sent to client 2026-05-28** by [[Daniel Guettler]] (to Andy/Jessica/Yovani/Tera), awaiting acceptance. Feature backlog: availability, user-gating, capabilities, location, track record, substitutes, core-matching.
- [[002-About Page as Auto-Populated Standardized Template]] — **proposed** ADR (2026-05-08). Replace free-text About page with structured template; services/equipment are source of truth. Depends on [[Core Browse UI Design]] schema.
- [[Stakeholder Focus Groups for User Feedback]] — three sessions captured (2026-04-08, 2026-04-30, 2026-05-08). Final session: cores building external front ends, About-page architectural debate.
- [[CachedTotalAuditor — Cache Drift Audit System]] — **✅ resolved (2026-06).** [pcms#2280](https://github.com/csb-ric/pcms/issues/2280) closed by PR [#2307](https://github.com/csb-ric/pcms/pull/2307): `Trackings::CachedTotalAuditor` + `audit:cached_totals` cron (3 tiers, Honeybadger on drift) now monitors cache accuracy continuously. Second root cause fixed too — recalc jobs switched `update_column` → `update_columns` so cache writes stamp `updated_at`. Pairs with [[Cached Total Resync on SR Cancel-Uncancel|#2337]].
- **Ask at next weekly sync**: do we still need [pcms#2080](https://github.com/csb-ric/pcms/issues/2080)?

## Related
- [[Index]]
