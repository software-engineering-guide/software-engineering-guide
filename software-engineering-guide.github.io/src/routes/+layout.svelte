<script>
  import SearchGate from '#lib/SearchGate.svelte';
  import { page } from '$app/state';
  import { goto } from '$app/navigation';
  import Sidebar from '#lib/Sidebar.svelte';
  import PickerBar from '@lilydesignsystem/svelte-picker-bar';
  import manifest from '#lib/manifest.json';
  import { locales as availableLocales, resolveLocale, topicsBase, topicsSlug } from '#lib/content.js';
  import { localeLabel, DEFAULT_LOCALE } from '#lib/locales.js';
  import { DEFAULT_UI } from '#lib/i18n.js';

  let { children } = $props();

  // The header (brand wordmark, nav labels, picker labels, footer text)
  // lives in the root layout, rendered on every route, but it must still
  // read as this locale on any /<code>/ page. Per
  // spec/locales-for-global-sharing-with-svelte/index.md's regression
  // watch-list ("UI chrome was hardcoded English in the .svelte templates
  // ... nav labels ... Fix: add i18n.js and threading ui(locale) through
  // every locale-scoped route" and "header/footer brand wordmark stayed
  // English ... Fix: have locales/[locale]/+layout.server.js supply this
  // locale's own title, which overrides the root layout's canonical one
  // via SvelteKit's merged page.data"): [locale=locale]/+layout.server
  // .js's load() puts `ui` in its data, and SvelteKit merges that into
  // page.data for the whole active route tree, so reading page.data here
  // (rather than a module-level `ui('en-us')` constant) makes the header
  // locale-reactive without the root layout needing to know the current
  // locale itself.
  let headerUi = $derived(page.data.ui ?? DEFAULT_UI);

  // The locale segment of the current URL ("/<code>/..."), or the default
  // locale for the English-only root sections ("/front-matter/...",
  // "/examples/...", and so on). `localeBase` keeps links inside the alias
  // ("/en/...") the visitor is browsing. Leaving the current locale
  // undefined for those routes would feed localeProps.defaultValue={undefined}
  // to the locale picker, which then falls back to its first list entry and
  // fires onChange on mount, silently redirecting every one of those pages.
  let pathname = $derived(page.url.pathname);
  let urlSegment = $derived(pathname.split('/')[1]);
  let urlLocale = $derived(resolveLocale(urlSegment));
  let currentLocale = $derived(urlLocale ?? DEFAULT_LOCALE);
  let localeBase = $derived(`/${urlLocale ? urlSegment : DEFAULT_LOCALE}`);

  // Home, contents, and chapters are translated per locale; front matter,
  // examples, contributing, and project are English-only sections at the
  // root, but their label text still reads in the visitor's language.
  let navLinks = $derived([
    { href: `${localeBase}/`, label: headerUi.home },
    { href: '/front-matter/what-is-software-engineering/', label: headerUi.startHere },
    { href: `${localeBase}/contents/`, label: headerUi.tableOfContents },
    { href: '/examples/', label: headerUi.examples },
    { href: '/contributing/', label: headerUi.contributing },
    { href: '/project/', label: headerUi.project }
  ]);

  // The link picker (the first button in the header bar) offers the same pages
  // as the nav row above, plus the project's source repository.
  let pickerLinks = $derived([
    ...navLinks.map((link) => ({ label: link.label, href: link.href, current: isCurrent(link.href) })),
    { label: 'GitHub', href: 'https://github.com/software-engineering-guide/software-engineering-guide', newTab: true }
  ]);

  let showSidebar = $derived(
    pathname.startsWith('/front-matter/') || (urlLocale !== null && pathname.startsWith(`${topicsBase(urlSegment)}/`))
  );
  let currentSlug = $derived(showSidebar ? (pathname.split('/').filter(Boolean).pop() ?? null) : null);

  /** @param {string} href */
  function isCurrent(href) {
    return pathname === href;
  }

  // Header picker bar: locale list, labels, and the locale switch itself.
  // PickerBar/LocalePicker only manage picker UI state — navigating to the
  // matching page in the newly-picked locale is this app's job.
  const pickerLocales = availableLocales();

  /**
   * Finds the equivalent page for `toLocale`, mapping the current chapter
   * across locales by its decimal number (per
   * spec/locales-for-global-sharing-with-svelte/index.md: "Nothing in the
   * site assumes slugs match across locales"). Falls back to that locale's
   * home page when there is no current chapter, or it is not yet
   * translated into `toLocale`.
   * @param {string} toLocale
   */
  function pathForLocale(toLocale) {
    const segments = pathname.split('/').filter(Boolean);
    if (urlLocale === null) return `/${toLocale}/`;
    if (segments[1] === 'contents') return `/${toLocale}/contents/`;
    if (segments[1] === topicsSlug(urlSegment) && segments[2]) {
      const decimal = manifest.locales[urlLocale]?.chapters.find((c) => c.slug === segments[2])?.decimal;
      const target = decimal ? manifest.locales[resolveLocale(toLocale) ?? toLocale]?.chaptersByDecimal?.[decimal] : null;
      if (target) return `${topicsBase(toLocale)}/${target.slug}/`;
    }
    return `/${toLocale}/`;
  }

  /** @param {string} toLocale */
  function onLocaleChange(toLocale) {
    if (toLocale === currentLocale) return;
    // A search (/?<target>) is on the root page: the picker's automatic
    // restore of the stored locale must not navigate away and drop it.
    if (page.url.pathname === '/' && page.url.search) return;
    goto(pathForLocale(toLocale));
  }
