# Documentation

Project documentation for the guidebook: how it is put together, how to build and
check it, and where the source of truth lives. For the book itself, see the
[table of contents](../README.md).

## Map of the project

- **The book:** `chapters/` (100 files), `front-matter/`, and the appendices in
  Part 12. The [repository index](../index.md) links every piece.
- **Source of truth:** [`spec/`](../spec/index.md). The structure is declared in
  `spec/structure.md` and the writing rules in `spec/conventions.md`. Everything
  else is built to match.
- **Tooling:** `tools/gen_nav.py` generates navigation; `tests/validate.py`
  enforces the spec; the `Makefile` wires them together.
- **Contributor guidance:** [`AGENTS.md`](../AGENTS.md),
  [`CONTRIBUTING.md`](../CONTRIBUTING.md), and the guides under `AGENTS/`.

## Build and check

Everything runs on Python 3 with no other dependencies and no network access.

```sh
make test    # validate structure, style, links, and spec-vs-disk
make nav     # regenerate README TOC, contents page, and subject index
make build   # nav, then test
make stats   # chapter and word counts
```

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

- **Flat, decimal-numbered chapters.** Files are `chapters/N.M-slug.md`. The part
  is a whole number; the chapter is a decimal; N.0 is the part introduction. This
  keeps stable identifiers and lets tools sort and group without a directory tree.
- **Generated navigation.** The table of contents, contents page, and subject
  index are generated, so they never drift from the chapters.
- **Offline, dependency-free tests.** The suite uses only the standard library so
  it runs anywhere, including CI and pre-commit hooks.
- **No em-dashes, by rule and by test.** A deliberate style choice, enforced so
  it stays true as the book grows.

## Further reading

- [`AGENTS/authoring.md`](../AGENTS/authoring.md) : writing and editing chapters.
- [`AGENTS/navigation.md`](../AGENTS/navigation.md) : how the generated files work.
- [`AGENTS/testing.md`](../AGENTS/testing.md) : what the tests check and how to fix failures.
- [`examples/`](../examples/) : small, concrete examples.
