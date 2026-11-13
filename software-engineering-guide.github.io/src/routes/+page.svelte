<script>
  import { localeLabel, DEFAULT_LOCALE } from '#lib/locales.js';
  import { locales } from '#lib/content.js';
  import { pickLocale } from '#lib/detect-locale.js';

  // "/" is the search page ("/?<target>") and the way in to the default
  // locale. A server-side redirect would drop the query string and break
  // search, so this prerendered page redirects in the browser, and only when
  // there is no query. The target is the locale that best matches the
  // browser's language (navigator.languages, then navigator.language; for
  // example "cy_GB" goes to /cy-001/ here, or /cy-gb/ where that locale is
  // served), falling back to DEFAULT_LOCALE. <noscript> covers visitors
  // without JavaScript, who get DEFAULT_LOCALE.
  $effect.pre(() => {
    if (!location.search) location.replace(`/${pickLocale(locales(), DEFAULT_LOCALE)}/`);
  });
</script>

<svelte:head>
  <title>Software Engineering Guide</title>
  <noscript><meta http-equiv="refresh" content="0; url=/{DEFAULT_LOCALE}/" /></noscript>
</svelte:head>

<p><a href="/{DEFAULT_LOCALE}/">{localeLabel(DEFAULT_LOCALE)}</a></p>

<ul>
  {#each locales() as code (code)}
    <li><a href="/{code}/">{localeLabel(code)}</a></li>
  {/each}
</ul>
