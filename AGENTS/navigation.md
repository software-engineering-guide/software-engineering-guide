# Navigation: how the generated files work

Three navigation files are generated from the chapters, not written by hand:

- `README.md` (the table of contents on the repository home page)
- `front-matter/table-of-contents.md`
- `chapters/12.7-index.md` (the subject index)

They are produced by [`tools/gen_nav.py`](../tools/gen_nav.py). Do not edit them
by hand, because the next generation will overwrite your change.

## When to regenerate

Run `make nav` (or `python3 tools/gen_nav.py`) whenever you:

- add, remove, rename, or renumber a chapter, or
- change a chapter's `# N.M Title` heading (the TOC uses it).

## How it works

`gen_nav.py` reads every `chapters/*.md` file, sorts by decimal number, groups by
part, and:

- builds the part-by-part table of contents from each chapter's H1 title,
- writes it into `README.md` and `front-matter/table-of-contents.md`,
- scans the substantive chapters (Parts 1 through 11) for a fixed list of key
  terms and writes the subject index to `chapters/12.7-index.md`.

Part titles live in the `PART_TITLES` dictionary near the top of the script. The
generator uses colon-style part headers ("Part 1: People"), never em-dashes.

## What it does not touch

`spec/index.md` and `spec/structure.md` are the hand-authored source of truth.
The generator does not write them. If you change the structure, update
`spec/structure.md` yourself, then run `make nav` for the derived files and
`make test` to confirm everything lines up.
