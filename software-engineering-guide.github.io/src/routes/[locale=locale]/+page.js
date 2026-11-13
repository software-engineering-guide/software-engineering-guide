import manifest from '#lib/manifest.json';
import { localeParams, resolveLocale } from '#lib/content.js';

export const prerender = true;

export function entries() {
  return localeParams().map((locale) => ({ locale }));
}

export async function load({ params }) {
  const locale = /** @type {string} */ (resolveLocale(params.locale));
  const localeManifest = manifest.locales[locale];

  if (localeManifest.hasHomePage) {
    // A translated locales/<code>/index.md exists: render it as the
    // locale's home page, same as the chapter/front-matter routes render
    // their markdown.
    const mod = await import(`../../content/locales/${locale}/index.md`);
    return { hasHomePage: true, content: mod.default };
  }

  return { hasHomePage: false };
}
