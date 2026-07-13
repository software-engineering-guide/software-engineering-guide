#!/usr/bin/env python3
"""Markdown statistics report for the guide.

Run:  just stats   (or: python3 tools/stats.py)

Prints per-chapter word counts sorted ascending, the substantive chapters
below the target depth, Wikipedia links and reference-section entries per
chapter, and totals. The output is Markdown so a report can be pasted
straight into an issue. Needs only Python 3, like tests/validate.py.
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "docs", "chapters")

# The depth every substantive chapter should reach (plan.md; the enforced
# floor in tests/validate.py is lower and shrinks the gap over time).
TARGET_WORDS = 3000
REFS_HEADING = "## References and further reading"


def dec(f):
    m = re.match(r"(\d+)-(\d+)-", os.path.basename(f))
    return (int(m.group(1)), int(m.group(2)))


def read(p):
    return open(p, encoding="utf-8").read()


def ref_entries(text):
    """Count list entries in the references section."""
    if REFS_HEADING not in text:
        return 0
    section = text.split(REFS_HEADING, 1)[1].split("\n## ", 1)[0]
    return sum(1 for ln in section.splitlines() if re.match(r"\s*[-*]\s", ln))


def main():
    chapters = sorted(glob.glob(os.path.join(CH, "*.md")), key=dec)
    rows = []
    for f in chapters:
        p, c = dec(f)
        t = read(f)
        h1 = next((ln[2:].strip() for ln in t.splitlines() if ln.startswith("# ")), "")
        title = re.sub(r"^\d+\.\d+\s+", "", h1)
        rows.append({
            "num": f"{p}.{c}",
            "title": title,
            "substantive": p <= 11 and c >= 1,
            "words": len(t.split()),
            "wiki": t.count("en.wikipedia.org/wiki/"),
            "refs": ref_entries(t),
        })

    subst = [r for r in rows if r["substantive"]]
    thin = sorted((r for r in subst if r["words"] < TARGET_WORDS),
                  key=lambda r: r["words"])

    print("# Guide statistics")
    print()
    print(f"- Chapters: **{len(rows)}** ({len(subst)} substantive, "
          f"{len(rows) - len(subst)} part introductions and appendices)")
    print(f"- Total words: **{sum(r['words'] for r in rows):,}**")
    print(f"- Mean words per substantive chapter: "
          f"**{sum(r['words'] for r in subst) // max(len(subst), 1):,}**")
    print(f"- Wikipedia links: **{sum(r['wiki'] for r in rows):,}**")
    print(f"- Reference entries: **{sum(r['refs'] for r in rows):,}**")
    print(f"- Substantive chapters below the {TARGET_WORDS:,}-word target: "
          f"**{len(thin)}**")
    print()

    print(f"## Substantive chapters below the {TARGET_WORDS:,}-word target")
    print()
    if thin:
        print("| Chapter | Title | Words | Gap |")
        print("| --- | --- | ---: | ---: |")
        for r in thin:
            print(f"| {r['num']} | {r['title']} | {r['words']:,} "
                  f"| {TARGET_WORDS - r['words']:,} |")
    else:
        print("None.")
    print()

    print("## All chapters by word count (ascending)")
    print()
    print("| Chapter | Title | Words | Wikipedia links | Reference entries |")
    print("| --- | --- | ---: | ---: | ---: |")
    for r in sorted(rows, key=lambda r: r["words"]):
        print(f"| {r['num']} | {r['title']} | {r['words']:,} "
              f"| {r['wiki']} | {r['refs']} |")


if __name__ == "__main__":
    main()
