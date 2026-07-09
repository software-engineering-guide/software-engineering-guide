# Changelog

Notable changes to the guidebook and its tooling. The most recent entries are at
the top. Dates use ISO 8601 (YYYY-MM-DD).

## [Unreleased]

### Added

- A "Questions to discuss with your team" section to every content chapter,
  placed before the examples, with three chapter-specific questions each backed
  by a comprehensive paragraph of context (81 chapters). The section is now part
  of the chapter template, the conventions spec, and the enforced test suite.
- A published documentation site built with Zensical, configured in
  `zensical.toml`, deployed to GitHub Pages by a GitHub Actions workflow, and
  described in `SITE.md`. Dependencies are managed with uv and tasks run
  through a `justfile` (which replaces the `Makefile`).
- A dev container definition (`.devcontainer/`) with uv, just, and git-lfs for
  building and serving the site.
- Build-time auto-linking of chapter cross-references: the `guide_xref`
  Markdown extension links plain-text references ("chapter 8.1", "(10.1)",
  reference tables) to the matching chapter pages on the published site, with
  tests in `tests/test_xref.py`; the generated subject index now links every
  entry.
- A startup example to every content chapter, placed before the enterprise and
  government examples, so each topic is illustrated at early-stage as well as at
  large-organization scale (81 chapters).
- Repository infrastructure: `AGENTS.md` with per-task guides and shared snippets
  under `AGENTS/`, a specification-driven `spec/` (structure, conventions,
  roadmap), a validation suite in `tests/validate.py`, the navigation generator
  moved into `tools/gen_nav.py`, a `Makefile`, `CONTRIBUTING.md`, `docs/`,
  `examples/`, and this changelog.
- `spec/structure.md`, the canonical chapter manifest that the tests check the
  files against.

### Changed

- Adopted the upstream README title and introduction ("Software Engineering
  Guide") in the generated navigation and the site name, and moved the project
  logo to `docs/assets/logo.png` so the published site uses it as its logo and
  favicon.
- Restructured the repository for site publishing: the book now lives under
  `docs/` (`docs/chapters/`, `docs/front-matter/`, `docs/spec/`,
  `docs/examples/`), the contributor guides moved to `docs/contributing/`, and
  the project documentation and this changelog moved to `docs/project/`.
- Consolidated the two goals-and-metrics chapters (OKRs and KPIs) into a single
  chapter, 11.4 "Objectives, key results, and key performance indicators," to
  reach exactly 100 chapters with no loss of substance.
- Updated the introduction's parts list so it reflects the chapters added after
  it was first written (systems engineering, embedded and real-time systems,
  interoperability, mobile, and OKRs and KPIs).
- `spec/index.md` rewritten as a hand-authored specification entry point; it is
  no longer overwritten by the navigation generator.

### Fixed

- Corrected three SWEBOK crosswalk entries that pointed to "2.3.1" instead of
  chapter 2.13, and reworded four bare cross-references to the house-style
  "chapter N.M" form.
- Removed all em-dashes across the book and reworded the text so it reads
  naturally, and removed stock LLM phrasing. Both are now enforced by the tests.

## History

The guidebook was built up in stages: an initial outline; full chapters across
ten parts; a flow part for discovery and delivery pipelines; alignment with the
SWEBOK body of knowledge; integration of ideas from public-sector engineering
handbooks; a warmth-and-readability pass; comprehensive Wikipedia linking with
link validation; and citation verification. It now stands at 12 parts and 100
chapters, with front matter and appendices.

## Conventions for this file

- Group changes under **Added**, **Changed**, **Fixed**, **Removed**, or
  **Deprecated**.
- Keep entries short and specific. One line each where possible.
- Do not use em-dashes here either; the tests check this file too.
