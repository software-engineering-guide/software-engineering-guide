import { defineParams } from '@sveltejs/kit/params';
import manifest from './lib/manifest.json' with { type: 'json' };

// SvelteKit loads this file in plain Node, so it cannot use the `#lib`
// helpers that import the manifest without a JSON import attribute. The rule
// is the same as resolveLocale() in src/lib/content.js: a full locale code,
// or the language alias ("en") of a `<lang>-001` world locale.
const codes = new Set(manifest.availableLocales);
const aliases = new Set(manifest.availableLocales.filter((c) => c.endsWith('-001')).map((c) => c.slice(0, -4)));

const topicsSlugs = new Set(Object.values(manifest.locales).map((l) => l.topicsSlug ?? 'topics'));

export const params = defineParams({
  // The translated topics path segment (`topics`, `themen`, `temas`, ...).
  topics: (/** @type {string} */ param) => (topicsSlugs.has(param) ? param : undefined),
  // Matches only real locale codes and language aliases, so `[locale=locale]`
  // never captures `front-matter`, `examples`, `contributing`, or `project`.
  locale: (/** @type {string} */ param) => (codes.has(param) || aliases.has(param) ? param : undefined)
});
