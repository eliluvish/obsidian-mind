---
date: "2026-05-25"
description: "Modal UI in eris adopts Microsoft's Fluent 2 design system as the visual / interaction baseline for dialogs and modal forms."
project: "rcservices"
status: accepted
tags:
  - decision
---

# 002 — Fluent 2 Modal Design System

## Context

The eris repo has reached the point where modal dialogs are no longer one-offs — the account-picker refactor (`fccfce33`) extracted a shared modal account-creation flow used across five subscription forms, and more form components (BriefCase admin, the in-flight RCC billing chatbot, future subscription wizards) are queued to follow the same pattern. Without a consistent visual and interaction baseline, each new modal would drift in spacing, focus management, button affordances, and close behavior.

Microsoft's [Fluent 2](https://fluent2.microsoft.design/) design system was selected as the baseline. Captured in-repo at `.claude/DECISION_LOG.md` on 2026-05-25; mirrored here as the canonical ADR.

## Triggering Issue

No single GitHub issue — emerged organically from the account-picker refactor (`fccfce33`) and the need to standardize modal patterns before the chatbot UI (`f33e252c`, on `origin/development`) and other queued form work land on master.

## Decision

**Modal UI in eris will follow the Fluent 2 design system** — dialogs, surfaces, buttons, form controls, focus rings, and interaction patterns inside modals derive from Fluent 2 tokens and component specs.

This is a baseline, not a wholesale theme swap: it governs **modals first**, with implicit room to extend to other surfaces (forms, toolbars, navigation) as the pattern proves out.

## Consequences

- **Visual consistency** across the account picker, future subscription wizards, BriefCase admin actions, and the RCC billing chatbot UI without re-litigating spacing / button hierarchy per modal.
- **Specification work needed**: someone must translate Fluent 2 tokens (color, type ramp, elevation, motion) into the existing Tailwind / asset pipeline. Until that's done, modal styling will be approximate.
- **Constrains future picks**: any modal component or library introduced later (date pickers, command palettes) should align with Fluent 2 or be wrapped to match — otherwise the consistency benefit erodes.
- **Bias toward Microsoft idioms** in interaction (e.g. primary action on the right, ESC to dismiss, specific focus-trap behavior). Worth flagging if it ever conflicts with MGB brand work that's already underway on `origin/development`.
- **Out of scope** (intentionally, for now): full theming of non-modal surfaces. The ADR doesn't say "eris becomes a Fluent app" — it says "modals follow Fluent."

## Related

- [[RC Services (Eris)|rcservices]]
- [[Briefcase Billing Takeover]] — admin modals likely to follow this pattern
- `.claude/DECISION_LOG.md` in eris — in-repo origin entry
