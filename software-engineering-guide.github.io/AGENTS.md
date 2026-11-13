# Software Engineering Guide — website

The published website for the Software Engineering Guide. See
[README.md](README.md) for the human-oriented overview.

## What this is

A SvelteKit project (`@sveltejs/adapter-static`) that prerenders the whole
book as a static site, deployed by GitHub Actions to
<https://software-engineering-guide.github.io/>. It does not own the book's
content — see below.

## Working rules

- `src/content/` is **generated** from the sibling `software-engineering-guide`
  repo by `scripts/sync-content.mjs`: each locale's topics from
  `locales/<code>/<topics_slug>/<slug>/index.md`, and the English-only sections
  (front-matter, examples, contributing, project) from `docs/`. Never hand-edit
  files under it. Edit the content repo, then run `pnpm run content` here.
- URLs: a locale is served at `/<code>/` and its topics at
  `/<code>/<topics_slug>/<slug>/`, where the topics segment is translated per
  locale (`topics`, `themen`, `temas`, ...) and read from `topics-slugs.json`
  (copied by the sync). Old `/<code>/chapters/` and `/locales/<code>/` URLs get
  redirect pages; `/` redirects by browser language
  (`src/lib/detect-locale.js`) and is the site search page when it has a query.
  The spec is in the book repo's `spec/locales-for-global-sharing-with-svelte/`.
- `src/lib/manifest.json` is **generated** by `scripts/generate-manifest.mjs`
  from `src/content/` — never hand-edit it.
- Chapter, front-matter, examples, contributing, and project pages are all
  rendered by the same pattern: a `[slug]/+page.js` with `entries()` sourced
  from the manifest, dynamically importing the matching `.md` file from
  `src/content/`, and a `+page.svelte` that renders `data.content` (the
  mdsvex-compiled component) inside the page chrome. Follow this pattern for
  any new content section rather than inventing a new one.
- Do not touch the sibling `software-engineering-guide` repository from here
  — that repo owns the book's content and spec.
- Run `pnpm run check` before committing changes to `src/`.
