#!/usr/bin/env node
// Copies the book's Markdown source from the sibling `software-engineering-guide`
// content repository into src/content/ here. The copied files are committed —
// this script exists to regenerate them after the source repo changes, the same
// way the Lily Design System monorepo regenerates `src/lib/components.ts` from
// `components.tsv`. Never hand-edit files under src/content/; edit the source
// repo and re-run `pnpm run content` instead.
//
// Chapters live under the source repo's locales/<code>/<topics_slug>/<slug>/index.md
// (one directory per chapter, per-locale slugs), not docs/chapters/<slug>.md
// (that flat layout was retired when the source repo added locale support; see
// its spec/locales-for-global-sharing-with-svelte/index.md). This script
// flattens each locale's chapters into src/content/locales/<code>/chapters/
// <slug>.md, and keeps syncing the English-only sections (front-matter,
// examples, contributing, project) from docs/ as before. The default English
// chapters/ section below is copied from locales/en-us/ specifically, so
// existing routes under /chapters/... keep working unchanged.
import { existsSync, mkdirSync, readdirSync, rmSync, copyFileSync, lstatSync, readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const sourceRoot = path.resolve(root, '../software-engineering-guide');
const sourceDocs = path.join(sourceRoot, 'docs');
const sourceLocales = path.join(sourceRoot, 'locales');
const targetContent = path.resolve(root, 'src/content');

// Per-locale name of the topics section (the book repo's directory and this
// site's URL segment), from the topics_slug column of locales.tsv. Saved as
// src/content/topics-slugs.json for the other build scripts.
const localesTsv = path.join(sourceRoot, 'spec', 'locales-for-global-sharing-with-svelte', 'locales.tsv');
/** @type {Record<string, string>} */
const topicsSlugs = {};
for (const line of readFileSync(localesTsv, 'utf-8').split('\n').slice(1)) {
  const [code, , , slug] = line.split('\t');
  if (code && slug) topicsSlugs[code] = slug;
}
mkdirSync(targetContent, { recursive: true });
writeFileSync(path.join(targetContent, 'topics-slugs.json'), JSON.stringify(topicsSlugs, null, 2) + '\n');

const NON_LOCALE_SECTIONS = ['front-matter', 'examples', 'contributing', 'project'];

if (!existsSync(sourceDocs) || !existsSync(sourceLocales)) {
  console.error(`Source repo not found as a sibling: ${sourceRoot}`);
  console.error('Expected the software-engineering-guide content repo checked out next to this one.');
  process.exit(1);
}

for (const section of NON_LOCALE_SECTIONS) {
  const from = path.join(sourceDocs, section);
  const to = path.join(targetContent, section);
  if (!existsSync(from)) {
    console.warn(`Skipping missing source section: ${section}`);
    continue;
  }
  rmSync(to, { recursive: true, force: true });
  mkdirSync(to, { recursive: true });
  const files = readdirSync(from).filter((f) => f.endsWith('.md'));
  for (const file of files) {
    copyFileSync(path.join(from, file), path.join(to, file));
  }
  console.log(`Synced ${files.length} file(s) into src/content/${section}/`);
}

/**
 * Flattens locales/<code>/chapters/<slug>/index.md into
 * <targetChaptersDir>/<slug>.md, skipping any topic directory that has no
 * index.md yet (an untranslated chapter in a partial locale).
 * @param {string} localeChaptersDir
 * @param {string} targetChaptersDir
 */
function syncChapterDirs(localeChaptersDir, targetChaptersDir) {
  rmSync(targetChaptersDir, { recursive: true, force: true });
  mkdirSync(targetChaptersDir, { recursive: true });
  let names;
  try {
    names = readdirSync(localeChaptersDir);
  } catch {
    return 0;
  }
  let count = 0;
  for (const name of names) {
    const topicDir = path.join(localeChaptersDir, name);
    if (!lstatSync(topicDir).isDirectory()) continue;
    const indexMd = path.join(topicDir, 'index.md');
    if (!existsSync(indexMd)) continue;
    copyFileSync(indexMd, path.join(targetChaptersDir, `${name}.md`));
    count++;
  }
  return count;
}

// English chapters, kept at the existing src/content/chapters/ path so
// today's /chapters/[slug]/ routes and manifest.json keep working unchanged.
const enUsChaptersCount = syncChapterDirs(
  path.join(sourceLocales, 'en-us', topicsSlugs['en-us'] ?? 'topics'),
  path.join(targetContent, 'chapters')
);
console.log(`Synced ${enUsChaptersCount} file(s) into src/content/chapters/ (from locales/en-us/)`);

// Every locale (including en-us again, so /locales/en-us/... also works)
// under src/content/locales/<code>/chapters/ and, where present, that
// locale's own translated home/contents page at
// src/content/locales/<code>/index.md.
const localeCodes = readdirSync(sourceLocales).filter((name) =>
  lstatSync(path.join(sourceLocales, name)).isDirectory()
);
const targetLocalesDir = path.join(targetContent, 'locales');
rmSync(targetLocalesDir, { recursive: true, force: true });
for (const code of localeCodes) {
  const localeDir = path.join(sourceLocales, code);
  const targetLocaleDir = path.join(targetLocalesDir, code);
  mkdirSync(targetLocaleDir, { recursive: true });
  const count = syncChapterDirs(path.join(localeDir, topicsSlugs[code] ?? 'topics'), path.join(targetLocaleDir, 'chapters'));
  const localeIndex = path.join(localeDir, 'index.md');
  if (existsSync(localeIndex)) {
    copyFileSync(localeIndex, path.join(targetLocaleDir, 'index.md'));
  }
  console.log(`Synced ${count} file(s) into src/content/locales/${code}/chapters/`);
}

console.log('Content sync complete. Run `pnpm run manifest` (or `pnpm run content` next time) to rebuild the navigation manifest.');
