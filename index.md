# Repository index

A map of everything in this repository. For the book itself, start with the
[table of contents](README.md) or the opening chapter,
[What is software engineering?](front-matter/what-is-software-engineering.md).

## The book

- **[README.md](README.md)** : the full table of contents (12 parts, 100 chapters).
- **[front-matter/what-is-software-engineering.md](front-matter/what-is-software-engineering.md)** : the opening essay. Start here.
- **[front-matter/introduction.md](front-matter/introduction.md)** : who the book is for and how it is organized.
- **[front-matter/table-of-contents.md](front-matter/table-of-contents.md)** : the contents page.
- **[chapters/](chapters/)** : the 100 chapter files, named `N.M-slug.md`.

## The appendices (Part 12)

- **[Glossary](chapters/12.1-glossary.md)** : definitions of key terms.
- **[Checklists](chapters/12.2-checklists.md)** : ready-to-use review and launch checklists.
- **[Templates](chapters/12.3-templates.md)** : ADRs, RFCs, postmortems, threat models, and more.
- **[Maturity self-assessment](chapters/12.4-maturity-self-assessment.md)** : the four-level model for every domain.
- **[References](chapters/12.5-references.md)** : the SWEBOK crosswalk, standards index, and bibliography.
- **[Adoption roadmap](chapters/12.6-adoption-roadmap.md)** : how to roll the practices out.
- **[Index](chapters/12.7-index.md)** : the subject index.

## Specification (source of truth)

- **[spec/index.md](spec/index.md)** : how the spec drives the book.
- **[spec/structure.md](spec/structure.md)** : the canonical chapter manifest.
- **[spec/conventions.md](spec/conventions.md)** : the writing and format specification.
- **[spec/roadmap.md](spec/roadmap.md)** : backlog and adoption checklists.

## Contributing and tooling

- **[AGENTS.md](AGENTS.md)** : guidance for AI agents and contributors.
- **[CONTRIBUTING.md](CONTRIBUTING.md)** : how to contribute.
- **[docs/](docs/)** : project documentation.
- **[examples/](examples/)** : small illustrative examples.
- **[tools/gen_nav.py](tools/gen_nav.py)** : navigation generator (`make nav`).
- **[tests/validate.py](tests/validate.py)** : validation suite (`make test`).
- **[CHANGELOG.md](CHANGELOG.md)** : history of notable changes.

## Quick start

```sh
make help    # list available tasks
make test    # validate the whole repository
make nav     # regenerate the generated navigation files
make stats   # chapter and word counts
```
