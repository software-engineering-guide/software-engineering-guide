# AGENTS

Guidance for AI agents and human contributors working in this repository. Read
this first. It is short on purpose; the details live in the linked files.

## What this repo is

An open guidebook of software engineering best practices for large developer
teams, including enterprise and government. It is 100 chapters across 12 parts,
plus front matter and appendices. The writing is deliberately warm, plain, and
opinionated, and it follows a strict house style.

## Golden rules (do not break these)

1. **No em-dashes.** Never use "—" (U+2014). Use a comma, colon, parentheses, or
   two sentences. En-dashes "–" are allowed only in numeric ranges.
2. **No stock LLM phrasing.** No "not only ... but also", "but also", or
   "load-bearing"; no "It's important to note", "In today's fast-paced world",
   and similar filler.
3. **Follow the chapter template.** Content chapters use the fixed section order
   in [`AGENTS/share/chapter-template.md`](AGENTS/share/chapter-template.md).
4. **Define terms on first use** and **link key concepts to Wikipedia** on first
   mention. Real references only; never fabricate a work or a URL.
5. **The spec is the source of truth.** Structure is declared in
   [`spec/structure.md`](spec/structure.md); style is declared in
   [`spec/conventions.md`](spec/conventions.md). Change the spec and the chapters
   together.
6. **Tests must pass.** Run `make test` before you consider a change done.

The full, enforceable version of rules 1 through 5 is
[`AGENTS/share/style-rules.md`](AGENTS/share/style-rules.md) and
[`spec/conventions.md`](spec/conventions.md).

## Repository layout

- `chapters/` : the 100 chapter files, named `N.M-slug.md` (flat, decimal-numbered).
- `front-matter/` : the opening essay, introduction, and table of contents.
- `spec/` : the specification-driven source of truth (structure, conventions, roadmap).
- `tools/` : `gen_nav.py`, which generates the README TOC, the contents page, and the subject index.
- `tests/` : `validate.py`, the enforcement suite.
- `docs/` : how to build, contribute, and understand the project.
- `examples/` : small illustrative examples (a chapter skeleton, OKRs, an ADR).
- `AGENTS/` : this guidance, plus per-task guides and shared snippets.

## Task guides

- Writing or editing a chapter: [`AGENTS/authoring.md`](AGENTS/authoring.md)
- Regenerating navigation after structure changes: [`AGENTS/navigation.md`](AGENTS/navigation.md)
- Running and understanding the tests: [`AGENTS/testing.md`](AGENTS/testing.md)

## Shared snippets

- Blank chapter template: [`AGENTS/share/chapter-template.md`](AGENTS/share/chapter-template.md)
- Style rules (enforceable): [`AGENTS/share/style-rules.md`](AGENTS/share/style-rules.md)
- Part index: [`AGENTS/share/part-index.md`](AGENTS/share/part-index.md)

## The usual workflow

1. Read the relevant task guide above.
2. Make the smallest change that satisfies the request.
3. If you changed the set of chapters, update `spec/structure.md` and run
   `make nav`.
4. Run `make test`. Fix anything it reports.
5. Update `CHANGELOG.md` with a one-line summary of what changed.

Every file in `AGENTS/` and `AGENTS/share/` is kept small (well under 40 KB) so
it loads cheaply into an agent's context.
