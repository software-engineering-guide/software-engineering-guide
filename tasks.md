# Improvement tasks

Actionable checklist implementing [`plan.md`](plan.md). Tasks are grouped into
phases; work the phases in order, but tasks marked **(P)** are parallelizable
within their phase. Every task ends with `just test` passing (run `just check`
if navigation or structure changed).

Legend: `[ ]` todo · `[~]` in progress · `[x]` done · **(P)** parallelizable.

Ground rules for every task (from [`AGENTS.md`](AGENTS.md)):

- No em-dashes (U+2014) anywhere; en-dashes only in numeric ranges.
- No stock LLM phrasing (see `docs/contributing/style-rules.md`).
- The spec is the source of truth: structural changes update
  [`spec/structure.md`](spec/structure.md) and content together.
- Adding or removing chapters requires updating the chapter-count constant in
  [`tests/validate.py`](tests/validate.py), the spec, and `just nav` output in
  the same change.
- New pages under `docs/` must be reachable from the Zensical nav (extend
  [`tools/gen_nav.py`](tools/gen_nav.py) when adding new document types).
- Real references only; never fabricate a work or URL.

---

## Phase 1: Tooling and enforcement gates

- [ ] 1.1 Add a PR validation workflow at `.github/workflows/test.yml`: on
      `pull_request` (and pushes to non-main branches), run `uv sync --locked`,
      `uv run python tests/validate.py`, `uv run python tests/test_xref.py`,
      and `uv run zensical build --clean`. Do not deploy. Keep the existing
      `docs.yml` deploy workflow unchanged.
- [ ] 1.2 **(P)** Extend `tests/validate.py`: enforce that the required `##`
      sections in substantive chapters appear in exactly the template order
      (compare the sequence, not just membership). Fix any chapters that fail.
- [ ] 1.3 **(P)** Extend `tests/validate.py`: minimum word count of 2,000 for
      substantive chapters (parts 1 through 11, chapter number >= 1), with an
      explicit allowlist for intentional exceptions. Emit the offending counts.
      (Bringing thin chapters up to depth is task 5.1; the allowlist may start
      large and shrink.)
- [ ] 1.4 **(P)** Extend `tests/validate.py`: chapter H1 titles must match the
      titles declared in `spec/structure.md`, character for character, not
      just the leading decimal. Fix mismatches on either side.
- [ ] 1.5 **(P)** Extend `tests/validate.py`: detect dangling prose
      cross-references. Reuse the reference pattern from
      `guide_xref/__init__.py` to find strings like "chapter 13.4" in all
      docs Markdown, and fail if the referenced chapter is not on disk. Add a
      matching test to `tests/test_xref.py` for the unknown-chapter case if
      one is not already there.
- [ ] 1.6 **(P)** Extend `tests/validate.py`: en-dash policy check. An
      en-dash (U+2013) may appear only between digits (numeric ranges).
      Fix violations.
- [ ] 1.7 **(P)** Add codespell: a `[tool.codespell]` section in
      `pyproject.toml` with an ignore list, a `just spell` target, and a run
      in the PR workflow. Fix every real misspelling it finds.
- [ ] 1.8 **(P)** Add a Vale configuration (`.vale.ini` plus a
      `styles/Guide/` rule set) encoding the house style: the banned-phrase
      list from `docs/contributing/style-rules.md`, the em-dash ban, and
      warnings for common filler phrases and stock LLM wording. Add `just lint`.
      Run it in the PR workflow at error severity only, so warnings inform
      but do not block.
- [ ] 1.9 **(P)** Add `.pre-commit-config.yaml` running the validator,
      codespell, and the em-dash grep on changed files. Document setup in
      `CONTRIBUTING.md`.
- [ ] 1.10 **(P)** Add a scheduled weekly workflow
      `.github/workflows/links.yml` running lychee over `docs/` and `spec/`
      with a committed `.lycheeignore`, opening or updating a single issue on
      failure. External links stay out of the PR path.
