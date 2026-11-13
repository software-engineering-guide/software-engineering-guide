<script>
  import Breadcrumb from '#lib/Breadcrumb.svelte';
  import ChapterPager from '#lib/ChapterPager.svelte';
  import manifest from '#lib/manifest.json';
  import { topicsBase } from '#lib/content.js';

  let { data } = $props();
  let localeManifest = $derived(manifest.locales[data.locale]);
  let part = $derived(localeManifest.parts.find((p) => p.number === data.chapter.part));
  let partIntro = $derived(part?.chapters.find((c) => c.chapter === 0));
</script>

<svelte:head>
  <title>{data.chapter.heading} — {data.ui.siteName}</title>
  <meta name="description" content="{data.ui.part} {data.chapter.part}: {part?.title ?? ''} — {data.chapter.title}" />
</svelte:head>

<Breadcrumb
  items={[
    { label: data.ui.home, href: `${data.base}/` },
    {
      label: `${data.ui.part} ${data.chapter.part}: ${part?.title ?? ''}`,
      href: partIntro ? `${data.topicsBase}/${partIntro.slug}/` : undefined
    },
    { label: data.chapter.decimal }
  ]}
/>

<span class="chapter-decimal">{data.chapter.decimal}</span>

{#if data.enChapter && data.locale !== 'en-us'}
  <p class="locale-notice">
    <a href="{topicsBase('en-us')}/{data.enChapter.slug}/">{data.ui.viewInEnglish}</a>
  </p>
{/if}

<data.content />

<ChapterPager
  prev={data.prev}
  next={data.next}
  hrefBase="{data.topicsBase}/"
  prevLabel={data.ui.previous}
  nextLabel={data.ui.next}
/>
