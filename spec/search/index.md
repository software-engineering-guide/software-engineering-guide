# Search

Every `*.github.io` SvelteKit site in this family offers site search with no
server: a static index built at publish time and a small client-side search.

## Route

Search lives on the root page `/` and is driven by the query string:

| URL | Meaning |
|---|---|
| `/?foo` | search for `foo` |
| `/?foo+bar` or `/?foo%20bar` | search for `foo bar` (every word must match) |
| `/?q=foo` | accepted as an alias of `/?foo` |
| `/` | no query: redirect to the default locale (client-side) |

The whole query string is the target, URL-decoded, with `+` read as a space.
A server-side redirect on `/` would drop the query string and break search, so
`/` is a small prerendered page. Its client script redirects to the default
locale only when there is no query string (the default locale is `en-us`); with a query it stays on `/` and
shows results. If JavaScript is off, a `<noscript>` meta refresh in the head
does the redirect.

The page stays prerendered: the query is read in the browser only, never during
prerendering. A search box on `/` navigates to `/?<target>`. Each locale's header has a plain
`<form action="/" method="get">` with an input named `q`, so search works from
every page, even without JavaScript (`/?q=<target>`).

## Index

- `scripts/build-search-index.mjs` runs after `vite build` (part of
  `npm run build`) and writes `build/search-index.json` by reading the generated
  HTML, so it works the same for every site layout and needs no dependencies.
- One entry per page: `{ u: url, t: title, h: headings, x: text }`. Text is the
  `<main>` content with markup removed, capped at 20 000 characters.
- Locales: pages under a locale prefix (`/xx-yy/…`) are
  indexed only for the site's default locale (first present of `en-gb`,
  `en-001`, `en-us`, `en`), plus every page that has no locale prefix. Language aliases such as `/en/…`
  duplicate their `-001` pages and are never indexed. The 404
  page and redirects are skipped.

## Matching and ranking

- Case-insensitive; every word of the query must appear in the page.
- Score = 10 × title hits + 4 × heading hits + body hits; ties by title.
- Results show title, URL and a snippet with matches highlighted; at most 50.
- An empty or unmatched search says so and links back to the home page.

## Verification

After each publish: `GET /search-index.json` returns 200 and contains known
text, and the same ranking function run against the live index finds results
for a known term. The query page itself (`/?foo`) returns 200.
