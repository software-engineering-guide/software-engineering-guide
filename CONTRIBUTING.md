# Contributing

Thank you for helping improve this guidebook. Contributions of all sizes are
welcome, from fixing a typo to writing a new chapter.

The full contributing guide lives in the book itself:
[docs/contributing/index.md](docs/contributing/index.md), published at
<https://software-engineering-guide.github.io/software-engineering-guide/contributing/>.

The short version:

- Follow the house style: no em-dashes, no stock phrasing, warm plain writing.
  The rules are in [docs/contributing/style-rules.md](docs/contributing/style-rules.md).
- Run `just test` before you consider a change done. `just spell` (codespell)
  and `just lint` (Vale, needs the [vale](https://vale.sh) binary) catch what
  the test suite does not; CI runs all three on every pull request, plus a
  full site build.
- If you change the set of chapters, update
  [spec/structure.md](spec/structure.md) and run `just nav`.
- Add a one-line entry to [docs/project/changelog.md](docs/project/changelog.md)
  under **Unreleased**.

## Pre-commit hooks (optional, recommended)

The repository ships a [pre-commit](https://pre-commit.com) configuration that
runs the validation suite, codespell, and an em-dash check before each commit:

```sh
uv tool install pre-commit   # or: pip install pre-commit
pre-commit install
```

After that, every `git commit` runs the checks against the staged files. Run
`pre-commit run --all-files` for a one-off pass over everything.
