# 2.14 Project and repository structure

## Overview and motivation

Project and repository structure is the physical organization of a codebase: the folders, files, and naming conventions that decide where any given thing lives. A *repository* (often shortened to "repo") is the [version-controlled](https://en.wikipedia.org/wiki/Version_control) container that holds a project's files and their history. A *project*, sometimes called a *solution* when it groups several related components, is the logical unit of software you are building. Structure is the map you use to find, understand, and change that software.

On a small team, one person can hold the whole layout in their head. On a large team, with hundreds or thousands of engineers, frequent moves between teams, and contractors joining and leaving, every repository that is organized differently charges a fresh cognitive tax. When you open an unfamiliar repo, you should be able to guess where the source, the tests, the documentation, and the deployment configuration live, without reading a manual. When every repo answers those questions the same way, mobility is cheap and onboarding is fast. When each repo is a snowflake, every context switch turns into a small research project.

In enterprise and government settings, consistent structure is also a control and assurance concern. Auditors, security reviewers, and long-term maintainers, often working years after the original authors have gone, need to reliably locate specification documents, licence files, security policies, and build definitions. A predictable layout also lets automated tooling (scanners, dependency analysers, compliance checks) work the same way across a whole portfolio of systems. So this chapter treats structure as a convention you decide once and apply everywhere. It is closely related to coding standards and style (chapter 2.1), version control and source management (chapter 2.6), and documentation (chapter 2.7).

## Key principles

- Follow the *[principle of least surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: the layout should match what an experienced engineer would expect, so nothing has to be memorized.
- Consistency across repositories beats local cleverness; a uniform-enough structure everywhere is worth more than the perfect structure in one place.
- The [README](https://en.wikipedia.org/wiki/README) is the front door; a newcomer should orient themselves from it alone.
- Make structure self-describing through naming, so folders and files announce their purpose.
- Enforce structure with scaffolding and templates, not with willpower and review comments.
- Separate concerns physically: source, tests, docs, build, and deployment belong in distinct, predictable places.
- Organize dependencies so they flow in one direction, from stable cores toward volatile edges.

## Recommendations

### Adopt a consistent top-level layout

Define a standard set of top-level folders that every repository uses where applicable, and document what each one is for. A common, vendor-neutral convention includes: a source folder (often `src`) for production code; a test folder (often `test` or `tests`) for automated tests; a `docs` folder for documentation; a `build` folder for build definitions and outputs; a `deploy` folder for deployment and *[infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (machine-readable definitions of servers, networks, and services, covered in chapter 8.2); a `scripts` folder for automation and developer tooling; an `examples` folder for runnable samples; and a `spec` or `specification` folder for requirements and design specifications. Not every repo needs every folder, but where a concern exists, it should live in the expected place with the expected name.

### Make the README the entry point

Require a README file at the repository root as the single, canonical starting point. It should state what the project is, how to build and run it, how to run the tests, where to find deeper documentation, who owns it, and how to contribute. The README is not the whole documentation set; it is the index that points to the rest (chapter 2.7). Treat a missing or stale README as a defect, because it is the first thing every new engineer, auditor, or integrator will read.

### Standardize editor and configuration files

Check shared editor and tooling configuration into the repository so every contributor gets consistent behaviour automatically. An `.editorconfig` file (a simple, editor-agnostic file that defines whitespace, indentation, and line-ending rules) keeps basic formatting uniform across different editors and operating systems. Add an ignore file for the version-control system (so build outputs and local artifacts are never committed), along with the shared formatter and linter configurations described in chapter 2.1. These files make the repository's conventions active, not just documented.

### Define naming and folder conventions

Agree on conventions for naming folders and files (casing, separators, singular versus plural, and required suffixes such as those marking tests) and apply them uniformly. Names should reveal intent and match the domain vocabulary used elsewhere in the organization. The goal is simple: a path should communicate meaning, so that reading a folder or file name tells you what is inside without opening it.

### Organize layers and dependencies deliberately

Structure the codebase so that its architectural layers show up in the folder layout, and so that dependencies flow in a single, sensible direction. Higher-level policy should not depend on low-level detail. Shared, stable code should sit where many modules can reach it without creating cycles. When you make the layering physical, reflected in the directory tree, engineers are more likely to respect it, and violations are easier to spot in review and in automated dependency checks.

### Enforce structure with scaffolding and templates

Provide *[scaffolding](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)*, the automated generation of a starter project, so that new repositories begin already correct. A *template* or *cookiecutter* (a parameterized project skeleton that generates a ready-made repository from answers to a few prompts) encodes the standard layout, the README, the config files, and the [CI](https://en.wikipedia.org/wiki/Continuous_integration) setup in one place. When engineers create new services from a shared template, consistency becomes the default instead of an aspiration, and improvements to the template flow through to future projects.

### Keep structure consistent across many repositories at scale

Treat the layout itself as a governed standard: maintained centrally like any other engineering standard (chapter 1.7), and versioned like code (chapter 2.6). Publish it, provide the templates that implement it, and allow deviations only through a documented exception process, so that "the standard" keeps its meaning. At portfolio scale, almost all the value of structure comes from its uniformity across repositories, so drift is the main risk to manage.

### Let structure inform the monorepo versus multi-repo choice

Relate structure to the repository-boundary decision covered in chapter 2.6. A *[monorepo](https://en.wikipedia.org/wiki/Monorepo)* (one repository holding many projects) needs a clear internal convention for separating projects and their shared code, so the single tree stays navigable. A *multi-repo* approach (many small repositories, one per project or service) needs strong cross-repo consistency, so that each repo feels familiar even though it stands alone. Either way, a documented, templated structure is what keeps navigation predictable. The boundary choice changes where you apply the convention, not whether you need one.

## Trade-offs: pros and cons

| Choice | Pros | Cons |
|---|---|---|
| Strict organization-wide standard layout | Instant familiarity; portable engineers; uniform tooling | Occasional poor fit for unusual projects; needs governance |
| Per-team freedom of layout | Local optimization; high autonomy | Fragmentation; costly context switching; inconsistent tooling |
| Scaffolding and templates | Correct-by-default repos; changes propagate | Template maintenance; risk of drift from generated repos |
| Deep, layered folder hierarchy | Explicit structure; clear boundaries | Navigation overhead; long paths; over-engineering risk |
| Flat, shallow layout | Easy to scan; low ceremony | Poor separation; breaks down as the project grows |

The dominant trade-off is uniformity versus autonomy. A single standard layout removes friction for the many engineers who move between codebases, at the cost of the occasional project whose needs do not fit the mold neatly. In a large organization, the collective gain from familiarity almost always outweighs that local loss. That is why the recommended posture is a strong default standard plus a documented exception path (chapter 1.7), rather than either rigid uniformity or unmanaged freedom. A secondary trade-off is depth versus simplicity: enough structure to separate real concerns, but not so much that navigation turns into a hike through empty folders.

## Questions to discuss with your team

1. **When an engineer moves to an unfamiliar repo of ours, how long until they can find the tests, the deploy config, and the owner?** This is the navigation tax that structure exists to eliminate, and at portfolio scale it is paid thousands of times a year in small increments that add up to serious lost engineering time. The point of the principle of least surprise is that an experienced engineer should be able to guess where source, tests, docs, and deployment live without reading a manual, so the honest test is whether that guess succeeds across your repos. Bring a real number to the meeting: time yourselves orienting in two or three unfamiliar internal repositories, or pull onboarding data on how long new joiners take to make a first change. If the answer is measured in days of research rather than minutes of recognition, you have quantified the cost of snowflake repos, and it justifies the one-time investment in a standard layout that every repo shares.

2. **Do our architectural layers show up in the folder tree, or do dependency cycles hide inside a flat layout?** Structure is about more than findability: when you make layering physical, engineers respect it and reviewers and automated dependency checks can spot violations, whereas a flat pile lets improper coupling and cycles creep in unnoticed until change becomes dangerous. On a large, long-lived system this is what keeps higher-level policy from quietly depending on low-level detail, and it is exactly the kind of erosion that is cheap to prevent and expensive to unwind. Bring your dependency graph or run a quick check: are there cycles, and does anything stable depend on something volatile? The answer should push you to reflect layers in directories and to add automated dependency-direction checks, so the boundaries are visible in the tree and enforced in the pipeline rather than living only in someone's mental model.

3. **Do our new repositories start correct from a template, or do we rely on a wiki page and good intentions?** Structure enforced by scaffolding is the default; structure described in a document drifts, because reality follows what generates repos, not what a page says they should look like. For a large or regulated organization this is also an assurance concern: when every repo is generated from a shared template, security scanners, dependency analysers, and auditors find the licence, the security policy, the specification, and the build definition in the same place every time, across vendors and across years. Bring the evidence: how many of your recent repos were scaffolded from the standard template versus hand-assembled, and how far have the templated ones since drifted? The action is to make the template the only easy way to start a repo, govern it as a versioned standard with a documented exception path, and detect drift automatically, because uniformity is where almost all the value of structure lives.

4. **Have we decided whether our standard spans a monorepo or many separate repositories, and does the same convention actually hold on both sides of that boundary?** The repository-boundary choice changes where you apply the convention, not whether you need one, and getting it wrong means a single giant tree nobody can navigate or a sprawl of repos that each feel foreign. A monorepo needs a clear internal convention for separating projects and their shared code so the one tree stays navigable, while a multi-repo approach needs strong cross-repo consistency so each standalone repo still feels familiar. Bring the current inventory: how many repos you have, how shared code is separated inside any monorepo, and a timed test of whether an engineer can find a project inside the big tree as fast as they find one in a standalone repo. For a large enterprise or a government programme where different vendors deliver separate repositories, decide deliberately which parts of the convention are universal and which are boundary-specific, because auditors and platform tooling have to work the same way whether the code arrives as one tree or fifty.

5. **Who owns our structure standard, and what actually happens when a project genuinely does not fit it?** At portfolio scale almost all the value of structure comes from uniformity, so the real risks are an ownerless standard that rots and an exception path so vague that every team quietly invents its own layout. The tension is between rigid uniformity that fits no unusual project and unmanaged freedom that fragments everything, and the healthy answer is a strong default plus a documented, auditable exception process governed by a named owner and versioned like code. Bring the evidence: is there a single accountable owner, a versioned standard document with a changelog, a log of exceptions granted and why, and a count of undocumented deviations you can find in the wild. In enterprise and government settings an exception nobody recorded is a control gap, so tie each deviation to a written justification and a review date, and make sure procurement contracts that mandate the layout also name who may approve departures from it.

6. **Do our README and checked-in configuration files make our conventions active, or are they decorative?** A README is the front door and the checked-in `.editorconfig`, ignore file, and linter configuration are what make conventions self-enforcing, yet these are the first things to go stale and the last things anyone notices until an auditor or a new joiner cannot get the project to build. The tension is between a lean README that stays current and a thorough one that drifts, and between trusting people to format code correctly and letting shared configuration enforce it automatically. Bring a sample: pull five repos and check how many READMEs actually state what the project is, how to build, test, and run it, and who owns it, and how many carry the shared configuration files rather than relying on individual habits. For a large or regulated organization, where integrators, security reviewers, and long-term maintainers read the README before anything else, treat a missing or stale front door as a defect with an owner, and check config-file presence automatically so conformance does not depend on goodwill.

## Sector lens

**Startup.** Speed wins, so agree one simple, flat-enough layout for your first repo (src, test, docs, scripts, a populated README, an `.editorconfig`, and ignore files) and save it as a lightweight template the same afternoon. Generate the second service from it so both repos feel familiar and a new contractor onboards in hours rather than reverse-engineering a snowflake. Resist deep hierarchies and heavy governance you do not need yet; the whole return here is that two founders and a contractor share one map.

**Small business.** With no platform specialist and a tight budget, adopt the conventional layout your language or framework already assumes rather than inventing one, so off-the-shelf tooling and any new hire arrive pre-trained on it. Buy scaffolding (a framework generator or a cookiecutter template) instead of building your own, and spend your scarce effort keeping a populated README current. That README is the cheapest insurance you have for the day the one person who knew the layout moves on.

**Enterprise.** Across many teams and hundreds of repositories the goal is uniformity: publish a versioned structure standard, generate every new service from shared templates, detect drift automatically, and allow deviations only through a documented exception process. Because every repo looks the same, an engineer reassigned to a new team is productive within hours and portfolio-wide security and dependency scanners find the licence, the security policy, and the build definition in the same place every time. Budget the template maintenance and drift detection explicitly, because that upkeep is what keeps the standard meaningful at scale.

**Government.** Procurement, transparency, and long-term accountability shape the layout, so mandate a common structure in the delivery standards that bind every vendor. Require a `specification` folder linking code to approved requirements, a licence and security-policy file at the root, and a `deploy` folder holding the infrastructure-as-code definitions, so auditors locate compliance artefacts the same way in every system. Because contractors from different vendors all follow one map, maintenance after a contract ends costs far less, and the public gains a defensible, inspectable trail from requirement to running code.

## Examples

**Startup.** A three-person startup agrees on a simple standard layout for its first repo (src, test, docs, scripts, a populated README, an .editorconfig, and ignore files) and saves it as a lightweight template. When they spin up their second service a month later, they generate it from that template, so both repos already feel familiar and the new contractor onboards in an afternoon. They resist deep folder hierarchies they do not need yet, keeping the tree flat enough to scan at a glance. The cost was one afternoon of setup, and it spares them the snowflake sprawl that would otherwise make every future repo a small research project.

**Enterprise.** A multinational retailer runs hundreds of services across several languages. Its platform team publishes a versioned repository-structure standard and a set of project templates that implement it. Every new service is generated from a template, so it arrives with the standard `src`, `test`, `docs`, `deploy`, and `scripts` folders, a populated README, an `.editorconfig`, ignore files, and a working CI pipeline. Because every repository looks the same, an engineer reassigned to a new team is productive within hours, and organization-wide security and dependency scanners run uniformly because they always find files where they expect them.

**Government.** A national agency modernizing legacy systems mandates a common repository layout as part of its delivery standards for all vendors. Each repository must contain a `specification` folder linking code to approved requirements, a documented README, a licence and security-policy file at the root, and a `deploy` folder holding the infrastructure-as-code definitions (chapter 8.2). Because contractors from different vendors all follow the same structure, the agency's auditors can locate compliance artifacts the same way in every system, and long-term maintenance after a contract ends costs far less because incoming maintainers already know the map.

## Business case: motivations, ROI, and TCO

The cost of adopting a structure standard is mostly one-time: agreeing on the layout, building the templates, and documenting the convention. The recurring cost is low, concentrated in maintaining the templates and governing exceptions. The cost of *not* having a standard is recurring and compounding: every engineer who opens an unfamiliar repo pays a navigation tax, every onboarding runs slower, and automated tooling has to be configured per-repo because nothing is where you expect it. Across a large organization, these small frictions multiply into serious losses of engineering time.

The return shows up as faster onboarding, cheaper mobility between teams, higher signal from portfolio-wide tooling, and, in regulated settings, lower audit and long-term-maintenance cost, because artifacts are always findable. The *total cost of ownership* (TCO, meaning the full lifetime cost of building, running, and maintaining a system) drops most in long-lived systems, where the maintainers who benefit from predictable structure are usually not the authors who created it. To make the case to leadership, frame structure as a low-cost, high-leverage standard that improves developer productivity and audit readiness, and put a number on today's cost of inconsistency using onboarding-time data and the effort spent hunting for things in unfamiliar repositories.

## Anti-patterns and pitfalls

- **The snowflake repository:** every repo organized differently, so each one must be relearned from scratch.
- **The missing or stale README:** no front door, forcing newcomers to reverse-engineer how to build and run the project.
- **Structure by document, not by template:** a wiki page describes the standard layout, but nothing generates or enforces it, so reality drifts away from it.
- **Template drift:** repositories generated from a template diverge over time and improvements to the template never reach them.
- **Over-engineered hierarchy:** deep nests of near-empty folders that add ceremony without aiding navigation.
- **Mixed concerns:** source, tests, build outputs, and secrets jumbled together with no clear separation.
- **Committed build outputs and local artifacts:** generated files checked in because ignore rules were never set up, polluting history and diffs.
- **Layer violations hidden by flat structure:** no physical boundaries, so dependency cycles and improper coupling creep in unnoticed.

## Maturity model

- **Level 1 (Initiate):** Each repository is organized ad hoc by its authors, reacting to whatever the moment needs; layouts vary widely; READMEs are missing or unreliable; newcomers must be walked through every repo by hand.
- **Level 2 (Develop):** Basic conventions exist informally and many repos resemble each other; some teams keep a starter layout of their own; but there is no authoritative standard, no shared scaffolding, and structure drifts noticeably from one team to the next.
- **Level 3 (Standardize):** A documented, versioned structure standard is enforced across the organization; new repositories are generated from shared templates carrying a standard layout, README, configuration files, and CI; deviations go through a documented exception process rather than happening silently.
- **Level 4 (Manage):** Conformance to the standard is measured and controlled with data: automated checks report what fraction of repos match the layout, how far templated repos have drifted, README completeness, and dependency-direction violations, all tracked against baselines; onboarding and navigation times are measured; exceptions are logged and reviewed, and template changes are approved on the evidence rather than on opinion.
- **Level 5 (Orchestrate):** Structure is continuously improved and adaptive: template improvements propagate automatically to existing repositories, structure governance is integrated with security, compliance, and platform tooling, and the standard evolves deliberately as languages, architectures, and the portfolio shift, keeping uniformity high while the organization changes around it.

## Ideas for discussion

- Which top-level folders should be truly universal across your organization, and which should be optional?
- How do you keep repositories generated from a template from drifting away from it over time?
- Where is the line between a helpful, layered hierarchy and over-engineered folder ceremony?
- How should your structure standard differ, if at all, between a monorepo and a multi-repo approach?
- What is the right exception process for a project whose genuine needs do not fit the standard layout?
- How much of your structure can be checked automatically, and what still relies on human review?
- Who owns the structure standard and its templates, and how do changes get proposed and rolled out?

## Key takeaways

- Organize every repository so that any engineer can navigate any codebase by expectation, following the principle of least surprise.
- Adopt a consistent top-level layout (source, test, docs, build, deploy, scripts, examples, specification) and make the README the entry point.
- Check in editor and tooling configuration (such as `.editorconfig`) so conventions are active, not merely written down.
- Enforce structure with scaffolding and templates so new repositories are correct by default.
- At scale, the value is in uniformity: govern the standard, manage drift, and allow deviations only by documented exception.

## References and further reading

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google*
- Scott Chacon and Ben Straub, *Pro Git*
- EditorConfig project documentation (as a reference standard for editor configuration)
