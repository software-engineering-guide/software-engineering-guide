<script>
  import manifest from '#lib/manifest.json';
</script>

<svelte:head>
  <title>Front matter — Software Engineering Guide</title>
</svelte:head>

<div class="prose">
  <h1>Front matter</h1>
  <p>Start here: what the guide is, who it is for, and the full contents.</p>
</div>

<ul class="card-grid">
  {#each manifest.frontMatter as entry (entry.slug)}
    <a class="card" href="/front-matter/{entry.slug}/">
      <h2 class="card-heading">{entry.title}</h2>
    </a>
  {/each}
</ul>
