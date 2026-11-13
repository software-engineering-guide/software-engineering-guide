<script>
  import manifest from '#lib/manifest.json';

  let { data } = $props();
</script>

<svelte:head>
  <title>Contributing — Software Engineering Guide</title>
</svelte:head>

<data.content />

<ul class="card-grid">
  {#each manifest.contributing as entry (entry.slug)}
    <a class="card" href="/contributing/{entry.slug}/">
      <h2 class="card-heading">{entry.title}</h2>
    </a>
  {/each}
</ul>
