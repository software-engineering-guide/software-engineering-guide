#!/usr/bin/env python3
"""Generate sitemap.xml for search engines.

Run:  just sitemap   (or: python3 tools/gen_sitemap.py)

Written to the repository root. Derived from the locale directories under
locales/ and the topics_slug column of
spec/locales-for-global-sharing-with-svelte/locales.tsv; never hand-edit it.
The separate software-engineering-guide.github.io repository serves it at the
site root.

URLs follow spec/locales-for-global-sharing-with-svelte/index.md: /<code>/,
/<code>/contents/, /<code>/about/, and /<code>/<topics_slug>/<topic>/. Each
topic lists its translations as hreflang alternates, matched through the shared
.locale-peer-id. Language aliases (/en/) are not listed: they carry a canonical
link to the -001 URL. The root / is the search and redirect page, also omitted.
"""
import glob
import os
import re
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://software-engineering-guide.github.io"
OUT = os.environ.get("SITEMAP_OUT") or ROOT
TSV = os.path.join(ROOT, "spec", "locales-for-global-sharing-with-svelte", "locales.tsv")
DEFAULT_LOCALE = "en-us"


def locale_table():
    rows = []
    for line in open(TSV, encoding="utf-8").read().splitlines()[1:]:
        c = line.split("\t")
        if len(c) >= 4 and os.path.isdir(os.path.join(ROOT, "locales", c[0], c[3])):
            rows.append((c[0], c[3]))
    return rows


def main():
    table = locale_table()
    by_peer = {}   # peer id -> [(code, url)]
    pages = []     # (url, peer id or None)
    for code, slug in table:
        pages += [(f"{SITE}/{code}/", None), (f"{SITE}/{code}/contents/", None),
                  (f"{SITE}/{code}/about/", None)]
        for d in sorted(glob.glob(os.path.join(ROOT, "locales", code, slug, "*", "index.md"))):
            topic = os.path.dirname(d)
            if not re.match(r"\d+-\d+-", os.path.basename(topic)):
                continue
            pid_path = os.path.join(topic, ".locale-peer-id")
            pid = open(pid_path).read().strip() if os.path.exists(pid_path) else None
            url = f"{SITE}/{code}/{slug}/{os.path.basename(topic)}/"
            pages.append((url, pid))
            if pid:
                by_peer.setdefault(pid, []).append((code, url))
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for url, pid in pages:
        out.append("  <url>")
        out.append(f"    <loc>{escape(url)}</loc>")
        alts = by_peer.get(pid, []) if pid else []
        if len(alts) > 1:
            for code, alt in alts:
                out.append(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{escape(alt)}"/>')
            default = next((a for c, a in alts if c == DEFAULT_LOCALE), None)
            if default:
                out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{escape(default)}"/>')
        out.append("  </url>")
    out.append("</urlset>")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"Wrote sitemap.xml: {len(pages)} URLs across {len(table)} locale(s).")


if __name__ == "__main__":
    main()
