# Authoring: writing and editing chapters

## Before you write

- Read the [style rules](style-rules.md) and
  [`spec/conventions.md`](../spec/conventions.md).
- Check [`spec/structure.md`](../spec/structure.md) to see where the topic fits
  and what number it should have.

## Writing a new chapter

1. Pick the part and the next free decimal number in that part. Numbering is
   contiguous, so a new chapter usually takes the next number after the last one
   in its part.
2. Create `docs/chapters/N.M-slug.md` from the
   [chapter template](chapter-template.md).
3. Write to the template. Every content chapter needs all of its sections:
   overview, key principles, recommendations, trade-offs (with a table),
   examples (one enterprise and one government), business case, anti-patterns, a
   four-level maturity model, discussion ideas, key takeaways, and references.
4. Define terms on first use. Add Wikipedia links to key concepts on first
   mention, in prose only.
5. Cross-reference related chapters by decimal, for example "(chapter 8.1)."
6. Add the chapter to `docs/spec/structure.md`.
7. If the part introduction (N.0) lists its chapters, add a bullet there.
8. Run `just nav`, then `just test`.

## Editing an existing chapter

- Keep the section order and headings intact. The tests check that content
  chapters still have every required section.
- Preserve inline definitions, Wikipedia links, tables, and the references list
  unless the edit is specifically about them.
- Do not introduce em-dashes or the forbidden phrases. If you are rephrasing,
  reword rather than dropping in a dash.

## Renaming or renumbering

- Rename the file, update its `# N.M Title` heading, update `docs/spec/structure.md`,
  and update every cross-reference that points to the old number.
- Run `just nav` and `just test`. The tests will flag a mismatch between the H1
  and the file name, a numbering gap, or a broken link.

## Tone reminder

Write like an experienced colleague who wants the reader to succeed. Warm, plain,
direct, and useful. Short sentences. No filler.
