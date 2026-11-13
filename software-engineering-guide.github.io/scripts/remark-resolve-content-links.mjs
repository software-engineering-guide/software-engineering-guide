// The book's chapters cross-link each other with ordinary relative Markdown
// links (e.g. "../chapters/01-00-people.md", "./style-rules.md",
// "index.md", or, for a chapter linking a sibling chapter,
// "../01-02-team-topologies/index.md") — that's how they resolve in the
// source content repo's own directory-per-chapter layout
// (locales/<code>/<topics_slug>/<slug>/index.md). Rewrite each into this site's
// route: strip the ".md"/".md#frag", resolve relative to the source file's
// *logical* directory (see logicalSourceDir below), and map a section's
// index.md to its bare section route ("/contributing/" rather than
// "/contributing/index/"). Leave external links, mailto:, anchors, and
// already-absolute paths untouched.
import path from 'node:path';
import { visit } from 'unist-util-visit';
import { DEFAULT_LOCALE } from '../src/lib/locales.js';
import { topicsSlug } from './topics-slugs.mjs';

const SECTIONS = new Set(['chapters', 'front-matter', 'examples', 'contributing', 'project']);

/**
 * scripts/sync-content.mjs flattens each chapter directory
 * (chapters/<slug>/index.md, or locales/<code>/chapters/<slug>/index.md)
 * into a single file (chapters/<slug>.md). The book repo's own relative
 * links between chapters are written for that original nested layout
 * ("../<sibling-slug>/index.md", meant to be resolved from inside
 * chapters/<own-slug>/). Recover that intent here by resolving against a
 * *logical* directory that adds the flattened slug back as a path
 * segment, rather than the file's real (flattened) directory.
 * @param {string} sourcePath
 */
function logicalSourceDir(sourcePath) {
  const dir = path.dirname(sourcePath);
  const base = path.basename(sourcePath, '.md');
  const isFlattenedChapter =
    path.basename(dir) === 'chapters' && /^\d{2}-\d{2}-/.test(base);
  return isFlattenedChapter ? path.join(dir, base) : dir;
}

export function remarkResolveContentLinks() {
  return (tree, file) => {
    const sourcePath = file?.filename ?? file?.path ?? file?.history?.[0];
    if (!sourcePath) return;
    const sourceDir = logicalSourceDir(sourcePath);

    // Find src/content/ in the source path so we can compute a
    // content-relative "<section>/<slug>.md" (or "locales/<code>/...")
    // for any resolved link.
    const contentRootMarker = `${path.sep}src${path.sep}content${path.sep}`;
    const markerIndex = sourcePath.indexOf(contentRootMarker);
    if (markerIndex === -1) return;
    const contentRoot = sourcePath.slice(0, markerIndex + contentRootMarker.length);

    visit(tree, 'link', (node) => {
      const url = node.url;
      if (!url || /^([a-z]+:)?\/\//i.test(url) || url.startsWith('#') || url.startsWith('mailto:')) return;
      if (!url.includes('.md')) return;

      const [rawPath, fragment] = url.split('#');

      // The book repo's own root has docs/ and locales/ as siblings, but
      // this site flattens docs/<section>/ to src/content/<section>/
      // while keeping src/content/locales/<code>/ (i.e. dropping one
      // level of nesting for docs/* but not for locales/*). A relative
      // link the book repo wrote correctly for its own tree ("../../
      // locales/en-us/...") therefore resolves to the wrong depth once
      // copied here. Since "locales/<code>/..." is unambiguous wherever
      // it appears in the path, match it directly rather than resolving
      // by directory depth.
      const localeMatch = /(?:^|\/)locales\/([^/]+)\/(?:([^/]+)\/([^/]+)\/)?index\.md$/.exec(rawPath);
      if (localeMatch) {
        const [, code, isChapters, slug] = localeMatch;
        const route = isChapters ? `/${code}/${topicsSlug(code)}/${slug}/` : localeHomeRoute(code);
        node.url = fragment ? `${route}#${fragment}` : route;
        return;
      }

      const resolved = path.resolve(sourceDir, rawPath);
      const relative = path.relative(contentRoot, resolved).split(path.sep).join('/');
      const segments = relative.split('/');

      // The link had no literal "locales/" substring (so the regex above
      // didn't match) but resolved into src/content/locales/ anyway — a
      // chapter linking a sibling chapter within the same locale, written
      // as "../<sibling-slug>/index.md" from its own logical directory.
      if (segments[0] === 'locales') {
        const code = segments[1];
        if (segments[2] === 'chapters' && segments[4] === 'index.md') {
          const slug = segments[3];
          const route = `/${code}/${topicsSlug(code)}/${slug}/`;
          node.url = fragment ? `${route}#${fragment}` : route;
        } else if (segments.length === 3 && segments[2] === 'index.md') {
          const route = localeHomeRoute(code);
          node.url = fragment ? `${route}#${fragment}` : route;
        }
        return;
      }

      // "../index.md" from a top-level section resolves to src/content's own
      // index.md — that's docs/index.md in the source repo, which this site
      // doesn't copy (its role is played by the hand-authored home page).
      if (relative === 'index.md') {
        node.url = fragment ? `/${DEFAULT_LOCALE}/#${fragment}` : `/${DEFAULT_LOCALE}/`;
        return;
      }

      const [section, ...rest] = segments;
      if (!SECTIONS.has(section)) return;

      // A sibling chapter's flattened file, reached as "<slug>/index.md"
      // from the logical per-chapter directory: rest is ["<slug>", "index.md"].
      const file2 =
        section === 'chapters' && rest.length === 2 && rest[1] === 'index.md'
          ? rest[0]
          : rest.join('/').replace(/\.md$/, '');
      const isIndex = file2 === 'index';
      const route =
        section === 'chapters'
          ? `/${DEFAULT_LOCALE}/${topicsSlug(DEFAULT_LOCALE)}/${file2}/`
          : isIndex
            ? `/${section}/`
            : `/${section}/${file2}/`;

      node.url = fragment ? `${route}#${fragment}` : route;
    });
  };
}

/** @param {string} code */
function localeHomeRoute(code) {
  return `/${code}/`;
}
