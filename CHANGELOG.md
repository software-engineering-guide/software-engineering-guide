# Changelog

Notable changes to the guidebook and its tooling. The most recent entries are at
the top. Dates use ISO 8601 (YYYY-MM-DD).

## [Unreleased]

### Added
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
- Consolidated the two goals-and-metrics chapters (OKRs and KPIs) into a single
  chapter, 11.4 "Objectives, key results, and key performance indicators," to
  reach exactly 100 chapters with no loss of substance.
- Updated the introduction's parts list so it reflects the chapters added after
  it was first written (systems engineering, embedded and real-time systems,
  interoperability, mobile, and OKRs and KPIs).
- `spec/index.md` rewritten as a hand-authored specification entry point; it is
  no longer overwritten by the navigation generator.

### Fixed
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
