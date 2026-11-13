<script>
  import manifest from '#lib/manifest.json';

  let { data } = $props();
</script>

<svelte:head>
  <title>Examples — Software Engineering Guide</title>
</svelte:head>

<data.content />

<ul class="card-grid">
  {#each manifest.examples as entry (entry.slug)}
    <a class="card" href="/examples/{entry.slug}/">
      <h2 class="card-heading">{entry.title}</h2>
    </a>
  {/each}
</ul>
