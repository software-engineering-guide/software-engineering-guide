// Builds build/sitemap.xml from the generated HTML, after `vite build`, so it
// lists exactly the pages that were prerendered (every served locale's
// chapters, contents, front-matter, examples, contributing, project and help
// pages). static/robots.txt points crawlers at it.
//
// 404.html is left out. Output is sorted so a rebuild of unchanged content is
// byte-identical.
import { readdirSync, writeFileSync } from 'node:fs';
import { join, relative, sep } from 'node:path';

const SITE = 'https://software-engineering-guide.github.io';
const BUILD = process.argv[2] ?? 'build';

/** @param {string} dir @param {string[]} out */
function walk(dir, out = []) {
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) walk(p, out);
    else if (e.name === 'index.html') out.push(p);
  }
  return out;
}

/** @param {string} s */
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const urls = walk(BUILD)
  .map((p) => relative(BUILD, join(p, '..')).split(sep).filter(Boolean))
  .map((segs) => `${SITE}/${segs.map(encodeURIComponent).join('/')}${segs.length ? '/' : ''}`)
  .sort();

const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((u) => `  <url><loc>${esc(u)}</loc></url>`).join('\n')}
</urlset>
`;
writeFileSync(join(BUILD, 'sitemap.xml'), xml);
console.log(`sitemap: ${urls.length} URLs`);
