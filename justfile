# Software Engineering Guide: build and check tasks.
# The validation suite needs only Python 3; the site build uses uv + Zensical.

# List available tasks.
default:
    @just --list --unsorted

# Run the validation suite and the cross-reference linking tests.
test:
    python3 tests/validate.py
    uv run python tests/test_xref.py

# Regenerate the TOC, contents page, subject index, and zensical.toml nav.
nav:
    python3 tools/gen_nav.py

# Regenerate navigation, then validate.
check: nav test

# Build the documentation site into site/.
build:
    uv run zensical build --clean

# Build and serve the documentation site locally with live reload.
serve:
    uv run zensical serve

# List any em-dashes left in the repository (should be none).
emdash:
    @grep -rn '—' --include='*.md' --exclude-dir=site --exclude-dir=.venv . || echo "no em-dashes found"

# Spell-check the repository (configured in pyproject.toml).
spell:
    uv run codespell

# Lint prose against the house style with Vale (see .vale.ini). Warnings
# inform; only errors fail. Requires the vale binary on PATH.
lint:
    vale docs spec *.md

# Print the Markdown stats report (per-chapter word counts, thin chapters,
# Wikipedia links, reference entries, totals).
stats:
    @python3 tools/stats.py
