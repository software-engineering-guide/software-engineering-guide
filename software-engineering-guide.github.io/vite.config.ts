import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import { mdsvex } from 'mdsvex';
import { fileURLToPath } from 'node:url';
import { remarkChapterLinks } from './scripts/remark-chapter-links.mjs';
import { remarkEscapeStrayLt } from './scripts/remark-escape-stray-lt.mjs';
import { remarkResolveContentLinks } from './scripts/remark-resolve-content-links.mjs';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

// mdsvex resolves a relative `layout` path against each Markdown file's own
// directory, not the project root — since src/content/ has several nested
// section directories, that relative resolution breaks. Use an absolute
// path instead.
const mdLayoutPath = fileURLToPath(new URL('./src/lib/MdLayout.svelte', import.meta.url));

/** @type {import('mdsvex').MdsvexOptions} */ const mdsvexOptions = {
  extensions: ['.md'],
  remarkPlugins: [
    remarkChapterLinks,
    remarkResolveContentLinks,
    remarkEscapeStrayLt
  ],
  layout: { _: mdLayoutPath }
};

export default defineConfig({
  plugins: [
    sveltekit({
      extensions: ['.svelte', '.md'],
      params: 'src/params.js',
      preprocess: [vitePreprocess(), mdsvex(mdsvexOptions)],
      adapter: adapter({
        pages: 'build',
        assets: 'build',
        fallback: '404.html',
        strict: true
      }),

      prerender: {
        // Every internal link resolves via remark-resolve-content-links.mjs —
        // fail the build (the default) if a future content change breaks one.
        handleHttpError: 'fail'
      }
    })
  ]
});
