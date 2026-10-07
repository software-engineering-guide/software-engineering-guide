# Locales for major projects with SvelteKit

Translate content into multiple locales.

How this site supports multiple locales end to end: content, web
routing, UI chrome, and bugs.

Read locales via file `locales.tsv`.

Locale code priority order:

- en
- cy
- zh
- sp
- ar

## Routes

A locale's pages live directly under its code. There is no `/locale/` or
`/locales/` path segment in any URL.

| URL | Meaning |
|---|---|
| `/` | no query: redirects to the default locale, e.g. `/en-us/`. With a query (`/?foo`): site search, no redirect. See [`spec/search`](../search/index.md) |
| `/en-us/` | home page in English (United States) |
| `/en-us/contents/` | contents page in English (United States) |
| `/en-us/topics/<topic-slug>/` | a topic (chapter) in English (United States) |
| `/de-de/themen/<topic-slug>/` | the same, in German: the `topics` segment is translated per locale |
| `/en-us/about/` | about page in English (United States) |

Example: `https://software-engineering-guide.github.io/en-us/` serves English
(United States).

- SvelteKit route directory is `src/routes/[locale]/`, not
  `src/routes/locales/[locale]/`.
- `[locale]` uses a param matcher (`src/params/locale.js`) that accepts only
  codes listed in `locales.tsv`, so it never captures `about`, `contents`,
  `contributing`, `project`, `examples`, or `front-matter`.
- Reserved root route names must never be used as locale codes.
- The default locale is `en-us`: `/` redirects there and search indexes it.
- Sections with no translations yet (`/front-matter/`, `/examples/`,
  `/contributing/`, `/project/`) stay English-only at the root, with no locale
  prefix. Their nav labels and breadcrumbs still use the default locale's
  `/<code>/` routes. When a section is translated it moves under `/<code>/`.
- Language aliases: a bare two-letter language code is an alias of that
  language's world locale, `<lang>-001`. `/en/` renders the content of
  `/en-001/`, `/es/` renders `/es-001/`, and so on, for every language that has
  a `-001` locale (`ar`, `cy`, `en`, `es`, `fr`, `hi`, `zh`). The alias renders
  in place (no redirect), and each aliased page sets
  `<link rel="canonical" href="/<lang>-001/...">` so search engines index one
  URL. Aliases apply to every sub-route (`/en/contents/`, `/en/about/`,
  `/en/topics/<topic-slug>/`). A language with no `-001` locale has no alias.
  The param matcher accepts both full codes and these aliases, and the alias
  codes are reserved like the other locale codes.
- Home, `contents`, and the topics section are localized: each exists once per locale
  under `/<code>/`, with its text and UI chrome from
  `ui(locale)` and `locales/<code>/`. The only locale-agnostic page is `/`, a small page that
  hosts search and the redirect below. There are no bare `/about/` or
  `/contents/` routes; they return 404.
- `/` must not redirect on the server: a server-side redirect drops the query
  string and breaks search at `/?<target>`. Instead `/` is a prerendered page
  whose client script redirects (`location.replace`) to the default locale only
  when `location.search` is empty. With JavaScript off, a `<noscript>`
  `<meta http-equiv="refresh">` in the head redirects to the default locale
  (no query is available without JavaScript to search anyway).
- Old `/locales/<code>/...` URLs redirect to `/<code>/...`. Old
  `/<code>/chapters/<slug>/` URLs redirect to `/<code>/<topics_slug>/<slug>/`.
- The topics path segment is translated per locale, in both the URL and the
  book-side directory. Its value is the `topics_slug` column of `locales.tsv`
  (`topics`, `temas`, `themen`, `sujets`, `pynciau`, `المواضيع`, `विषय`,
  `主题`). The same name is used for `locales/<code>/<topics_slug>/` and for
  `/<code>/<topics_slug>/<topic-slug>/`. The param matcher also reads it, and
  topics slugs are reserved like locale codes. Tools and tests read the column;
  they never hardcode `topics`.
- The book-side content directory stays `locales/<code>/`; only the URL changes.

## .locale-peer.id file

`.locale-peer-id` file is a byte-identical 32-character hexadecimal lowercase
number then newline, across every locale's version of "the same" topic,
regardless of slug.

`.locale-peer-id` id is how the project resolves "this page, in locale X".

## Guidance

- en-us: consistent American spelling; fix any stray en-gb forms (organisation→organization, licence→license, programme→program, cancelled→canceled, analogue→analog).

- en-gb: the -ize/-ise family (optimise, realise, organise, prioritise, utilise, etc.), -or/-our (colour, behaviour, favour, labour, neighbours), -er/-re (centre, theatre for the metaphorical sense), -ense/-ce (defence, licence), doubled-L forms (modelled, labelled, cancelled, enrol/enrolment), analogue, programme, and math→maths.

