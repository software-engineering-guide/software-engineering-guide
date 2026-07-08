# Software Engineering Recommendations: build and check tasks.
# The validation suite needs only Python 3; the site build uses uv + Zensical.

# List available tasks.
default:
    @just --list --unsorted

# Run the validation suite.
test:
    python3 tests/validate.py

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

# Print chapter and word counts.
stats:
    @echo "chapters: $(ls docs/chapters/*.md | wc -l | tr -d ' ')"
    @echo "words:    $(cat docs/chapters/*.md | wc -w | tr -d ' ')"
    @echo "wiki links: $(grep -rho 'en.wikipedia.org/wiki' docs/chapters/*.md | wc -l | tr -d ' ')"
