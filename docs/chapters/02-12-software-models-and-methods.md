# 2.12 Software models and methods

## Overview and motivation

A software model is a deliberate simplification of a system, built to answer a specific question. A method is a disciplined way of producing software, including the models it uses along the way. Together they form a Software Engineering Body of Knowledge (SWEBOK) knowledge area, because they are the mental tools you use to reason about a system before, during, and after you build it. A UML ([Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)) class diagram, an [entity-relationship diagram](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), a [state machine](https://en.wikipedia.org/wiki/Finite-state_machine), a [formal specification](https://en.wikipedia.org/wiki/Formal_specification), and a throwaway prototype are all models. [Waterfall](https://en.wikipedia.org/wiki/Waterfall_model), [prototyping](https://en.wikipedia.org/wiki/Software_prototyping), formal development, and [agile](https://en.wikipedia.org/wiki/Agile_software_development) are all methods.

Why bother with models at all? Because human working memory is small and software systems are large. No one can hold a hundred-thousand-line system in their head, so we draw pictures and write abstractions that show one facet at a time: the data, the control flow, the states, the interactions. A model is never meant to be faithful to the code; it is meant to be fit for a decision. A good model shows exactly what you need to decide something, and hides everything else.

On large teams, the real stakes are coordination and communication. When hundreds of engineers, architects, analysts, and auditors work on one system, shared models are the common ground where they negotiate design, requirements, and risk. So think of modelling as a tool with a job to do. It pays off when a model is cheaper than the mistake it prevents. It becomes waste when you draw it for its own sake, keep it long after it has gone stale, or elaborate it past the decision it was meant to serve. Modelling connects tightly to software requirements (chapter 2.8), software design principles (chapter 2.2), architecture and its notations such as C4 and arc42 (chapter 3.1), and agile ways of working (chapter 10.7).

## Key principles

- Every model has a purpose; if you cannot name the decision a model informs, do not draw it.
- Abstraction is the core act of modelling: include what matters for the purpose, omit the rest.
- Consistency matters within and across models; contradictory models are worse than none.
- Models are communication artefacts first; their audience determines their notation and detail.
- Prefer the lightest model that answers the question; elaboration has a carrying cost.
- A model is only as good as its analysis; an unchecked model is an untested assumption.
- Choose the method to fit the problem's uncertainty, risk, and consequence of failure.

## Recommendations

### Model with abstraction, purpose, and consistency

Start every model by naming its purpose and audience. Then abstract ruthlessly toward that purpose: a sequence diagram meant to resolve a race condition should show timing and messages, not every field. Keep your models consistent with one another, so the entities in an ERD, the classes in a class diagram, and the nouns in the requirements all agree, and consistent with reality, which means you update or delete a model when the system moves on. A stale model that people trust is a hazard. A stale model that everyone ignores is waste that still costs attention.

### Choose structural or behavioural models to match the question

Use structural models to show what a system is made of and how the parts relate: class diagrams, component diagrams, and entity-relationship diagrams for data structure. Use behavioural models to show what a system does over time: state machines for objects with meaningful lifecycles, sequence diagrams for interactions across components, and activity diagrams for workflows and business processes. Pick the one notation that exposes the decision in front of you. Most systems need only a handful of diagram types, drawn selectively, not the full UML catalogue applied to everything.

### Analyse models, do not just draw them

A model earns its keep through analysis, not just drawing. Check a state machine for unreachable states, missing transitions, and deadlock. Check an ERD for normalization problems and orphaned relationships. Walk a sequence diagram against the requirements to find missing error paths. Review your models with the domain experts who can spot what is wrong. And where the cost of failure is high, reach for tool-supported analysis (model checkers, consistency checkers, simulation) rather than eyeballing it.

### Apply heuristic methods as the default

Most software is built with heuristic methods: experience-based, iterative approaches that use models informally and judge results against expectations rather than proofs. For most business and government systems, that is exactly right: requirements evolve, and a defect is usually recoverable. Heuristic methods pair naturally with agile (chapter 10.7): model just enough to align the team, then build and learn.

### Reserve formal methods for high-consequence cores

[Formal methods](https://en.wikipedia.org/wiki/Formal_methods) express specifications in mathematics and use verification, whether proof or exhaustive [model checking](https://en.wikipedia.org/wiki/Model_checking), to establish properties. They cost real skill and time, and they pay off precisely where failure is catastrophic or irreversible: safety-critical control, cryptographic protocols, financial settlement cores, and the like. Apply them to the small critical core, not the whole system. And note that formal specification alone, even without full proof, often adds value simply by forcing you to be precise.

### Use prototyping to retire uncertainty

When requirements or feasibility are unclear, build a prototype to learn, then decide, on purpose, whether to evolve it or discard it. Throwaway prototypes explore a question cheaply and are then deleted. Evolutionary prototypes become the product and must be built to production standards. The classic failure is letting a throwaway prototype slip into production by accident. So name the prototype's type before you build it.

### Match the method to risk, not to fashion

Choose methods by the problem's uncertainty and the consequence of failure. High uncertainty favours prototyping and agile iteration. High consequence favours formal analysis and rigorous verification. A system with both needs a critical formal core inside an otherwise agile envelope. Whatever you do, don't adopt a method just because it is prestigious or because a vendor is selling it.

## Trade-offs: pros and cons

| Model or method | Applied well | Failure mode |
|---|---|---|
| Structural models (UML, ERD) | Shared picture of parts and data | Diagram sprawl; drift from code |
| Behavioural models (state, sequence, activity) | Expose timing, states, and edge cases | Over-detailed diagrams nobody reads |
| Heuristic methods | Fast, flexible, fit most systems | Undisciplined; hidden assumptions |
| Formal methods | Provable properties for critical cores | High cost; misapplied to whole system |
| Prototyping | Cheap learning; retires risk early | Throwaway code promoted to production |
| Agile methods | Adapts to changing requirements | Skips modelling needed for hard problems |

The recurring tension is between rigour and speed. Too little modelling ships hidden assumptions into production. Too much modelling burns effort on diagrams that never inform a decision and rot the moment the code changes. There is no fixed dose that fixes this, only a rule of proportion: invest in a model or method in proportion to the uncertainty it resolves and the cost of getting the decision wrong. A payments engine and a marketing microsite deserve different treatment.

## Questions to discuss with your team

1. **Do we analyse our models, or do we just draw them and move on?** A model earns its keep through analysis, not through existing: a state machine you never check for unreachable states or missing transitions is an untested assumption dressed up as a diagram. On a large team this is where real defects hide, because a plausible-looking picture gets trusted precisely when no one has walked it against the requirements to find the missing error path or the orphaned relationship. Bring your most important behavioural model to the meeting and try to break it: which transition is undefined, which state has no exit, which sequence has no timeout? Where the cost of failure is high, the answer should push you toward tool-supported analysis (model checkers, consistency checkers, simulation) rather than eyeballing, because the whole reason to model a critical core is to find the flaw on a whiteboard instead of in production.

2. **When two of our models disagree, which one wins, and who notices the contradiction?** Consistency matters within and across models, and contradictory models are worse than none, because people act on both. On a big system the entities in the data model, the classes in the design, and the nouns in the requirements drift apart quietly as different teams update different artefacts, and the first sign is often a production bug where two components disagreed about what a thing is. Bring an example: pick a core concept and check whether the ERD, the code, and the requirements actually agree on its shape and its lifecycle. If they do not, decide which artefact is authoritative and who is responsible for keeping the others in step, and be willing to delete a model rather than let a stale one keep lying to the team.

3. **Which core in our system, if it is wrong, loses real money or harms someone, and does it get the rigour it deserves?** The central move of this chapter is matching the method to risk: heuristic and agile methods for the recoverable majority, formal specification and verification for the small high-consequence core, and cheap prototyping for the genuinely uncertain. The failure modes are symmetrical and both expensive: applying formal methods to a marketing microsite burns money, and treating a settlement engine or an eligibility rule set as ordinary agile work invites the catastrophic, irreversible defect. Bring a map of your system and mark where an error is catastrophic versus recoverable, and where requirements are certain versus unknown. The answer should concentrate your modelling investment where the money and the ambiguity are, and explicitly withhold it everywhere else, so a critical formal core can sit inside an otherwise agile envelope without either method leaking into the other's territory.

4. **How much modelling do we do before we write code, and does that dose change with the uncertainty in front of us?** Big design up front and no design at all are both failure modes, and the right dose sits between them, governed by how much uncertainty a model actually retires. On a large team the pressure runs both ways: a governance process may demand a full set of diagrams before any code, locking in decisions made with the least information, while delivery pressure may push a team to skip the one state machine that would have caught a costly edge case. Bring your last two projects and sort the models you produced into those that informed a real decision and those drawn only because a template asked for them. In enterprise and government programmes, where a phase gate or approval board often mandates documents up front, come ready to argue for modelling that tracks risk rather than a fixed deliverable list, so the payments core gets its rigour and the internal reporting tool does not drown in diagrams nobody reads.

5. **Have we agreed a shared notation and a single home for our models, or does every team invent its own?** Models are communication artefacts first, and their value collapses when a state machine drawn in one team's tool cannot be read, found, or trusted by the team that inherits it. For hundreds of engineers the competing considerations are real: a mandated notation and repository buy consistency and discoverability, but they also impose a learning cost and can push people toward heavyweight tools when a photographed whiteboard would serve. Bring examples of where a model actually lived (a wiki, a diagram tool, a slide deck, someone's laptop) and ask who could find and understand it six months later. In enterprise and regulated settings the audit angle sharpens this: an auditor who cannot locate the current data model or trace a decision back to a documented state machine will treat the system as undocumented, so agree a small shared notation and a durable location, and accept lightweight capture over ceremony wherever the consequence is low.

6. **Before we build a prototype, do we decide on purpose whether it is throwaway or evolutionary, and do we hold ourselves to that choice?** The classic, expensive failure is a throwaway prototype that quietly slips into production because it demoed well and nobody named its type up front. The tension is genuine: throwaway prototypes buy the cheapest possible learning and should be deleted, while evolutionary prototypes become the product and must be built to production standards from the first line, and confusing the two either wastes rework or ships fragile code into a role it was never engineered for. Bring a recent prototype and ask what was decided before it was built, who held authority to promote or discard it, and whether that decision survived delivery pressure. In government and other accountable settings, where a citizen-facing system carries transparency and reliability obligations, treat accidental promotion as a control failure: fix the prototype's fate in advance, and make discarding a successful throwaway a celebrated outcome rather than a waste to be avoided.

## Sector lens

**Startup.** Model on a whiteboard, photograph it, and move on. Your scarcest resource is engineering attention, so reach for a model only when it is cheaper than the mistake it prevents: a subscription state machine before you code the billing edge cases, not a full UML catalogue for a product that may pivot next month. Stay heuristic and agile, keep formal methods off the table entirely, and treat every prototype as throwaway unless you consciously decide otherwise.

**Small business.** You likely have no one whose job is formal modelling, so lean on the models already embedded in the tools and frameworks you buy rather than standing up a modelling practice of your own. Frame the few models you do draw around concrete decisions: a simple data-model sketch to agree what customer data you hold, a state diagram for the one workflow that loses you a customer when it breaks. Prefer a bought product with a proven data model over building and documenting your own, and keep whatever you draw light enough that one person can maintain it.

**Enterprise.** The core problem is coordination across many teams, so shared models become the common ground: an agreed data model, a consistent notation, and a home where the ERD, the C4 diagrams, and the state machines can be found and trusted. Standardize a small notation and enforce consistency so the entities in the requirements, the design, and the database do not drift apart between teams. Reserve formal specification and model checking for the high-consequence cores (settlement, reconciliation, access control), fund the specialist skill that demands, and keep an audit trail from each documented model back to the decision it justified.

**Government.** Rules set in law must be traceable to statute, which is where formal specification earns its cost: specify eligibility or assessment logic precisely, verify key properties, and let auditors trace every outcome back to the rule that produced it. Procurement adds its own weight, since documents and models are often contractual deliverables, so agree which models are genuinely decision-bearing rather than produced only to satisfy a checklist. Publish plain-language descriptions of how consequential systems work, and use throwaway prototyping to test citizen-facing intake with real users before committing to a production build.

## Examples

**Startup.** A small startup building a subscription billing product sketches the subscription lifecycle (trial, active, past-due, cancelled, reactivated) as a state machine on a whiteboard before writing code. Walking the diagram, they notice they never defined what happens when a past-due account's payment finally clears, an edge case that would have stranded real customers in limbo. That five-minute model saves a production headache, and they photograph it rather than maintaining a heavyweight diagram tool. Everywhere else they stay agile and model just enough to align, because at their scale a defect is recoverable and formal methods would be pure cost.

**Enterprise.** A global bank builds a new payments platform. The team uses an entity-relationship diagram to agree on the shared data model across the accounts, ledger, and messaging teams, and C4 diagrams (chapter 3.1) to show how the services fit together. They model the transaction lifecycle (pending, cleared, settled, reversed, disputed) as an explicit state machine, and analysis reveals it is missing a transition for partial reversals. The gap gets fixed on a whiteboard rather than in production. Sequence diagrams walk the settlement flow against the requirements (chapter 2.8) to surface missing timeout and retry paths. Day-to-day delivery is agile, but the core reconciliation algorithm, where an error means real money lost, gets a formal specification and is model-checked before implementation. Modelling is concentrated where the money and the ambiguity are, and kept light everywhere else.

**Government.** A national tax agency modernizes benefits assessment. Because eligibility rules are set in law and audited, the team writes a formal specification of the rules as pure transformations and verifies key properties, such as no claimant being both eligible and ineligible and every case reaching a decision, so auditors can trace outcomes back to statute. Alongside the formal core, the team builds a throwaway prototype of the citizen-facing intake form to test with real users. They learn that a multi-step wizard reduces errors, then discard the prototype and rebuild the intake to production standards. Activity diagrams document the end-to-end caseworker process for training and audit. The high-consequence rules get formal rigour; the uncertain user experience gets cheap prototyping; neither method is applied where the other belongs.

## Business case: motivations, ROI, and TCO

The return on modelling comes from finding defects earlier, where they are far cheaper to fix. A contradiction found on a whiteboard costs minutes. The same contradiction found in production can cost an outage, a rework programme, or, in regulated domains, a legal liability. Models also lower the total cost of ownership by serving as durable communication. A system that outlives its authors, the normal case in enterprise and government, is far cheaper to maintain when its data model, state machines, and key flows are documented accurately.

The costs are real, and you have to weigh them. Models take time to build, skill to build well, and ongoing effort to keep current; formal methods add specialist labour. The break-even point is governed by uncertainty and consequence. Where both are low, heavy modelling destroys value and agile heuristics win. Where either is high, targeted modelling, and, for the critical core, formal verification, pays back many times over by preventing the expensive class of failure. To make the case to leadership, tie modelling investment to specific risks retired and to the maintainability of long-lived systems. And track whether models are actually consulted, because an unused model is pure cost.

## Anti-patterns and pitfalls

- **Modelling for its own sake:** producing diagrams because a process demands them, not because they inform a decision.
- **Stale models trusted as truth:** diagrams that no longer match the code but are still relied upon.
- **Big design up front:** exhaustive models produced before any code, locking in decisions made with the least information.
- **Diagram sprawl:** every UML type applied uniformly, drowning the few useful views in noise.
- **Formal methods everywhere:** applying expensive verification to code where the consequence of failure does not justify it.
- **Accidental prototype promotion:** a throwaway prototype quietly shipped as the product.
- **Notation over substance:** arguing about UML correctness instead of whether the model answers the question.

## Maturity model

- **Level 1 (Initiate):** Modelling is ad hoc or absent and purely reactive; no method is named; models, when drawn at all, are inconsistent, unanalysed, and abandoned as soon as the meeting ends.
- **Level 2 (Develop):** Some teams draw common diagrams and follow a named method, but practice is uneven across the organization: models are often produced ceremonially, drift from the code, and are rarely analysed for defects.
- **Level 3 (Standardize):** A shared notation, a documented method-selection guide, and consistency rules are defined and enforced org-wide; models are chosen by purpose, kept in step with the system, reviewed for defects, and the method is matched to each problem's risk.
- **Level 4 (Manage):** Modelling is measured and controlled against baselines; teams track how many defects analysis catches before implementation, how far models drift from the code, whether each model was actually consulted for a real decision, and the rework and cycle time saved versus a defined baseline; method choice is calibrated to measured uncertainty and consequence, and critical cores are formally verified against agreed coverage targets.
- **Level 5 (Orchestrate):** Modelling and method selection are continuously improved and integrated with delivery and risk planning across the organization; investment adapts as uncertainty and consequence shift, models are routinely kept current, retired, or deepened on evidence, and formal, heuristic, and prototyping methods are composed so each sits exactly where it pays off.

## Ideas for discussion

- For your last project, which models informed a real decision, and which were drawn only because a process demanded them?
- Where in your systems would a formal specification pay for itself, and where would it be waste?
- How do you decide whether a prototype is throwaway or evolutionary, and do you enforce that decision?
- How do you keep models from drifting out of sync with the code, or do you accept that some should be deleted instead?
- What is the right amount of modelling before code in your context, and how does it change with uncertainty?
- Which behavioural model (state, sequence, or activity) would have caught your most recent production incident?

## Key takeaways

- A model is a purposeful abstraction; if you cannot name the decision it informs, do not draw it.
- Match structural and behavioural models to the specific question, and keep them consistent and current.
- Analyse models; an unchecked model is an untested assumption.
- Heuristic and agile methods fit most systems; reserve formal methods for high-consequence cores.
- Use prototypes to retire uncertainty, and decide up front whether they are throwaway or evolutionary.
- Invest in modelling in proportion to the uncertainty it resolves and the cost of getting the decision wrong.

## References and further reading

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, Software Engineering Models and Methods knowledge area
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modeling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modeling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* and *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (the Alloy modeling language)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (the C4 model)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
