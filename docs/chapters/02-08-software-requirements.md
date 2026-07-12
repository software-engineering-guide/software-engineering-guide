# 2.8 Software requirements

## Overview and motivation

A [software requirement](https://en.wikipedia.org/wiki/Software_requirements) is a statement of a capability or condition that a system must provide, satisfy, or possess to be acceptable to its stakeholders. [Requirements engineering](https://en.wikipedia.org/wiki/Requirements_engineering), the disciplined work of eliciting, analysing, specifying, validating, and managing those statements, sits right at the front of the value chain. Everything downstream, from architecture to code to [acceptance testing](https://en.wikipedia.org/wiki/Acceptance_testing), is an attempt to satisfy requirements. So when requirements are wrong, incomplete, or ambiguous, all the effort spent building the wrong thing correctly is pure waste, and it is the most expensive waste there is, because you discover it latest. The [Software Engineering Body of Knowledge](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) Software Requirements knowledge area treats this as a real engineering discipline, not a clerical prelude to the real work.

For large teams, requirements are the shared understanding that lets many people build one coherent system. A single developer can hold the intent in their head; hundreds of people across many teams cannot. Requirements become the contract between those who need a capability and those who build it, the basis for splitting work across teams, and the yardstick for judging when something is "done." They connect directly to discovery (chapter 11.1), where problems and opportunities surface; to UX foundations (chapter 5.1), where you understand user needs; to APIs and interface design (chapter 2.3), where interface obligations get fixed; to architecture and quality attributes (chapter 3.1), where nonfunctional requirements drive structure; and to project management (chapter 10.6), where scope, cost, and schedule are planned around them.

In enterprise and government settings, requirements carry legal, contractual, and safety weight. A regulated system has to show that every mandated obligation (accessibility, privacy, security, records retention, financial control) is captured as a requirement, implemented, and verified with evidence. Government procurements are often built around a requirements specification, and payment, audit, and certification all depend on tracing each requirement to the evidence that it was met. Here, requirements are more than good practice: they are the backbone of accountability.

## Key principles

- A requirement expresses a need or constraint, not a solution; it says what and why, not how.
- Every requirement must be necessary, unambiguous, verifiable, feasible, and traceable.
- Requirements are discovered and negotiated with stakeholders, not invented in isolation.
- Nonfunctional requirements and constraints shape architecture as much as functionality does.
- Requirements evolve; manage change deliberately rather than freezing or ignoring it.
- Traceability, from need to requirement to design to test to evidence, is the connective tissue of accountability.
- The right level of formality depends on risk, scale, and regulatory context, not habit.

## Recommendations

### Define requirements clearly and categorize them

Name the categories on purpose. **[Functional requirements](https://en.wikipedia.org/wiki/Functional_requirement)** state what the system must do: the behaviours, transformations, and services it provides. **[Nonfunctional requirements](https://en.wikipedia.org/wiki/Non-functional_requirement)** (quality attributes) state how well it must do them: performance, availability, security, usability, accessibility, maintainability, and more; these bind tightly to architecture (chapter 3.1). **Constraints** are the non-negotiable boundaries on the solution: mandated technologies, standards, budgets, legal rules, or interfaces to existing systems. And separate **business requirements** (why the organization wants the system) from **user requirements** (what users need to accomplish) from **system requirements** (what the software must therefore do). Blur these levels together and scope confusion soon follows.

### Elicit from real sources, not assumptions

Elicitation is active discovery. Draw requirements from stakeholders through interviews, workshops, observation, [prototypes](https://en.wikipedia.org/wiki/Software_prototyping), and analysis of existing systems and documents. Track down every relevant stakeholder, including the ones easy to overlook: operators, auditors, support staff, and people affected by the system who never use it directly. Tie elicitation to the discovery pipeline (chapter 11.1) and UX research (chapter 5.1), so stated wants trace back to the underlying needs. Record the source and rationale of each requirement, because knowing why a requirement exists is exactly what lets you change it safely later.

### Analyse, negotiate, and prioritize

Raw elicited needs conflict, overlap, and add up to more than is feasible. Analysis is how you reconcile them: classify requirements, spot conflicts, weigh feasibility and risk, and negotiate priorities with stakeholders. Prioritize out in the open, say with must/should/could distinctions or value-versus-cost ranking, so when time runs short, you cut the right scope. And model the requirements wherever a model adds clarity: process flows, state diagrams, data models, and interface definitions surface gaps that prose hides.

### Specify at the right level of formality

Write requirements down in a form that fits the risk and the audience. A high-assurance government system may warrant a formal specification structured to a standard such as IEEE 29148; a fast-moving product team may capture requirements as [user stories](https://en.wikipedia.org/wiki/User_story) with acceptance criteria in a backlog. Either way, each requirement should be atomic, verifiable, and free of slippery words like "fast," "user-friendly," or "etc." Attach acceptance criteria, so you define how to verify a requirement at the same moment you write it. And keep one authoritative source, rather than letting requirements scatter across emails, tickets, and slides.

### Validate before building

Validation confirms that the requirements you've specified are the right ones and hang together. Review them with stakeholders, walk through scenarios, and where you can, use prototypes to make abstract statements concrete. Validation is cheaper than any later correction: a defect caught in a requirements review costs a fraction of the same defect caught in production.

### Manage requirements and maintain traceability

Requirements change. Your job is to control that change, not resist it. Set up a change process: weigh each proposed change for impact, cost, and downstream effect before you accept it. Baseline requirements at agreed points and version them. Keep **[bidirectional traceability](https://en.wikipedia.org/wiki/Requirements_traceability)** that links each requirement forward to design, code, and tests, and backward to the need it came from. Traceability answers the two questions large teams live by: if this need changes, what does it affect; and for this delivered feature, which need justified it? In regulated contexts, extend the trace all the way to acceptance evidence (test results, audit records, sign-offs) so you can demonstrate compliance rather than just assert it.

### Adapt to agile and plan-driven contexts

In plan-driven and regulated programmes, you specify and baseline requirements fairly early, with formal change control. In agile contexts, requirements live as a prioritized, evolving backlog, elaborated just before implementation and validated continuously through working software. The underlying activities are the same in both; only the timing, formality, and artifacts differ. Large organizations often blend the two: they specify and trace stable, high-assurance obligations formally, while elaborating product behaviour iteratively. Choose the balance by risk, not ideology.

## Trade-offs: pros and cons

| Approach | Best for | Pros | Cons |
|---|---|---|---|
| Formal upfront specification | High-assurance, regulated, fixed-scope contracts | Strong traceability; clear acceptance basis; auditable | Slow to change; risks over-specifying before learning |
| Agile backlog | Evolving products with engaged stakeholders | Fast feedback; adapts to learning; less waste on unbuilt scope | Weaker long-range traceability; harder to audit and contract |
| Hybrid (formal constraints + agile behaviour) | Enterprises with mixed obligations | Rigour where it matters, flexibility elsewhere | Requires judgement about which parts are which |

The central tension is between stability and learning. Fixing requirements early buys you a firm acceptance basis and auditability, but costs you the ability to adapt to what you learn while building. Deferring them buys adaptability, but costs you long-range traceability and contractual clarity. Investing more in requirements engineering also trades near-term speed for less rework later: a trade that pays off as a system's scale, longevity, and consequence of failure rise. The largest projects and the most regulated ones sit firmly on the high-investment side. A low-stakes internal tool does not.

## Questions to discuss with your team

1. **Who counts as a stakeholder for our highest-risk system, and which ones do we keep leaving out until acceptance?** On a large programme the people who get skipped are rarely the obvious users: they are the operators who run the thing at 3am, the auditors who have to certify it, the support staff who field the failures, and the affected non-users who never log in but whose data you hold. Miss them and you discover their requirements at the most expensive moment, during acceptance or after a regulator asks. Bring a concrete stakeholder map to the meeting and stress-test it: for each mandated obligation (accessibility, privacy, records retention, security) name the person who owns it and the requirement that captures it. If you cannot name an owner, you have found a gap, and the fix is to add that stakeholder to elicitation now rather than to retrofit their needs into a fixed architecture later.

2. **When a requirement changes, can we answer what it affects before we approve the change?** This is the practical test of whether your bidirectional traceability is real or decorative. In a large or regulated system a single rule change can ripple into design, code, tests, and acceptance evidence, and approving it blind is how you ship a compliant-looking system that quietly violates a rule it used to satisfy. Bring a recent change request and try to trace it forward in the meeting: if it takes an afternoon of archaeology, your traceability is not doing its job. The answer should reshape your change process, so that impact assessment is a fast query against a live trace rather than a manual hunt, and so baselines and versioning give you a stable point to change against.

3. **Where does the single authoritative source of our requirements live, and how much truth is scattered outside it?** Requirements sprawl (the real spec living across emails, tickets, slides, and someone's memory) is one of the most common failures on big teams, and it is fatal in audited systems where you must show what was agreed. Decide, out loud, which system of record is canonical, and treat anything stated elsewhere as a draft until it lands there with its source and rationale attached. Bring evidence: count how many recent scope disputes came down to two people citing different "final" versions. If the count is greater than zero, the action is to consolidate to one source and to write down the rationale for each requirement, because knowing why a requirement exists is exactly what lets you change or drop it safely later.

4. **Are our nonfunctional requirements captured early enough to drive architecture, or do we keep discovering them after the structure is fixed?** Performance, availability, security, and accessibility obligations shape architecture more than most features do, and on a large programme they are the requirements most often surfaced too late, once the structure that would have to satisfy them is already poured in concrete. The competing pull is real: functional behaviour is what stakeholders ask for out loud and demo well, while a "sub-second response under peak load" or "WCAG accessibility conformance" requirement is invisible until it is violated. Bring the current list of nonfunctional requirements for your highest-risk system, the point in the timeline each was written, and whether architecture (chapter 3.1) received them as explicit drivers or inferred them. In enterprise and government settings, add the mandated quality obligations (encryption, records retention, accessibility law) and check that each one is a written, measurable requirement handed to design rather than an assumption, because retrofitting a quality attribute after acceptance is where budgets and schedules quietly die.

5. **What level of formality is right for each system we own, and do we choose it by risk or by habit?** A single large organization usually runs a spread of systems, from a throwaway internal tool to a life-or-safety regulated platform, and applying one ceremony to all of them either buries the low-risk work in paperwork or leaves the high-risk work under-specified. The tension is between the auditability and firm acceptance basis of formal upfront specification and the fast feedback and reduced waste of an evolving backlog, and the honest answer for most enterprises is a deliberate blend: formalize and trace the stable, high-assurance obligations while elaborating product behaviour iteratively. Bring a short inventory of your systems ranked by consequence of failure, regulatory exposure, and rate of change, and for each name the formality you actually use versus the formality the risk warrants. For a government programme anchored to a solicitation and a standard such as IEEE 29148, the formality is partly dictated by the contract, so the discussion is where you can layer agile elaboration on top without breaking the traceability the audit depends on.

6. **Can every requirement in our highest-risk system be verified, and does each carry acceptance criteria written the moment the requirement was?** A requirement you cannot verify is not a requirement, it is a wish, and slippery words like "fast," "secure," or "user-friendly" pass review precisely because nobody can fail them. For a large team this matters twice over: unverifiable requirements produce scope disputes at acceptance, and they make it impossible to say when a feature is genuinely done. The competing consideration is speed, since attaching a measurable criterion and a verification method to each requirement is slower upfront than writing prose, but it is the cheapest defence against the most expensive late rework. Bring a sample of recent requirements and test each against a simple bar: is it atomic, is it measurable, and does it name how it will be checked. In regulated and government contexts, extend the test to evidence: a requirement without traced, passing acceptance evidence is not considered delivered no matter what the software appears to do, so acceptance criteria are the seed of the compliance record you will eventually have to produce.

## Sector lens

**Startup.** With a tiny team and little runway, keep requirements as lightweight as you can get away with: user stories with acceptance criteria in one shared backlog, not a specification document. The discipline that pays off even here is talking to real users before you build and recording the source and rationale of each story, so the week you would have wasted building the wrong feature is the week you save. Skip formal traceability, but never skip the conversation that tells you what the actual need is.

**Small business.** You likely have no business analyst or requirements specialist, so the work falls to whoever is closest to the customer, and the buy-versus-build question dominates. Frame requirements as a short, prioritized list of the outcomes you need, then use it to evaluate off-the-shelf tools rather than to specify a bespoke build. Be strict about separating the underlying need from a vendor's feature list, because a requirement written as "we need product X" quietly forecloses cheaper options that would have met the real need.

**Enterprise.** Scale turns requirements into the contract that lets many teams build one coherent system, so the priority is a standard process applied consistently: defined categories, bidirectional traceability from need to test, a single authoritative source, and controlled change with baselines. Separate business, user, and system requirements explicitly and hand nonfunctional requirements to architecture as drivers, so scope and quality obligations do not scatter across teams. Blend formal specification for stable, high-assurance obligations with agile elaboration of product behaviour, and govern the balance by risk rather than by any one team's preference.

**Government.** Procurement rules often build the whole contract around a requirements specification, frequently structured to a standard such as IEEE 29148, so precision and completeness are contractual, not optional. Maintain a requirements traceability matrix that links each requirement to design, test cases, and acceptance evidence, because vendor payment, audit, and the authority to operate all depend on demonstrated coverage. Transparency and public accountability raise the bar further: mandated obligations for accessibility, privacy, and records retention must each appear as an explicit, verifiable requirement, and a requirement without traced, passing evidence is simply not delivered.

## Examples

**Startup.** A four-person startup building a scheduling app captures requirements as user stories with acceptance criteria in a shared backlog, not a formal specification. Before writing the calendar-sync feature, the founder spends an afternoon talking to five prospective customers and learns that the real need is avoiding double-bookings across two tools, not the syncing they had assumed. That one conversation reframes the story and saves a week of building the wrong thing. Even at this scale they write down the source and rationale of each story, so when priorities shift they can drop or rework scope without relitigating why it existed.

**Enterprise.** A multinational bank replaces its loan-origination platform. The requirements team separates business requirements (reduce approval time, meet lending regulations), user requirements (loan officers need to compare offers in one view), and system requirements (the platform must integrate with three core systems). Nonfunctional requirements (sub-second response for common queries, 99.95% availability, encryption of personal data) are captured explicitly and handed to architecture (chapter 3.1) as drivers. Every requirement is traced through the backlog to automated acceptance tests. So when a regulator asks how a specific lending rule is enforced, the team just follows the trace from the rule to the test that verifies it.

**Government.** A national agency procures a benefits-eligibility system through a formal solicitation. The contract is anchored to a requirements specification structured to IEEE 29148, covering functional eligibility rules, mandated accessibility conformance, privacy and records-retention constraints, and security controls. A requirements traceability matrix links each requirement to design elements, test cases, and acceptance evidence. Vendor payments and the authority to operate (the formal approval to run the system in production) both depend on demonstrated coverage. A requirement without traced, passing acceptance evidence simply isn't considered delivered, no matter what the software appears to do.

## Business case: motivations, ROI, and TCO

The economic argument for requirements engineering rests on the cost of fixing defects late. Industry studies consistently find that requirements defects are among the most common and most expensive causes of project failure, and that the cost to fix a defect climbs by orders of magnitude from the requirements phase to production. So money spent clarifying and validating requirements is really leverage: a modest investment early spares you from building, testing, and operating the wrong thing.

The total cost of ownership of requirements includes the ongoing effort of elicitation, specification, tooling, and change management across the system's whole life; it is not a one-time cost. Against it stands the cost of poor requirements: rework, scope disputes, schedule overruns, failed acceptance, contractual penalties, and, in regulated settings, fines or loss of authorization. For leadership, frame requirements maturity as risk reduction and predictability. Track requirements volatility, defect origin, and the share of delivered work traceable to a validated need, and connect these to project management forecasting (chapter 10.6). The return doesn't show up as a feature. It shows up as the failures and rework that never happened.

## Anti-patterns and pitfalls

- **Solutions disguised as requirements:** specifying a chosen technology or screen layout instead of the underlying need, foreclosing better options.
- **Ambiguous language:** "fast," "secure," "intuitive" with no measurable criterion, making the requirement unverifiable.
- **[Gold-plating](https://en.wikipedia.org/wiki/Gold_plating_(software_engineering)):** capturing requirements no stakeholder actually needs, inflating scope and cost.
- **Missing nonfunctional requirements:** discovering performance, security, or accessibility obligations only after architecture is fixed.
- **Requirements sprawl:** the truth scattered across emails, tickets, and slides with no authoritative source.
- **Frozen or uncontrolled change:** either refusing all change or accepting every change without impact assessment.
- **No traceability:** inability to answer what a change affects or why a feature exists, fatal in audited systems.
- **Analysis paralysis:** endless specification that delays learning from working software.
- **Ignored stakeholders:** operators, auditors, and affected non-users left out until acceptance.

## Maturity model

- **Level 1, Initiate.** Requirements are implicit or verbal, captured inconsistently and reactively. Scope disputes and rework are common; there is no traceability, no acceptance criteria, and no defined process.
- **Level 2, Develop.** Some teams write requirements down and track them per project, with basic prioritization and ad hoc change handling. Practices exist but vary by team and person, so categories, formality, and quality are inconsistent across the organization.
- **Level 3, Standardize.** A standard requirements process is documented and enforced organization-wide: defined categories, elicitation and validation practices, acceptance criteria attached at authoring time, a single authoritative source, and bidirectional traceability from need to test, adapted consistently to agile or plan-driven context.
- **Level 4, Manage.** The process is measured and controlled with data. Requirements volatility, defect origin, traceability coverage, and the share of delivered work traceable to a validated need are tracked against baselines; traceability extends to acceptance evidence and compliance; and requirements metrics feed project forecasting (chapter 10.6), so change and quality decisions rest on evidence rather than opinion.
- **Level 5, Orchestrate.** Requirements practice is continuously improved and integrated across the organization. Formality is tuned adaptively by risk and outcome, elicitation and traceability tooling connect to discovery, architecture, and delivery, and the organization uses its own measurement history to prevent recurring requirements defects before they reach code.

## Ideas for discussion

- How do you tell a genuine requirement from a premature solution when a senior stakeholder states it as a solution?
- What level of requirements formality is right for your highest-risk system versus your lowest-risk one, and who decides?
- How do you keep bidirectional traceability current in a fast-moving agile backlog without it becoming bureaucratic overhead?
- Which nonfunctional requirements are most often discovered too late in your organization, and why?
- In a regulated programme, what constitutes sufficient acceptance evidence that a requirement was met?
- How should AI-assisted elicitation and specification tools change your requirements practice, and what new risks do they introduce?

## Key takeaways

- Requirements state needs and constraints, not solutions; they must be necessary, unambiguous, verifiable, and traceable.
- Separate functional, nonfunctional, and constraint requirements, and the business, user, and system levels.
- Elicit from real stakeholders, analyse and prioritize, specify at fitting formality, validate before building, and manage change.
- Bidirectional traceability from need to acceptance evidence is the backbone of accountability, especially in regulated settings.
- Agile and plan-driven contexts share the same activities; they differ in timing, formality, and artifacts, so choose by risk.
- The cost of poor requirements is paid late and multiplied; investing early is leverage against rework and failed acceptance.

## References and further reading

- IEEE and ISO/IEC, *Guide to the Software Engineering Body of Knowledge (SWEBOK)*, Software Requirements knowledge area
- Karl Wiegers and Joy Beatty, *Software Requirements*
- ISO/IEC/IEEE 29148, *Systems and software engineering: Life cycle processes: Requirements engineering*
- Suzanne Robertson and James Robertson, *Mastering the Requirements Process*
- Dean Leffingwell, *Agile Software Requirements*
- Mike Cohn, *User Stories Applied*
- Ian Sommerville, *Software Engineering* (requirements engineering chapters)
