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

The full rules are in [`spec/conventions.md`](spec/conventions.md) and the short
version is [`AGENTS/share/style-rules.md`](AGENTS/share/style-rules.md). The
tests enforce the mechanical parts.

## Setup

You need Python 3. There are no other dependencies.

```sh
make help    # list tasks
make test    # run the validation suite
make nav     # regenerate the generated navigation files
make stats   # chapter and word counts
```

## Making a change

1. Read the relevant guide: [`AGENTS/authoring.md`](AGENTS/authoring.md) for
   chapters, [`AGENTS/navigation.md`](AGENTS/navigation.md) for the generated
   files, [`AGENTS/testing.md`](AGENTS/testing.md) for the tests.
2. Make the smallest change that does the job.
3. If you added, removed, renamed, or renumbered a chapter, update
   [`spec/structure.md`](spec/structure.md) and run `make nav`.
4. Run `make test`. It must pass.
5. Add a one-line entry to [`CHANGELOG.md`](CHANGELOG.md) under **Unreleased**.

## What to work on

- Fix errors, unclear passages, or stale references.
- Improve examples, especially concrete enterprise and government ones.
- Verify citations against real sources.
- Fill gaps in a chapter's coverage without breaking the template.

## What to avoid

- Do not edit the generated files by hand (`README.md`,
  `front-matter/table-of-contents.md`, `chapters/12.7-index.md`). Change the
  chapters and run `make nav` instead.
- Do not add a chapter without also updating `spec/structure.md`.
- Do not introduce em-dashes or the forbidden phrases; the tests will fail.

## Reporting issues

Open an issue describing the problem, the file and chapter, and, where relevant,
the correct source or reference. Small, specific reports are the easiest to act
on.
