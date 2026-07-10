# Contributing

Thank you for helping improve this guidebook. Contributions of all sizes are
welcome, from fixing a typo to writing a new chapter.

## Ground rules

The book follows a strict house style. The essentials:

- No em-dashes. Use a comma, colon, parentheses, or two sentences.
- No stock phrasing ("not only ... but also", "load-bearing", and similar).
- Warm, plain, direct writing. Address the reader as "you." Short sentences.
- Define terms on first use. Link key concepts to Wikipedia on first mention.
- Real references only.

The full rules are in `spec/conventions.md` at the repository root, and the short
version is the [style rules](style-rules.md). The
tests enforce the mechanical parts.

## Setup

You need Python 3, [uv](https://docs.astral.sh/uv/), and
[just](https://github.com/casey/just). See [`SITE.md`](https://github.com/software-engineering-guide/software-engineering-guide/blob/main/SITE.md)
for how the published site is built.

```sh
just         # list tasks
just test    # run the validation suite
just nav     # regenerate the generated navigation files
just build   # build the documentation site
just serve   # serve the site locally with live reload
just stats   # chapter and word counts
```

## Making a change

1. Read the relevant guide: [authoring](authoring.md) for
   chapters, [navigation](navigation.md) for the generated
   files, [testing](testing.md) for the tests.
2. Make the smallest change that does the job.
3. If you added, removed, renamed, or renumbered a chapter, update
   `spec/structure.md` at the repository root and run `just nav`.
4. Run `just test`. It must pass.
5. Add a one-line entry to the [changelog](../project/changelog.md) under **Unreleased**.

## What to work on

- Fix errors, unclear passages, or stale references.
- Improve examples, especially concrete enterprise and government ones.
- Verify citations against real sources.
- Fill gaps in a chapter's coverage without breaking the template.

## What to avoid

- Do not edit the generated files by hand (`README.md`, `docs/index.md`,
  `docs/front-matter/table-of-contents.md`, `docs/chapters/12-07-index.md`, and
  the `nav` block in `zensical.toml`). Change the chapters and run `just nav`
  instead.
- Do not add a chapter without also updating `spec/structure.md`.
- Do not introduce em-dashes or the forbidden phrases; the tests will fail.

## Reporting issues

Open an issue describing the problem, the file and chapter, and, where relevant,
the correct source or reference. Small, specific reports are the easiest to act
on.
