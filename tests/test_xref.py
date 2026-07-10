#!/usr/bin/env python3
"""Tests for the guide_xref auto-linking Markdown extension.

Run:  uv run python tests/test_xref.py   (or `just test`)

Each fixture is a Markdown snippet with the number of chapter links the
extension must produce. The negative fixtures are real phrases from the book
that look like chapter numbers but are versions or quantities; they must
never be linked.
"""
import re
import sys

import markdown

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(
    __import__("os").path.abspath(__file__))))
from guide_xref import GuideXrefExtension  # noqa: E402

TABLE_HEAD = "| a | b |\n| --- | --- |\n"

# (name, page_path, markdown source, expected number of chapter links)
CASES = [
    # -- formats that must link ------------------------------------------
    ("chapter word", "chapters/x.md",
     "as described in chapter 1.6, records matter.", 1),
    ("chapter chain with descriptions", "chapters/x.md",
     "See chapters 1.5 (governance), 1.6 (decision records), 2.1 "
     "(coding standards), 12.2 (checklists), and 12.3 (templates).", 5),
    ("chapter range", "chapters/x.md",
     "the standards of chapters 4.1–4.6 apply.", 2),
    ("chapter to chapter", "chapters/x.md",
     "the pipelines (chapters 11.1 to 11.2) shape flow.", 2),
    ("title parens", "chapters/x.md",
     "Portfolio and program management (10.1) sets direction and Agile "
     "(10.7) is the adaptive option.", 2),
    ("parens list", "chapters/x.md",
     "the guardrails (10.2, 10.3) manage what surrounds delivery.", 2),
    ("parens see", "chapters/x.md", "accessibility (see 5.3) is a floor.", 1),
    ("chapter after comma", "project/changelog.md",
     'consolidated into a single chapter, 11.4 "Objectives".', 1),
    ("bold part-intro item", "chapters/x.md",
     "- **1.1 Software engineering values:** The behaviors that scale.", 1),
    ("bold item trailing period", "chapters/x.md",
     "- **3.1 Architecture fundamentals**. The decisions that matter.", 1),
    ("table ref run", "chapters/x.md",
     TABLE_HEAD + "| Requirements | 2.8, 11.1, 5.1 |", 3),
    ("table title cells", "chapters/x.md",
     TABLE_HEAD + "| ISO 27017 | 4.3 Infrastructure and cloud security; "
     "4.5 Privacy |", 2),
    ("table range", "chapters/x.md",
     TABLE_HEAD + "| WCAG | 5.3 Accessibility; 5.1–5.6 UX chapters |", 3),
    # -- version numbers and quantities that must NOT link ----------------
    ("wcag", "chapters/x.md", "must meet WCAG 2.2 AA.", 0),
    ("wcag pair", "chapters/x.md", "WCAG 2.1 and 2.2 are organized.", 0),
    ("wcag cell", "chapters/x.md", TABLE_HEAD + "| WCAG (2.1 / 2.2) | w |", 0),
    ("apache", "chapters/x.md", "licensed under Apache 2.0 terms.", 0),
    ("oauth", "chapters/x.md", "Aaron Parecki, *OAuth 2.0 Simplified*.", 0),
    ("swebok", "chapters/x.md", "the SWEBOK V4.0 knowledge areas.", 0),
    ("ai rmf", "chapters/x.md", "NIST AI Risk Framework (AI RMF 1.0).", 0),
    ("okr grade", "chapters/x.md", "graded at 1.0 it was set too low.", 0),
    ("okr scale", "chapters/x.md", "scored on a 0.0 to 1.0 scale.", 0),
    ("numeric table", "chapters/x.md",
     TABLE_HEAD + "| Consolidate | 1.5 |", 0),
    ("numeric matrix", "chapters/x.md",
     TABLE_HEAD + "| Migrate batch | 1.5 |\n| SAST | 2.0 |", 0),
    ("not a chapter", "chapters/x.md", "see chapter 13.1 for details.", 0),
    ("heading", "chapters/x.md", "# 12.7 Index", 0),
    ("code span", "chapters/x.md", "run `chapter 1.2` now.", 0),
    ("bold non-title", "chapters/x.md", "- **2.0 Simplified**: a book.", 0),
]

CH_HREF = re.compile(r'href="([^"]*\d+-\d+-[a-z0-9-]+\.md)"')

failures = []
for name, page, src, want in CASES:
    ext = GuideXrefExtension(page_path=page)
    html = markdown.markdown(src, extensions=["tables", ext])
    got = CH_HREF.findall(html)
    ok = len(got) == want
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" +
          ("" if ok else f"  expected {want}, got {len(got)}: {got}\n  {html}"))
    if not ok:
        failures.append(name)

# links are relative to the page's directory
html = markdown.markdown("see chapter 11.4 for OKRs.",
                         extensions=[GuideXrefExtension(page_path="project/changelog.md")])
ok = 'href="../chapters/11-04-objectives-and-key-results.md"' in html
print(f"[{'PASS' if ok else 'FAIL'}] relative href from project/  {'' if ok else html}")
if not ok:
    failures.append("relative href")

# authored links are left alone (no nested or duplicate links)
html = markdown.markdown("see [chapter 1.2](01-02-team-topologies.md).",
                         extensions=[GuideXrefExtension(page_path="chapters/x.md")])
ok = html.count("<a ") == 1
print(f"[{'PASS' if ok else 'FAIL'}] authored links untouched  {'' if ok else html}")
if not ok:
    failures.append("authored links")

print()
if failures:
    print(f"RESULT: {len(failures)} test(s) FAILED")
    sys.exit(1)
print("RESULT: all xref tests passed")
sys.exit(0)
