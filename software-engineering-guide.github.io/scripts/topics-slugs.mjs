// The per-locale name of the topics section, in both the book repo's
// directories (locales/<code>/<topics_slug>/) and this site's URLs
// (/<code>/<topics_slug>/<slug>/). The source of truth is the topics_slug
// column of the book repo's spec/locales-for-global-sharing-with-svelte/
// locales.tsv; scripts/sync-content.mjs copies it into
// src/content/topics-slugs.json, which the build scripts read through here.
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
export const topicsSlugsFile = path.resolve(here, '../src/content/topics-slugs.json');

/** @returns {Record<string, string>} locale code -> topics URL segment */
export function topicsSlugs() {
  try {
    return JSON.parse(readFileSync(topicsSlugsFile, 'utf-8'));
  } catch {
    return {};
  }
}

/** @param {string} code */
export function topicsSlug(code) {
  return topicsSlugs()[code] ?? 'topics';
}
