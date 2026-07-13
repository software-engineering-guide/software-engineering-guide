# 1.6 Decision records

## Overview and motivation

A **decision record** is a document that captures an important decision along with its context and consequences. The best-known form is the **[architecture decision record](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, a short, immutable-by-preference note that records one architecturally significant choice, why it was made, and what follows from it. A project's full set of records is its **decision log (ADL)**, and the discipline of keeping them is part of **architecture knowledge management (AKM)**. This chapter builds on the decision-making and governance practices of chapter 1.5, focusing on how you write, store, and sustain decision records at scale.

The motivation is simple, and painful to learn the hard way. On any long-lived system, the most expensive question is "why on earth was it built this way?", asked months or years later by people who were not in the room. Code shows *what* the system does. Tests show that it *works*. But neither captures *why* you chose this path over the alternatives you considered and rejected. Without decision records, that reasoning evaporates with staff turnover. Teams relitigate settled questions, reverse good decisions for bad reasons, or keep bad decisions out of fear. A decision record is a cheap letter to the future that preserves the reasoning.

For large teams, this is a coordination tool as much as a memory aid. Enterprises run dozens of teams making overlapping choices. A shared decision log turns one team's hard-won reasoning into a reusable asset, and prevents divergent, incompatible decisions. In government and regulated settings, decision records are close to mandatory. Auditors, oversight bodies, and successor contractors all need a traceable rationale connecting architecturally significant requirements to the choices made against them. A well-kept decision log is often the difference between a system you can assure and audit and one you cannot.

## Key principles

- **Record the *why*, not just the *what*.** Context and rejected alternatives are the point.
- **One decision per record.** Keep each record specific and self-contained.
- **Small and lightweight beats comprehensive and unused.** A one-page record that exists beats a report that never gets written.
- **Timestamp everything.** Costs, constraints, and vendors change; date each claim.
- **Prefer a living log, pragmatically.** Immutability is the ideal; in practice, amend with dated notes.
- **Words over abbreviations.** "Decisions" invites more contribution than "ADRs."
- **Make decisions discoverable and, where possible, testable.** Surface the right record at the right moment; assure it with fitness functions.

## Recommendations

### Capture the essential structure

A good decision record has a few essential sections. Adapt a known template rather than inventing one:

- **Title:** a short, present-tense imperative phrase ("Use [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) for the ledger").
- **Status:** proposed, accepted, superseded, deprecated.
- **Context:** the situation, forces, business priorities, and constraints that make this decision necessary; include the architecturally significant requirement it addresses.
- **Decision:** the choice made, stated plainly.
- **Consequences:** what becomes easier and what becomes harder, follow-on decisions triggered, and risks accepted.

Popular templates include Michael Nygard's (simple and widely adopted), Tyree and Akerman's (more elaborate, with weighted alternatives), MADR (Markdown Any Decision Records, strong on options and their pros/cons), and Y-statements (a one-sentence structured form). Standardize on one per organization, so records are comparable. See chapter 12.3 for a copy-paste template.

### Write records that are specific, dated, and immutable-ish

Keep each record about exactly one decision. Timestamp individual claims, especially anything that drifts: pricing, scaling numbers, vendor capabilities, licence terms. In theory, a record should be immutable. When a decision changes, you write a *new* record that supersedes the old one, preserving history. In practice, many teams find a **living-document** approach works better: insert new information into the existing record with a date stamp and a note that it arrived after the decision. Both are legitimate. The immutable style is stronger for audit trails; the living style is better for everyday team knowledge. Choose deliberately, and be consistent.

### Store records where the work is

Put decision records in [version control](https://en.wikipedia.org/wiki/Version_control) alongside the code: a `decisions/` (or `adr/`) directory of [Markdown](https://en.wikipedia.org/wiki/Markdown) files, one per decision, named with a lowercase, dash-separated imperative verb phrase (`choose-database.md`, `format-timestamps.md`). This gives you history, review, and diffing for free, and keeps the rationale next to what it explains. If your team prefers [wikis](https://en.wikipedia.org/wiki/Wiki), Google Docs, or a Jira-style tracker, use those instead. The tool matters far less than the habit. A lightweight command-line tool (such as `adr-tools`) can scaffold and index records.

### Name them "decisions," and broaden beyond architecture

A practical insight from many teams: the label matters. Some developers and managers bristle at the word "architecture," and "record" can feel like after-the-fact paperwork. Renaming the directory simply "decisions" often flips a switch. Teams start recording vendor choices, planning decisions, scheduling decisions, data and compliance decisions, all with the same template. People learn faster from words than from abbreviations, and they contribute more when the framing is "help your future teammates think" rather than "file the mandatory form."

### Define the lifecycle and governance

For decision records to scale, agree on the surrounding process (this is where chapter 1.5's governance meets practice):

- **Who can raise one, and what justifies it:** typically any informed contributor; raise a record when future developers will need the *why*, and skip it for low-risk, self-contained, or already-documented choices.
- **Lifecycle:** a simple flow such as *Initiating → Researching → Evaluating → Implementing → Maintaining → Sunsetting*, with acceptance criteria to move between stages (problem articulated, alternatives considered, trade-offs documented, stakeholders consulted).
- **Roles:** proposer, researcher, reviewer, approver, and an accountable maintainer who reviews the record periodically (at least annually) and drives eventual sunsetting.
- **Governance:** how consensus, conflict, escalation, and veto work, and any compliance constraints. Lean on principles like *bias for action* and *[disagree-and-commit](https://en.wikipedia.org/wiki/Disagree_and_commit)*, and reserve heavier process for irreversible, high-blast-radius ("one-way door") decisions.

### Make decisions testable and discoverable

A decision record *documents* a decision; a **fitness function** *assures* it: an automated check, run in [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), that verifies the decision still holds ("all state changes must emit events," "no module may import across these boundaries," using tools like ArchUnit). This turns governance from periodic manual review into continuous, scalable enforcement, which is especially valuable for regulatory and audit goals (chapters 3.1, 4.6, 8.5). Then surface the *right* record at the *right* moment. Tooling that attaches relevant decisions to a pull request, when a developer touches the code they govern, beats hoping people read a docs folder.

## Trade-offs: pros and cons

| Choice | Pros | Cons |
|---|---|---|
| **Lightweight ADRs (Nygard/MADR)** | Fast to write, actually get written; low ceremony | Less rigour for high-stakes, contested decisions |
| **Heavyweight templates (Tyree-Akerman)** | Weighted alternatives; strong for big, costly choices | Slower; can deter routine recording |
| **Immutable + supersede** | Clean audit trail; history preserved | More records; readers must trace chains |
| **Living document (dated amendments)** | Single current source of truth; easy to maintain | Weaker audit story; risk of quiet edits |
| **In-repo Markdown** | Versioned, reviewable, next to code | Less friendly to non-developers |
| **Wiki / docs tool** | Accessible to all roles | History and review weaker; drifts from code |

The core tension is **rigour versus adoption**. The most rigorous system that no one uses records nothing. The lightest system that everyone uses compounds in value. Default to lightweight, and reserve heavier process for the few decisions that are expensive and hard to reverse.

## Questions to discuss with your team

1. **How will the right decision record reach a developer at the moment they touch the code it governs, rather than sitting in a folder no one opens?** A write-only log records reasoning that never changes behaviour, which is the most common way decision records fail: they exist, and no one reads them when it matters. The competing consideration is effort, because surfacing records automatically (attaching them to a pull request when someone edits the governed code) takes tooling investment that a wiki or docs folder does not. Bring evidence to the discussion: when someone recently reversed or relitigated a settled question, was the relevant record discoverable at that moment, or buried? For a large organization running dozens of teams, discoverability is what turns one team's hard-won reasoning into a reusable asset instead of a private archive. Decide whether to store records in version control next to the code and wire them into the pull-request flow, so the record appears where the work happens.

2. **Who is the accountable maintainer for each record, and what stops your log from decaying into confident misinformation?** A decision log's dangerous failure mode is not an empty folder, it is a folder full of records whose costs, vendor capabilities, and constraints silently went stale years ago. Every record needs an accountable owner who reviews it on a cadence (at least annually) and drives superseding or sunsetting, or the log rots into folklore people cite selectively and trust little. Bring evidence: how many of your records are undated, how many describe a vendor or price that has since changed, and when each was last reviewed. In government and regulated settings this runs sharper, because an immutable, superseded chain is exactly what auditors and successor contractors rely on for a traceable rationale. Decide your lifecycle explicitly, timestamp individual claims that drift, and assign maintainers, so the log stays a living asset rather than a graveyard.

3. **Should you standardize on one template across all teams, and how much rigour do your highest-stakes decisions actually need?** Comparability is a real benefit: when every team uses the same shape (Nygard, MADR, or similar), a new team can find three prior records and adopt the reasoning in an afternoon instead of a month of debate. The core tension is rigour versus adoption, because the heaviest template that no one uses records nothing, while the lightest one that everyone uses compounds in value. Bring evidence: are records actually getting written, and separately, have any big, contested, expensive decisions been under-analysed because the lightweight form skipped weighing alternatives? For enterprises coordinating overlapping choices across teams, a shared template plus a searchable index prevents divergent, incompatible decisions. Default to lightweight for the common case, and agree in advance which one-way-door decisions warrant a heavier form with weighted alternatives.

4. **What actually justifies raising a decision record, and who has the authority to say a choice does not need one?** Set the bar too high and the reasoning behind consequential choices evaporates; set it too low and the log fills with trivia that buries the records people genuinely need. For a large organization, an unclear threshold means each team improvises its own, so coverage becomes uneven and no one can trust that a missing record signals an unimportant decision. Bring evidence to the discussion: a handful of recent decisions that were recorded but need not have been, and painful ones that went unrecorded and later cost you a rediscovery. Agree a plain test, such as recording whenever a future developer will need the *why* and skipping low-risk, self-contained, or already-documented choices. In regulated and government settings the calculus shifts, because an audit mandate may require a record for every architecturally significant requirement whether or not the team judges it worth writing, so name which decisions are non-negotiable up front.

5. **Are your records genuine reasoning captured at the moment of decision, or paperwork written afterward to satisfy a mandate?** A record produced after the fact to close a ticket tends to launder the chosen option and quietly omit the alternatives that were actually weighed, which is precisely the information a future reader needs most. The competing pressure is real: writing the *why* before or during a decision feels slower than shipping, and admitting the rejected paths in writing takes psychological safety that some teams lack. Bring a sample of recent records to the table and ask honestly whether the context and rejected alternatives read as real deliberation or as retrofitted justification. For a large team, hollow records are worse than none, because they teach people that the log cannot be trusted. In enterprise and government audit this distinction is sharp: oversight bodies and successor contractors depend on a rationale that reflects what was truly considered, and a record that reads as theatre undermines the assurance the log exists to provide.

6. **Which of your highest-stakes decisions can you assure with an automated fitness function, rather than trusting that periodic manual review will catch a violation?** A decision record documents a choice, but only an automated check run in continuous integration keeps that choice from eroding silently as dozens of developers touch the code over years. The trade-off is investment, because writing and maintaining fitness functions (with tools such as ArchUnit) costs engineering time, and many decisions, especially process or vendor choices, are not mechanically testable at all. Bring evidence: which boundary decisions (module dependencies, event emission, data-access rules) have been quietly violated and caught only late in review or in production. For an enterprise running many teams, fitness functions turn governance from a central bottleneck into continuous enforcement that scales without slowing everyone down. In regulated and government contexts, an automated, always-on check is far stronger audit evidence than a signature on a review, because it proves the decision still holds today rather than that someone once approved it.

## Sector lens

**Startup.** Keep it to the habit and nothing else: a `decisions/` folder in your main repo, and a two-section note (context and choice) whenever you make a call your future self will question. Skip lifecycle, roles, and approvers entirely, because process you cannot sustain is process you will abandon. The single record that spares your first hire from asking why the system is built this way already pays for the whole practice.

**Small business.** With no dedicated architect and little time, put records wherever your team already works, whether a wiki, a shared doc, or the repo, rather than buying a dedicated tool. The habit matters far more than the tooling, so lower the barrier: name the directory `decisions` rather than `adr`, and capture vendor and buy-versus-build choices in the same breath as technical ones. When you lean on outside contractors, a short dated record of why you picked a vendor or a platform is cheap insurance against being locked into a choice no one can later explain.

**Enterprise.** The work is coordination across many teams: standardize on one template, publish a searchable cross-team index, and back key boundary decisions with fitness functions so violations fail the build rather than waiting for review. Assign an accountable maintainer to each record with a review cadence, so the log stays a living asset instead of decaying into folklore. Done well, one team's reasoning on a hard choice becomes an asset the next team adopts in an afternoon instead of relitigating.

**Government.** Procurement rules, transparency, and public accountability make decision records close to mandatory. Require an immutable, superseded record for every architecturally significant requirement, each linking the choice to the mandate or compliance control it satisfies, so oversight bodies find a traceable rationale rather than a reconstruction. Because public systems span multi-year, multi-vendor lifespans, a well-kept log is often what lets a successor contractor understand why the system is shaped as it is and continue the work without relitigating settled ground.

## Examples

**Startup.** A five-person startup adds a plain `decisions/` folder to its main repo, with a two-section note (context and choice) whenever someone makes a call their future selves will question. There is no lifecycle, no roles, and no approvers: just the habit of writing the *why* next to the code. When their first hire joins six months later, she reads the whole folder in an hour and stops asking "why is it built this way?" The lightweight log costs minutes per entry and spares them the rediscovery tax that bites long before a team grows large.

**Enterprise.** A retailer with 30 engineering teams standardizes on MADR-format records in each repo, plus a searchable central index. When a new team faces "[monorepo](https://en.wikipedia.org/wiki/Monorepo) vs. multirepo," they find three prior records with context and consequences, and adopt the reasoning in an afternoon instead of a month of debate. Key boundary decisions (service ownership, data-access rules) are backed by ArchUnit fitness functions, so violations fail the build rather than getting caught in review. That is governance that scales without a central bottleneck.

**Government.** An agency modernizing a benefits system requires an ADR for every architecturally significant requirement, each linking the decision to the mandate or compliance control it satisfies (accessibility, data residency, auditability). Records are immutable and superseded, producing a traceable log that satisfies oversight review. Crucially, it also lets a successor contractor understand *why* the system is shaped as it is, preserving continuity across the multi-year, multi-vendor lifespans typical of public programmes (chapters 4.6, 10.4).

## Business case: motivations, ROI, and TCO

A decision record costs minutes to write and a few more to review. The return is avoided *re-decision* cost and avoided *wrong-reversal* cost, both of which are large and recurring on long-lived systems. Every time a team relitigates a settled question, or reverses a sound choice because no one remembered the constraint behind it, they pay in senior-engineer time and often in an incident. A decision log converts that recurring tax into a one-time write.

On **total cost of ownership**, decision records are among the highest-leverage documentation you can keep, because they target the single most turnover-sensitive asset: rationale. Onboarding is faster (new hires read the *why*, not just the code). Modernization is safer (chapter 3.6: you can tell essential decisions from incidental ones). Audits are cheaper (the evidence already exists). The cost of *not* keeping them is invisible on any dashboard, and it compounds silently with every departure. To make the case to leadership, point to a recent expensive rediscovery, or a reversed decision that caused an incident, and note that the fix costs almost nothing to institute.

## Anti-patterns and pitfalls

- **Recording *what* without *why*:** omitting context and rejected alternatives, the whole point.
- **After-the-fact paperwork:** records written to satisfy a mandate, not to think; they read as hollow and no one trusts them.
- **Multi-decision mega-documents:** one giant page no one can navigate or supersede cleanly.
- **Undated claims:** costs and constraints that were true once, presented as timeless.
- **Silent edits:** changing a decision's history with no dated note, destroying the audit trail.
- **Write-only logs:** records created and never surfaced at the moment they're relevant, so they don't influence behaviour.
- **Abbreviation gatekeeping:** insisting on "ADR" and "architecture" and thereby discouraging contribution.
- **No lifecycle:** records that never get reviewed, superseded, or sunset, decaying into misinformation.

## Maturity model

- **Level 1 (Initiate):** Decisions live in people's heads, chat threads, and commit messages; capture is reactive and ad hoc, and rationale is routinely lost with staff turnover.
- **Level 2 (Develop):** Some teams keep records, in varied formats and templates, whenever an individual remembers to; the practice is inconsistent across teams, with no shared log, naming, or process.
- **Level 3 (Standardize):** A single template, in-repo storage, and a defined lifecycle and governance (raise/skip criteria, roles, review cadence) are documented and applied consistently org-wide; records are reviewed and superseded rather than silently edited.
- **Level 4 (Manage):** The decision log is measured against baselines: coverage (the share of architecturally significant decisions that carry a record), freshness (the share of records reviewed within their cadence, plus the count of undated or stale claims), and discoverability (how often a relevant record actually reached the developer who changed the governed code). Accountable maintainers act on these metrics, superseding stale records and closing coverage gaps on evidence rather than anecdote.
- **Level 5 (Orchestrate):** A searchable cross-team decision log is integrated into daily work: relevant records surface automatically on the changes they govern, key decisions are assured by fitness functions in continuous integration, and the log feeds onboarding, modernization, and audit as a living asset. The organization continuously improves the practice itself, retiring, superseding, and re-scoping records as the system and its constraints shift, and rebalancing where it invests rigour as the portfolio of decisions grows.

## Ideas for discussion

1. What was the last decision your team reversed or relitigated because no one remembered the original reasoning?
2. Would renaming your `adr/` directory to `decisions/` change who contributes and what gets recorded?
3. Which of your critical decisions could be assured by an automated fitness function today?
4. Immutable-and-supersede or living-document: which fits your audit obligations and your culture, and why?
5. How would a new hire (or a successor contractor) currently discover *why* your system is shaped the way it is?
6. What justifies raising a decision record on your team, and what justifies *not* raising one?

## Key takeaways

- A decision record captures one important decision with its **context and consequences**: the *why*, not just the *what*.
- Keep records **specific, timestamped, and lightweight**; standardize on one template (Nygard, MADR, or similar).
- Store them **in version control next to the code**; consider naming them "decisions" to broaden contribution.
- Define a **lifecycle and governance** (raise/skip criteria, roles, review cadence); reserve heavy process for one-way-door decisions.
- Make decisions **discoverable** at the moment of change and, where possible, **testable** via fitness functions.
- The ROI is avoided rediscovery and wrong-reversal cost; the TCO case is strongest where turnover, modernization, and audit matter most. See chapter 1.5 (decision-making and governance) and chapter 3.1 (architecture fundamentals).

## References and further reading

- Michael Nygard, "Documenting Architecture Decisions" (2011): the foundational lightweight ADR.
- MADR: Markdown Any Decision Records project (adr.github.io/madr).
- Jeff Tyree and Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" and "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: templates, examples, and teamwork guidance (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (fitness functions).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" and "Architecturally significant requirements."
