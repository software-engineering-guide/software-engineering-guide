<script>
  import manifest from '#lib/manifest.json';

  let { data } = $props();
  let localeManifest = $derived(manifest.locales[data.locale]);
  let query = $state('');
  let q = $derived(query.trim().toLowerCase());

  /** @param {{ title: string, decimal: string }} chapter @param {string} q */
  function matches(chapter, q) {
    if (!q) return true;
    return chapter.title.toLowerCase().includes(q) || chapter.decimal.includes(q);
  }
</script>

<svelte:head>
  <title>{data.ui.tableOfContents} — {data.ui.siteName}</title>
  <meta
    name="description"
    content="{data.ui.tableOfContents}: {localeManifest.parts.length} / {localeManifest.chapters.length}"
  />
</svelte:head>

<div class="prose">
  <h1>{data.ui.tableOfContents}</h1>
</div>

<input
  class="toc-search"
  type="search"
  placeholder={data.ui.filterChapters}
  aria-label={data.ui.filterChapters}
  bind:value={query}
/>

  <ul class="contents-list">
    {#each localeManifest.parts as part (part.number)}
      {@const visible = part.chapters.filter((c) => matches(c, q))}
      {#if visible.length}
        <li>
          {part.number} {part.title}
          <ul>
            {#each visible as chapter (chapter.slug)}
              <li>
                <a href="{data.topicsBase}/{chapter.slug}/">{chapter.decimal} {chapter.title}</a>
              </li>
            {/each}
          </ul>
        </li>
      {/if}
    {/each}
  </ul>
