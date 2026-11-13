import { error } from '@sveltejs/kit';
import manifest from '#lib/manifest.json';
import { topicsBase } from '#lib/content.js';

export const prerender = true;

// Old URL: /<code>/chapters/<slug>/ . The topics segment is now translated
// per locale (/<code>/<topics_slug>/<slug>/), so every locale whose segment
// is no longer "chapters" gets a redirect page here.
export function entries() {
  return manifest.availableLocales.flatMap((locale) =>
    manifest.locales[locale].chapters.map((c) => ({ locale, slug: c.slug }))
  );
}

export function load({ params }) {
  const chapter = manifest.locales[params.locale]?.chapters.find((c) => c.slug === params.slug);
  if (!chapter) error(404, 'Not found');
  return { to: `${topicsBase(params.locale)}/${params.slug}/` };
}
