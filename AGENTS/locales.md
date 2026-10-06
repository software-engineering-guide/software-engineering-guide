# Locales and translation

Full rules: [`spec/locales-for-global-sharing-with-svelte/index.md`](../spec/locales-for-global-sharing-with-svelte/index.md).

- Content for a locale lives in `locales/<code>/<topics_slug>/<slug>/`.
  `topics_slug` comes from `locales.tsv`; slugs are per-locale and translated
  (accented or native script is fine). Nothing assumes slugs match across
  locales.
- `.locale-peer-id` is a 32-character lowercase hex id plus newline, identical
  across every locale's version of the same topic, whatever the slug. It is how
  the site resolves "this page, in locale X". Never change one without changing
  all locales.
- The numeric `PP-CC-` prefix of a slug stays the same in every locale.
- Keep proper nouns unconverted (for example a real program name).
- URLs: a locale is served at `/<code>/`, topics at `/<code>/<topics_slug>/<slug>/`.
  There is no `/locales/` segment. A bare language code is an alias of its
  `-001` locale.
- Adding a locale: add a row (with `topics_slug`) to `locales.tsv`, scaffold
  `index.md`, the `README.md` symlink, and `.locale-peer-id`, then run `just test`.
- Renaming a slug or the topics segment: rename with `git mv`, then fix every
  relative link that pointed at the old name.
