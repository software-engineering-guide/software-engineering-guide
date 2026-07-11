# Improvement plan

This plan describes major improvements to the Software Engineering Guide across
five areas: capabilities (tooling and enforcement), functionality (the
published site and output formats), documentation (contributor and project
docs), tutorials (hands-on walkthroughs), and examples (worked artifacts).
The companion file [`tasks.md`](tasks.md) breaks the plan into an actionable,
phased checklist sized for agent-driven execution.

## Where the project stands

The book is substantially complete: 133 chapters across 12 parts, roughly
368,000 words, a strict house style, a spec-driven structure
([`spec/structure.md`](spec/structure.md)), a validation suite
([`tests/validate.py`](tests/validate.py)), a navigation generator
([`tools/gen_nav.py`](tools/gen_nav.py)), an auto-linking cross-reference
extension ([`guide_xref/`](guide_xref/__init__.py)), and a Zensical static
site deployed by GitHub Actions.

The main gaps, in order of leverage:

1. **CI runs only on push to main.** Pull requests are never validated, so a
   contributor can open a broken PR and nobody learns until after merge.
2. **Validation is shallow in places.** Section presence is checked but not
   section order; internal links are checked but external URLs are not;
   cross-references like "chapter 9.9" are auto-linked but a reference to a
   chapter that does not exist fails silently; there is no spell check, no
   prose linter, and no minimum-depth check even though the project targets
   roughly 3,000 words per chapter.
3. **The site underuses its content.** There are no reading paths for
   different audiences, no per-chapter summaries or related-chapter links, no
   downloadable single-document build (EPUB or PDF), and the glossary is a
   page rather than a linked vocabulary.
4. **Examples are thin.** Three example files (an ADR, OKRs, a chapter
   skeleton) support a 133-chapter book whose templates appendix promises many
   more artifact types.
5. **There are no tutorials.** The book says what to do; nothing walks a
   reader through doing it.
6. **The release phase of the roadmap is open.** [`spec/roadmap.md`](spec/roadmap.md)
   phase 13 (consistency, copyedit, citation verification, v1.0) is mostly
   unchecked.

## Workstream A: Capabilities (tooling and enforcement)

Goal: every rule the spec states should be enforced by a test, and every test
should run before merge, not after.

- **PR validation workflow.** Add a GitHub Actions workflow that runs the full
  validation suite, the xref tests, and a site build on every pull request.
  Keep the existing deploy workflow for pushes to main.
- **Deeper structural validation.** Extend `tests/validate.py` to check:
  section order matches the chapter template exactly (not just presence);
  every substantive chapter meets a minimum word count; H1 titles match
  `spec/structure.md` titles, not just numbers; no duplicate chapter slugs;
  en-dashes appear only in numeric ranges; each chapter's first Wikipedia link
  targets a distinct article (catch copy-paste duplicates).
- **Dangling cross-reference detection.** A validator check that finds
  prose references such as "chapter 13.4" pointing at chapters that do not
  exist, using the same pattern the `guide_xref` extension uses.
- **External link checking.** A scheduled (weekly) CI job using a link checker
  (for example lychee) with a committed ignore list, so citation URLs rot
  visibly instead of silently. Keep it out of the PR path to avoid flaky
  failures.
- **Spell check and prose lint.** Add codespell with a project word list, and
  a Vale (or equivalent) configuration that encodes the golden rules
  (banned phrases, em-dash ban, filler phrases) so style drift is caught
  mechanically rather than by review memory.
- **Task runner and pre-commit.** Add `just lint`, `just links`, and `just
  spell` targets, and a pre-commit configuration so contributors get fast
  local feedback.
- **Stats and coverage reporting.** Extend `just stats` into a small report:
  words per chapter, chapters under target depth, Wikipedia-link density,
  reference counts, so quality passes can be targeted instead of exhaustive.

## Workstream B: Functionality (site and outputs)

Goal: make the same content useful in more ways and to more audiences.

- **Reading paths.** A new front-matter page (or small set of pages) that
  defines guided paths through the book: "new engineering manager,"
  "startup founding team," "enterprise modernization lead," "public-sector
  delivery team," "new graduate." Each path is an ordered list of 10 to 15
  chapters with one sentence on why each is included.
- **Per-chapter metadata and related chapters.** Add a short summary and a
  "Related chapters" block to each chapter, generated or checked by tooling so
  the links stay valid. This turns a linear book into a navigable web.
- **Glossary auto-linking.** Extend the `guide_xref` extension (or add a
  sibling extension) so first mentions of glossary terms in a chapter link to
  the glossary entry, mirroring how chapter references already auto-link.
