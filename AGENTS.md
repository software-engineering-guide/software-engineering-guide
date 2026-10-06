# AGENTS

Guidance for AI agents and human contributors working in this repository. Read
this first. It is short on purpose; the details live in the linked files.

## What this repo is

An open guidebook of software engineering best practices for large developer
teams, including enterprise and government. It is 147 chapters across 12 parts,
plus front matter and appendices. The writing is deliberately warm, plain, and
opinionated, and it follows a strict house style. This repository holds the
book's content and specification; it is rendered into a website by the
separate `software-engineering-guide.github.io` repository.

## Golden rules (do not break these)

1. **No em-dashes.** Never use "—" (U+2014). Use a comma, colon, parentheses, or
   two sentences. En-dashes "–" are allowed only in numeric ranges.
2. **No stock LLM phrasing.** No "not only ... but also", "but also", or
   "load-bearing"; no "It's important to note", "In today's fast-paced world",
   and similar filler.
3. **Follow the chapter template.** Content chapters use the fixed section order
   in [`docs/contributing/chapter-template.md`](docs/contributing/chapter-template.md).
4. **Define terms on first use** and **link key concepts to Wikipedia** on first
   mention. Real references only; never fabricate a work or a URL.
5. **The spec is the source of truth.** It lives at the repository root in
   [`spec/`](spec/index.md), not under `docs/`, because the book (not the site)
   is what it governs. Structure is declared in
   [`spec/structure.md`](spec/structure.md); style is declared in
   [`spec/conventions.md`](spec/conventions.md). Change the spec and
   the chapters together.
6. **Tests must pass.** Run `just test` before you consider a change done.

The full, enforceable version of rules 1 through 5 is
[`docs/contributing/style-rules.md`](docs/contributing/style-rules.md) and
[`spec/conventions.md`](spec/conventions.md).

## Topic guides

- [`AGENTS/layout.md`](AGENTS/layout.md) : where everything lives, including the `locales/` tree
- [`AGENTS/style.md`](AGENTS/style.md) : the house style in one page
- [`AGENTS/locales.md`](AGENTS/locales.md) : translation, slugs, peer ids, URLs
- [`AGENTS/workflow.md`](AGENTS/workflow.md) : the usual workflow, git, dependencies

## Task guides

- Writing or editing a chapter: [`docs/contributing/authoring.md`](docs/contributing/authoring.md)
- Regenerating navigation after structure changes: [`docs/contributing/navigation.md`](docs/contributing/navigation.md)
- Running and understanding the tests: [`docs/contributing/testing.md`](docs/contributing/testing.md)

## Shared snippets

- Blank chapter template: [`docs/contributing/chapter-template.md`](docs/contributing/chapter-template.md)
- Style rules (enforceable): [`docs/contributing/style-rules.md`](docs/contributing/style-rules.md)
- Part index: [`docs/contributing/part-index.md`](docs/contributing/part-index.md)

## The usual workflow

Read the task guide, make the smallest change, run `just test`, update
`docs/project/changelog.md`. Details: [`AGENTS/workflow.md`](AGENTS/workflow.md).

Every file in `docs/contributing/` and `AGENTS/` is kept small (well under 40 KB) so it loads
cheaply into an agent's context.
