#!/bin/bash
# SessionStart hook for Claude Code (web and CLI): install the project
# dependencies and wire the pre-commit hooks into .git/hooks, so every
# commit runs the validation suite, codespell, and the em-dash check.
#
# All pre-commit hooks are local (see .pre-commit-config.yaml) and codespell
# is a uv dev dependency, so this needs PyPI at most and works in the
# Claude Code web sandbox, where GitHub cloning and binary downloads are
# blocked. Vale (`just lint`) is the one tool this cannot install there;
# it runs in CI and can be installed locally from https://vale.sh.
set -euo pipefail

cd "$CLAUDE_PROJECT_DIR"

if ! command -v uv >/dev/null 2>&1; then
  echo "session-start: uv not found; skipping dependency and pre-commit setup." >&2
  echo "session-start: install uv (https://docs.astral.sh/uv/) and run: uv sync && uv run pre-commit install" >&2
  exit 0
fi

# Project dependencies plus the dev tools (codespell, pre-commit), pinned
# by uv.lock. Idempotent and fast when already synced.
uv sync --locked

# Wire the hooks into .git/hooks (idempotent; skipped in a worktree-less
# checkout such as a bare CI clone).
if [ -e .git ]; then
  uv run pre-commit install
fi
