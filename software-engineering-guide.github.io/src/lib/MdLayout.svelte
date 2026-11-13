<!--
  Default mdsvex layout applied to every compiled Markdown file (see
  svelte.config.js). Kept deliberately minimal: it just supplies the
  `.prose` typography wrapper. Page chrome (breadcrumb, chapter number,
  prev/next pager) lives in the route +page.svelte files instead, since
  those need the manifest entry, not just the rendered body.
-->
<div class="prose">
  <slot />
</div>
