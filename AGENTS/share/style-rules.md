# Style rules (shared, enforceable)

The house style in one place. Items marked "(test)" are enforced by
`tests/validate.py`; a violation fails the build. The full narrative version is
[`spec/conventions.md`](../../spec/conventions.md).

## Hard rules

- **No em-dashes.** Never use "—" (U+2014). Use a comma, colon, parentheses, or
  two sentences. En-dashes "–" are allowed only in numeric ranges such as
  `1–9` or `4.1–4.6`. (test)
- **No stock phrasing.** Do not use "not only ... but also", "but also", or
  "load-bearing". Avoid "It's important to note", "In today's fast-paced world",
  "It's crucial to consider", "It appears that", "One could argue", and the
  "it's not just X, it's Y" formula. (test, for the first three)
- **Define terms on first use.** Expand acronyms and define jargon the first
  time each chapter uses them, for example "service level objective (SLO)."
- **Link key concepts to Wikipedia** on first mention, once per chapter, in
  prose only. Form: `[term](https://en.wikipedia.org/wiki/Article_Title)`. Never
  in headings, tables, code, or the references section. (link form is a test)
- **Real references only.** Author and title of genuine works. No invented
  titles, authors, or URLs.

## Voice

- Warm, direct, encouraging. Address the reader as "you." Short sentences, plain
  words. Lead with the point.
- Opinionated and practical. Vendor-neutral. Name products only as factual
  examples.

## Structure (test)

- Content chapters use the exact section order in
  [`chapter-template.md`](chapter-template.md).
- The first heading is `# N.M Title`, and `N.M` matches the file name.
- Numbering within each part is contiguous and starts at N.0.

## After editing

- If you changed the set of chapters, update `spec/structure.md` and run
  `make nav`.
- Always run `make test`.
