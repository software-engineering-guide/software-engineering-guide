<script>
  import manifest from '#lib/manifest.json';

  let { data } = $props();
</script>

<svelte:head>
  <title>Project — Software Engineering Guide</title>
</svelte:head>

<data.content />

<ul class="card-grid">
  {#each manifest.project as entry (entry.slug)}
    <a class="card" href="/project/{entry.slug}/">
      <h2 class="card-heading">{entry.title}</h2>
    </a>
  {/each}
</ul>
