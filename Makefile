# Software Engineering Recommendations: build and check tasks.
# Requires only Python 3. No third-party packages, no network.

.DEFAULT_GOAL := help
PY := python3

.PHONY: help test nav build check emdash stats

help: ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'

test: ## Run the validation suite.
	@$(PY) tests/validate.py

nav: ## Regenerate the table of contents, contents page, and subject index.
	@$(PY) tools/gen_nav.py

build: nav test ## Regenerate navigation, then validate.

check: test ## Alias for test.

emdash: ## List any em-dashes left in the repository (should be none).
	@grep -rn '—' --include='*.md' . || echo "no em-dashes found"

stats: ## Print chapter and word counts.
	@echo "chapters: $$(ls chapters/*.md | wc -l | tr -d ' ')"
	@echo "words:    $$(cat chapters/*.md | wc -w | tr -d ' ')"
	@echo "wiki links: $$(grep -rho 'en.wikipedia.org/wiki' chapters/*.md | wc -l | tr -d ' ')"
