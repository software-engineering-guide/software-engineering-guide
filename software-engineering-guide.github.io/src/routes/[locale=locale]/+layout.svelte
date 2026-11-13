<script>
  import { page } from '$app/state';

  // The <html lang>/<html dir> attributes themselves are set server-side
  // (so prerendered HTML is correct before any JS runs) by the
  // transformPageChunk hook in src/hooks.server.js, which reads this same
  // /<code>/ URL prefix. This wrapper covers the client-rendered case
  // (client-side navigation between locales) and gives the locale subtree an
  // explicit lang/dir for assistive technology regardless.
  let { data, children } = $props();

  // A language alias ("/en/...") duplicates its world locale ("/en-001/...").
  let canonical = $derived(
    data.isAlias
      ? `https://software-engineering-guide.github.io${page.url.pathname.replace(/^\/[^/]+/, `/${data.locale}`)}`
      : null
  );
</script>

<svelte:head>
  {#if canonical}<link rel="canonical" href={canonical} />{/if}
</svelte:head>

<div class="locale-scope" lang={data.lang} dir={data.dir}>
  {@render children()}
</div>
