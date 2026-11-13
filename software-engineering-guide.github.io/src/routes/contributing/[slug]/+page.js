import { error } from '@sveltejs/kit';
import manifest from '#lib/manifest.json';

export const prerender = true;

export function entries() {
  return manifest.contributing.map((c) => ({ slug: c.slug }));
}

export async function load({ params }) {
  const entry = manifest.contributing.find((c) => c.slug === params.slug);
  if (!entry) error(404, 'Page not found');
  const mod = await import(`../../../content/contributing/${params.slug}.md`);
  return { entry, content: mod.default };
}