- **Single-document builds.** A `just book` target that assembles the chapters
  in order and produces EPUB and PDF via pandoc, published as artifacts from
  the deploy workflow and linked from the site home page. This is the largest
  single functionality win: the book becomes portable and citable.
- **Downloadable checklists and templates.** Extract the checklists and
  templates appendices into standalone Markdown files under `docs/` that
  readers can copy directly, with the appendix chapters linking to them.
- **Site polish.** Social cards and description metadata, a 404 page, and a
  visible "last updated" and changelog link so readers can judge freshness.

## Workstream C: Documentation (contributor and project docs)

Goal: a stranger (human or agent) can make a correct, style-clean contribution
on the first try, and the project's own operating rules are written down.

- **Document the toolchain.** A contributor page for `guide_xref` (how the
  extension works, how to test it) and for `tools/gen_nav.py` (what it
  generates, when to run it), plus an architecture note explaining the
  spec-is-source-of-truth model end to end.
- **Release and versioning policy.** Define what v1.0 means, how errata are
  handled, how chapters are added or renumbered after release, and record it
  in `docs/project/` with the changelog.
- **Review workflow.** A documented subject-matter-expert review process per
  part, with a tracking page recording which parts have been reviewed and
  when. This closes the largest open item in roadmap phase 13.
- **Keep AGENTS.md and CONTRIBUTING.md current** as the tooling from
  Workstream A lands (new just targets, new checks, pre-commit).

## Workstream D: Tutorials (hands-on walkthroughs)

Goal: pair the reference book with doing. Create `docs/tutorials/` with its own
template, nav section, and validator support.

- **Tutorial template and conventions.** A fixed structure: goal, audience,
  prerequisites, numbered steps, verification, where to go next. Registered in
  the spec and enforced by the validator like chapters are.
- **Initial tutorial set** (each anchored to one or two chapters):
  1. Write your first architecture decision record.
  2. Run a blameless postmortem.
  3. Define SLOs and an error budget for one service.
  4. Set up trunk-based development with branch protection and CI gates.
  5. Threat model a feature with STRIDE.
  6. Write OKRs and connect them to KPIs.
  7. Run a maturity self-assessment and turn it into a quarterly plan.
  8. Stand up docs-as-code for a team (this repository as the worked example).
- **Cross-linking.** Each tutorial links to the chapters it applies, and each
  applicable chapter links to its tutorial.

## Workstream E: Examples (worked artifacts)

Goal: every template the book recommends has at least one realistic, complete,
filled-in example under `docs/examples/`.

- Expand from the current three examples to a full set: an RFC, a postmortem,
  a runbook, a threat model, an SLO document, a risk register, a career-ladder
  excerpt, a code-review checklist in use, an incident communication timeline,
  a C4 context diagram description, a KPI tree, and a filled-in maturity
  self-assessment.
- Each example states its scenario in two or three sentences, is internally
  consistent (same fictional organization across examples where possible), and
  links back to the chapter and template it illustrates.
- The templates appendix (chapter 12.3) links every template to its example.

## Content quality (cross-cutting)

Alongside the workstreams, close roadmap phase 13 with targeted passes driven
by the stats reporting from Workstream A:

- Bring the thinnest substantive chapters up to the roughly 3,000-word target.
- Verify citations part by part: every referenced work is real, every URL
  resolves, formats are consistent.
- A terminology consistency pass using the glossary as the canonical
  vocabulary.
- Tag v1.0 once SME review, copyedit, and citation verification are done, and
  update `spec/roadmap.md` to reflect reality as items complete.

## Sequencing and dependencies

Phase 1 (do first): PR CI, deeper validation, spell and prose lint, stats
reporting. Everything later is safer and cheaper once these gates exist.

Phase 2 (parallelizable): examples (E), tutorials (D), and contributor docs
(C) can proceed independently once the gates are in place, because the
validator will catch style and structure mistakes.

Phase 3: site functionality (B), since reading paths and related-chapter
links want the full example and tutorial inventory to point at, and the
EPUB/PDF build should come after the content quality passes.

Phase 4: content quality passes and the v1.0 release.

## Constraints that every task must respect

- The golden rules in [`AGENTS.md`](AGENTS.md): no em-dashes, no stock LLM
  phrasing, the fixed chapter template, real references only.
- The spec is the source of truth: structural changes update
  `spec/structure.md` and the chapters together, then `just nav`, then
  `just test`.
- `tests/validate.py` pins the chapter count (currently 133); adding or
  removing chapters means updating that constant, the spec, and the generated
  navigation in the same change.
- New document types (tutorials, standalone examples) must be added to the
  nav generator and the Zensical nav, or check 11 (every docs page reachable)
  fails.
- `just test` must pass before any change is considered done.
