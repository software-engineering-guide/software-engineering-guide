# Software Engineering Guide: Specification

This is the source of truth for the guide. The guide is a **book**. The book is
made of **chapters**. The chapters are **Markdown**. The words in those chapters
are the product. Everything else in the repository exists to serve them.

If you are an author or an agent about to change anything, read this file first.
It tells you what the book is, how spec-driven development works here, and which
rules you may not break.

## This is a book, not a website

The book is written and lives as Markdown chapters. It is authored, read,
reviewed, and versioned as prose. The published website is a rendering of that
prose, not the thing itself.

- The **source of truth** is the Markdown in `docs/chapters/`, the front matter,
  the appendices, and this specification.
- The **website is a side effect.** It is generated from the same Markdown by a
  static site generator. How that works, what it produces, and how it deploys is
  a separate concern, specified in
  [mkdocs-zensical/index.md](mkdocs-zensical/index.md). Nothing in that layer
  decides what the book says.
- If the site and the book ever disagree, the **book wins.** You could delete the
  site generator, the theme, and the entire toolchain, and still have the whole
  book intact in plain text. That is the test of what is authoritative here.

So write for a reader holding a book, chapter by chapter. Do not write for a
navigation sidebar, a search box, or a theme. Those are downstream.

## What spec-driven development means here

The spec comes first, the chapters conform to it, and the tests enforce it.

1. **Declare intent in the spec.** What chapters exist, in what order, and what
   shape each chapter takes is decided here and in the companion spec files, not
   improvised chapter by chapter.
2. **Bring the chapters into line.** Chapters are written and edited to satisfy
   the spec. A chapter that does not follow the template or the house style is a
   defect, not a variation.
3. **Enforce mechanically what can be enforced.** `tests/validate.py` checks the
   structure and the rules that a machine can check. `just test` must pass before
   any change is considered done.

The rule that ties these together: **change the spec and the chapters in the same
change.** Never let the manifest, the conventions, and the actual chapter files
drift apart. If you want to change what the book is or how it reads, edit the
spec first, then make the chapters match.

## The specification files

This overview is the entry point for the **content**. The enforceable detail
lives in three companion files.

- **[structure.md](structure.md)** is the canonical manifest: every part and
  every chapter, with its decimal number, title, and file name. It is the sole
  authority for which chapters exist and how they are numbered. The test suite
  checks that the files on disk match it exactly.
- **[conventions.md](conventions.md)** is the writing and format specification:
  the numbering scheme, the chapter template, the house style, and the hard rules
  the tests enforce.
- **[roadmap.md](roadmap.md)** is the authoring backlog and the adoption
  checklists organizations can use to put the guidance into practice.

The **rendering** side effects (the MkDocs and Zensical website, the generated
navigation, and the deployment) are specified separately in
[mkdocs-zensical/index.md](mkdocs-zensical/index.md). Keep the two apart on
purpose: this file and its companions govern the book; that file governs the
machine that renders it.

## The shape of the book

The book is organized as numbered parts, each made of numbered chapters.

- Parts are whole numbers (1 through 12). Chapters are decimals within a part,
  for example `8.1`.
- Chapter **N.0** is the part introduction. Chapters **N.1, N.2, ...** are the
  content chapters. Numbering within a part is contiguous and starts at N.0.
- Chapter files live in `docs/chapters/` and are named `PP-CC-slug.md` with a
  zero-padded, dash-separated, sortable numeric prefix (two-digit part, two-digit
  chapter; the N.0 introduction is `PP-00`), for example `01-00-people.md` and
  `08-01-ci-cd-and-delivery.md`, so a plain lexical sort lists them in reading
  order. The slug is lowercase with dashes.
- The first heading of every chapter file is `# N.M Title` using the unpadded,
  dotted chapter number, and that number must match the file's `PP-CC` prefix.
- Part 12 is the appendices: glossary, checklists, templates, maturity
  self-assessment, references, adoption roadmap, and index.

The authoritative list of parts and chapters is [structure.md](structure.md).
This overview never restates that list, so the two can never fall out of sync.

## The chapter template

Every content chapter (N.1 and up, in Parts 1 through 11) uses these sections, in
this order. All are required and checked.

1. `# N.M Title`
2. `## Overview and motivation`
3. `## Key principles`
4. `## Recommendations`
5. `## Trade-offs: pros and cons`
6. `## Questions to discuss with your team`
7. `## Examples`
8. `## Business case: motivations, ROI, and TCO`
9. `## Anti-patterns and pitfalls`
10. `## Maturity model`
11. `## Ideas for discussion`
12. `## Key takeaways`
13. `## References and further reading`

Part introductions (N.0) use a lighter shape: two or three framing paragraphs, a
`## Chapters in this part` list, and a `## How these chapters interrelate`
section. The full definition of each section, including what belongs inside it,
is in [conventions.md](conventions.md).

## Golden rules

These come from the house style and are not negotiable. The full, enforceable
version is in [conventions.md](conventions.md).

1. **No em-dashes.** Never use the em-dash character (U+2014). Use a comma, a
   colon, parentheses, or two sentences. En-dashes are allowed only in numeric
   ranges.
2. **No stock LLM phrasing.** No "not only ... but also", no "load-bearing", no
   "It's important to note", and no similar filler.
3. **Follow the chapter template.** Content chapters use the fixed section order
   above.
4. **Define terms on first use, and link key concepts to Wikipedia** on first
   mention. Real references only; never fabricate a work or a URL.
5. **The spec is the source of truth.** Structure is declared in
   [structure.md](structure.md); style is declared in
   [conventions.md](conventions.md). Change the spec and the chapters together.
6. **Tests must pass.** Run `just test` before you consider a change done.

## The usual workflow

1. Decide the change as a change to the book: which chapters, which sections,
   which words.
2. Edit the spec first if the change touches structure, numbering, or
   conventions.
3. Edit or write the chapters to match, following the template and the house
   style.
4. If the set of chapters changed, regenerate the rendering artifacts as
   described in [mkdocs-zensical/index.md](mkdocs-zensical/index.md) (`just nav`).
   That regeneration is downstream bookkeeping; the book is already correct
   before it runs.
5. Run `just test`. Fix anything it reports.
6. Record the change in `docs/project/changelog.md`.