- en-gb-oxendict: use en-gb then revert just the -ise family back to Oxford -ize spelling (optimize, realise→realize, organise→organize, etc.), while correctly keeping -yse forms (analyse/analysable) unchanged, since Oxford style never uses -yze, and keeping all other British forms (colour, centre, defence, licence, programme, maths, modelled) intact.

## Identical locales

`zh-001` (Chinese, World) is identical in content to `zh-cn` (Chinese, China): same
topics, slugs, and `.locale-peer-id` files, since the Simplified Chinese text has no
country-specific usage to remove. Edit `zh-cn` first, then mirror the change into
`zh-001` (`rsync -a --delete locales/zh-cn/ locales/zh-001/`).

## Guard against corruption

Keep proper nouns unconverted. Example: "Hospital Readmissions Reduction Program" (a real United States federal program name).

## Verify

For each locale subdirectory:

- File exists: `index.md`
- Symlink exists: `README.md`
- Locale peer id tracking file exists: `.locale-peer-id`

Then:

- Fix any broken internal links
- Fix any residual wrong-dialect spellings
- Update `./spec/locale/index.md`

## Content structure (book side)

Each locale is `locales/<code>/` in the book repo, containing:

- `locales/<code>/<topics_slug>/<slug>/index.md` + `.locale-peer-id`: one per topic
  (`<topics_slug>` is the locale's translated `topics`, from `locales.tsv`).
  `README.md` is a symlink to `index.md`.
- `locales/<code>/index.md` + `.locale-peer-id` + `README.md` symlink: the
  locale's own translated README (site home/contents page source). Every
  locale gets this file scaffolded (matching the topic-file pattern) even
  before it has a translation; it starts empty.

## Slugs

Slugs are per-locale, not shared. Translated locales rename topic directories
to native-script/accented slugs.

Example: `es-001` `año-de-vida-ajustado-por-calidad`, `ur-001` `صحت-ایڈجسٹڈ-متوقع-زندگی`.

Nothing in the site assumes slugs match across locales.

## Locale picker (labels + ordering)

- Labels live in `locales.js`'s `LOCALE_LABELS`, one entry per code, in that
  language (e.g. `'fr-001': 'Français (Monde)'`). Falls back to the raw code
  via `localeLabel()` if a code has no label yet.
- Header `PickerBar` order comes from `content.js`'s `locales()` (sorted by
  code): the `-001` suffix happens to sort before any letter-starting
  regional suffix, so variants already come first there.
- Home page's locale list (`+page.server.js`) sorts explicitly: default
  locale first, then grouped by language name (label text before the `(`),
  with the `-001`/World variant sorted before its regional siblings within
  each group, then alphabetically by label. This does not fall out of
  alphabetical-by-label sort on its own (e.g. "España" < "Mundo"); it needs
  the explicit `-001` check.

## Bug fixes (regression watch-list)

### Bug: ASCII-only `\w` regexes broke every non-Latin/non-accented slug

Bug: matched topic slugs with `[\w.-]+` (ASCII word chars only). Any locale with
an accented or native-script slug (Spanish, French, Russian, Chinese, Arabic,
Welsh, Hindi, Bengali, Portuguese, Indonesian, Urdu) silently failed peer-id
resolution and cross-topic links.

Fix by widening the slug capture group to `[^/]+`.

### Bug: Every locale's home/contents page showed canonical English content

Bug: code and content always read a single top-level `/README.md` for title,
intro, "New here?" picks, part headings, and blurbs: only topic _links_ were
ever localized.

Fix: populate the previously-empty `locales/<code>/index.md` per locale.

## Bug: Link extraction was hardcoded to literal English phrase

Bug: link silently found nothing once the README was translated.

Fix: extract all links from the whole pre-`##` intro block instead of
regex-matching the English sentence.

### Bug: UI chrome was hardcoded English in the `.svelte` templates

Bug: nav labels, subtitles, page titles, intros, breadcrumbs, topic position,
pagination, picker/share labels.

Fix: add `i18n.js` and threading `ui(locale)` through every locale-scoped route
and `+layout.svelte`.

### Bug: header/footer brand wordmark stayed English

Bug: wordmark came only from the root (locale-agnostic) `+layout.server.js`,
which deliberately never picks a locale.

Fix: have `[locale]/+layout.server.js` supply this locale's own title,
which overrides the root layout's canonical one via SvelteKit's merged
`page.data` on any route under `/<locale>/`. The root
page `/` (no locale in the URL) correctly keeps the canonical English title.
