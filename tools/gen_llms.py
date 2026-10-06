#!/usr/bin/env python3
"""Generate llms.txt and llms.json for AI agents and crawlers.

Run:  just llms   (or: python3 tools/gen_llms.py)

Both files are written to the repository root. They are derived from the
single sources of truth: the locale directories under locales/ and the
topics_slug column of spec/locales-for-global-sharing-with-svelte/locales.tsv.
Never hand-edit the output; re-run this script after adding or renaming a
topic or locale. The separate software-engineering-guide.github.io repository
serves them at the site root.

llms.txt follows the llmstxt.org convention (H1, blockquote summary, then
sections of links). llms.json carries the same information for programs.
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://software-engineering-guide.github.io"
REPO = "https://github.com/software-engineering-guide/software-engineering-guide"
OUT = os.environ.get("LLMS_OUT") or ROOT
TSV = os.path.join(ROOT, "spec", "locales-for-global-sharing-with-svelte", "locales.tsv")
DEFAULT_LOCALE = "en-us"
SUMMARY = (
    "An open guidebook of software engineering best practices for large developer "
    "teams, including enterprise and government: 147 chapters (called topics) across "
    "12 parts, plus front matter and appendices, in a warm, plain, opinionated style."
)


def locale_table():
    """Return [(code, label, topics_slug)] for every locale with a topics directory."""
    rows = []
    for line in open(TSV, encoding="utf-8").read().splitlines()[1:]:
        c = line.split("\t")
        if len(c) >= 4 and os.path.isdir(os.path.join(ROOT, "locales", c[0], c[3])):
            label = c[1] if c[1] and c[1] != "?" else c[2]
            rows.append((c[0], label, c[3]))
    return rows


def topics(code, slug):
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, "locales", code, slug, "*", "index.md"))):
        base = os.path.basename(os.path.dirname(path))
        m = re.match(r"(\d+)-(\d+)-", base)
        if not m:
            continue
        h1 = next((l for l in open(path, encoding="utf-8").read().splitlines() if l.startswith("# ")), "# ")
        title = re.sub(r"^#\s+\d+\.\d+\s+", "", h1).strip()
        out.append({"number": f"{int(m.group(1))}.{int(m.group(2))}", "title": title,
                    "url": f"{SITE}/{code}/{slug}/{base}/"})
    return out


def main():
    table = locale_table()
    data = {
        "name": "Software Engineering Guide",
        "description": SUMMARY,
        "site": SITE + "/",
        "repository": REPO,
        "defaultLocale": DEFAULT_LOCALE,
        "conventions": {
            "urlPattern": SITE + "/<locale>/<topics-segment>/<topic-directory>/",
            "topicsSegment": "Translated per locale; the topics_slug column of spec/locales-for-global-sharing-with-svelte/locales.tsv",
            "sourceOfTruth": "locales/en-us/ (English); other locales are hand-translated",
            "specification": REPO + "/tree/main/spec",
            "agentGuide": REPO + "/blob/main/AGENTS.md",
            "topicNumbering": "Parts are whole numbers; topics are decimals (N.0 introduces part N, N.1, N.2, ... follow).",
        },
        "locales": [{"code": c, "label": lab, "home": f"{SITE}/{c}/", "topicsSegment": s,
                     "topics": topics(c, s)} for c, lab, s in table],
    }
    with open(os.path.join(OUT, "llms.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")

    en = next(l for l in data["locales"] if l["code"] == DEFAULT_LOCALE)
    lines = [f"# {data['name']}", "", f"> {SUMMARY}", "",
             "The guide is published in several locales. The English locale below is the default; "
             "every other locale uses the same URL pattern with its own code and topics segment, "
             "and the full list of topics per locale is in llms.json.", "",
             "## Start here", "",
             f"- [Home]({SITE}/{DEFAULT_LOCALE}/): the opening page",
             f"- [Contents]({SITE}/{DEFAULT_LOCALE}/contents/): all parts and topics"]
    part = None
    for t in en["topics"]:
        p = int(t["number"].split(".")[0])
        if p != part:
            part = p
            lines += ["", f"## Part {p}", ""]
        lines.append(f"- [{t['number']} {t['title']}]({t['url']})")
    lines += ["", "## Locales", ""]
    lines += [f"- [{lab} ({c})]({SITE}/{c}/)" for c, lab, _ in table]
    lines += ["", "## For contributors and agents", "",
              f"- [AGENTS.md]({REPO}/blob/main/AGENTS.md): repository orientation and the golden rules",
              f"- [spec/]({REPO}/tree/main/spec): the specification, the single source of truth",
              f"- [llms.json]({SITE}/llms.json): the same information, machine-readable, for every locale", ""]
    with open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Wrote llms.txt and llms.json for {len(table)} locale(s), {len(en['topics'])} topics in {DEFAULT_LOCALE}.")


if __name__ == "__main__":
    main()
