<script>
  // A prerendered stand-in for a URL that moved. GitHub Pages serves static
  // files and cannot send a 301, so the old path gets a small page that
  // redirects in the browser (meta refresh, which works without JavaScript)
  // and names the new URL as canonical for search engines.
  let { to } = $props();
</script>

<svelte:head>
  <meta http-equiv="refresh" content="0; url={to}" />
  <link rel="canonical" href={to} />
  <meta name="robots" content="noindex" />
</svelte:head>

<p>This page has moved to <a href={to}>{to}</a>.</p>
