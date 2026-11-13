<script>
  import Breadcrumb from '#lib/Breadcrumb.svelte';
  import { DEFAULT_LOCALE } from '#lib/locales.js';

  let { data } = $props();
</script>

<svelte:head>
  <title>{data.entry.title} — Software Engineering Guide</title>
</svelte:head>

<Breadcrumb items={[{ label: 'Home', href: `/${DEFAULT_LOCALE}/` }, { label: 'Examples', href: '/examples/' }, { label: data.entry.title }]} />

<data.content />
