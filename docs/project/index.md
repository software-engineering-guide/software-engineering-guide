# About this project

Project documentation for the guidebook: how it is put together, how to build and
check it, and where the source of truth lives. For the book itself, see the
[table of contents](../index.md).

## Map of the project

- **The book:** `docs/chapters/` (100 files), `docs/front-matter/`, and the
  appendices in Part 12.
- **Source of truth:** `spec/` at the repository root (not published to the
  site). The structure is declared in `spec/structure.md` and the writing rules
  in `spec/conventions.md`. Everything else is built to match.
- **Tooling:** `tools/gen_nav.py` generates navigation; `tests/validate.py`
  enforces the spec; the `justfile` wires them together.
- **Contributor guidance:**
  [`AGENTS.md`](https://github.com/software-engineering-guide/software-engineering-guide/blob/main/AGENTS.md)
  at the repository root, and the guides in the
  [contributing section](../contributing/index.md).

## Build and check

The validation suite runs on Python 3 with no other dependencies and no network
access. Tasks run through [just](https://github.com/casey/just).

```sh
just test    # validate structure, style, links, and spec-vs-disk
just nav     # regenerate the generated navigation files
just check   # nav, then test
just stats   # chapter and word counts
```

This repository holds the book's content and specification. It is rendered
into a website by the separate
[`software-engineering-guide.github.io`](https://github.com/software-engineering-guide/software-engineering-guide.github.io)
repository.

## How specification-driven development works here

The specification comes first. `spec/structure.md` says which chapters exist and
how they are numbered. `spec/conventions.md` says how they must be written. The
chapters are authored to satisfy both. `tools/gen_nav.py` derives the navigation
from the chapters, and `tests/validate.py` checks the result back against the
spec. If the chapters and the spec ever disagree, the tests fail, which is the
signal to bring them back into line.

This keeps drift out: a change is only "done" when the spec, the chapters, the
generated navigation, and the tests all agree.

## Design decisions worth knowing

- **Flat, decimal-numbered chapters.** Files are `docs/chapters/N.M-slug.md`.
  The part is a whole number; the chapter is a decimal; N.0 is the part
  introduction. This keeps stable identifiers and lets tools sort and group
  without a directory tree.
- **Generated navigation.** The table of contents, contents page, and subject
  index are generated, so they never drift from the chapters.
- **Offline, dependency-free tests.** The suite uses only the standard library so
  it runs anywhere, including CI and pre-commit hooks.
- **Cross-references stay plain text.** Prose refers to chapters by decimal
  number ("see chapter 8.1"), as the spec requires; the rendering site is
  responsible for turning those references into links.
- **No em-dashes, by rule and by test.** A deliberate style choice, enforced so
  it stays true as the book grows.

## Further reading

- [Authoring](../contributing/authoring.md) : writing and editing chapters.
- [Navigation](../contributing/navigation.md) : how the generated files work.
- [Testing](../contributing/testing.md) : what the tests check and how to fix failures.
- [Examples](../examples/index.md) : small, concrete examples.
- [Changelog](changelog.md) : history of notable changes.
