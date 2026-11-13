<script>
  import manifest from '#lib/manifest.json';
  import { HERO, ENDONYMS } from '#lib/hero.js';

  let { data } = $props();
  let localeManifest = $derived(manifest.locales[data.locale]);
  let hero = $derived(HERO[data.locale] ?? HERO['en-001']);
  let isEnglish = $derived(data.lang.startsWith('en'));
  let firstChapter = $derived(localeManifest.chapters[0]?.slug);
  const translations = Object.keys(manifest.locales).filter((code) => code.endsWith('-001') && code in ENDONYMS);
</script>

<svelte:head>
  <title>{hero.headline} — {data.localeLabel}</title>
</svelte:head>

{#if data.hasHomePage}
  <data.content />
{:else}
  <section class="hero">
    <p class="hero-eyebrow">{hero.tagline}</p>
    <h1>{hero.headline}</h1>
    <p class="hero-tagline">{hero.intro}</p>
    <div class="button-row">
      {#if isEnglish}
        <a class="button button-primary" href="/front-matter/what-is-software-engineering/">{hero.start}</a>
      {:else if firstChapter}
        <a class="button button-primary" href="{data.topicsBase}/{firstChapter}/">{hero.start}</a>
      {/if}
      <a class="button button-secondary" href="{data.base}/contents/">{hero.contents}</a>
      {#if isEnglish}<a class="button button-secondary" href="/examples/">{data.ui.examples}</a>{/if}
    </div>
    <p class="hero-translations">
      {hero.translations}{#each translations as code, i (code)}{i ? ', ' : ''}<a
          href="/{code}/"
          aria-current={code === data.locale ? 'page' : undefined}>{ENDONYMS[code]}</a
        >{/each}
    </p>
  </section>

  <section class="section">
    <ul class="contents-list">
      {#each localeManifest.parts as part (part.number)}
        <li>
          {part.number} {part.title}
          <ul>
            {#each part.chapters as chapter (chapter.slug)}
              <li>
                <a href="{data.topicsBase}/{chapter.slug}/">{chapter.decimal} {chapter.title}</a>
              </li>
            {/each}
          </ul>
        </li>
      {/each}
    </ul>
  </section>
{/if}
