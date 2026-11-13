import { error } from '@sveltejs/kit';
import manifest from '#lib/manifest.json';
import { topicsBase } from '#lib/content.js';

export const prerender = true;

// Old URL: /locales/<code>/chapters/<slug>/ . Now /<code>/<topics_slug>/<slug>/ .
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
