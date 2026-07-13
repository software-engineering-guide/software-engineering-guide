# Changelog

Notable changes to the guidebook and its tooling. The most recent entries are at
the top. Dates use ISO 8601 (YYYY-MM-DD).

## [Unreleased]

### Added

- A Claude Code SessionStart hook (`.claude/hooks/session-start.sh`) that
  syncs dependencies and installs the pre-commit hooks when a session opens,
  in the web sandbox and the CLI alike. The codespell pre-commit hook now
  runs from the uv-managed dev dependencies instead of cloning GitHub, so
  hook install and execution need no network access.
- Tooling and enforcement gates (Phase 1 of `tasks.md`): a PR validation
  workflow (`test.yml`) that runs the full check suite and site build without
  deploying; five new validator checks (template section order, a 2,000-word
  minimum for content chapters, H1 titles matched against `spec/structure.md`,
  dangling prose cross-references, and an en-dash-only-in-numeric-ranges
  policy); codespell with `just spell`; Vale with a `styles/Guide/` rule set
  and `just lint` (errors block CI, warnings inform); a pre-commit
  configuration; a weekly external link check (`links.yml`, lychee) that
  reports into a single issue; and `tools/stats.py`, a Markdown stats report
  behind `just stats`.
- Ten more chapters, taking the book from 123 to 133: 1.11 Engineering
  management; 1.12 Diversity, equity, inclusion, and belonging; 2.20 Error
  handling and resilience patterns; 3.14 Multi-tenancy and SaaS architecture;
  5.8 Design research and usability testing; 5.9 Service design; 6.8 AI
  evaluation and testing; 10.16 Stakeholder management and communication; 10.17
  Organizational change management; and 10.18 Open source program office (OSPO)
  and upstream contribution.
- Twelve more chapters, taking the book from 111 to 123: 2.17 Concurrency and
  parallelism; 2.18 Dependency and supply-chain management; 2.19 Refactoring and
  technical debt; 3.11 Cloud architecture; 3.12 Event-driven architecture and
  messaging; 3.13 Networking and connectivity; 7.6 Real-time and streaming data;
  7.7 Data modeling and the semantic layer; 7.8 Data quality and observability;
  9.6 Chaos engineering and resilience testing; 10.14 Product management and
  discovery; and 10.15 Estimation and forecasting.
- Ten new chapters, taking the book from 100 to 111: 1.8 Hiring, interviewing,
  and onboarding; 1.9 Distributed and remote work; 1.10 Engineering
  effectiveness and developer productivity; 2.15 Debugging and troubleshooting;
  2.16 Performance engineering; 4.7 Identity and access management; 4.8
  Cryptography and key management; 6.7 AI agents and agentic systems; 8.6 Release
  management and progressive delivery; and 9.5 Disaster recovery and business
  continuity. Each follows the full chapter template.
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

- Renamed every chapter file to a zero-padded, dash-separated, sortable prefix,
  `PP-CC-slug.md` (for example `01-00-people.md`, `08-01-ci-cd-and-delivery.md`),
  so a plain lexical sort lists chapters in reading order. Chapter numbers in
  prose, headings, and cross-references stay in the unpadded dotted form (`8.1`).
  The convention is recorded in the spec, and the `gen_nav.py` and `validate.py`
  parsers were updated accordingly.
- Split the combined OKR/KPI chapter into two: 11.4 Objectives and key results
  (OKRs) and 11.5 Key performance indicators (KPIs), each a standalone chapter.
- Raised the target chapter length in the spec to roughly 3,000 words, deepening
  recommendations, examples, and trade-offs rather than padding.
- Moved the specification out of `docs/spec/` to the repository root at `spec/`,
  making it the standalone source of truth for the book (chapters as Markdown)
  rather than a published site section. Added `spec/mkdocs-zensical/index.md` as
  the source of truth for the rendering side effects (site build, navigation,
  deployment). The site navigation no longer lists a "Specification" section, and
  the tests, `AGENTS.md`, `SITE.md`, `CONTRIBUTING.md`, and the contributor
  guides now point at the repository-root `spec/`.
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
