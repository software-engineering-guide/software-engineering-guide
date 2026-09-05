---
name: software-engineering-guide-maintainer-skill
description: Use when working IN the software-engineering-guide repository (writing or editing chapters, changing spec/structure, regenerating navigation, running tests/lint/spell, updating the changelog) or IN the software-engineering-guide.github.io website repository (syncing content, regenerating the manifest, svelte-check). For maintainers of these two repositories only. For readers who just want to consult the guide's content, use software-engineering-guide-skill instead.
---

# Software Engineering Guide: maintainer

Two sibling repositories, each with its own `AGENTS.md` as the canonical,
enforceable source of truth. Read the relevant one in full before editing;
this skill is a map to it, not a replacement for it.

- **`software-engineering-guide`** owns the book's content and spec (100
  chapters across 12 parts, front matter, appendices).
- **`software-engineering-guide.github.io`** owns the SvelteKit site that
  renders it. It never owns content; it copies it in.

## Content repo: `software-engineering-guide`

Read `AGENTS.md` at the repo root first. Golden rules (enforced by
`tests/validate.py` where marked "test" in
`docs/contributing/style-rules.md`):

1. No em-dashes ("—"). En-dashes are fine only in numeric ranges (`4.1–4.6`).
2. No stock LLM phrasing ("not only ... but also", "load-bearing", "It's
   important to note", etc.).
3. Content chapters follow the fixed section order in
   `docs/contributing/chapter-template.md`.
4. Define terms on first use; link key concepts to Wikipedia on first mention
   in prose. Real references only, never fabricated.
5. `spec/` (not `docs/`) is the source of truth for structure
   (`spec/structure.md`) and conventions (`spec/conventions.md`). Change the
   spec and the chapters together.

Workflow for any change:

1. Read the matching task guide: `docs/contributing/authoring.md` (writing or
   editing a chapter), `docs/contributing/navigation.md` (structure changes),
   or `docs/contributing/testing.md` (understanding the test suite).
2. Make the smallest change that satisfies the request.
3. If the set of chapters changed, update `spec/structure.md` and run
   `just nav` to regenerate the README TOC, site home page, contents page,
   and subject index.
4. Run `just test` (required), then `just spell` and `just lint` (CI runs all
   three; `just lint` needs the `vale` binary on PATH). `just check` runs
   `nav` then `test` in one step.
5. Add a one-line entry to `docs/project/changelog.md` under **Unreleased**.

Pre-commit hooks run the same checks automatically (`uv sync && uv run
pre-commit install`); Claude Code sessions get this via the SessionStart hook
in `.claude/hooks/session-start.sh`.

## Website repo: `software-engineering-guide.github.io`

Read its `AGENTS.md` first. It is a SvelteKit static site
(`@sveltejs/adapter-static`) that prerenders the book; it does not author
content.

- `src/content/` is **generated** from the sibling content repo's `docs/` by
  `scripts/sync-content.mjs`. Never hand-edit it. After editing the content
  repo, run `pnpm run content` here to re-sync and rebuild the manifest.
- `src/lib/manifest.json` is **generated** by `scripts/generate-manifest.mjs`.
  Never hand-edit it.
- New content sections follow the existing route pattern: a
  `[slug]/+page.js` with `entries()` sourced from the manifest, dynamically
  importing the matching `.md` file, and a `+page.svelte` rendering the
  compiled content inside the page chrome.
- Never touch the sibling content repo from here; it owns the book.
- Run `pnpm run check` (svelte-check) before committing changes to `src/`.

This repo assumes `software-engineering-guide` is checked out as a sibling
directory (`../software-engineering-guide` relative to this repo).

## When a change touches both repos

Edit the content repo first (chapters, spec, nav), finish its checklist
above, then switch to the website repo and run `pnpm run content` to pull the
change in before committing there. The two are independent git repos with
independent commits; don't conflate their changelogs or checks.
