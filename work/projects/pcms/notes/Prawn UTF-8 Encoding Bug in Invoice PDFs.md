---
date: "2026-04-05"
description: "RESOLVED — Prawn IncompatibleStringEncoding crash on invoice PDF generation, switched to external fonts for UTF-8 — GitHub #2271"
status: completed
project: "pcms"
github_issue: 2271
tags:
  - work-note
---

# Prawn UTF-8 Encoding Bug in Invoice PDFs

> [!danger] High Priority
> Invoice PDF generation is failing silently for some invoices. BPC core affected, likely others too.

## Context

[[Jessica Cho]] reported that an Error Invoice Report for the BPC core showed 3 failed invoices out of 210, but only 1 invoice number was listed in the error email. The failed invoices don't appear in the system's Unsent Invoices tab either — making them hard to find and re-send.

## Root Cause

Prawn is throwing `Prawn::Errors::IncompatibleStringEncoding` because invoice data contains characters outside Windows-1252. Prawn's built-in PDF fonts only support Windows-1252 — full UTF-8 requires switching to external fonts.

## Fix

Switch Prawn to use external fonts (e.g., a TTF with full UTF-8 support) instead of built-in PDF fonts.

## Impact

- Invoices with non-ASCII characters silently fail to generate
- Failed invoices don't surface clearly in error reports or the UI
- Cores can't locate or re-send the failed invoices

## Related

- [[PCMS]]
- [[Jessica Cho]]
- [[Daniel Guettler]] — assigned on GitHub
