# 2.7 Documentation

## Overview and motivation

[Documentation](https://en.wikipedia.org/wiki/Software_documentation) is the written knowledge that lets people use, operate, and change software without having to piece together understanding from the code alone. It comes in many genres: how to get started, how to accomplish a task, how a system is structured, how to respond to an incident, what an [API](https://en.wikipedia.org/wiki/API) accepts and returns. Each one serves a different reader with a different need. Good documentation is not optional. It is the difference between knowledge that scales across a large organization and knowledge that lives in just a few people's heads.

For large teams, documentation is your best defence against key-person risk (the danger when critical knowledge sits with only one or a few people) and your fastest way to onboard newcomers. When hundreds of engineers depend on systems they didn't build, and people join, move, and leave all the time, the organization can only function if knowledge is written down and easy to find. Undocumented systems turn fragile: only their authors can safely change them, and when those authors leave, the organization loses the ability to maintain its own software. That's one of the most common and expensive failures at scale.

Enterprise and government contexts raise the stakes further. Systems live a long time, so your documentation has to serve maintainers years, even decades, after the original team is gone. Regulatory and audit regimes often mandate specific documents as evidence of control: architecture records, [runbooks](https://en.wikipedia.org/wiki/Runbook) (step-by-step operational and incident-response procedures), and decision logs. Public-sector systems handed between vendors rely entirely on documentation to carry knowledge across contract boundaries. And yet documentation is famously prone to rot, so the real challenge is keeping it accurate as the software changes.

## Key principles

- Write for a specific reader with a specific need; different documentation types serve different purposes.
- Keep documentation close to the code and treat it as code (docs-as-code).
- Accuracy beats completeness; a small amount of trustworthy documentation beats a large amount that is wrong.
- Generate what can be generated; do not hand-maintain what a tool can produce from the source of truth.
- Fight documentation rot actively; stale docs are worse than none because they mislead.
- Make documentation discoverable; unfindable knowledge is effectively absent.
- Record decisions and their rationale, not just the current state.

## Recommendations

### Adopt docs-as-code

Keep documentation in [version control](https://en.wikipedia.org/wiki/Version_control) right alongside the code it describes, write it in plain-text markup, and review it through the same pull-request process. That keeps it versioned, reviewable, and close to the code, so you can update both together. Publish it through an automated pipeline so the latest version is always available. Treating docs as code brings the same discipline that keeps code trustworthy: review, history, and automation.

### Structure content with the Diátaxis framework

Organize documentation into four distinct types, because mixing them serves no reader well: tutorials (learning-oriented, for newcomers), how-to guides (task-oriented, for a specific goal), reference (information-oriented, precise and complete), and explanation (understanding-oriented, the why and the context). Keep these separate and everything gets easier to write, navigate, and maintain, because each page has one clear job and one clear audience.

### Maintain the essential operational documents

Give every repository a clear [README](https://en.wikipedia.org/wiki/README) as its front door: what it is, how to build and run it, and where to go next. Write runbooks for operational tasks and incident response, so anyone on call can act, not just the experts. Keep architecture documentation that explains the system's structure and key components. And provide onboarding documentation that gets a new engineer productive quickly. These are the documents you miss most when they aren't there.

### Generate API docs and changelogs from the source of truth

Generate your API reference documentation from the machine-readable contract or code annotations, so it can't drift from the actual interface. Keep a [changelog](https://en.wikipedia.org/wiki/Changelog), ideally generated from structured commits or release notes, so consumers can see what changed between versions. Automating these takes the most rot-prone hand-maintained documentation off your plate and keeps it trustworthy.

### Record architecture decisions

Capture significant architectural and design decisions as lightweight, dated records that state the context, the decision, and its consequences. These decision records preserve the rationale that would otherwise be lost, so future maintainers can see why the system is the way it is instead of second-guessing it or repeating old mistakes. They pay off especially over the long lifespans of enterprise and government systems.

### Fight documentation rot deliberately

Treat stale documentation as a defect. Update the docs as part of the same change that alters behaviour, and make that a review expectation. Assign ownership so every important document has someone responsible for it. Review high-value documentation for accuracy now and then, prune what's obsolete, and remove or clearly flag anything you no longer trust. The documentation that rots least is living documentation: generated or tested against the system itself.

### Invest in knowledge management and discoverability

Make documentation findable through good search, clear navigation, and a known home, so people can locate what they need without having to ask someone. Don't let it fragment across too many disconnected wikis and tools. And capture [tacit knowledge](https://en.wikipedia.org/wiki/Tacit_knowledge), the informal understanding that lives in chat threads and people's heads, into durable, findable form before it slips away.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| Docs-as-code | Versioned, reviewable, close to code; low rot | Requires engineer discipline; less friendly to non-technical authors |
| Wiki / knowledge base | Easy to edit; accessible to everyone | Drifts from code; fragments; rots silently |
| Generated docs (API, changelog) | Always accurate; low maintenance | Limited to what the source expresses; needs tooling |
| Hand-written explanation | Rich context and rationale machines can't produce | Labour-intensive; prone to going stale |
| Diátaxis structure | Clear purpose per page; easier to navigate and maintain | Upfront structuring effort; requires author discipline |

The central trade-off is effort versus accuracy and durability. The cheapest documentation to write, a quick wiki page, is also the most prone to rot and fragmentation. The most durable documentation, generated from the source or reviewed as code, costs more discipline up front but stays trustworthy. A good rule of thumb: generate what you can, keep the rest close to the code and reviewed like code, and save labour-intensive hand-written explanation for the rationale that only humans can provide.

## Questions to discuss with your team

1. **Are your documents separated by reader need, or do tutorials, reference, and explanation jumble together on one page?** This chapter recommends the Diátaxis split into tutorials, how-to guides, reference, and explanation, and lists mixing types as an anti-pattern that serves no reader well. At scale, a newcomer learning the system and an on-call engineer hunting a precise fact need different pages, and a single mixed page slows both. Bring the signal: pick your most-visited docs and check whether each has one clear job and one clear audience. Restructure the worst offenders into distinct types, so every page is easier to write, navigate, and keep current. That structure is what makes documentation maintainable as the org grows.

2. **Do you capture significant architecture decisions with their rationale, or only the current state?** The chapter recommends lightweight, dated decision records that state context, decision, and consequences, and notes they pay off most over the long lifespans of enterprise and government systems. Without them, a maintainer years later cannot see why the system is the way it is, so they second-guess sound choices or repeat old mistakes. Bring a recent hard decision whose reasoning now lives only in a chat thread or someone's memory as the concrete signal. Adopt a short decision-record format and make writing one part of any significant design change. The rationale is exactly the knowledge that only humans can provide and that rots fastest when unwritten.

3. **Can any on-call engineer respond to an incident from your runbooks alone, without paging the person who built the system?** This chapter names runbooks as an essential operational document so that anyone on call can act, not just the experts, and describes a government team that could only inherit a system because runbooks carried the knowledge across a contract boundary. Key-person risk is the failure this guards against: when the one expert is unreachable or gone, an undocumented recovery procedure turns a routine incident into an outage. Bring the evidence: take a recent incident and check whether the runbook alone would have resolved it. Write and test runbooks for the procedures people dread, and treat a runbook that cannot stand on its own as a defect. That is the difference between a 2 a.m. recovery and a 2 a.m. escalation.

4. **Which of your API references and changelogs are generated from the source of truth, and which are still hand-maintained and quietly drifting?** This chapter tells you to generate reference documentation from the machine-readable contract or code annotations so it cannot diverge from the actual interface, and it lists hand-maintaining generatable content as an anti-pattern. For a large team, a hand-written API doc that lags the real interface is worse than none: every consumer who trusts it writes a broken integration, and the failure surfaces far from the stale page that caused it. Bring the concrete signal: sample a handful of your most-used interfaces and diff the published reference against the real contract to see how far each has drifted. Where you find drift, wire the reference into the build so it regenerates on every change, and retire the hand-kept copy. In enterprise and government settings, where interfaces are consumed across teams, vendors, and contract boundaries you never see, an authoritative generated reference is often the only thing that keeps integrators from building against fiction.

5. **Who owns each high-value document, and how would you notice today if one had gone stale?** The chapter treats stale documentation as a defect and warns that unowned documents rot because updating them is nobody's job, while stale docs presented as current destroy trust in all your documentation. At scale the danger is not a single wrong page but the slow erosion of confidence: once readers get burned by out-of-date instructions, they stop trusting the whole corpus and go back to interrupting people. Bring an ownership map of your most critical documents and an honest answer to how rot gets detected, whether by review cadence, generation, tests against the system, or pure luck. Assign a named owner to every document that matters, and prefer living documentation that is generated or tested so staleness shows up mechanically rather than through an embarrassed reader. For enterprise and government systems that outlive their original teams, unowned documentation is a liability an auditor or an inheriting vendor will eventually charge you for.

6. **How discoverable is your documentation, and how much critical knowledge still lives only in chat threads and people's heads?** This chapter says unfindable knowledge is effectively absent, warns against fragmenting docs across too many disconnected wikis and tools, and urges you to capture tacit knowledge into durable, findable form before it slips away. In a large organization the same fact often gets rediscovered, re-asked, and re-answered a hundred times because nobody can find where it was already written, and each departure takes irreplaceable context out the door. Bring the evidence: count how many separate documentation homes you maintain, try to find three important facts by search alone, and note where the real answers turned out to live in someone's memory or a buried message. Consolidate toward a known home with real search and clear navigation, and make capturing tacit knowledge a routine part of the work rather than a heroic rescue. In public-sector and heavily outsourced contexts, where systems pass between vendors and teams by contract, discoverable written knowledge is the only thing that survives the handover.

## Sector lens

**Startup.** With a handful of engineers and no runway to spare, document only what a 2 a.m. outage or a new hire would actually need: a real README per service, one tested runbook for the deploy-and-recover procedure everyone fears, and a few dated notes on the decisions you would otherwise forget. Generate API docs from the contract so you never hand-maintain them. Resist building a documentation platform; a versioned folder of markup beside the code is enough until you feel real pain.

**Small business.** With no technical writer and a tight budget, lean on the documentation your tools already generate and on lightweight docs-as-code rather than a staffed programme. Frame the choice as buy versus build: prefer platforms that produce their own current reference and searchable knowledge base over a wiki you must tend by hand. Spend your scarce effort on the two or three documents whose absence would stop the business, and let a wrong or missing page be the trigger to fix ownership.

**Enterprise.** Across many teams the problem is consistency and discoverability: a shared docs-as-code pipeline, a common structure such as Diátaxis, generated API references and changelogs, and decision records applied the same way everywhere so knowledge does not fragment across dozens of wikis. Assign ownership for every high-value document and measure accuracy, not just presence. Treat architecture records, runbooks, and decision logs as audit evidence, and standardize how they are produced so a control review finds a documented, defensible trail rather than a scramble.

**Government.** Procurement rules and public accountability make documentation a deliverable, not a courtesy. Write architecture documentation, runbooks, and decision records into contracts as mandated artefacts, reviewed for accuracy so knowledge survives a vendor transition and a system can be operated by whoever inherits it. Require that any authorized operator can respond to an incident from the runbook alone, and keep decision logs as a transparent public record of why choices were made. Thin documentation here is not a private inconvenience; it becomes costly reverse-engineering funded by the taxpayer.

## Examples

**Startup.** A five-person startup writes a real README for each service and a short runbook for the one deploy-and-recover procedure everyone dreads, so a 2 a.m. outage does not depend on waking the single founder who knows the system. They generate API docs from the contract instead of hand-writing them, and jot a few dated notes explaining why they chose their database and their auth approach. It stays lightweight, but it means the sixth and seventh hires onboard from documents rather than by interrupting everyone.

**Enterprise.** A large software company keeps all its documentation in the same repositories as its code, written in markup and reviewed in pull requests right alongside the changes they describe. API references are generated from service contracts, so they never drift. Changelogs are generated from structured commits, and architecture decision records preserve the reasoning behind major choices. A published documentation site builds automatically on every merge. New engineers get productive fast because onboarding guides and runbooks are current and findable, and on-call engineers lean on runbooks instead of paging the original authors.

**Government.** A national agency inherits a system from a departing contractor, depending entirely on documentation to carry knowledge across the contract boundary. Because the previous vendor maintained architecture documentation, runbooks, and decision records as mandated deliverables, the new team can operate and modify the system without the original authors. Where documentation was thin, the agency faces costly reverse-engineering. That experience drives a new policy: documentation is a contractual deliverable, reviewed for accuracy rather than treated as an afterthought, and runbooks must let any authorized operator respond to incidents.

## Business case: motivations, ROI, and TCO

Documentation pays you back in shorter onboarding time, less key-person risk, faster incident response, and a lower cost of change over a system's life. New engineers reaching productivity in days rather than weeks, on-call staff resolving incidents from a runbook instead of escalating, maintainers changing a system confidently years after it was built: these are large, recurring savings that compound across a big organization and a long system lifespan.

What does documentation cost? Authoring and maintenance effort. What does *not* documenting cost? You pay continuously: in slow onboarding, repeated questions, key-person bottlenecks, slower incident recovery, and, at the extreme, systems no one can safely change, forcing expensive rewrites or reverse-engineering. In vendor-transition and audit scenarios, missing documentation can carry direct contractual and compliance costs. To make the case to leadership, put numbers on onboarding time, incident-response time, and how much critical knowledge sits in individual heads. Then frame docs-as-code and generation as ways to get durable documentation without a matching maintenance burden. And stress that inaccurate documentation is a liability, so the investment has to include keeping it current.

## Anti-patterns and pitfalls

- **Stale documentation presented as current:** misleads readers and destroys trust in all documentation.
- **The write-once wiki:** pages created and never updated, silently drifting from reality.
- **Documentation fragmentation:** knowledge scattered across many tools and wikis so nothing can be found.
- **Mixing documentation types:** tutorials, reference, and explanation jumbled on one page, serving no reader well.
- **Hand-maintaining generatable content:** manually written API docs that inevitably diverge from the actual interface.
- **Tribal knowledge:** critical understanding kept only in people's heads and chat history, lost when they leave.
- **Documentation as an afterthought:** written at the end, if at all, rather than alongside the change.
- **No ownership:** documents with no responsible owner rot because updating them is nobody's job.

## Maturity model

- **Level 1, Initiate.** Documentation is sparse, scattered, and stale, and knowledge lives in people's heads. What exists was written once and never touched again, so an outage or a departure means reverse-engineering the system.
- **Level 2, Develop.** Key documents exist, such as READMEs and a few runbooks, but they are maintained inconsistently and are hard to find. Some teams document well and others barely at all, and there is no shared expectation about what a repository should carry or where it should live.
- **Level 3, Standardize.** Docs-as-code is the norm across the organization: a common structure such as Diátaxis, generated API references and changelogs, decision records, and an expectation in review that docs change with the code they describe. Every high-value document has a named owner, and there is one known home with real search.
- **Level 4, Manage.** Documentation is measured, not just present. You track coverage of the essential documents, doc-change rate against code-change rate, onboarding time, incident resolution from runbooks alone, and freshness against a defined staleness threshold, and you review those metrics against baselines. Rot is caught mechanically through generation, tests against the system, and link and accuracy checks, and stale pages are flagged or pruned on evidence rather than by chance.
- **Level 5, Orchestrate.** Documentation is continuously improved and integrated across the organization: living, largely generated or tested against the system, owned, discoverable, and adaptive. Metrics feed back into where you invest, tacit knowledge is captured as a routine part of the work, and the corpus is actively rebalanced and pruned as systems, teams, and readers change.

## Ideas for discussion

- Which documentation, if it vanished tomorrow, would hurt your organization most, and does it currently exist and stay current?
- How do you make updating documentation a natural part of changing code rather than a separate chore?
- Where can you replace hand-written documentation with generated documentation tied to the source of truth?
- How do you measure whether your documentation is accurate and used, not just present?
- How should AI assistants change how you write, maintain, and search documentation, and where might they introduce plausible-but-wrong content?
- How do you capture tacit knowledge before the people who hold it leave?

## Key takeaways

- Treat documentation as code: versioned, reviewed, close to the source, and published automatically.
- Structure content by reader need using tutorials, how-to guides, reference, and explanation.
- Maintain the high-value essentials: READMEs, runbooks, architecture docs, onboarding, and decision records.
- Generate API docs and changelogs so they cannot drift from the source of truth.
- Fight rot with ownership, review expectations, and pruning; inaccurate documentation is worse than none.

## References and further reading

- Daniele Procida, *Diátaxis* documentation framework
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* and Season of Docs guidance (as reference exemplars)
- Michael Nygard, *Documenting Architecture Decisions* (architecture decision records)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (on knowledge and documentation)
- *Keep a Changelog* (as a reference convention)
