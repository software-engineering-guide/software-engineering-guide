# Contributing

Thank you for helping improve this guidebook. Contributions of all sizes are
welcome, from fixing a typo to writing a new chapter.

The full contributing guide lives in the book itself:
[docs/contributing/index.md](docs/contributing/index.md), published at
<https://software-engineering-guide.github.io/software-engineering-guide/contributing/>.

The short version:

- Follow the house style: no em-dashes, no stock phrasing, warm plain writing.
  The rules are in [docs/contributing/style-rules.md](docs/contributing/style-rules.md).
- Run `just test` before you consider a change done.
- If you change the set of chapters, update
  [spec/structure.md](spec/structure.md) and run `just nav`.
- Add a one-line entry to [docs/project/changelog.md](docs/project/changelog.md)
  under **Unreleased**.
