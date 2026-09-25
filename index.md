# Repository index

A map of everything in this repository. For the book itself, start with the
[table of contents](README.md) or the opening chapter,
[What is software engineering?](docs/front-matter/what-is-software-engineering.md).
The book is published as a website at
<https://software-engineering-guide.github.io/>.

## The book (everything under `docs/` and `locales/` is published)

- **[README.md](README.md)** : the full table of contents (12 parts, 147 chapters).
- **[docs/index.md](docs/index.md)** : the home page of the published site.
- **[docs/front-matter/what-is-software-engineering.md](docs/front-matter/what-is-software-engineering.md)** : the opening essay. Start here.
- **[docs/front-matter/introduction.md](docs/front-matter/introduction.md)** : who the book is for and how it is organized.
- **[docs/front-matter/table-of-contents.md](docs/front-matter/table-of-contents.md)** : the contents page.
- **[locales/en-us/chapters/](locales/en-us/chapters/)** : the canonical English chapter content, one directory per chapter (`N.M-slug/index.md`).
- **[locales/](locales/)** : the same chapters translated per locale (`locales/<code>/chapters/<translated-slug>/index.md`), per `spec/locales-for-global-sharing-with-svelte/index.md`.

## The appendices (Part 12)

- **[Glossary](locales/en-us/chapters/12-01-glossary/index.md)** : definitions of key terms.
- **[Checklists](locales/en-us/chapters/12-02-checklists/index.md)** : ready-to-use review and launch checklists.
- **[Templates](locales/en-us/chapters/12-03-templates/index.md)** : ADRs, RFCs, postmortems, threat models, and more.
- **[Maturity self-assessment](locales/en-us/chapters/12-04-maturity-self-assessment/index.md)** : the four-level model for every domain.
- **[References](locales/en-us/chapters/12-05-references/index.md)** : the SWEBOK crosswalk, standards index, and bibliography.
- **[Adoption roadmap](locales/en-us/chapters/12-06-adoption-roadmap/index.md)** : how to roll the practices out.
- **[Index](locales/en-us/chapters/12-07-index/index.md)** : the subject index.

## Specification (source of truth)

The book is the source of truth; the published website is a rendering of it,
built by the separate `software-engineering-guide.github.io` repository. The
spec lives at the repository root, not under `docs/`, and is not published to
the site.

- **[spec/index.md](spec/index.md)** : how the spec drives the book.
- **[spec/structure.md](spec/structure.md)** : the canonical chapter manifest.
- **[spec/conventions.md](spec/conventions.md)** : the writing and format specification.
- **[spec/roadmap.md](spec/roadmap.md)** : backlog and adoption checklists.

## Contributing and tooling

- **[AGENTS.md](AGENTS.md)** : guidance for AI agents and contributors.
- **[CONTRIBUTING.md](CONTRIBUTING.md)** : how to contribute.
- **[docs/contributing/](docs/contributing/index.md)** : the contributor guides and shared snippets.
- **[docs/project/](docs/project/index.md)** : project documentation.
- **[docs/examples/](docs/examples/index.md)** : small illustrative examples.
- **[tools/gen_nav.py](tools/gen_nav.py)** : navigation generator (`just nav`).
- **[tests/validate.py](tests/validate.py)** : validation suite (`just test`).
- **[docs/project/changelog.md](docs/project/changelog.md)** : history of notable changes.
- **[justfile](justfile)** : the task runner (`just` lists all tasks).
- **[.devcontainer/](.devcontainer/devcontainer.json)** : dev container with git-lfs and just preinstalled.

## Quick start

```sh
just         # list available tasks
just test    # validate the whole repository
just nav     # regenerate the generated navigation files
just stats   # chapter and word counts
```
