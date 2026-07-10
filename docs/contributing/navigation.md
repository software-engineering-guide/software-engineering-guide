# Navigation: how the generated files work

Five navigation artifacts are generated from the chapters, not written by hand:

- `README.md` (the table of contents on the repository home page)
- `docs/index.md` (the home page of the published site)
- `docs/front-matter/table-of-contents.md`
- `docs/chapters/12.7-index.md` (the subject index, with links)
- the `nav` block in `zensical.toml` (the site navigation)
- `guide_xref/chapters.py` (the chapter map used to auto-link plain-text
  cross-references like "chapter 8.1" when the site is built)

They are produced by
[`tools/gen_nav.py`](https://github.com/software-engineering-guide/software-engineering-guide/blob/main/tools/gen_nav.py).
Do not edit them by hand, because the next generation will overwrite your
change.

## When to regenerate

Run `just nav` (or `python3 tools/gen_nav.py`) whenever you:

- add, remove, rename, or renumber a chapter, or
- change a chapter's `# N.M Title` heading (the TOC uses it).

## How it works

`gen_nav.py` reads every `docs/chapters/*.md` file, sorts by decimal number,
groups by part, and:

- builds the part-by-part table of contents from each chapter's H1 title,
- writes it into `README.md`, `docs/index.md`, and
  `docs/front-matter/table-of-contents.md`,
- rewrites the `nav` block in `zensical.toml` between its marker comments, so
  the site navigation always lists every page,
- scans the substantive chapters (Parts 1 through 11) for a fixed list of key
  terms and writes the subject index to `docs/chapters/12.7-index.md`,
- regenerates `guide_xref/chapters.py` so build-time cross-reference linking
  always matches the chapters on disk.

Part titles live in the `PART_TITLES` dictionary near the top of the script. The
generator uses colon-style part headers ("Part 1: People"), never em-dashes.

## What it does not touch

The specification at the repository root (`spec/index.md`, `spec/structure.md`,
and its companions) is the hand-authored source of truth. The generator does not
write it, and it is not part of the published site. If you change the structure,
update `spec/structure.md` yourself, then run `just nav` for the derived files and
`just test` to confirm everything lines up.