- [ ] 1.11 **(P)** Extend `just stats` into `tools/stats.py`: per-chapter word
      counts sorted ascending, chapters below target depth, Wikipedia links
      per chapter, reference-section entry counts, and totals. Output
      Markdown so reports can be pasted into issues.
- [ ] 1.12 Update `AGENTS.md`, `CONTRIBUTING.md`, and
      `docs/contributing/testing.md` to describe the new targets and checks
      added in this phase.

## Phase 2: Examples and tutorials

### Examples (each **(P)**; share one consistent fictional organization)

Each example: two or three sentences of scenario framing, a complete
realistic artifact, links back to the chapter and to the template in chapter
12.3 it illustrates, and an entry in the examples index and nav.

- [ ] 2.1 RFC example (`docs/examples/rfc-example.md`), anchored to the
      decision-making and decision-records chapters.
- [ ] 2.2 Postmortem example (`docs/examples/postmortem-example.md`),
      anchored to the incident-management chapter.
- [ ] 2.3 Runbook example (`docs/examples/runbook-example.md`), anchored to
      the SRE and operations chapters.
- [ ] 2.4 Threat model example (`docs/examples/threat-model-example.md`),
      STRIDE-based, anchored to the application-security chapter.
- [ ] 2.5 SLO document example (`docs/examples/slo-example.md`) with SLIs,
      targets, and an error-budget policy.
- [ ] 2.6 Risk register example (`docs/examples/risk-register-example.md`),
      anchored to the risk, audit, and assurance chapter.
- [ ] 2.7 Career ladder excerpt (`docs/examples/career-ladder-example.md`),
      two adjacent levels, anchored to the roles and growth chapter.
- [ ] 2.8 Incident communication timeline
      (`docs/examples/incident-comms-example.md`): internal updates plus a
      public status-page sequence.
- [ ] 2.9 C4 context and container description
      (`docs/examples/c4-example.md`), prose plus a Mermaid diagram if the
      site build supports it (verify first; otherwise structured text).
- [ ] 2.10 KPI tree example (`docs/examples/kpi-tree-example.md`) connecting
      one business outcome through product KPIs to team-level metrics,
      anchored to the OKR and KPI chapters.
- [ ] 2.11 Filled-in maturity self-assessment
      (`docs/examples/maturity-assessment-example.md`) for the fictional
      organization, anchored to chapter 12.4.
- [ ] 2.12 Update `docs/examples/index.md`, the templates appendix (chapter
      12.3, linking every template to its example), and the nav generator so
      all examples are listed and reachable.

### Tutorials

- [ ] 2.13 Create the tutorials scaffold: `docs/tutorials/index.md`, a
      tutorial template at `docs/contributing/tutorial-template.md` (goal,
      audience, prerequisites, numbered steps, verification, where to go
      next), a spec section registering the document type, nav-generator and
      `zensical.toml` support, and a validator check that tutorials follow
      the template sections. This task blocks 2.14 through 2.21.
- [ ] 2.14 **(P)** Tutorial: write your first architecture decision record.
- [ ] 2.15 **(P)** Tutorial: run a blameless postmortem.
- [ ] 2.16 **(P)** Tutorial: define SLOs and an error budget for one service.
- [ ] 2.17 **(P)** Tutorial: set up trunk-based development with branch
      protection and CI quality gates.
- [ ] 2.18 **(P)** Tutorial: threat model a feature with STRIDE.
- [ ] 2.19 **(P)** Tutorial: write OKRs and connect them to KPIs.
- [ ] 2.20 **(P)** Tutorial: run a maturity self-assessment and turn it into
      a quarterly plan.
- [ ] 2.21 **(P)** Tutorial: stand up docs-as-code for a team, using this
      repository's own toolchain as the worked example.
- [ ] 2.22 Cross-link: each tutorial links to the chapters it applies, and
      each of those chapters gains a link to the tutorial (in References and
      further reading or a short pointer where it fits naturally).

### Contributor and project documentation **(P with examples/tutorials)**

