<script>
  /** @type {{ items: Array<{ label: string, href?: string }> }} */
  let { items } = $props();
</script>

<nav class="breadcrumb" aria-label="Breadcrumb">
  {#each items as item, i (item.label)}
    {#if i > 0}<span class="sep" aria-hidden="true">/</span>{/if}
    {#if item.href}
      <a href={item.href}>{item.label}</a>
    {:else}
      <span aria-current="page">{item.label}</span>
    {/if}
  {/each}
</nav>
