<script>
  import manifest from '#lib/manifest.json';
  import { DEFAULT_LOCALE } from '#lib/locales.js';
  import { topicsBase } from '#lib/content.js';

  /** @type {{ currentSlug?: string | null, locale?: string, base?: string, placeholder?: string }} */
  let { currentSlug = null, locale = DEFAULT_LOCALE, base = `/${DEFAULT_LOCALE}`, placeholder = 'Filter chapters…' } = $props();

  let parts = $derived(manifest.locales[locale]?.parts ?? manifest.parts);

  let query = $state('');

  /** @param {{ title: string, decimal: string }} chapter @param {string} q */
  function matches(chapter, q) {
    if (!q) return true;
    return chapter.title.toLowerCase().includes(q) || chapter.decimal.includes(q);
  }
</script>

<nav class="sidebar" aria-label={placeholder}>
  <input
    class="sidebar-search"
    type="search"
    {placeholder}
    aria-label={placeholder}
    bind:value={query}
  />
  {#each parts as part (part.number)}
    {@const q = query.trim().toLowerCase()}
    {@const hasCurrent = part.chapters.some((c) => c.slug === currentSlug)}
    {@const visible = part.chapters.filter((c) => matches(c, q))}
    {#if visible.length}
      <details class="sidebar-part" open={hasCurrent || q !== ''} data-current={hasCurrent}>
        <summary><span class="part-number">{part.number}</span> {part.title}</summary>
        <ul class="sidebar-chapter-list">
          {#each visible as chapter (chapter.slug)}
            <li>
              <a
                href="{topicsBase(base.slice(1))}/{chapter.slug}/"
                aria-current={chapter.slug === currentSlug ? 'page' : undefined}
              >
                <span class="decimal">{chapter.decimal}</span>{chapter.title}
              </a>
            </li>
          {/each}
        </ul>
      </details>
    {/if}
  {/each}
</nav>
