---
date: "2026-05-18"
description: "RPR incident — participant email is shared across studies; a non-study user's change on one study altered the participant's email on study 2022P000780, misrouting a gift card. No PII exposed. Unresolved; proposed fix: email per study."
project: rpr
github_issue:
status: active
tags:
  - work-note
---

# Cross-Study Email Mutation Incident

## Context

Reported 2026-05 by Emmett, a research coordinator on **The BEHOLD Study (#2022P000780)**, to [[Gala Laffey]], who escalated to Eli.

A study participant did not receive an issued gift card. It had been sent to a **different email that did not belong to the participant**. The activity log showed that **someone not associated with the BEHOLD study had updated the participant's email** without the BEHOLD team's knowledge. The team has since restored the correct email and reissued the gift card.

**No PII/PHI was exposed.** The concern is data integrity and access scope: how a non-study user altered another study's participant payment routing.

## Root Cause

The participant is enrolled in **two studies**, but RPR records **only one email per participant**. When one study team changes the email, it changes it on the shared participant record — so the other study's record changes too. A prior "additional check for email" was believed to prevent this, but it either was not implemented or does not cover this path.

## Proposed Fix

**One email per study** (per study-participant enrollment) rather than one email per participant. Changing the email in one study would no longer affect the participant's email in other studies, while the records stay tied to the same underlying participant. Raised with [[Gala Laffey]] 2026-05-05; **awaiting decision**.

> [!warning] Open decision
> "Email per participant vs. email per study" is an unresolved design decision. Promote to an ADR in `rpr/decisions/` once [[Gala Laffey]] confirms direction.

## Status

**Unresolved.** Immediate participant impact remediated by the BEHOLD team (email restored, gift card reissued). Underlying model fix not yet decided or built.

## Action Items

- [ ] Get a decision from [[Gala Laffey]] on email-per-study
- [ ] Confirm what the prior "additional email check" actually does / why it didn't prevent this
- [ ] On approval: model + migration for per-study email; create ADR
- [ ] Review the activity log / access scope — how a non-study user could edit this study's participant

## Related

- [[Research Participant Remuneration|rpr]]
- [[Gotchas#Participant email is shared across all of a participant's studies]]
- [[Gala Laffey]]
- [[Order Limit Raised to 1500 Deploy Hold]]
- [[Index]]
