import { resolveLocale } from '#lib/content.js';
import { langAttr, localeDir } from '#lib/locales.js';

/** @type {import('@sveltejs/kit/hooks').Handle} */
export async function handle({ event, resolve }) {
  // The first path segment is a locale code or a language alias ("/en/"),
  // never a section name: resolveLocale() only accepts real locales.
  const locale = resolveLocale(event.url.pathname.split('/')[1]);

  return resolve(event, {
    transformPageChunk: ({ html }) => {
      if (!locale) return html;
      // src/app.html declares <html lang="en">; swap in this locale's
      // language and text direction so the prerendered HTML is correct
      // before any client JS runs (screen readers, hyphenation, etc.).
      return html.replace(
        '<html lang="en">',
        `<html lang="${langAttr(locale)}" dir="${localeDir(locale)}">`
      );
    }
  });
}
