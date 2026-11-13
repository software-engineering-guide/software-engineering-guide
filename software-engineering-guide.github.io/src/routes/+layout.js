// Every route link in this site is written in directory style
// ("/chapters/slug/"). GitHub Pages serves static files, not a server that
// can rewrite "/x" -> "/x/" itself, so prerendering must emit
// "chapters/slug/index.html" to match — hence 'always' rather than the
// SvelteKit default of 'never'.
export const trailingSlash = 'always';

// The whole site is static content; prerender everything by default. Each
// dynamic [slug] route also declares its own `entries()` to enumerate slugs.
export const prerender = true;
