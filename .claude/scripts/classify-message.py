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
            # English
            "decided", "deciding", "decision", "we chose", "agreed to",
            "let's go with", "the call is", "we're going with",
            # Japanese
            "決定した", "決めた", "合意した",
            # Korean
            "결정했어", "결정했습니다", "합의했어",
            # Chinese
            "决定了", "我们决定", "确定了", "同意",
        ],
    },
    {
        "name": "ARCHITECTURE",
        "message": "ARCHITECTURE discussion — consider creating a reference note in reference/ or a decision record",
        "patterns": [
            # English
            "architecture", "system design", "rfc", "tech spec",
            "trade-off", "design doc", "adr",
            # Japanese
            "アーキテクチャ", "システム設計",
            # Korean
            "아키텍처", "시스템 설계",
            # Chinese
            "架构", "系统设计", "技术规范",
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
            # Japanese
            "言ってた", "フィードバック", "話した",
            # Korean
            "말했어", "피드백", "얘기했어", "언급했어",
            # Chinese
            "说了", "提到", "反馈", "提及",
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
            # Japanese
            "スプリント", "マイルストーン", "マージした", "リリースしました",
            # Korean
            "스프린트", "마일스톤", "배포", "릴리스", "병합",
            # Chinese (发布了, 上线 shared with WIN)
            "迭代", "里程碑", "发布了", "上线", "合并了",
        ],
    },
    {
        "name": "PROJECT SWITCH",
        "message": "PROJECT SWITCH detected — consider using /context-switch to reload project context",
        "patterns": [
            # English
            "switching to", "context switch", "jumping to", "moving to",
            "working on", "back to", "picking up",
            # Japanese
            "切り替え", "に移る",
            # Korean
            "전환", "으로 이동",
            # Chinese
            "切换到", "转到",
        ],
    },
    {
        "name": "DEPLOY",
        "message": "DEPLOY detected — consider using /deploy-checklist for the target project",
        "patterns": [
            # English
            "deploy", "deploying", "deployment",
            "release", "releasing", "production",
            "staging", "capistrano", "going live",
            # Japanese
            "デプロイ", "リリース", "本番",
            # Korean
            "배포", "릴리스", "프로덕션",
            # Chinese
            "部署", "发布", "上线", "生产环境",
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
            # Japanese
            "コンプライアンス", "個人情報",
            # Korean
            "컴플라이언스", "개인정보",
            # Chinese
            "合规", "个人信息", "审计",
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
