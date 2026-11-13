#!/usr/bin/env node
// Scans src/content/ and writes src/lib/manifest.json: the structured table of
// contents (parts, chapters, prev/next order) that drives navigation, the
// contents page, and the "chapter N.M" auto-linking remark plugin.
// Regenerate after `pnpm run content`, or whenever src/content/ changes:
//   pnpm run manifest
import { readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { partTitles } from '../src/lib/i18n.js';
import { topicsSlugs } from './topics-slugs.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const contentDir = path.resolve(root, 'src/content');
const outFile = path.resolve(root, 'src/lib/manifest.json');

// Matches spec/structure.md / tests/validate.py PART_TITLES in the content
// repo (English). Per-locale overrides live in src/lib/i18n.js.
const PART_TITLES = partTitles('en-us');

function firstH1Title(text) {
  const line = text.split('\n').find((l) => l.startsWith('# '));
  return line ? line.slice(2).trim() : '';
}

function readSectionFiles(section, dir = path.join(contentDir, section)) {
  let names;
  try {
    names = readdirSync(dir).filter((f) => f.endsWith('.md'));
  } catch {
    return [];
  }
  return names.sort();
}

const chapterRe = /^(\d{2})-(\d{2})-(.+)\.md$/;

/**
 * Builds the {chapters, parts, chaptersByDecimal, order} shape for one
 * chapters/ directory, English or a locale's.
 * @param {string} dir
 * @param {string} fileRelPrefix
 * @param {Record<number, string>} titles
 */
function buildChapterManifest(dir, fileRelPrefix, titles = PART_TITLES) {
  const files = readSectionFiles('chapters', dir);
  const chapters = [];
  for (const file of files) {
    const m = chapterRe.exec(file);
    if (!m) {
      console.warn(`Skipping chapter file with unexpected name: ${fileRelPrefix}/${file}`);
      continue;
    }
    const [, pp, cc] = m;
    const part = Number(pp);
    const chapter = Number(cc);
    const text = readFileSync(path.join(dir, file), 'utf-8');
    const h1 = firstH1Title(text);
    // H1 is "P.C Title" — strip the leading decimal to get the display title.
    const decimal = `${part}.${chapter}`;
    const title = h1.startsWith(decimal) ? h1.slice(decimal.length).trim() : h1;
    chapters.push({
      part,
      chapter,
      decimal,
      slug: file.replace(/\.md$/, ''),
      title,
      heading: h1,
      file: `${fileRelPrefix}/${file}`
    });
  }
  chapters.sort((a, b) => a.part - b.part || a.chapter - b.chapter);

  const partNumbers = [...new Set(chapters.map((c) => c.part))].sort((a, b) => a - b);
  const parts = partNumbers.map((number) => ({
    number,
    title: titles[number] ?? PART_TITLES[number] ?? `Part ${number}`,
    chapters: chapters.filter((c) => c.part === number)
  }));

  const chaptersByDecimal = Object.fromEntries(chapters.map((c) => [c.decimal, c]));
  const order = chapters.map((c) => c.decimal);

  return { chapters, parts, chaptersByDecimal, order };
}

// --- English chapters (src/content/chapters/PP-CC-slug.md) ---
const { chapters, parts, chaptersByDecimal, order } = buildChapterManifest(
  path.join(contentDir, 'chapters'),
  'chapters'
);

// --- Every locale (src/content/locales/<code>/chapters/PP-CC-slug.md) ---
let localeCodes = [];
try {
  localeCodes = readdirSync(path.join(contentDir, 'locales')).sort();
} catch {
  // No locales synced yet.
}
const locales = {};
for (const code of localeCodes) {
  const localeDir = path.join(contentDir, 'locales', code);
  const hasHomePage = (() => {
    try {
      // Per spec, every locale gets index.md scaffolded even before it has
      // a translation, and it starts empty — so "exists" isn't enough.
      return readFileSync(path.join(localeDir, 'index.md'), 'utf-8').trim().length > 0;
    } catch {
      return false;
    }
  })();
  locales[code] = {
    ...buildChapterManifest(path.join(localeDir, 'chapters'), `locales/${code}/chapters`, partTitles(code)),
    hasHomePage,
    topicsSlug: topicsSlugs()[code] ?? 'topics'
  };
}

// --- Other sections: front-matter, examples, contributing, project ---
function readSimpleSection(section) {
  const files = readSectionFiles(section);
  return files
    .filter((f) => f !== 'index.md')
    .map((file) => {
      const text = readFileSync(path.join(contentDir, section, file), 'utf-8');
      return {
        slug: file.replace(/\.md$/, ''),
        title: firstH1Title(text),
        file: `${section}/${file}`
      };
    });
}

const frontMatter = readSimpleSection('front-matter');
const examples = readSimpleSection('examples');
const contributing = readSimpleSection('contributing');
const project = readSimpleSection('project');

const manifest = {
  generatedBy: 'scripts/generate-manifest.mjs',
  parts,
  chapters,
  chaptersByDecimal,
  order,
  frontMatter,
  examples,
  contributing,
  project,
  locales,
  availableLocales: localeCodes,
  totals: {
    parts: parts.length,
    chapters: chapters.length
  }
};

writeFileSync(outFile, JSON.stringify(manifest, null, 2) + '\n');
console.log(
  `Wrote ${outFile}: ${parts.length} parts, ${chapters.length} chapters, ` +
    `${localeCodes.length} locale(s) (${localeCodes
      .map((c) => `${c}: ${locales[c].chapters.length}`)
      .join(', ')}).`
);
