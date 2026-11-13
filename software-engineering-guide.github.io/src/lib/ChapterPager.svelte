<script>
  /** @type {{ prev: null | { slug: string, decimal: string, title: string }, next: null | { slug: string, decimal: string, title: string }, hrefBase?: string, prevLabel?: string, nextLabel?: string }} */
  let { prev = null, next = null, hrefBase = '/chapters/', prevLabel = '←', nextLabel = '→' } = $props();
</script>

{#if prev || next}
  <nav class="chapter-pager" aria-label="Chapter navigation">
    {#if prev}
      <a class="chapter-pager-link prev" href="{hrefBase}{prev.slug}/">
        <span class="chapter-pager-label">{prevLabel} {prev.decimal}</span>
        <span class="chapter-pager-title">{prev.title}</span>
      </a>
    {:else}
      <span></span>
    {/if}
    {#if next}
      <a class="chapter-pager-link next" href="{hrefBase}{next.slug}/">
        <span class="chapter-pager-label">{next.decimal} {nextLabel}</span>
        <span class="chapter-pager-title">{next.title}</span>
      </a>
    {:else}
      <span></span>
    {/if}
  </nav>
{/if}
