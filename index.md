# Repository index

A map of everything in this repository. For the book itself, start with the
[table of contents](README.md) or the opening chapter,
[What is software engineering?](docs/front-matter/what-is-software-engineering.md).
The book is published as a website at
<https://software-engineering-guide.github.io/software-engineering-guide/>.

## The book (everything under `docs/` is published)

- **[README.md](README.md)** : the full table of contents (12 parts, 100 chapters).
- **[docs/index.md](docs/index.md)** : the home page of the published site.
- **[docs/front-matter/what-is-software-engineering.md](docs/front-matter/what-is-software-engineering.md)** : the opening essay. Start here.
- **[docs/front-matter/introduction.md](docs/front-matter/introduction.md)** : who the book is for and how it is organized.
- **[docs/front-matter/table-of-contents.md](docs/front-matter/table-of-contents.md)** : the contents page.
- **[docs/chapters/](docs/chapters/)** : the 100 chapter files, named `N.M-slug.md`.

## The appendices (Part 12)

- **[Glossary](docs/chapters/12.1-glossary.md)** : definitions of key terms.
- **[Checklists](docs/chapters/12.2-checklists.md)** : ready-to-use review and launch checklists.
- **[Templates](docs/chapters/12.3-templates.md)** : ADRs, RFCs, postmortems, threat models, and more.
- **[Maturity self-assessment](docs/chapters/12.4-maturity-self-assessment.md)** : the four-level model for every domain.
- **[References](docs/chapters/12.5-references.md)** : the SWEBOK crosswalk, standards index, and bibliography.
- **[Adoption roadmap](docs/chapters/12.6-adoption-roadmap.md)** : how to roll the practices out.
- **[Index](docs/chapters/12.7-index.md)** : the subject index.

## Specification (source of truth)

- **[docs/spec/index.md](docs/spec/index.md)** : how the spec drives the book.
- **[docs/spec/structure.md](docs/spec/structure.md)** : the canonical chapter manifest.
- **[docs/spec/conventions.md](docs/spec/conventions.md)** : the writing and format specification.
- **[docs/spec/roadmap.md](docs/spec/roadmap.md)** : backlog and adoption checklists.

## Contributing and tooling

- **[AGENTS.md](AGENTS.md)** : guidance for AI agents and contributors.
- **[CONTRIBUTING.md](CONTRIBUTING.md)** : how to contribute.
- **[docs/contributing/](docs/contributing/index.md)** : the contributor guides and shared snippets.
- **[docs/project/](docs/project/index.md)** : project documentation.
- **[docs/examples/](docs/examples/index.md)** : small illustrative examples.
- **[tools/gen_nav.py](tools/gen_nav.py)** : navigation generator (`just nav`).
- **[guide_xref/](guide_xref/__init__.py)** : build-time auto-linking of chapter cross-references.
- **[tests/validate.py](tests/validate.py)** : validation suite (`just test`).
- **[docs/project/changelog.md](docs/project/changelog.md)** : history of notable changes.

## The published site

- **[zensical.toml](zensical.toml)** : site configuration and navigation (the `nav` block is generated).
- **[SITE.md](SITE.md)** : how the site is built and deployed.
- **[justfile](justfile)** : the task runner (`just` lists all tasks).
- **[.github/workflows/docs.yml](.github/workflows/docs.yml)** : builds and deploys the site to GitHub Pages.
- **[.devcontainer/](.devcontainer/devcontainer.json)** : dev container with uv and just preinstalled.

## Quick start

```sh
just         # list available tasks
just test    # validate the whole repository
just nav     # regenerate the generated navigation files
just build   # build the documentation site into site/
just serve   # serve the site locally with live reload
just stats   # chapter and word counts
```
