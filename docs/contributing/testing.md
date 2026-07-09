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

- **Exactly 100 chapters.**
- **Contiguous numbering** within each part, starting at N.0.
- **H1 matches the file name** decimal for every chapter.
- **Required sections** are present in every content chapter (Parts 1 through 11,
  chapter N.1 and up).
- **No em-dashes** in any Markdown file.
- **No forbidden phrases** ("not only", "but also", "load-bearing").
- **All internal `.md` links resolve.**
- **Wikipedia links are well-formed** (`https://en.wikipedia.org/wiki/...`).
- **`docs/spec/structure.md` matches the files on disk**, in both directions.
- **README and the contents page link every chapter.**

## When a check fails

The failing line names the file and the problem. Common fixes:

- Em-dash found: reword the sentence to remove the "—". Do not just delete it.
- Missing section: add the missing `##` section from the chapter template.
- Structure mismatch: you added or renamed a chapter without updating
  `docs/spec/structure.md`, or vice versa. Bring them back in line.
- Broken link: fix the path, or update it after a rename.
- Numbering gap: renumber so the part is contiguous from N.0.

## Not covered by the tests

The suite checks structure and style, not truth. It cannot tell whether a
reference is real or whether prose is accurate. Verify citations and facts by
hand or with a research pass. Wikipedia link existence (as opposed to link form)
also needs a network check, which the suite deliberately leaves out so it can run
offline.
