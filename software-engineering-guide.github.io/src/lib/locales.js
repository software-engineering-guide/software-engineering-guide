// Locale labels, one entry per code, each written in that language (its own
// endonym), per spec/locales-for-global-sharing-with-svelte/index.md
// ("Labels live in locales.js's LOCALE_LABELS ... Falls back to the raw
// code via localeLabel() if a code has no label yet"). This list only needs
// to cover locales the book repo actually publishes under locales/<code>/.
/** @type {Record<string, string>} */
export const LOCALE_LABELS = {
  'en-001': 'English',
  'en-gb': 'English - Great Britain',
  'en-us': 'English - United States',
  'cy-001': 'Cymraeg',
  'cy-gb': 'Cymraeg - Prydain Fawr',
  'da-001': 'Dansk',
  'hi-001': 'हिन्दी',
  'hi-in': 'हिन्दी - भारत',
  'zh-001': '中文',
  'zh-cn': '中文 - 简体',
  'de-001': 'Deutsch',
  'de-de': 'Deutsch',
  'es-001': 'Español',
  'fr-001': 'Français',
  'ar-001': 'العربية',
  'bn-001': 'বাংলা',
  'id-001': 'Bahasa Indonesia',
  'id-id': 'Bahasa Indonesia',
  'ja-jp': '日本語',
  'ja-001': '日本語',
  'ko-kr': '한국어',
  'ko-001': '한국어',
  'sv-se': 'Svenska',
  'sv-001': 'Svenska',
  'sw-001': 'Kiswahili',
  'sw-tz': 'Kiswahili',
  'vi-vn': 'Tiếng Việt',
  'vi-001': 'Tiếng Việt',
  'nl-nl': 'Nederlands',
  'nl-001': 'Nederlands',
  'is-is': 'Íslenska',
  'is-001': 'Íslenska',
  'pt-001': 'Português',
  'ru-001': 'Русский',
  'ur-001': 'اردو'
};

/** @param {string} code */
export function localeLabel(code) {
  return LOCALE_LABELS[code] ?? code;
}

/** Right-to-left locale codes among the ones this site publishes. */
export const RTL_LOCALES = new Set(['ar-001', 'ur-001']);

/**
 * @param {string} code
 * @returns {'ltr' | 'rtl'}
 */
export function localeDir(code) {
  return RTL_LOCALES.has(code) ? 'rtl' : 'ltr';
}

/**
 * BCP 47-ish language tag for the `lang` attribute. The book's locale codes
 * are already close to BCP 47 (`cy-001`/`hi-001`/`es-001` are CLDR "worldwide"
 * region codes, not real BCP 47 regions), so strip the synthetic `-001` and
 * lowercase-region codes like `zh-cn` to the conventional `zh-CN` casing.
 * @param {string} code
 */
export function langAttr(code) {
  if (code.endsWith('-001')) return code.slice(0, -4);
  const [lang, region] = code.split('-');
  return region ? `${lang}-${region.toUpperCase()}` : lang;
}

/**
 * The locale `/` redirects to, and the one site search indexes. English
 * (United States) matches the book's house spelling. See
 * spec/locales-for-global-sharing-with-svelte/index.md ("Routes").
 */
export const DEFAULT_LOCALE = 'en-us';
