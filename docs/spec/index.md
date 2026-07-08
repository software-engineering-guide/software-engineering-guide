# Specification

This directory is the specification-driven source of truth for the guidebook.
The chapters, navigation, and appendices are built to conform to what is written
here, and the test suite enforces it. If you want to change what the book is or
how it reads, change the spec first, then bring the chapters into line.

## The spec files

- **[structure.md](structure.md)** is the canonical manifest: every part and
  chapter, with its decimal number, title, and file. It is the authority for
  what chapters exist and how they are numbered. `tests/validate.py` checks that
  the files on disk match it exactly.
- **[conventions.md](conventions.md)** is the writing and format specification:
  the chapter template, the numbering scheme, the house style, and the rules the
  tests enforce (no em-dashes, define terms on first use, and so on).
- **[roadmap.md](roadmap.md)** is the authoring backlog and the adoption
  checklists organizations can use to put the recommendations into practice.

The rendered book lives in [`../index.md`](../index.md) (the site home page
and table of contents), [`../front-matter/`](../front-matter/table-of-contents.md)
(introduction and contents), and `../chapters/` (100 flat, decimal-numbered
chapter files; Part 12 holds the appendices). The site is published with
Zensical; the navigation in `zensical.toml` is generated from the chapters.

## How the pieces fit together

1. `spec/structure.md` and `spec/conventions.md` define what should exist and how
   it should read.
2. The chapter files in `../chapters/` are written to satisfy that definition.
3. `tools/gen_nav.py` (at the repository root) derives the README table of
   contents, the site home page, the `front-matter/table-of-contents.md` page,
   the subject index (`chapters/12.7-index.md`), and the `nav` block in
   `zensical.toml` from the chapter files.
4. `tests/validate.py` (at the repository root) checks the whole thing back against the spec: the
   count, the numbering, the required sections, the style rules, the links, and
   whether `structure.md` still matches the files on disk.

Run `just test` (or `python3 tests/validate.py`) after any change. Run
`just nav` (or `python3 tools/gen_nav.py`) after adding, removing, or renaming a
chapter, so the generated navigation stays in sync.

## Purpose and audience

- **Purpose:** give large teams a shared, opinionated baseline of practices that
  scale across hundreds or thousands of engineers, multiple business units, and
  multi-year (often multi-decade) system lifetimes.
- **Primary audience:** engineering leaders, staff and principal engineers,
  architects, platform teams, security teams, and program managers in enterprise
  and government contexts.
- **Secondary audience:** any engineer who wants to understand the reasoning
  behind an organization's standards.

## Guiding principles (the spine of the book)

1. Optimize for the team and the decade, not the individual and the sprint.
2. Make the right thing the easy thing: invest in paved roads and golden paths.
3. Prefer boring, proven technology; reserve novelty budget for differentiators.
4. Everything as code: infrastructure, policy, pipelines, docs, and configuration.
5. Shift left, and shift everywhere: quality, security, and accessibility early and continuous.
6. Automate toil; reserve human judgment for design, risk, and ethics.
7. Measure outcomes, not activity: instrument, learn, and iterate.
8. Design for failure, change, and audit: assume incidents, turnover, and scrutiny.
9. Least privilege and least surprise, in security and in APIs alike.
10. Inclusive by default: accessible, internationalized, and equitable.

## Cross-cutting themes

Security, privacy, and accessibility appear in every part, not once. Automation
and "everything as code" underpin repeatability and audit. Measurement and
feedback loops turn practices into learning systems. Documentation and knowledge
continuity protect against turnover and scale. Regulatory and government
constraints are treated as design inputs, not afterthoughts.
