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
    10: "Project/Product/Programme Management", 11: "Flow: Discovery and Delivery Pipelines",
    12: "Appendices",
}
REQUIRED_SECTIONS = [
    "## Overview and motivation", "## Key principles", "## Recommendations",
    "## Trade-offs: pros and cons", "## Questions to discuss with your team",
    "## Sector lens", "## Examples", "## Business case",
    "## Anti-patterns", "## Maturity model", "## Ideas for discussion",
    "## Key takeaways", "## References and further reading",
]
FORBIDDEN = [r"\bnot only\b", r"\bbut also\b", r"\bload.bearing\b"]

# Minimum word count for substantive chapters (parts 1-11, chapter >= 1).
# Chapters listed in the allowlist are intentionally below the floor; shrink
# the list as thin chapters are brought up to depth (see tasks.md, task 5.1).
WORD_FLOOR = 2000
WORD_FLOOR_ALLOWLIST: set[str] = set()

# The prose cross-reference pattern, kept in sync with guide_xref/__init__.py
# (validate.py stays dependency-free, so the regexes are duplicated here
# rather than imported; guide_xref imports the markdown package).
_REF = r"\d{1,2}\.\d{1,2}"
_DESC = r"(?:\s*\([^()]*\))?"
_CONN = r"(?:[,;]?\s+(?:and\s+|or\s+|to\s+|through\s+)?|[,;]\s*|\s*[–-]\s*)"
XREF_CHAIN = re.compile(rf"(?i)\bchapters?[,:]?\s+(?:{_REF}{_DESC}{_CONN}?)+")

# These files document the style rules, so they are allowed to quote the very
# tokens the rules forbid (the em-dash character and the banned phrases). Every
# other file, including all chapters and examples, must stay clean.
STYLE_EXEMPT = {
    "AGENTS.md", "docs/contributing/testing.md", "docs/contributing/style-rules.md",
    "spec/conventions.md", "spec/index.md", "spec/README.md", "docs/contributing/index.md",
}

failures = []
def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(name + (f": {detail}" if detail else ""))

def read(p): return open(p, encoding="utf-8").read()
def dec(f):
    m = re.match(r"(\d+)-(\d+)-", os.path.basename(f))
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

# 1. Exactly 147 chapters.
check("exactly 147 chapters", len(chapters) == 147, f"found {len(chapters)}")

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

# 4b. The required sections appear in exactly the template order (the sequence
# of recognized ## headings, not just membership). Extra unrecognized headings
# are allowed anywhere.
disorder = {}
for f in chapters:
    p, c = dec(f)
    if p <= 11 and c >= 1:
        seq = []
        for ln in read(f).splitlines():
            if ln.startswith("## "):
                for s in REQUIRED_SECTIONS:
                    if ln.startswith(s):
                        seq.append(s)
                        break
        if seq != REQUIRED_SECTIONS:
            disorder[os.path.basename(f)] = seq
check("required sections in exact template order", not disorder,
      f"{dict(list(disorder.items())[:2])}")

# 4c. Substantive chapters meet the minimum word count, unless allowlisted.
thin = {}
for f in chapters:
    p, c = dec(f)
    if p <= 11 and c >= 1 and f"{p}.{c}" not in WORD_FLOOR_ALLOWLIST:
        words = len(read(f).split())
        if words < WORD_FLOOR:
            thin[f"{p}.{c}"] = words
check(f"substantive chapters have at least {WORD_FLOOR} words", not thin,
      f"offending counts: {dict(sorted(thin.items(), key=lambda kv: kv[1]))}")

# 5. No em-dash anywhere in prose files (style-documentation files exempt).
em = {os.path.relpath(f, ROOT): read(f).count("—") for f in all_md
      if os.path.relpath(f, ROOT) not in STYLE_EXEMPT and read(f).count("—")}
check("no em-dashes (U+2014)", not em, f"{em}")

