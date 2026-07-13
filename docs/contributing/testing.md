# Testing: the validation suite

## Run it

```sh
just test
# or
python3 tests/validate.py
```

It runs from anywhere and needs only Python 3 (no third-party packages, no
network). It prints one line per check and exits non-zero if any check fails, so
it works in CI and as a pre-commit hook.

## What it checks

- **The expected chapter count** (the constant at the top of the script).
- **Contiguous numbering** within each part, starting at N.0.
- **H1 matches the file name** decimal for every chapter.
- **H1 titles match `spec/structure.md`** character for character, not just
  the leading decimal.
- **Required sections** are present in every content chapter (Parts 1 through 11,
  chapter N.1 and up), **in exactly the template order**.
- **A minimum word count** for every content chapter (2,000 words), with an
  allowlist in the script for intentional exceptions.
- **No em-dashes** in any Markdown file.
- **En-dashes only between digits**, so "4.1–4.6" passes and everything else
  fails.
- **No forbidden phrases** ("not only", "but also", "load-bearing").
- **All internal `.md` links resolve.**
- **Prose cross-references point at real chapters**: a reference to a chapter
  number with no matching file on disk fails, using the same reference
  pattern `guide_xref` links at build time.
- **Wikipedia links are well-formed** (`https://en.wikipedia.org/wiki/...`).
- **`spec/structure.md` matches the files on disk**, in both directions.
- **README, the home page, and the contents page link every chapter**, and the
  `zensical.toml` nav lists every docs page.
- **`guide_xref/chapters.py` matches the chapters on disk** (run `just nav`
  after structure changes).

## When a check fails

The failing line names the file and the problem. Common fixes:

- Em-dash found: reword the sentence to remove the "—". Do not just delete it.
- Missing section: add the missing `##` section from the chapter template.
- Structure mismatch: you added or renamed a chapter without updating
  `spec/structure.md`, or vice versa. Bring them back in line.
- Broken link: fix the path, or update it after a rename.
- Numbering gap: renumber so the part is contiguous from N.0.

## Beyond the validation suite

- `just spell` runs [codespell](https://github.com/codespell-project/codespell)
  over the repository. The configuration, including the false-positive ignore
  list, is the `[tool.codespell]` section in `pyproject.toml`.
- `just lint` runs [Vale](https://vale.sh) against the house style. The rules
  live in `.vale.ini` and `styles/Guide/`: the banned phrases and the em-dash
  ban are errors, filler and stock LLM wording are warnings. CI fails on
  errors only, so warnings inform without blocking.
- `.pre-commit-config.yaml` wires the validator, codespell, and an em-dash
  grep into [pre-commit](https://pre-commit.com); see CONTRIBUTING.md for
  setup.
- `just stats` prints a Markdown report (per-chapter word counts, thin
  chapters, Wikipedia links, reference entries) from `tools/stats.py`.

## Continuous integration

- `.github/workflows/test.yml` runs on every pull request and on pushes to
  non-main branches: the validation suite, the xref tests, codespell, Vale at
  error severity, and a full site build. It never deploys.
- `.github/workflows/docs.yml` validates, builds, and deploys the site on
  pushes to main.
- `.github/workflows/links.yml` checks external links weekly with
  [lychee](https://github.com/lycheeverse/lychee) (ignore patterns in
  `.lycheeignore`) and keeps the results in a single "Link checker report"
  issue. External links stay out of the PR path on purpose.

## Not covered by the tests

The suite checks structure and style, not truth. It cannot tell whether a
reference is real or whether prose is accurate. Verify citations and facts by
hand or with a research pass. Wikipedia link existence (as opposed to link form)
also needs a network check, which the suite deliberately leaves out so it can run
offline.
