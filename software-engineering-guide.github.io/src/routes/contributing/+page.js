export const prerender = true;

export async function load() {
  const mod = await import('../../content/contributing/index.md');
  return { content: mod.default };
}