# 5b. En-dashes (U+2013) appear only between digits, i.e. in numeric ranges
# such as 1–9 or 4.1–4.6 (style-documentation files exempt).
endash = []
for f in all_md:
    rel = os.path.relpath(f, ROOT)
    if rel in STYLE_EXEMPT:
        continue
    t = read(f)
    for m in re.finditer("–", t):
        prev = t[m.start() - 1] if m.start() else ""
        nxt = t[m.end()] if m.end() < len(t) else ""
        if not (prev.isdigit() and nxt.isdigit()):
            endash.append(f"{rel}:{t.count(chr(10), 0, m.start()) + 1}")
check("en-dashes (U+2013) only between digits", not endash, f"{endash[:8]}")

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

# 7b. Prose cross-references ("chapter 8.1", "chapters 4.1-4.6") in the site
# sources point at chapters that exist on disk, so guide_xref never leaves a
# reference unlinked and readers never chase a chapter that is not there.
dangling = []
for f in all_md:
    rel = os.path.relpath(f, ROOT)
    if not rel.startswith("docs" + os.sep):
        continue
    t = read(f)
    for cm in XREF_CHAIN.finditer(t):
        for num in re.findall(_REF, cm.group(0)):
            if num not in disk:
                dangling.append(f"{rel}: chapter {num}")
check("prose cross-references point at existing chapters", not dangling,
      f"{dangling[:8]}")

# 8. Wikipedia links are well-formed.
badwiki = []
for f in chapters:
    for m in re.finditer(r"\]\((https?://[^)]*wikipedia[^)]*)\)", read(f)):
        if not m.group(1).startswith("https://en.wikipedia.org/wiki/"):
            badwiki.append(f"{os.path.basename(f)}: {m.group(1)}")
check("wikipedia links well-formed", not badwiki, f"{badwiki[:8]}")

# 9. spec/structure.md lists exactly the chapters on disk.
sp = os.path.join(ROOT, "spec", "structure.md")
if os.path.exists(sp):
    spec_ch = set(re.findall(r"^\| (\d+\.\d+) \|", read(sp), re.M))
    check("spec/structure.md matches disk (missing)", not (disk - spec_ch), f"{sorted(disk - spec_ch)[:8]}")
    check("spec/structure.md matches disk (extra)", not (spec_ch - disk), f"{sorted(spec_ch - disk)[:8]}")
    # 9b. Chapter H1 titles match the titles declared in the spec manifest,
    # character for character (not just the leading decimal).
    spec_titles = dict(re.findall(r"^\| (\d+\.\d+) \| (.+?) \| \[", read(sp), re.M))
    tmm = []
    for f in chapters:
        d = f"{dec(f)[0]}.{dec(f)[1]}"
        h1 = next((ln[2:].strip() for ln in read(f).splitlines() if ln.startswith("# ")), "")
        want = f"{d} {spec_titles.get(d, '')}"
        if h1 != want:
            tmm.append(f"{os.path.basename(f)}: {h1!r} != {want!r}")
    check("chapter H1 titles match spec/structure.md", not tmm, f"{tmm[:4]}")
else:
    check("spec/structure.md exists", False, "file missing")

# 10. README, the site home page, and the contents page link every chapter file.
for navrel in ["README.md", "docs/index.md", "docs/front-matter/table-of-contents.md"]:
    nav = read(os.path.join(ROOT, navrel))
    linked = set(f"{int(a)}.{int(b)}" for a, b in re.findall(r"chapters/(\d+)-(\d+)-", nav))
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

# 12. The generated chapter map used by the guide_xref auto-linking extension
# matches the chapters on disk.
xr_path = os.path.join(ROOT, "guide_xref", "chapters.py")
if os.path.exists(xr_path):
    xr = dict(re.findall(r"^    \"(\d+\.\d+)\": \('([^']+)'", read(xr_path), re.M))
    want = {f"{dec(f)[0]}.{dec(f)[1]}": os.path.basename(f) for f in chapters}
    check("guide_xref/chapters.py matches disk", xr == want,
          f"stale entries: {sorted(set(xr.items()) ^ set(want.items()))[:6]}")
else:
    check("guide_xref/chapters.py exists", False, "file missing (run `just nav`)")

print()
if failures:
    print(f"RESULT: {len(failures)} check(s) FAILED")
    sys.exit(1)
print("RESULT: all checks passed")
sys.exit(0)
