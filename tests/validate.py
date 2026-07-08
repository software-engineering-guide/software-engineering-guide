#!/usr/bin/env python3
"""
Comprehensive validation suite for the Software Engineering Recommendations guidebook.

Run:  python3 tests/validate.py   (from the repository root, or anywhere)

Exit code 0 if every check passes, 1 otherwise. Designed for CI and pre-commit use.
The checks below are the executable form of the conventions in spec/conventions.md.
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "docs", "chapters")

PART_TITLES = {
    1: "People", 2: "Software Programming", 3: "Systems", 4: "Security",
    5: "UI/UX Design", 6: "Artificial Intelligence", 7: "Data, Analytics, and Insight",
    8: "Automation", 9: "Operations, Reliability, and Observability",
    10: "Project/Product/Program Management", 11: "Flow: Discovery and Delivery Pipelines",
    12: "Appendices",
}
REQUIRED_SECTIONS = [
    "## Overview and motivation", "## Key principles", "## Recommendations",
    "## Trade-offs: pros and cons", "## Examples", "## Business case",
    "## Anti-patterns", "## Maturity model", "## Ideas for discussion",
    "## Key takeaways", "## References and further reading",
]
FORBIDDEN = [r"\bnot only\b", r"\bbut also\b", r"\bload.bearing\b"]

# These files document the style rules, so they are allowed to quote the very
# tokens the rules forbid (the em-dash character and the banned phrases). Every
# other file, including all chapters and examples, must stay clean.
STYLE_EXEMPT = {
    "AGENTS.md", "docs/contributing/testing.md", "docs/contributing/style-rules.md",
    "docs/spec/conventions.md", "docs/contributing/index.md",
}

failures = []
def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(name + (f": {detail}" if detail else ""))

def read(p): return open(p, encoding="utf-8").read()
def dec(f):
    m = re.match(r"(\d+)\.(\d+)-", os.path.basename(f))
    return (int(m.group(1)), int(m.group(2)))

chapters = sorted(glob.glob(os.path.join(CH, "*.md")), key=dec)
# Walk the repository for Markdown files, skipping build output, virtual
# environments, and other hidden or vendored directories.
SKIP_DIRS = {"site", "node_modules", "__pycache__"}
all_md = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if not d.startswith(".") and d not in SKIP_DIRS]
    all_md += [os.path.join(dirpath, fn) for fn in filenames if fn.endswith(".md")]
disk = set(f"{dec(f)[0]}.{dec(f)[1]}" for f in chapters)

# 1. Exactly 100 chapters.
check("exactly 100 chapters", len(chapters) == 100, f"found {len(chapters)}")

# 2. Per-part numbering is contiguous starting at N.0.
byp = {}
for f in chapters:
    p, c = dec(f); byp.setdefault(p, []).append(c)
bad = [p for p in byp if sorted(byp[p]) != list(range(len(byp[p])))]
check("per-part numbering contiguous from N.0", not bad, f"parts with gaps: {bad}")

# 3. H1 heading matches the filename decimal.
mm = []
for f in chapters:
    d = f"{dec(f)[0]}.{dec(f)[1]}"
    h1 = next((ln[2:].strip() for ln in read(f).splitlines() if ln.startswith("# ")), "")
    if not h1.startswith(d): mm.append(os.path.basename(f))
check("H1 matches filename decimal", not mm, f"{mm}")

# 4. Substantive chapters (parts 1-11, chapter >= 1) have all required sections.
missing = {}
for f in chapters:
    p, c = dec(f)
    if p <= 11 and c >= 1:
        t = read(f)
        miss = [s for s in REQUIRED_SECTIONS if s not in t]
        if miss: missing[os.path.basename(f)] = miss
check("substantive chapters have all required sections", not missing, f"{missing}")

# 5. No em-dash anywhere in prose files (style-documentation files exempt).
em = {os.path.relpath(f, ROOT): read(f).count("—") for f in all_md
      if os.path.relpath(f, ROOT) not in STYLE_EXEMPT and read(f).count("—")}
check("no em-dashes (U+2014)", not em, f"{em}")

# 6. No forbidden LLM phrases (style-documentation files exempt).
ph = {}
for f in all_md:
    if os.path.relpath(f, ROOT) in STYLE_EXEMPT: continue
    hits = sum(len(re.findall(pat, read(f), re.I)) for pat in FORBIDDEN)
    if hits: ph[os.path.relpath(f, ROOT)] = hits
check("no forbidden phrases (not only / but also / load-bearing)", not ph, f"{ph}")

# 7. All internal .md links resolve.
broken = []
for f in all_md:
    base = os.path.dirname(f)
    for m in re.finditer(r"\]\((?!https?://|#|mailto:)([^)]+\.md)(?:#[^)]*)?\)", read(f)):
        if not os.path.exists(os.path.normpath(os.path.join(base, m.group(1)))):
            broken.append(f"{os.path.relpath(f, ROOT)} -> {m.group(1)}")
check("all internal .md links resolve", not broken, f"{broken[:8]}")

# 8. Wikipedia links are well-formed.
badwiki = []
for f in chapters:
    for m in re.finditer(r"\]\((https?://[^)]*wikipedia[^)]*)\)", read(f)):
        if not m.group(1).startswith("https://en.wikipedia.org/wiki/"):
            badwiki.append(f"{os.path.basename(f)}: {m.group(1)}")
check("wikipedia links well-formed", not badwiki, f"{badwiki[:8]}")

# 9. spec/structure.md lists exactly the chapters on disk.
sp = os.path.join(ROOT, "docs", "spec", "structure.md")
if os.path.exists(sp):
    spec_ch = set(re.findall(r"^\| (\d+\.\d+) \|", read(sp), re.M))
    check("docs/spec/structure.md matches disk (missing)", not (disk - spec_ch), f"{sorted(disk - spec_ch)[:8]}")
    check("docs/spec/structure.md matches disk (extra)", not (spec_ch - disk), f"{sorted(spec_ch - disk)[:8]}")
else:
    check("docs/spec/structure.md exists", False, "file missing")

# 10. README, the site home page, and the contents page link every chapter file.
for navrel in ["README.md", "docs/index.md", "docs/front-matter/table-of-contents.md"]:
    nav = read(os.path.join(ROOT, navrel))
    linked = set(re.findall(r"chapters/(\d+\.\d+)-", nav))
    check(f"{navrel} links every chapter", not (disk - linked), f"missing {sorted(disk - linked)[:8]}")

# 11. The zensical.toml navigation lists every page under docs/, so every page
# is reachable from the published site's navigation.
zt_path = os.path.join(ROOT, "zensical.toml")
if os.path.exists(zt_path):
    zt = read(zt_path)
    docs_pages = [os.path.relpath(f, os.path.join(ROOT, "docs")).replace(os.sep, "/")
                  for f in all_md if f.startswith(os.path.join(ROOT, "docs") + os.sep)]
    unlisted = [p for p in sorted(docs_pages) if f'"{p}"' not in zt]
    check("zensical.toml nav lists every docs page", not unlisted, f"{unlisted[:8]}")
else:
    check("zensical.toml exists", False, "file missing")

print()
if failures:
    print(f"RESULT: {len(failures)} check(s) FAILED")
    sys.exit(1)
print("RESULT: all checks passed")
sys.exit(0)
