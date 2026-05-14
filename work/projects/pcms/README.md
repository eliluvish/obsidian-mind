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

- [[2026-05-14 Meeting — pcms]] — weekly sync; four-bucket client recap sent; commit `60b8ae3` broke the calendar events API for cross-core SRs (see [[Gotchas#PCMS calendar_events API now scoped by core (commit 60b8ae3)]])
- [[Core Browse UI Design]] — design spec for filterable card grid browse UI; ready for agent feasibility review against schema
- [[Ragon Equipment Chatbot]] — in progress. Equipment-search chatbot for Ragon core; feature backlog captured (availability, user-gating, capabilities, location, track record, substitutes).
- [[002-About Page as Auto-Populated Standardized Template]] — **proposed** ADR (2026-05-08). Replace free-text About page with structured template; services/equipment are source of truth. Depends on [[Core Browse UI Design]] schema.
- [[Stakeholder Focus Groups for User Feedback]] — three sessions captured (2026-04-08, 2026-04-30, 2026-05-08). Final session: cores building external front ends, About-page architectural debate.
- [pcms#2280](https://github.com/csb-ric/pcms/issues/2280) — Investigate whether cached charges are keeping up.
- **Ask at next weekly sync**: do we still need [pcms#2080](https://github.com/csb-ric/pcms/issues/2080)?

## Related
- [[Index]]
