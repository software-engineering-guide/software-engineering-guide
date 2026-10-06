# Repository layout

Where things live. Paths are relative to the repository root.

- `locales/<code>/` : the book's content, one tree per locale (`en-us`, `de-de`,
  `cy-001`, and so on). The locale list is `spec/locales-for-global-sharing-with-svelte/locales.tsv`.
  - `locales/en-us/topics/PP-CC-slug/index.md` : the English chapters (called
    topics). `PP` is the two-digit part, `CC` the two-digit chapter, `00` is the
    part introduction. In text the number stays dotted (`8.1`).
  - Other locales translate both the `topics` path segment and each slug. The
    segment name is the `topics_slug` column of `locales.tsv`. Never hardcode
    `topics`.
  - Every topic directory holds `index.md`, a `README.md` symlink to `index.md`,
    and a `.locale-peer-id`.
- `docs/` : everything the published site contains, rendered elsewhere.
  - `docs/front-matter/` : the opening essay, introduction, table of contents.
  - `docs/examples/` : small illustrative examples.
  - `docs/contributing/` : contributor and agent guides, plus shared snippets.
  - `docs/project/` : project documentation and the changelog.
- `spec/` : the source of truth (structure, conventions, locales, search,
  contents, roadmap). Hand-authored, not published.
- `skills/` : AI agent skills (`software-engineering-guide-skill`,
  `software-engineering-guide-maintainer-skill`).
- `tools/` : `gen_nav.py` (README TOC, site home, contents page, subject index)
  and `stats.py` (`just stats`).
- `tests/validate.py` : the enforcement suite (`just test`).
- `styles/`, `.vale.ini` : Vale prose rules (`just lint`).
- `.github/workflows/` : `test.yml` (PR checks), `links.yml` (weekly link check).
- `justfile`, `pyproject.toml`, `uv.lock` : task runner and Python dev tooling.
- `plan.md`, `tasks.md` : planning notes.

Generated files (do not hand-edit): `README.md`, `docs/index.md`,
`docs/front-matter/table-of-contents.md`, and
`locales/en-us/topics/12-07-index/index.md`. Change the topics and run `just nav`.
