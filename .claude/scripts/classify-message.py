#!/usr/bin/env python3
"""Classify user messages and inject routing hints for Claude.

Architecture: data-driven signal matching. Each signal has a list of trigger
patterns checked via regex with Latin-letter lookarounds (not \\b). Words can
appear in multiple signals (explicit overlaps) because the cost of a false
positive hint is ~0 (Claude ignores irrelevant hints) while a false negative
means missed routing.

Patterns include English, Japanese, Korean, and Simplified Chinese to support
multilingual users. The Latin-letter lookaround approach allows mixed
Latin/CJK text without relying on Python word-boundary behavior.
"""
import json
import sys
import re


# Each signal: name, routing message, and trigger patterns.
# Patterns are checked with Latin-letter lookarounds — safe for CJK/Latin mixed text.
# Words MAY appear in multiple signals to express natural category overlaps.
SIGNALS = [
    {
        "name": "DECISION",
        "message": "DECISION detected — consider using /decision to create an ADR in the project's decisions/ folder",
        "patterns": [
            "decided", "deciding", "decision", "we chose", "agreed to",
            "let's go with", "the call is", "we're going with",
        ],
    },
    {
        "name": "ARCHITECTURE",
        "message": "ARCHITECTURE discussion — consider creating a reference note in reference/ or a decision record",
        "patterns": [
            "architecture", "system design", "rfc", "tech spec",
            "trade-off", "design doc", "adr",
        ],
    },
    {
        "name": "PERSON CONTEXT",
        "message": "PERSON CONTEXT detected — consider updating the relevant person note in org/people/",
        "patterns": [
            # English
            "told me", "said that", "feedback from", "met with",
            "talked to", "spoke with",
            "mentioned that", "mentioned the", "mentioned a",
        ],
    },
    {
        "name": "PROJECT UPDATE",
        "message": "PROJECT UPDATE detected — consider updating the work note in work/projects/<name>/notes/",
        "patterns": [
            # English
            "project update", "sprint", "milestone",
            # Delivery — English (shared with WIN)
            "shipped", "shipping", "ships", "shipped feature",
            "launched", "launching", "launches",
            "completed", "completing", "completes",
            "released", "releasing", "releases",
            "deployed", "deploying", "deploys",
            # Delivery-only — English (not wins on their own)
            "went live", "rolled out", "rolling out",
            "merged", "merging", "merges",
            "cut the release", "release cut",
        ],
    },
    {
        "name": "PROJECT SWITCH",
        "message": "PROJECT SWITCH detected — consider using /context-switch to reload project context",
        "patterns": [
            # English
            "switching to", "context switch", "jumping to", "moving to",
            "working on", "back to", "picking up",
        ],
    },
    {
        "name": "DEPLOY",
        "message": "DEPLOY detected — consider using /deploy-checklist for the target project",
        "patterns": [
            # English
            "deploy", "deploying", "deployment",
            "release", "releasing", "production",
            "staging", "going live",
        ],
    },
    {
        "name": "COMPLIANCE",
        "message": "COMPLIANCE detected — consider checking reference/compliance/ and noting in the project's compliance section",
        "patterns": [
            # English
            "hipaa", "irb", "phi", "audit log", "de-identify",
            "de-identification", "compliance", "ferpa", "pii",
            "data use agreement", "dua",
        ],
    },
]


def _any_word_match(pattern_words: list, text: str) -> bool:
    """Check if any phrase appears as a whole word/phrase in text.

    Uses Latin-letter boundaries instead of \\b. Python's \\b treats CJK
    characters as word characters (\\w), so \\bdecision\\b fails to match
    in "のdecisionについて" (no boundary between Hiragana and Latin).

    (?<![a-zA-Z]) and (?![a-zA-Z]) ensure English keywords aren't part of
    a larger English word, while allowing CJK adjacency.
    """
    for phrase in pattern_words:
        if re.search(r'(?<![a-zA-Z])' + re.escape(phrase) + r'(?![a-zA-Z])', text):
            return True
    return False


def classify(prompt: str) -> list:
    p = prompt.lower()
    signals = []
    for sig in SIGNALS:
        if _any_word_match(sig["patterns"], p):
            signals.append(sig["message"])
    return signals


def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError, EOFError):
        sys.exit(0)

    prompt = input_data.get("prompt", "")
    if not isinstance(prompt, str) or not prompt:
        sys.exit(0)

    try:
        signals = classify(prompt)
    except Exception:
        sys.exit(0)

    if signals:
        hints = "\n".join(f"- {s}" for s in signals)
        output = {
            "hookSpecificOutput": {
                "additionalContext": (
                    "Content classification hints (act on these if the user's message contains relevant info):\n"
                    + hints
                    + "\n\nRemember: use proper templates, add [[wikilinks]], follow CLAUDE.md conventions."
                )
            }
        }
        json.dump(output, sys.stdout)
        sys.stdout.flush()

    sys.exit(0)

if __name__ == "__main__":
    main()
