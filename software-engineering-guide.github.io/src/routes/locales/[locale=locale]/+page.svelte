<script>
  import Redirect from '#lib/Redirect.svelte';
  let { data } = $props();
</script>

<Redirect to={data.to} />
