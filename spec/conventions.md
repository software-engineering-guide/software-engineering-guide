# Conventions

This is the writing and format specification for the guidebook. Chapters are
written to satisfy it, and `tests/validate.py` enforces the parts that can be
checked mechanically. When a rule below says "enforced," the test suite will fail
if it is broken.

## Numbering and file names

- Parts are whole numbers (1 through 12). Chapters are decimals within a part.
- Chapter **N.0** is the part introduction. Chapters **N.1, N.2, ...** are the
  content chapters. Numbering within each part is contiguous and starts at N.0.
  (enforced)
- Chapter files live in `chapters/` and are named `N.M-slug.md`, for example
  `8.1-ci-cd-and-delivery.md`. The slug is lowercase with dashes.
- The first heading of every chapter file is `# N.M Title`, and the `N.M` must
  match the file name. (enforced)
- Part 12 is the appendices (glossary, checklists, templates, maturity
  self-assessment, references, adoption roadmap, and index).

## Chapter template (content chapters, N.1 and up in Parts 1 through 11)

Every content chapter uses these sections, in this order. All are required and
checked. (enforced)

1. `# N.M Title`
2. `## Overview and motivation` (what it is, why it matters for large teams, and enterprise and government relevance)
3. `## Key principles` (a short bulleted list)
4. `## Recommendations` (the core, under `###` subheadings)
5. `## Trade-offs: pros and cons` (at least one Markdown table plus prose)
6. `## Examples` (at least one enterprise and one government example)
7. `## Business case: motivations, ROI, and TCO`
8. `## Anti-patterns and pitfalls`
9. `## Maturity model` (four levels: 1 Initial, 2 Managed, 3 Defined, 4 Optimizing)
10. `## Ideas for discussion` (four to six questions)
11. `## Key takeaways`
12. `## References and further reading`

Part introductions (N.0) use a lighter shape: two or three framing paragraphs, a
`## Chapters in this part` list, and a `## How these chapters interrelate`
section. Part 12 appendices are reference material and do not follow the content
template.

## House style

- Write for a colleague, not a spec sheet. Be warm, direct, and encouraging.
  Address the reader as "you." Prefer short sentences and plain words.
- Be opinionated and practical. Give guidance, not a survey. Lead with the point.
- Stay vendor-neutral. Name products only as factual examples, never as
  endorsements.
- Keep chapters roughly 1,300 to 2,000 words unless the topic genuinely needs
  more.

## Hard rules

- **No em-dashes.** Do not use the em-dash character "—" (U+2014) anywhere. Use a
  comma, colon, parentheses, or two sentences. En-dashes "–" (U+2013) are allowed
  only in numeric ranges (for example, `Parts 1–9`, `4.1–4.6`). (enforced)
- **No stock LLM phrasing.** Do not use "not only ... but also", "but also", or
  "load-bearing". Avoid "It's important to note", "In today's fast-paced world",
  "It's crucial to consider", "It appears that", "One could argue", and the
  "it's not just X, it's Y" formula. (partly enforced)
- **Define terms on first use.** The first time a chapter uses a technical term,
  methodology, or acronym, define or expand it, for example "continuous
  integration (CI)."
- **Link key concepts to Wikipedia on first mention.** Wrap well-established
  encyclopedic terms in a link to their English Wikipedia article, for example
  `[continuous integration](https://en.wikipedia.org/wiki/Continuous_integration)`.
  Link each concept once per chapter. Do not put links in headings, tables, code,
  or the references section. Only link terms that have a real article. (link form
  is enforced)
- **Real references only.** The references section lists real books, papers, and
  standards by author and title. Do not fabricate works or invent URLs.

## Cross-references

Refer to other chapters by decimal number, for example "see chapter 8.1" or
"(chapter 3.1)." Do not hard-code file paths in chapter prose.

## Changing the structure

To add, remove, rename, or renumber a chapter:

1. Edit the chapter file (or create it following the template).
2. Update `spec/structure.md` so the manifest matches.
3. If a part's introduction lists its chapters, update that list.
4. Run `make nav` to regenerate the table of contents, index, and TOC page.
5. Run `make test`. It must pass before the change is complete.
