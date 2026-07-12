# 1.5 Decision-making and governance

## Overview and motivation

Every software system is the sum of thousands of decisions: which [database](https://en.wikipedia.org/wiki/Database), which architecture, which library, whether to build or buy, when to take on debt and when to pay it down. Governance is how you make these decisions well and consistently, involve the right people without creating bottlenecks, and preserve the reasoning so future teams are not doomed to relearn it. In a small team, decisions happen in conversation and live in shared memory. At scale, that memory evaporates. People leave, teams reorganize, and the "why" behind a critical choice is lost, leaving successors to either cargo-cult it or rip it out blindly. Good governance is the machinery that makes decisions visible, deliberate, and durable across a large and changing organization.

The central challenge for large teams is balancing autonomy against alignment. Push all decisions up to a central board, and you get consistency, but at the cost of crippling bottlenecks and disempowered teams. Push all decisions down, and you get speed, but at the cost of chaos: incompatible technologies, duplicated effort, and repeated mistakes. The mature answer is neither centralization nor anarchy. It is a layered model. Teams decide most things locally within a well-marked "paved road," while a lightweight, transparent process governs the genuinely cross-cutting and hard-to-reverse choices. The goal is to make good decisions the easy default, and to spend scarce governance attention only where it truly matters.

Enterprises and government carry heightened stakes. They must satisfy auditors, regulators, and oversight bodies who demand documented, defensible decisions. They work on long time horizons, where a poor architectural choice or an unmanaged pile of [technical debt](https://en.wikipedia.org/wiki/Technical_debt) can burden them for a decade. And their procurement and compliance obligations make build-versus-buy decisions especially consequential and hard to reverse. For these organizations, disciplined, well-recorded decision-making is not bureaucracy for its own sake. It is risk management, institutional memory, and the foundation of accountability.

## Key principles

- Record decisions and their reasoning; a decision without a rationale is a liability.
- Push decisions to the lowest level that has the context, within clear guardrails.
- Match the weight of the process to the weight and reversibility of the decision.
- Distinguish reversible ("two-way door") from irreversible ("one-way door") decisions and govern them differently.
- Prefer paved roads and defaults over case-by-case approvals.
- Treat technical debt as a managed portfolio, not a moral failing to hide.
- Make governance transparent; hidden decision-making breeds distrust and rework.

## Recommendations

### Adopt Architecture Decision Records and a right-sized RFC process

An [Architecture Decision Record](https://en.wikipedia.org/wiki/Architectural_decision) (ADR) is a short, immutable document capturing one significant decision: its context, the options considered, the choice made, and the consequences. Store ADRs in version control alongside the code, so the reasoning travels with the system. For decisions that need input before they are made, use a lightweight [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (request for comments) process: circulate a proposal, invite comment for a bounded period, then decide and record. Keep both lightweight. The value is in the thinking and the durable record, not in elaborate templates. Together, ADRs and RFCs turn tacit, forgotten reasoning into a searchable institutional memory.

### Govern through paved roads, not gatekeepers

Rather than reviewing every decision one by one, invest in a "paved road": a set of blessed, well-supported defaults, approved languages, frameworks, deployment pipelines, and patterns, that teams can adopt with little friction and plenty of support. Teams that stay on the paved road need little governance, because the safe, compliant choice is also the easy one. Teams with a genuine reason to leave it can, but they take on the extra responsibility and a lightweight review. This "golden path" model scales far better than a central board approving everything, because it shifts governance from case-by-case gatekeeping to well-designed defaults.

### Use architecture review boards sparingly and transparently

An architecture review board, or its equivalent, has a legitimate role for the largest, most cross-cutting, or most irreversible decisions, and for setting the standards that define the paved road. Keep its scope narrow, its criteria published, and its process fast and advisory, not a mandatory bottleneck for routine work. The board's job is to steward coherence and share knowledge, not to approve every choice. When a board becomes a queue that every project must wait in, it has failed. Delegate aggressively, and reserve central review for the few decisions that genuinely warrant it.

### Make build-versus-buy-versus-adopt a deliberate analysis

For any significant capability, weigh three paths: build it in-house, buy a commercial product, or adopt an [open-source](https://en.wikipedia.org/wiki/Open-source_software) solution. Build when the capability is a genuine differentiator and core to your mission. Buy or adopt the undifferentiated capabilities that others do better. Count [total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO), not just up-front price. Buying incurs licensing, integration, and [lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in) costs. Building incurs perpetual maintenance and staffing. Adopting open source incurs support and security-tracking obligations. Record the decision and its assumptions as an ADR, so you can revisit it when circumstances change.

### Manage technical debt as a portfolio

Technical debt is not inherently bad. Sometimes taking it on to ship sooner is the right call. What is bad is unmanaged, invisible, forgotten debt. Keep an explicit inventory of significant debt. For each item, note the cost it imposes (the ongoing "interest") and the cost to fix it. Then manage it like a financial portfolio. Pay down high-interest debt that slows the team every day. Tolerate low-interest debt in stable corners. Make debt decisions consciously rather than by accident. Set aside a standing fraction of capacity to pay down debt, so it never compounds into a crisis.

### Distinguish reversible from irreversible decisions

Not all decisions deserve equal deliberation. Reversible "two-way door" decisions are easily undone, so make them fast and local, by the team, with a bias toward action. Agonizing over them wastes time and slows learning. Irreversible or costly-to-reverse "one-way door" decisions, a public [API](https://en.wikipedia.org/wiki/API) contract, a data model at scale, a multi-year vendor commitment, deserve slow, careful, senior deliberation and a recorded rationale. Classifying decisions this way is one of the highest-leverage governance habits you have. It aims scarce scrutiny where it pays off, and unblocks everything else.

## Trade-offs: pros and cons

| Governance approach | Pros | Cons |
| --- | --- | --- |
| Central review board for all | Maximum consistency and oversight | Severe bottleneck; disempowers teams; slow |
| Paved road with local autonomy | Scales, fast, safe default, empowers teams | Requires up-front platform investment; some drift off-road |
| Full team autonomy, no governance | Fast, high ownership | Fragmentation, duplication, repeated mistakes |
| ADRs / RFCs | Durable memory, better decisions, transparency | Writing overhead; ignored if not maintained |

| Sourcing choice | Pros | Cons |
| --- | --- | --- |
| Build | Full control, fits exactly, can differentiate | Perpetual maintenance and staffing cost |
| Buy | Fast, supported, someone else maintains it | Licensing cost, lock-in, imperfect fit |
| Adopt (open source) | No licence fee, inspectable, community | Support and security burden falls on you |

The unifying trade-off is control versus speed, and central consistency versus local autonomy. Every governance choice sits on this spectrum. The recommended posture, paved roads plus reversibility-based delegation, deliberately buys most of the speed of autonomy while keeping the consistency that matters. It does this by making the aligned choice the easy one, and reserving heavyweight process for the rare irreversible decision.

## Questions to discuss with your team

1. **Who decides whether a given decision is a one-way door, and how will you catch misclassifications in both directions?** Classifying decisions by reversibility is one of the highest-leverage governance habits, and its value collapses if you label things wrong: treat a reversible choice as irreversible and you drown it in deliberation, treat an irreversible one as reversible and you ship a data model or public API contract you cannot cheaply undo. The competing risk is that the person closest to the work may be biased toward speed, while a central board may be biased toward caution. Bring concrete examples to the discussion: what would it actually cost, in time and money, to reverse each decision, and who bears that cost. In enterprise and government settings, procurement commitments and data at scale turn many choices into one-way doors that looked reversible up front. Agree on who classifies, and build a habit of a quick second opinion on anything near the boundary, so scarce scrutiny lands where reversal is genuinely expensive.

2. **Who owns, funds, and staffs the paved road, and what stops it from decaying into a gatekeeper?** A paved road only works if the blessed defaults are genuinely well supported and easier than the alternatives, and that requires sustained investment that is easy to underfund. The trade-off is stark: an under-resourced paved road becomes a set of mandates without support, which is exactly the gatekeeping the model was meant to replace, and teams then route around it. Bring evidence of the road's health: adoption rates, how current the approved tools are, how fast the platform team responds, and how often teams file to go off-road. For large and regulated organizations, the paved road is also how the compliant choice becomes the easy one, so its funding is a compliance investment, not just a convenience. Decide on a clear owner and a standing budget, and measure whether teams choose the road because it is genuinely the easiest path.

3. **Where are teams routing around your governance, and what is that shadow IT telling you?** Teams evade the sanctioned path when it is more painful than the workaround, so widespread shadow IT is less a discipline problem than a design verdict on your governance. The competing considerations are real: some evasion is reckless, and much of it is rational avoidance of a review board that has become a multi-week queue. Bring the evidence: which approvals get skipped, which unofficial tools have quietly spread, and how long the official path actually takes. In enterprise and government contexts the stakes run higher, because unsanctioned tools can breach audit, security, and procurement obligations that carry legal weight. If the pattern shows people routing around a bottleneck, the fix is to speed and widen the paved road and shrink the board's scope to the few cross-cutting, irreversible decisions, not to add more approvals.

4. **How much of our delivery capacity actually goes to paying down technical debt, and can we name the highest-interest items it should target first?** Technical debt behaves like compounding interest, a quiet tax on every future change, and a large organization can carry it for years before anyone notices the system has become slow and brittle to modify. The competing pressure is blunt: every hour spent on debt is an hour not spent on features leadership can see, so paydown is the first thing cut when a deadline tightens. Bring real evidence to the discussion, a written inventory of significant debt, an honest estimate of the ongoing cost each item imposes and the cost to fix it, and the actual fraction of recent capacity that went to paydown versus new work. For enterprises and government bodies on decade-long time horizons, unmanaged debt eventually forces a costly rewrite or an audit finding, so treat a standing paydown allocation as risk management and decide who guards it when schedules slip.

5. **When we need the reasoning behind a decision made two years ago, can we actually find it, and is anyone keeping that record alive?** The whole value of an Architecture Decision Record is that reasoning outlives the people who made it, and that value collapses if ADRs are written once, never searched, and quietly drift out of date. The tension is between the writing discipline it takes to capture context, options, and consequences at the moment of decision, and the daily pressure to just ship and move on. Bring concrete tests to the discussion: pick three important recent decisions and see whether anyone can locate the recorded rationale in minutes, and check whether superseded ADRs are marked as such rather than silently contradicting current practice. In enterprise and government settings, that searchable record is exactly the defensible evidence auditors and oversight bodies demand, so decide where ADRs live, who reviews them, and what makes a decision significant enough to record.

6. **When did we last reopen a major build-versus-buy decision against its original assumptions, and would we even notice when those assumptions expire?** Sourcing choices are among the most expensive and hard-to-reverse decisions you make, and the assumptions behind them (a vendor's pricing, your own staffing, the maturity of an open-source option) quietly go stale while the decision stays frozen in place. The competing considerations weigh the sunk cost and disruption of switching against the mounting cost of lock-in, an imperfect fit, or a maintenance burden you no longer want. Bring the original ADR and its stated assumptions, a current total-cost-of-ownership estimate for each path including licensing, integration, staffing, and exit cost, and any signal, a price change or a support downgrade, that a premise has shifted. For government and regulated buyers, procurement rules and multi-year contracts make these one-way doors especially binding, so agree in advance on the triggers and the cadence that will force a deliberate re-decision rather than a blind renewal.

## Sector lens

**Startup.** Govern almost nothing and lean hard on speed: for reversible two-way-door choices, decide at the desk and move on. Reserve your one governance habit for the handful of one-way doors, a core data model or a foundational vendor, and capture each in a single paragraph so a future teammate is not relitigating it from scratch. Skip review boards and paved roads entirely, because at your size they are overhead you cannot afford and the whole team already shares the context.

**Small business.** With no architect on staff, make build-versus-buy your central governance question and answer it on total cost of ownership rather than preference. Default to buying or adopting well-supported tools for anything that is not your core differentiator, because perpetual maintenance is the cost you can least afford to carry. Keep one lightweight decision log so the reasoning behind your few consequential choices survives a key person leaving.

**Enterprise.** Your problem is balancing autonomy against alignment across many teams, so invest in a funded paved road and reserve a narrow, fast architecture review board for the genuinely cross-cutting and irreversible decisions. Standardize ADRs so reasoning becomes searchable institutional memory, and manage technical debt and sourcing choices as portfolios with standing budgets. Measure whether teams choose the road because it is easiest, and shrink any board that has decayed into a queue.

**Government.** Documented, defensible decisions are not optional here: auditors and oversight bodies expect to see the reasoning, the options weighed, and the assumptions behind every consequential choice. Run build-versus-buy as a recorded total-cost-of-ownership analysis, honour procurement rules that constrain sole-source lock-in, and keep ADRs as the audit-ready evidence trail. Treat long time horizons seriously, because a data model or vendor commitment made today may bind the organization for a decade, so classify it as a one-way door and deliberate accordingly.

## Examples

**Startup.** A four-person startup makes most decisions in minutes across a shared desk, and for reversible two-way-door choices that speed is a real advantage, so they resist any governance overhead. But when they pick a database and a data model that will be painful to change later (a one-way door), they pause to write a single-paragraph note: the options, the choice, and the assumptions behind it. A year later, hitting scaling limits, that one note saves them from relitigating the question from scratch. They govern almost nothing, and reserve their one lightweight habit for the few decisions that are genuinely costly to reverse.

**Enterprise.** A large enterprise's platform teams were paralysed by an architecture review board that had to approve every technology choice, creating multi-week queues. The enterprise restructured governance around a paved road: a curated catalogue of approved, fully supported languages, data stores, and pipelines that teams could adopt instantly. ADRs recorded any decision to deviate, and a fast, advisory review handled only off-road choices. The board's scope shrank to standards-setting and the handful of truly cross-cutting decisions. Delivery accelerated sharply. Consistency actually improved, because the easy path was now the compliant one. And the ADR archive gave the organization a searchable record of why things were built as they were.

**Government.** A government department faced a major build-versus-buy decision for a case-management platform under strict procurement and audit rules. Rather than deciding by preference, it ran a documented total-cost-of-ownership analysis across three options: building custom, buying a commercial product, and adopting an open-source base. It weighed licensing, integration, long-term maintenance, staffing, and lock-in, and recorded the decision and its assumptions as an ADR. Years later, when a vendor's terms changed, the department revisited that ADR, found its original assumptions no longer held, and re-decided with full knowledge of the prior reasoning, avoiding a blind and costly migration. The recorded rationale was also exactly the defensible evidence auditors required.

## Business case: motivations, ROI, and TCO

Decisions are the highest-leverage and lowest-visibility cost in software. A single poor, irreversible architectural or sourcing choice can impose years of drag or a nine-figure remediation. Governing it well, a few hours of deliberation and a written record, costs almost nothing by comparison. The return on ADRs and reversibility-based delegation comes from two sources: avoiding expensive mistakes on the one-way-door decisions, and avoiding wasted deliberation and rework on everything else. Recorded rationale also slashes the recurring cost of re-litigating settled questions and of teams reverse-engineering the intent behind inherited systems.

Technical debt makes the TCO argument concrete. Unmanaged debt behaves exactly like compounding interest: a growing tax on every future change, until the system becomes effectively unmaintainable and demands a costly rewrite. Managing debt as a portfolio, with a standing capacity allocation to pay down the high-interest items, is far cheaper than the eventual crisis. Good governance is cheap to adopt, mostly the discipline of writing decisions down and the up-front investment in a paved road. Skipping it is expensive: you pay in avoidable rewrites, lock-in surprises, audit failures, and lost institutional memory. To persuade leadership, frame governance in their language: risk reduction, avoided rework, faster delivery via the paved road, and audit-ready defensibility. Show that the goal is not more process but better-aimed process, heavy scrutiny only where reversal is costly, and frictionless speed everywhere else.

## Anti-patterns and pitfalls

- Undocumented decisions: reasoning lost the moment the people who made it leave.
- Approval-board bottleneck: a central body every project must queue behind.
- One-size process: forcing trivial reversible decisions through heavyweight review.
- Analysis paralysis: agonizing over easily reversible two-way-door decisions.
- [Shadow IT](https://en.wikipedia.org/wiki/Shadow_IT): teams evading governance entirely because the sanctioned path is too painful.
- Invisible technical debt: debt never inventoried, never paid down, quietly compounding.
- Build-everything or buy-everything reflexes: sourcing by habit rather than TCO analysis.
- Governance theatre: documents and boards that exist for appearance but do not shape decisions.

## Maturity model

- Level 1 (Initiate): Decisions are ad hoc and unrecorded; governance is either absent or a blanket bottleneck; technical debt is invisible and the reasoning behind choices evaporates when people leave.
- Level 2 (Develop): Some decisions get documented and some review exists, but the practice is inconsistent across teams and the process is often mismatched to the weight and reversibility of the decision.
- Level 3 (Standardize): ADRs, a paved road, reversibility-based delegation, and a debt inventory are documented and enforced org-wide, so the compliant choice is the easy default and reasoning is searchable.
- Level 4 (Manage): Governance is measured against baselines: paved-road adoption, ADR coverage, decision cycle time, debt as a share of capacity, and off-road exception rates are tracked, and decisions to pay down debt or revisit sourcing are triggered by that evidence rather than by crisis.
- Level 5 (Orchestrate): Governance is continuously tuned and integrated with delivery and risk planning; scrutiny is precisely aimed at irreversible decisions; debt and sourcing choices are actively rebalanced as portfolios and re-decided on evidence as circumstances shift.

## Ideas for discussion

- For our most important recent decisions, can we find the recorded reasoning behind them?
- Where is our governance a bottleneck, and where is it absent when it is needed?
- Which of our current decisions are one-way doors, and are we treating them as such?
- How much of our capacity goes to paying down technical debt, and is it enough?
- Do our teams follow the paved road because it is genuinely the easiest path, or route around it?
- When did we last revisit a major build-versus-buy decision against its original assumptions?

## Key takeaways

- Record significant decisions and their rationale with ADRs; make reasoning durable.
- Govern through paved roads and defaults, not case-by-case gatekeeping.
- Match process weight to decision weight and reversibility; delegate two-way doors, deliberate on one-way doors.
- Analyse build-versus-buy-versus-adopt on total cost of ownership, and record the assumptions.
- Manage technical debt as an explicit portfolio with a standing paydown allocation.
- Keep governance transparent and lightweight; aim scarce scrutiny where reversal is costly.

## References and further reading

- Michael Nygard, "Documenting Architecture Decisions" (the original ADR pattern)
- Gregor Hohpe, "The Software Architect Elevator" and "37 Things One Architect Knows"
- Amazon shareholder letters on Type 1 vs Type 2 (one-way vs two-way door) decisions
- Ward Cunningham, the original "technical debt" metaphor
- Martin Fowler, writings on technical debt and evolutionary architecture
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (loosely coupled architecture and autonomy)
- ISO/IEC/IEEE 42010 on architecture description
