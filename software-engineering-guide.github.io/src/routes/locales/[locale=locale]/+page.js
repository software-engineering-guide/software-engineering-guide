import manifest from '#lib/manifest.json';

export const prerender = true;

// Old URL: /locales/<code>/ . A locale is now served directly at /<code>/.
export function entries() {
  return manifest.availableLocales.map((locale) => ({ locale }));
}

export function load({ params }) {
  return { to: `/${params.locale}/` };
}
