export const prerender = true;

export async function load() {
  const mod = await import('../../content/examples/index.md');
  return { content: mod.default };
}
