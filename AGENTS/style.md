# House style (golden rules)

The enforceable version is
[`docs/contributing/style-rules.md`](../docs/contributing/style-rules.md) and
[`spec/conventions.md`](../spec/conventions.md). The tests check most of this.

1. **No em-dashes.** Never use U+2014. Use a comma, colon, parentheses, or two
   sentences. En-dashes are allowed only in numeric ranges.
2. **No stock LLM phrasing.** No "not only ... but also", "but also",
   "load-bearing", "It's important to note", "In today's fast-paced world".
3. **Follow the chapter template**, in
   [`docs/contributing/chapter-template.md`](../docs/contributing/chapter-template.md).
4. **Define terms on first use** and **link key concepts to Wikipedia** on first
   mention. Real references only; never fabricate a work or a URL.
5. **The spec is the source of truth.** Change the spec and the chapters
   together.
6. **Tests must pass.** Run `just test` before calling a change done.

Tone: warm, plain, opinionated. American spelling in `en-us`; see
[`spec/locales-for-global-sharing-with-svelte/index.md`](../spec/locales-for-global-sharing-with-svelte/index.md)
for the `en-gb` and Oxford variants.