- [ ] 2.23 Write `docs/contributing/xref-extension.md`: how `guide_xref`
      works, its chapter map, how to run its tests, and its failure modes.
- [ ] 2.24 Write `docs/contributing/toolchain.md`: what `tools/gen_nav.py`
      generates, when to run `just nav`, how the spec, chapters, validator,
      and site relate (the spec-is-source-of-truth model end to end).
- [ ] 2.25 Write `docs/project/release-policy.md`: what v1.0 means, semantic
      versioning for a book, errata handling, and the renumbering policy for
      adding chapters after release. Link it from the changelog.
- [ ] 2.26 Write `docs/project/review-tracking.md`: the subject-matter-expert
      review process and a per-part table of review status and dates.

## Phase 3: Site functionality and outputs

- [ ] 3.1 Reading paths page `docs/front-matter/reading-paths.md`: five
      guided paths (new engineering manager; startup founding team;
      enterprise modernization lead; public-sector delivery team; new
      graduate), each an ordered list of 10 to 15 chapters with one sentence
      per chapter on why it is included. Add to nav.
- [ ] 3.2 Related chapters: add a `## Related chapters` block (3 to 5 links
      with a phrase each) to every substantive chapter, placed just before
      References. Update the chapter template, the spec, and the validator's
      required-sections list in the same change. Generate candidate links
      from the existing cross-reference graph where possible; curate by hand.
- [ ] 3.3 Glossary auto-linking: extend `guide_xref` (or add a sibling
      extension in the same package) to link the first mention of a glossary
      term in each chapter to its entry in chapter 12.1. Build a term map
      generated by `tools/gen_nav.py` from the glossary headings. Add tests
      in `tests/test_xref.py`. Guard against linking inside code spans and
      existing links.
- [ ] 3.4 Single-document build: `tools/build_book.py` that concatenates
      front matter and chapters in spec order, rewrites internal links to
      anchors, and produces EPUB and PDF with pandoc. Add `just book`. In the
      deploy workflow, build both files, publish them into the site, and link
      them from `docs/index.md`. Document prerequisites in `SITE.md`.
- [ ] 3.5 Standalone checklists and templates: extract each checklist from
      chapter 12.2 and each template from chapter 12.3 into individual files
      under `docs/checklists/` and `docs/templates/`, with index pages, nav
      support, and links from the appendix chapters. Keep the appendix
      chapters as annotated guides to the standalone files rather than
      duplicating full content.
- [ ] 3.6 Site polish: site description and social-card metadata in
      `zensical.toml` (as supported), a 404 page, and a home-page section
      linking the changelog, the EPUB/PDF downloads, and the reading paths.

## Phase 4: Content quality and release

- [ ] 4.1 Depth pass: using the Phase 1 stats report, bring every substantive
      chapter below the word-count floor up to the roughly 3,000-word target,
      following the chapter template and house style. Shrink the task-1.3
      allowlist as chapters are fixed. Work part by part; one part per run.
- [ ] 4.2 Citation verification, one part per run (12 runs): every entry in
      References and further reading is a real work, correctly attributed;
      every URL resolves (use the lychee report); formats are consistent.
      Replace or remove anything that cannot be verified.
- [ ] 4.3 Terminology consistency pass: use the glossary (chapter 12.1) as
      canonical vocabulary; align chapter usage with it; add missing glossary
      entries for terms the book defines and uses repeatedly.
- [ ] 4.4 Copyedit pass, one part per run: plain language, tone, sentence
      length, and Vale warnings triaged (fix or explicitly waive).
- [ ] 4.5 Cross-cutting themes audit: verify security, privacy,
      accessibility, and automation concerns appear in every part where they
      apply; add short subsections where they are missing.
- [ ] 4.6 Update `spec/roadmap.md` to reflect actual status (many completed
      items are still unchecked) and add these phases so the roadmap and this
      file agree.
- [ ] 4.7 Release v1.0: confirm all gates green, write the changelog entry,
      tag the release, state the update cadence in
      `docs/project/release-policy.md`, and announce on the site home page.
