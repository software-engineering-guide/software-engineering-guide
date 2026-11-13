import manifest from '#lib/manifest.json';
import { DEFAULT_LOCALE } from '#lib/locales.js';

export { DEFAULT_LOCALE };

/**
 * Every locale this site publishes, sorted by code. This is the order the
 * header PickerBar's LocalePicker shows its listbox in — the `-001`
 * suffix happens to sort before any letter-starting regional suffix, so
 * variants (e.g. `en-001`) already come first within their language group
 * here (see spec/locales-for-global-sharing-with-svelte/index.md). The
 * home page's own locale list sorts differently (default locale first,
 * then grouped by language); see +page.server.js for that.
 */
export function locales() {
  return [...manifest.availableLocales].sort();
}

/** @param {string} decimal e.g. "1.2" */
export function chapterByDecimal(decimal) {
  return manifest.chaptersByDecimal[decimal] ?? null;
}

/**
 * @param {string} locale
 * @param {string} decimal
 */
export function localeChapterByDecimal(locale, decimal) {
  return manifest.locales[locale]?.chaptersByDecimal?.[decimal] ?? null;
}

/**
 * Language aliases: a bare two-letter language code is an alias of that
 * language's world locale, so `/en/` renders `/en-001/`. Only languages that
 * have a `<lang>-001` locale get one.
 * @returns {Record<string, string>} alias -> canonical locale code
 */
export function localeAliases() {
  /** @type {Record<string, string>} */
  const aliases = {};
  for (const code of manifest.availableLocales) {
    if (code.endsWith('-001')) aliases[code.slice(0, -4)] = code;
  }
  return aliases;
}

/**
 * Maps a URL locale segment (a full code or a language alias) to the
 * canonical locale code, or null when it is neither.
 * @param {string | undefined} param
 */
export function resolveLocale(param) {
  if (!param) return null;
  if (manifest.availableLocales.includes(param)) return param;
  return localeAliases()[param] ?? null;
}

/**
 * The URL segment for a locale's topics section, translated per locale
 * (`topics`, `themen`, `temas`, ...). It comes from the topics_slug column of
 * the book repo's locales.tsv. Accepts a language alias ("en") too.
 * @param {string} locale
 */
export function topicsSlug(locale) {
  const code = resolveLocale(locale) ?? locale;
  return manifest.locales[code]?.topicsSlug ?? 'topics';
}

/**
 * `/<locale-or-alias>/<topics-slug>`: where a locale's topic pages live.
 * @param {string} locale the URL segment, a code or alias
 */
export function topicsBase(locale) {
  return `/${locale}/${topicsSlug(locale)}`;
}

/** Every valid `[topics]` URL segment: one per locale. */
export function allTopicsSlugs() {
  return [...new Set(Object.values(manifest.locales).map((l) => l.topicsSlug ?? 'topics'))];
}

/** Every valid `[locale]` URL segment: full codes plus language aliases. */
export function localeParams() {
  return [...manifest.availableLocales, ...Object.keys(localeAliases())];
}
