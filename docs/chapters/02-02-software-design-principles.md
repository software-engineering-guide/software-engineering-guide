# 2.2 Software design principles

## Overview and motivation

Software design principles are heuristics for arranging code so you can understand, change, and extend it over time. They include named acronyms ([SOLID](https://en.wikipedia.org/wiki/SOLID) for five [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) design principles, [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) for don't-repeat-yourself, [KISS](https://en.wikipedia.org/wiki/KISS_principle) for keep-it-simple, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) for you-aren't-gonna-need-it), structural concepts ([coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)), catalogued [design patterns](https://en.wikipedia.org/wiki/Software_design_pattern), higher-level modelling approaches such as [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) (modelling software in the language of the business domain), and the choice between object-oriented, [functional](https://en.wikipedia.org/wiki/Functional_programming), and [data-oriented](https://en.wikipedia.org/wiki/Data-oriented_design) styles. None of these are laws. They are compressed experience, and you have to apply them with judgement.

For large teams, the value of shared principles is coordination. When hundreds of engineers work on the same system, they need a common vocabulary for design discussions and a common set of defaults so that independently written modules fit together. Good design is what lets many people change a system in parallel without constant collisions. It is also what keeps a system changeable a decade later, the normal lifespan of enterprise and government systems, long past the tenure of their original authors.

The critical skill is not memorizing principles. It is knowing when each one misleads you. Every principle has a failure mode: DRY can produce the wrong abstraction, SOLID can produce needless indirection, YAGNI can starve extensibility you genuinely need. This chapter treats principles as tools with a domain of applicability, and it emphasizes coupling and cohesion as the deeper properties the acronyms are trying to serve.

## Key principles

- Manage coupling and cohesion first; most named principles are indirect ways of improving these two properties.
- Optimize for change: good design minimizes the cost of the changes you will actually need to make.
- Prefer the simplest design that works now, but keep boundaries where change is likely.
- Duplication is cheaper than the wrong abstraction; wait until the pattern is clear.
- Make dependencies explicit and point them toward stable things.
- Model the domain in the language of the domain; align software boundaries with business boundaries.
- Choose paradigms to fit the problem, not ideology; most large systems are pragmatically mixed.

## Recommendations

### Use SOLID as a lens, not a checklist

Apply single-responsibility to keep modules cohesive, dependency-inversion to point dependencies at abstractions where a boundary genuinely exists, and open-closed where extension points are real. Don't manufacture interfaces, factories, and layers just to satisfy the acronym when there is only one implementation and no second one in sight. Indirection has a cost, and you pay it on every read.

### Apply DRY to knowledge, not to text

DRY is about not duplicating a single authoritative piece of *knowledge*. It is not about eliminating lines that merely look alike. Two pieces of code that look similar but change for different reasons should stay separate. Prefer a little duplication over a premature shared abstraction that couples unrelated things. Extract the abstraction once the real pattern has shown up two or three times.

### Let KISS and YAGNI resist speculation

Build for the requirements you have, not the ones you imagine. Avoid speculative generality, such as configurable frameworks, plugin systems, and extension points nobody has asked for. The counter-balance is that some flexibility really is cheaper to build in early, like a stable interface or a clean seam. YAGNI argues against speculative *implementation*, not against thoughtful boundaries.

### Design for low coupling and high cohesion explicitly

Make each module do one well-defined thing (cohesion), and depend on as few other modules as possible, through narrow interfaces (low coupling). When you review a design, ask which changes ripple across module boundaries. Those ripples are the true measure of coupling. Separation of concerns is the same idea applied to layers and cross-cutting concerns.

### Use design patterns as vocabulary, apply anti-patterns as warnings

Patterns are useful shared names for recurring solutions. Reach for one when the problem actually matches it. Don't impose patterns to look sophisticated, because pattern-heavy code is often a sign of over-engineering. Learn the common [anti-patterns](https://en.wikipedia.org/wiki/Anti-pattern) (god objects, anaemic models where inappropriate, big balls of mud, distributed monoliths) as diagnostic labels.

### Adopt Domain-Driven Design where the domain is complex

For systems with rich business rules, use DDD's tactical and strategic tools: a ubiquitous language shared with domain experts, bounded contexts that carve the system into independently modelled pieces, and context maps that describe how those pieces relate. Bounded contexts are especially valuable at enterprise scale, because they line up team ownership with model boundaries. DDD is overkill for simple [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (create, read, update, delete) systems.

### Choose paradigms by fit

Use object orientation for encapsulating stateful behaviour and modelling domains. Use functional style for transformations, concurrency, and predictability through [immutability](https://en.wikipedia.org/wiki/Immutable_object). Use data-oriented design where performance and cache behaviour dominate. Large systems mix all three. Make the choice per component, and keep the boundaries between styles clean.

## Trade-offs: pros and cons

| Principle / approach | Applied well | Failure mode |
|---|---|---|
| SOLID | Clear seams where change happens; testable units | Interface and layer proliferation; indirection with no payoff |
| DRY | Single source of truth for real knowledge | Wrong abstraction coupling unrelated code |
| KISS / YAGNI | Lean, comprehensible systems | Under-designed seams; costly retrofits of needed flexibility |
| Design patterns | Shared vocabulary; proven structures | Pattern cargo-culting; accidental complexity |
| Domain-Driven Design | Aligned models and teams; tamed complexity | Heavy ceremony on simple domains; misplaced context boundaries |
| Functional / immutable | Predictability; safer concurrency | Awkward fit for inherently stateful problems; performance surprises |

The recurring tension is between under-design and over-design. Under-designed systems accrue coupling and become rigid. Over-designed systems drown in abstraction that someone has to understand and maintain. The answer is not a fixed point. It is a discipline: defer decisions until you have enough information, while keeping the seams that let you change your mind.

## Questions to discuss with your team

1. **What is your concrete threshold for extracting a shared abstraction, and how do you stop DRY from producing the wrong one?** This chapter is blunt that duplication is cheaper than the wrong abstraction, and that you should wait until the pattern has appeared two or three times before extracting. On a large team the danger is that someone factors two look-alike snippets into a shared module across team boundaries, then every future change to one caller ripples into the other. The signal to bring is whether the duplicates change for the same reason or merely look alike right now. Agree a rule of three, and require that a candidate abstraction has actually changed together before you couple the callers. That single agreement prevents a class of coupling that is expensive to unwind once many teams depend on it.

2. **How do you make coupling and cohesion visible in design review instead of leaving them to gut feel?** The key principles put coupling and cohesion above every acronym, and define coupling as the changes that ripple across module boundaries. Intuition does not scale across hundreds of engineers who each see only their corner of the system. Bring evidence a machine can produce: dependency graphs, and co-change data showing which modules keep getting edited together in the same commits. Add an explicit review question that asks which module boundaries a change forces you to cross. When two modules always change together, that is your cue to either merge them or fix the boundary between them.

3. **Where is the line in your systems between a domain rich enough to justify Domain-Driven Design and a plain CRUD app where it is overkill?** The chapter recommends DDD's bounded contexts precisely because they line team ownership up with model boundaries, and warns that DDD is overkill for simple create-read-update-delete systems and degrades into ceremony without real modelling. Getting this wrong in either direction is costly: heavy DDD on a thin domain buries a simple app in ceremony, while a sprawling shared model across many teams forces constant cross-team coordination. Bring the signals that actually decide it: the density of business rules, and how many teams need to own pieces independently. Reserve the strategic machinery for the complex core, and let the simple edges stay simple. That keeps you clear of both DDD theatre and the big ball of mud.

4. **When is an abstraction, interface, or design pattern worth the indirection it adds, and who has the authority to call a design over-engineered?** This chapter is explicit that indirection has a cost you pay on every read, and that manufacturing interfaces, factories, and layers to satisfy SOLID or to look sophisticated is a failure mode. On a large team the pressure runs the other way: reviewers wave through extra abstraction because it looks disciplined, and nobody wants to be the person arguing for less structure. The competing consideration is real, because some seams genuinely earn their keep and removing them later is expensive. Bring concrete evidence to the discussion: how many implementations an interface actually has today, how often the extension point has ever flexed, and how many files a reader must open to follow one code path. Agree that a single implementation with no second one in sight is a default reason to inline, and name who can label a design over-engineered without it reading as an insult. In enterprise and government systems that outlive their authors by a decade, gratuitous indirection is a tax every future maintainer pays, so treat "what does this abstraction buy us" as a standing review question, not a personal challenge.

5. **How do you decide which paradigm each component uses, object-oriented, functional, or data-oriented, and how do you keep the boundaries between them clean?** The chapter argues that large systems are pragmatically mixed and that you should choose per component by fit, using object orientation for stateful domains, functional style for transformations and concurrency, and data-oriented design where performance and cache behaviour dominate. Left unmanaged, paradigm choice becomes a matter of whoever wrote the module first, and mutable state leaks into what should be pure transformations, or a functional purism fights an inherently stateful problem. The evidence worth bringing is where your actual pain is: which components are hard to test because of hidden state, which hot paths are cache-bound, and where the current style forces awkward workarounds. Decide the default paradigm for each layer deliberately and write down where the seams between styles fall, so a functional core and an imperative edge do not bleed into each other. For a regulated or government system where a calculation must be auditable and reproducible for a given period, an immutable, functional core is often a compliance requirement rather than a taste, and that constraint should drive the boundary rather than follow it.

6. **How do you keep these principles from hardening into dogma, and where do you record the reasoning behind a design decision so a future team can revisit it?** Every principle in this chapter has a domain of applicability and a failure mode, and the whole framing treats them as tools to apply with judgement rather than laws to enforce. On a large team a principle quietly becomes a rule: DRY forbids any duplication, SOLID mandates an interface per class, and pragmatic exceptions get blocked in review by people citing the acronym rather than the outcome. The tension is that some consistency genuinely helps hundreds of engineers coordinate, so you cannot simply declare every principle optional. Bring examples where following a principle to the letter produced a worse design, and bring the decision records, if any, that explain why a given boundary or abstraction exists. Agree that principles are defaults an engineer may deviate from with a recorded reason, and capture consequential design choices in a short architecture decision record so the next team inherits the reasoning and not just the code. In enterprise and public-sector systems, where the original authors are long gone and audits ask why the system is shaped as it is, that written trail is the difference between a design future teams can safely change and one they are afraid to touch.

## Sector lens

**Startup.** Favour the simplest design that ships and keep one well-factored module until a real second use case forces a seam. Your scarcest resource is engineering attention, so premature interfaces, layers, and speculative frameworks are pure cost. Follow the rule of three before extracting any shared abstraction, and let YAGNI kill the extension points nobody has asked for yet.

**Small business.** With no dedicated architect and a tight budget, lean on the design already baked into the frameworks and libraries you buy rather than inventing your own patterns. Reserve custom design effort for the handful of rules that are genuinely your business, and keep everything else conventional so a contractor or a new hire can read it. A little duplication you understand beats a clever abstraction only its author can maintain.

**Enterprise.** The payoff of shared principles is coordination across many teams: a common vocabulary for design review, and bounded contexts that line model boundaries up with team ownership so groups evolve independently. Manage coupling and cohesion explicitly with dependency and co-change data, and record consequential design decisions so systems stay changeable long after their authors move on. Guard equally against the wrong abstraction that couples teams and the over-engineering that taxes every reader.

**Government.** Auditability and reproducibility often dictate the design. An immutable, functional core lets you reproduce a historical calculation exactly for a given period, which a tangled object graph with hidden mutable state cannot guarantee. Prefer explicit published contracts over shared tables at context boundaries, and keep the design and its decision records legible to auditors and to whichever team inherits the system a decade later.

## Examples

**Startup.** A three-engineer startup building its first product resists the urge to split every feature into layers of interfaces and factories, keeping a single well-factored module until a real second use case shows up. When the same logic appears a third time across the signup and billing flows, they extract one small shared function rather than a speculative framework. This keeps the codebase small enough that any of them can hold it in their head, and the few seams they do draw fall where the product is most likely to change.

**Enterprise.** A large insurance platform models policy, claims, and billing as separate bounded contexts, each owned by a dedicated team with its own data model and service boundary. Where the contexts meet, as when a claim references a policy, they talk through explicit published contracts rather than shared database tables. This lets the three teams evolve independently, and the ubiquitous language keeps conversations with underwriters and actuaries precise. An earlier version had shared a single sprawling model, and every change required cross-team coordination.

**Government.** A national tax-processing system deliberately favours a data-oriented, functional core for its calculation engine. Tax rules are expressed as pure transformations over immutable input records, which makes them auditable, testable, and reproducible for a given tax year. The imperative, stateful parts (workflow, notifications) are kept at the edges. Auditors can point to a specific rule version and reproduce any historical calculation exactly, which is a legal requirement that a tangled object graph with hidden mutable state could not guarantee.

## Business case: motivations, ROI, and TCO

Design quality is an investment in the *changeability* of a system, and changeability dominates total cost of ownership. Most of a system's cost lands after its first release, in modification and extension. Well-designed systems keep the cost of change roughly flat over time. Poorly designed ones see the cost of each change climb until the system becomes effectively unmodifiable and has to be rewritten, the most expensive outcome of all.

The adoption cost is mainly skill and review discipline: teaching the principles, and spending design time up front. The cost of not adopting them is the slow buildup of [technical debt](https://en.wikipedia.org/wiki/Technical_debt), falling delivery velocity, rising defect rates, and eventual costly rewrites. To make the case to leadership, connect design discipline to delivery predictability and to avoiding rewrite programmes, and track leading indicators such as change-failure rate and the time to implement comparable features over time. Watch out for the opposite failure, too: over-investing in design for uncertain futures also destroys value. So the argument is for *appropriate* design, calibrated to how likely and how costly future change is.

## Anti-patterns and pitfalls

- **Speculative generality:** building extensibility for imagined requirements that never arrive.
- **The wrong abstraction:** forcing unrelated code together to satisfy DRY, creating coupling that is worse than duplication.
- **Pattern cargo-culting:** applying design patterns for their own sake, adding indirection without benefit.
- **Anaemic or god objects:** models with no behaviour, or objects that do everything; both signal misplaced responsibilities.
- **Distributed monolith:** services split physically but still tightly coupled, combining the costs of both approaches.
- **Big ball of mud:** no discernible structure; every change risks everything.
- **DDD theatre:** adopting the vocabulary and folder structure without the domain modelling that gives it value.

## Maturity model

- **Level 1, Initiate:** Design is ad hoc and reactive; coupling accumulates unchecked; principles are unknown or invoked as slogans, and abstractions appear or vanish by individual habit.
- **Level 2, Develop:** Teams know the principles and apply them, but inconsistently and often dogmatically; some groups manage coupling and cohesion deliberately while others do not, and there is no shared vocabulary across the org.
- **Level 3, Standardize:** A shared design vocabulary, a rule of three for extracting abstractions, coupling and cohesion analysis, and bounded contexts aligned to teams are documented and expected org-wide, applied consistently in design review rather than left to individual taste.
- **Level 4, Manage:** Design health is measured against baselines: coupling and co-change data, change-failure rate, and the time to implement comparable features are tracked over time, so that abstractions and boundaries are added, kept, or removed on evidence, and over-engineering and the wrong abstraction are caught by data rather than opinion.
- **Level 5, Orchestrate:** Design discipline is integrated with delivery and risk planning across the org; principles are applied with nuance and known failure modes; paradigm and boundary choices are deliberate and continuously revisited, and the organization routinely refactors, re-scopes, and retires abstractions as the domain and the evidence shift.

## Ideas for discussion

- How do you tell the difference between a needed seam and speculative generality before you have the future requirement?
- When has DRY led your team to the wrong abstraction, and how did you recognize it?
- Where should bounded-context boundaries fall, and how closely should they mirror the org chart?
- How much design should precede code in your context, and how do you record the decisions?
- Which parts of your system would benefit from a more functional or data-oriented style?
- How do you keep design principles from hardening into dogma that resists pragmatic exceptions?

## Key takeaways

- Coupling and cohesion are the properties that matter; the acronyms are means to those ends.
- Every principle has a failure mode; know when each one misleads.
- Prefer a little duplication to a premature or wrong abstraction.
- Use DDD and bounded contexts to align complex domains with team ownership.
- Choose paradigms by fit; large systems are pragmatically mixed.
- Design for the changes you will actually need, avoiding both under- and over-design.

## References and further reading

- Robert C. Martin, *Clean Architecture* and *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* and *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
