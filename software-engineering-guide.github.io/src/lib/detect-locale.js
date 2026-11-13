// Picks which served locale a visitor hitting the bare domain root ("/")
// should be redirected to. The root route has no locale segment of its own
// (see src/routes/[locale=locale]/), so landing on "/" directly previously 404ed;
// this is the client-side replacement for a server-side Accept-Language
// redirect, which a static GitHub Pages deployment (adapter-static, no
// origin server) cannot perform at request time.
//
// Preference order, each tier used only if the previous one yields no match:
//   1. navigator.languages — the browser's full, ordered language
//      preference list (richest signal; not available in every browser).
//   2. navigator.language — the single primary language tag every browser
//      exposes. This is the closest a static page can get to reading the
//      request's Accept-Language header: browsers deliberately do not
//      expose that raw header to page JavaScript (it would add a
//      fingerprinting signal beyond navigator.language/.languages), and
//      without an origin server there is no request to read a header from
//      in the first place. navigator.language is derived from the same
//      underlying OS/browser setting Accept-Language itself is built from.
//   3. defaultCode — a fixed fallback (this site passes DEFAULT_LOCALE).
//
// Matching a tag against the served codes tries, per tag:
//   a. an exact, case-insensitive match against a served code
//      ("en-GB" -> "en-gb"), then
//   b. the language's international superset: "<language>-001" if served
//      ("en-AU" -> "en-001", never the "/en/" alias), then
//   c. a primary-language match against the first "-"-delimited segment of
//      each served code (first served code starting "<language>-",
//      preferring defaultCode if it is one of the candidates).
//
// Pure and dependency-free so it is unit-testable without a browser or a
// SvelteKit test harness; see spec/locale-default/index.md for the full
// specification this implements.

/**
 * @param {string} tag
 * @param {string[]} servedCodes
 * @param {string} defaultCode
 * @returns {string | undefined}
 */
function matchTag(tag, servedCodes, defaultCode) {
  const normalized = tag.trim().toLowerCase().replace(/_/g, '-');
  if (!normalized) return undefined;

  const exact = servedCodes.find((code) => code.toLowerCase() === normalized);
  if (exact) return exact;

  const language = normalized.split('-')[0];
  if (!language) return undefined;

  const superset = servedCodes.find((code) => code.toLowerCase() === `${language}-001`);
  if (superset) return superset;

  const candidates = servedCodes.filter((code) => code.toLowerCase().split('-')[0] === language);
  if (candidates.length === 0) return undefined;
  return candidates.includes(defaultCode) ? defaultCode : candidates[0];
}

/**
 * @param {string[] | undefined | null} tags
 * @param {string[]} servedCodes
 * @param {string} defaultCode
 * @returns {string | undefined}
 */
function matchFirst(tags, servedCodes, defaultCode) {
  for (const tag of tags ?? []) {
    const match = matchTag(tag, servedCodes, defaultCode);
    if (match) return match;
  }
  return undefined;
}

/**
 * Pure matching function: given the visitor's language preferences in
 * priority order (already-flattened, e.g. [...navigator.languages,
 * navigator.language]) and the site's served locale codes, picks one.
 * Always returns a value (falls back to defaultCode).
 *
 * @param {string[] | undefined | null} acceptedLanguages
 * @param {string[]} servedCodes
 * @param {string} defaultCode
 * @returns {string}
 */
export function detectLocale(acceptedLanguages, servedCodes, defaultCode) {
  return matchFirst(acceptedLanguages, servedCodes, defaultCode) ?? defaultCode;
}

/**
 * Browser-environment convenience wrapper: reads navigator.languages (tier
 * 1) and navigator.language (tier 2) itself, then delegates to
 * detectLocale(). Only call this in the browser (guard so it only runs in the browser); navigator is undefined during prerendering.
 *
 * @param {string[]} servedCodes
 * @param {string} defaultCode
 * @returns {string}
 */
export function pickLocale(servedCodes, defaultCode) {
  /** @type {string[]} */
  const tags = [];
  if (typeof navigator !== 'undefined') {
    if (Array.isArray(navigator.languages)) tags.push(...navigator.languages);
    if (navigator.language) tags.push(navigator.language);
  }
  return detectLocale(tags, servedCodes, defaultCode);
}
