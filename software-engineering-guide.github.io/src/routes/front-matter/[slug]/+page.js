import { error } from '@sveltejs/kit';
import manifest from '#lib/manifest.json';

export const prerender = true;

export function entries() {
  return manifest.frontMatter.map((c) => ({ slug: c.slug }));
}

export async function load({ params }) {
  const entry = manifest.frontMatter.find((c) => c.slug === params.slug);
  if (!entry) error(404, 'Page not found');
  const mod = await import(`../../../content/front-matter/${params.slug}.md`);
  return { entry, content: mod.default };
}
