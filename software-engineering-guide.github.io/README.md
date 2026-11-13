# Software Engineering Guide — website

The published website for the [Software Engineering
Guide](https://github.com/software-engineering-guide/software-engineering-guide):
a guidebook of good practices for software developer teams. Live at
<https://software-engineering-guide.github.io/>.

Built with [SvelteKit](https://svelte.dev/docs/kit) (`@sveltejs/adapter-static`,
fully prerendered) and styled with the [Lily Design
System](https://lilydesignsystem.com/) class-hook conventions. Chapter content
is Markdown, compiled with [mdsvex](https://mdsvex.pngwn.io/).

## Where the content comes from

The book's Markdown lives in the sibling
[`software-engineering-guide`](https://github.com/software-engineering-guide/software-engineering-guide)
repository: the topics under `locales/<code>/<topics_slug>/<slug>/index.md` (the
topics path segment is translated per locale, from `locales.tsv` in that repo's
spec) and the English-only sections under `docs/`. This repo copies them into `src/content/` (see
[`scripts/sync-content.mjs`](scripts/sync-content.mjs)) and generates a
navigation manifest from it (see
[`scripts/generate-manifest.mjs`](scripts/generate-manifest.mjs)).

**Never hand-edit files under `src/content/`.** Edit the source repo instead,
then regenerate:

```sh
pnpm run content   # re-copies locales/ and docs/ from ../software-engineering-guide, then rebuilds the manifest
```

This assumes `software-engineering-guide` is checked out as a sibling
directory (`../software-engineering-guide` relative to this repo).

## Claude Code skills

Two [Claude Code](https://claude.com/claude-code) skills for this project
live in the content repo's
[`skills/`](https://github.com/software-engineering-guide/software-engineering-guide/tree/main/skills)
directory: `software-engineering-guide-skill` for readers who want guidance
grounded in the book, and `software-engineering-guide-maintainer-skill` for
maintainers of both this site and the content repo, including the content
sync and manifest steps above. Copy either folder into a project's
`.claude/skills/` to install it.

## Development

```sh
pnpm install
pnpm run dev       # http://localhost:5173
pnpm run build     # prerenders the full site into build/
pnpm run preview   # serve the production build locally
pnpm run check     # svelte-check
```

`pnpm run dev` and `pnpm run build` both copy the Lily themes into
`static/themes/` and regenerate `src/lib/manifest.json` first (see the
`themes` and `manifest` scripts). The manifest never needs to be committed
stale — though it is committed, since `src/content/` is committed too; the
themes are not committed at all.

## Structure

- `src/content/{chapters,front-matter,examples,contributing,project}/` :
  synced Markdown source (see above).
- `src/lib/manifest.json` : generated table of contents (parts, chapters,
  ordering, prev/next) — see `scripts/generate-manifest.mjs`.
- `src/routes/[locale=locale]/` : the translated pages, served at `/<code>/`
  (for example `/en-us/`): the locale home, `contents/`, and
  `chapters/[slug]/`. `[locale]` also accepts a language alias (`/en/`
  renders `/en-001/`); `src/params.js` holds the matcher. There is no
  `/locales/` path segment.
- `src/routes/+page.svelte` : `/` redirects to the default locale in the
  browser, only when there is no query string (so `/?<target>` search works).
- `src/routes/front-matter/[slug]/`, `examples/[slug]/`,
  `contributing/[slug]/`, `project/[slug]/` : English-only dynamic routes that
  prerender one page per Markdown file, using `entries()` to enumerate slugs
  from the manifest.
- `src/lib/Sidebar.svelte`, `Breadcrumb.svelte`, `ChapterPager.svelte` : the
  book chrome.
- `scripts/remark-chapter-links.mjs` : auto-links plain-text chapter
  cross-references ("see chapter 8.1") to their route, mirroring the
  `guide_xref` extension in the content repo's former Zensical build.
- `static/assets/style.css` : the whole design — Lily is headless and ships
  no CSS, so this hand-authored stylesheet (using Lily's semantic class
  hooks: `.button`, `.card`, `.prose`, …) is the site's look.
- `static/themes/` : the 45 Lily reference themes the theme picker loads
  (`themesUrl="/themes/"`). Not committed: `scripts/copy-lily-themes.mjs`
  copies them from the
  [`@lilydesignsystem/themes`](https://www.npmjs.com/package/@lilydesignsystem/themes)
  package before every `dev` and `build` (or run `pnpm run themes`). To update
  the themes, bump that package's version in `package.json`; never edit the
  copies.

## Deployment

[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) builds and
deploys to GitHub Pages on every push to `main`. For the first deployment,
set repository **Settings → Pages → Build and deployment → Source → GitHub
Actions**.