</script>

<a class="skip-link" href="#main">{headerUi.skipToContent}</a>

<header class="site-header">
  <div class="site-header-inner">
    <a class="site-brand" href="{localeBase}/" aria-label="{headerUi.siteName} home">
      <img class="site-brand-mark" src="/assets/favicon.svg" alt="" aria-hidden="true" />
      <span>{headerUi.siteName}</span>
    </a>
    <nav class="site-nav" aria-label="Main">
      {#each navLinks as link (link.href)}
        <a href={link.href} aria-current={isCurrent(link.href) ? 'page' : undefined}>{link.label}</a>
      {/each}
      <a href="https://github.com/software-engineering-guide/software-engineering-guide">GitHub</a>
    </nav>
    <!--
      Keyed on currentLocale: LocalePicker's `value` is "two-way bindable"
      but PickerBar only exposes it via a plain (one-way) `localeProps.value`
      spread, with no way to `bind:` through that spread. Passing a
      continuously-recomputed `value: currentLocale` there fights the
      picker's own internal selection state — every click momentarily
      selects the new locale, then the still-current `value` prop snaps it
      straight back, so `onChange` never fires and the picker looks like it
      does nothing. Fix: seed the initial selection with `defaultValue`
      (which the picker only reads once, on mount, so it stops fighting
      clicks) and key the whole bar on `currentLocale` so it fully remounts
      — reseeding that initial value — whenever the URL's locale changes for
      a reason other than this picker (a chapter link, browser back/forward,
      or a direct URL edit), keeping the shown selection honest.

      shareProps below sets strategy: 'list', pinning SharePicker to its
      in-page dropdown. Its default 'auto' tries navigator.share() first on
      any browser that exposes it, but the promise can reject for reasons
      other than the user dismissing the sheet (no share targets
      registered, no secure context, automated/embedded browsers) —
      SharePicker treats every rejection as a dismissal and does not fall
      back to the list, so the button then does nothing at all. With only
      two targets (email, copy link), the plain list is simpler and
      reliable on every platform anyway.
    -->
    {#key currentLocale}
      <PickerBar
        class="site-picker-bar"
        labels={{
          link: headerUi.pickerLink,
          search: headerUi.search,
          searchInput: headerUi.searchInput,
          searchSubmit: headerUi.searchSubmit,
          theme: headerUi.pickerTheme,
          locale: headerUi.pickerLocale,
          textSize: headerUi.pickerTextSize,
          share: headerUi.pickerShare
        }}
        links={pickerLinks}
        linkProps={{ navigate: goto }}
        searchProps={{ navigate: goto }}
        themesUrl="/themes/"
        themeProps={{ storageKey: 'lily-theme', detectFromSystem: true }}
        locales={pickerLocales}
        localeProps={{
          defaultValue: currentLocale,
          localeLabels: Object.fromEntries(pickerLocales.map((code) => [code, localeLabel(code)])),
          onChange: onLocaleChange
        }}
        shareTargets={[
          {
            id: 'email',
            label: headerUi.shareEmail,
            href: (url, title) => `mailto:?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(url)}`
          }
        ]}
        shareProps={{ copyLabel: headerUi.shareCopyLink, strategy: 'list' }}
      />
    {/key}
  </div>
</header>

<main id="main" class="site-main" class:has-sidebar={showSidebar}>
  {#if showSidebar}
    <Sidebar
      {currentSlug}
      locale={currentLocale}
      base={localeBase}
      placeholder={headerUi.filterChapters}
    />
  {/if}
  <div class="site-content">
    <SearchGate {children} />
  </div>
</main>

<footer class="site-footer">
  <div class="site-footer-inner">
    <p>
      {headerUi.footerTagline}
      <a href="https://github.com/software-engineering-guide">software-engineering-guide</a> {headerUi.footerOrgSuffix}
    </p>
    <p>
      {headerUi.footerLedBy}
      <a href="https://linkedin.com/in/joelparkerhenderson">Joel Parker Henderson</a>.
    </p>
    <div class="site-footer-links">
      <a href="https://github.com/software-engineering-guide/software-engineering-guide">{headerUi.contentSource}</a>
      <a href="https://github.com/software-engineering-guide/software-engineering-guide.github.io">{headerUi.siteSource}</a>
      <a href="{localeBase}/contents/">{headerUi.tableOfContents}</a>
      <a href="/contributing/">{headerUi.contributing}</a>
    </div>
  </div>
</footer>
