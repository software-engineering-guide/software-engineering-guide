import { error } from '@sveltejs/kit';
import manifest from '#lib/manifest.json';

export const prerender = true;

export function entries() {
  return manifest.examples.map((c) => ({ slug: c.slug }));
}

export async function load({ params }) {
  const entry = manifest.examples.find((c) => c.slug === params.slug);
  if (!entry) error(404, 'Example not found');
  const mod = await import(`../../../content/examples/${params.slug}.md`);
  return { entry, content: mod.default };
}
