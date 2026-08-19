# Software Engineering Guide: content and check tasks.
# This repository holds the book's content and specification; it is rendered
# into a website by the separate software-engineering-guide.github.io repository.
# The validation suite needs only Python 3.

# List available tasks.
default:
    @just --list --unsorted

# Run the validation suite.
test:
    python3 tests/validate.py

# Regenerate the TOC, contents page, and subject index.
nav:
    python3 tools/gen_nav.py

# Regenerate navigation, then validate.
check: nav test

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
