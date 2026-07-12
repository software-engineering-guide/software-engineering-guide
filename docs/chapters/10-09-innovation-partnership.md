# 10.9 Innovation partnership

## Overview and motivation

An innovation partnership is a deliberate collaboration between your organization and an external party (a startup, vendor, university, research lab, [consortium](https://en.wikipedia.org/wiki/Consortium), or public agency) to develop capability that neither of you would build as effectively alone. It ranges from lightweight arrangements (pilots, joint research, open-source collaboration) to deep ones (co-development, [joint ventures](https://en.wikipedia.org/wiki/Joint_venture), [corporate venture capital](https://en.wikipedia.org/wiki/Corporate_venture_capital), and the formal "innovation partnership" procurement procedures now written into public law). The common thread is sharing risk, knowledge, and reward to reach an innovation faster or more cheaply than internal effort or an off-the-shelf purchase would allow. This chapter sits in the management part because deciding when and how to partner for innovation is a portfolio and procurement decision (chapters 10.1, 10.3) as much as a technical one.

Here is the motivation. No large organization can build everything, so the "build vs. buy" question (chapter 6.1) has a crucial third option: *partner*. When a capability is too novel to buy off the shelf, too far from the core to build well internally, or too risky to fund alone, a partnership can turn an uncertain bet into a shared, staged one. Partnerships also import talent, technology, and fresh thinking that established organizations struggle to grow on their own, the classic antidote to the incumbent's innovation problem. Done well, they extend your reach and speed. Done badly, they produce "pilot purgatory" (pilots that succeed but never reach production), leaked [intellectual property](https://en.wikipedia.org/wiki/Intellectual_property) (IP), and dependence on a partner whose incentives diverge from yours.

For enterprise and government the stakes and mechanisms are distinctive. Enterprises use corporate venture arms, accelerators, and co-development deals to stay close to emerging technology. Governments have built formal instruments for the same purpose. The European Union's *innovation partnership* procurement procedure lets a public buyer develop and then purchase a not-yet-existing solution. The U.S. [Small Business Innovation Research](https://en.wikipedia.org/wiki/Small_Business_Innovation_Research) (SBIR) programme and challenge/prize mechanisms fund external innovation for public missions. "GovTech" programmes partner agencies with startups. These exist precisely because normal procurement (chapter 10.3) buys what already exists, while public missions increasingly need what does not yet exist.

## Key principles

- **Partner when you can neither buy nor build well alone.** It is the third option, chosen deliberately.
- **Align incentives first.** A partnership only works if both sides win from the same outcome.
- **Stage the risk.** Fund in increments tied to validated milestones, not one big commitment.
- **Settle IP, data, and exit up front.** The hardest conversations are cheapest before signing.
- **Protect the core; open the edges.** Share enough to collaborate, not enough to hollow yourself out.
- **Move pilots to production deliberately.** A pilot that cannot scale is a demo, not a partnership.
- **Manage the relationship, not just the contract.** Trust and governance carry it, not the paperwork.

## Recommendations

### Choose the partnership model to fit the goal

Different goals call for different structures; pick the lightest one that achieves it:

- **Pilots and [proofs of concept](https://en.wikipedia.org/wiki/Proof_of_concept):** cheap, time-boxed tests of a startup's or vendor's technology against a real problem.
- **Co-development / joint development agreements:** shared build of a specific capability, with defined contributions and IP split.
- **Research partnerships:** with universities or labs, for capability that is still pre-product.
- **Corporate venture capital (CVC) and accelerators:** equity stakes or cohort programmes to stay close to emerging technology and talent.
- **Consortia and open-source collaboration:** shared investment in non-differentiating infrastructure (chapter 10.3).
- **Public innovation instruments:** EU innovation partnerships, SBIR/STTR, challenges and prizes, and GovTech programmes for missions where the solution must be created.

### Align incentives and govern the relationship

The most common cause of partnership failure is misaligned incentives dressed up in an aligned contract. Before you settle on a structure, ask what each party actually wants (revenue, market access, a reference customer, research output, mission impact) and confirm that the *same* outcome makes both sides win. Then govern the relationship actively: a shared roadmap, regular joint reviews, clear decision rights, and named accountable owners on each side (the ADR, or architecture decision record, and governance disciplines of chapters 1.5–1.6 apply). Partnerships live or die on trust and communication far more than on the contract clauses.

### Settle IP, data, security, and exit before signing

The conversations you most want to defer are exactly the ones to have first: who owns the intellectual property, who can use the data, how security and compliance obligations flow to the partner, and how either side exits. Unresolved IP ownership poisons otherwise successful co-development. Unmanaged data sharing creates privacy and security exposure (chapters 4.5, 4.3). No exit plan creates lock-in. Treat a partner as part of your supply chain for risk and assurance purposes (chapter 10.2), including third-party security review.

### Stage investment and beat pilot purgatory

Fund innovation partnerships the way good investors fund startups: in stages, each tranche released against validated milestones (the discovery discipline of chapter 11.1). This caps your downside on the many bets that will not pan out while preserving upside on the few that do. The specific enterprise trap is *pilot purgatory*: a graveyard of successful pilots that never reach production because no one owns the path to scale, the budget, or the integration work. Design the production path from the start. Name the internal owner who will operationalize a successful pilot, and treat "can this scale into our estate?" as a gating question, not an afterthought.

### Protect the core while opening the edges

Partner most freely on non-differentiating capability and pre-competitive research, and guard your genuine sources of advantage. Share enough context, data, and access for the partner to succeed. But structure the relationship so you are not transferring your core value or becoming dependent on a single external party for something mission-critical (concentration risk, chapter 10.2). The aim is to import innovation at the edges without hollowing out the centre.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| **Partner (co-develop)** | Shared risk; imported talent/tech; faster than build | IP/incentive complexity; coordination cost; dependence |
| **Build internally** | Full control and IP; deep fit | Slow; may lack the talent/novelty; opportunity cost |
| **Buy off the shelf** | Fast, proven, supported | Only buys what exists; commoditized, no edge |
| **Equity / CVC** | Close to emerging tech; upside | Distraction; misaligned horizons; governance load |
| **Public innovation procedures (EU IP, SBIR)** | Legally develop the not-yet-existing; mission fit | Procedural complexity; long cycles; administrative burden |

The defining tension is **openness vs. protection**. Innovation partnerships require sharing knowledge, data, and access, yet the same openness can leak advantage or create dependence. The resolution is deliberate scoping, being generous at the non-differentiating edges and disciplined about the core, plus staged commitment, so trust and value are proven before exposure deepens.

## Questions to discuss with your team

1. **Do we fund innovation partnerships as a staged portfolio with a deliberately high failure rate, or bet big on each one?** Good partnerships behave like venture bets: most fail, a few pay for everything, and the way to survive that math is to fund in tranches released against validated milestones. A single large upfront commitment removes your option to walk away cheaply, which is the main advantage partnering has over building. For an enterprise or agency running several partnerships at once, set an explicit budget that expects most pilots to end and a few to scale. Bring last year's partnership spend, how many bets you funded, and how many reached production. If every partnership was a big-bang commitment with no staging, you are carrying downside you could have capped.

2. **Before signing, have we confirmed both sides win from the same outcome, and who governs the relationship afterward?** The most common cause of partnership failure is misaligned incentives dressed up in an aligned contract. Ask what each party actually wants (revenue, a reference customer, research output, mission impact) and confirm the same result makes both sides succeed. Then decide who governs the relationship after signing: named accountable owners on each side, a shared roadmap, and regular joint reviews, because partnerships live on trust and communication far more than on clauses. Record the decision rights the way you would an architecture decision. Come with the actual incentive of each party written plainly, and if they do not point at the same outcome, fix the structure before you commit.

3. **Do we treat partners as part of our supply chain for security and concentration risk?** A partner with access to your data and systems is a third party, and their weaknesses become yours. Run the same security review and due diligence you apply to any supplier, and settle data rights, security obligations, and exit before work begins, because those are the cheapest conversations before signing and the most poisonous after. Watch for concentration risk: a mission-critical capability locked to a single external partner is a dependency, not a partnership. Bring a map of what each partner can access and what would break if they failed or walked. If any single partner holds something you could not replace, design the exit now.

4. **For each pilot we fund, who owns the path to production, and what integration and budget does scaling actually require?** Pilot purgatory is the signature failure of large-organization innovation: pilots that succeed technically, impress a sponsor, and then die because nobody owned the unglamorous work of scaling them into the estate. The competing pull is real, since naming a production owner and reserving integration budget up front feels premature when most pilots will fail anyway, yet without it even the winners stall. Bring the count of pilots you ran last year, how many reached production, and for the survivors the integration cost and the internal owner by name. For an enterprise, the blocker is usually estate integration and platform fit; for an agency, it is the follow-on procurement and budget line that must exist before the pilot ends, or the successful prototype has nowhere to land.

5. **What exactly are we willing to share, and where is the line that protects our core advantage?** Partnerships only work if you share enough context, data, and access for the partner to succeed, and the same openness can leak the very capability that differentiates you. The tension is genuine: scope too tight and the partner cannot deliver, scope too loose and you hand over your edge or create a dependence you cannot unwind. Bring an explicit inventory of what is non-differentiating and safe to open, what is core and stays protected, and which data sets carry privacy or contractual limits on sharing. In an enterprise this line should map to your concentration-risk and IP strategy; in government, add the transparency and fair-competition obligations that may require you to share more openly with all bidders while still guarding citizen data and avoiding vendor lock-in.

6. **Have we matched each partnership to the lightest model that achieves the goal, including the public innovation instruments available to us?** The structure carries real cost and risk, and teams often default to a heavy vehicle (equity, a joint venture, a multi-year co-development deal) when a time-boxed pilot or research agreement would answer the question more cheaply. Weigh the coordination load, governance burden, and exit difficulty of each model against how much certainty you actually need before committing. Bring the goal stated plainly (revenue, capability, talent access, mission outcome), the shortest structure that could test it, and the exit cost of the structure you are proposing. For a public body, this is also a legal question: instruments such as the EU innovation partnership procedure, SBIR/STTR awards, and challenge prizes exist precisely to let you develop and then buy what does not yet exist, and choosing the right one keeps the procurement lawful, competitive, and auditable.

## Sector lens

**Startup.** Partner to borrow what you cannot afford to build: hardware, domain science, distribution, or a reference customer. Keep every deal time-boxed and cheap to exit, because your scarcest resource is engineering attention and a co-development commitment you cannot staff will sink the company faster than the missing capability would. Settle IP and customer ownership in writing before the first sprint, since giving away your core in an early partnership is a mistake you cannot buy back.

**Small business.** With no corporate venture arm or innovation team, treat partnering as a buy-versus-build shortcut rather than a strategy: find one vendor, lab, or local university willing to run a small paid pilot on a concrete problem. Watch the concentration risk, because a single partner holding a capability you depend on is a bigger threat to a small firm than to a large one. Prefer partners who leave you owning your data and able to walk away without rewriting your operations.

**Enterprise.** The task is portfolio governance across many teams: a shared partnering playbook covering model selection, staged milestone funding, IP and data and exit terms, third-party security review, and a named production owner for every pilot. Standardize the interface and integration layer so a successful pilot has somewhere to land, and manage partnerships as a book of staged options with a deliberately high failure rate rather than a scatter of announcements. Budget the scaling work explicitly, because pilot purgatory is where enterprise innovation money quietly disappears.

**Government.** Procurement rules, transparency, and public accountability shape every partnership. Use the formal instruments built for this (the EU innovation partnership procedure, SBIR/STTR, challenges and prizes) so you can lawfully fund suppliers to develop what does not yet exist, then procure the best at scale. Keep competition fair and the process auditable, insist on IP and data terms that prevent lock-in to a single vendor, and publish enough about the arrangement to satisfy public scrutiny while protecting citizen data.

## Examples

**Startup.** A four-person climate-data startup lacks the sensor hardware and domain science to validate its models alone, so it partners with a university lab for a time-boxed joint research pilot. They settle the terms first: the lab publishes the science, the startup keeps its software and its customer relationships, and each stage of funding depends on hitting a shared, agreed milestone. Because the startup names one founder as the owner of turning any promising result into a shippable feature, the pilot produces a real product increment instead of a paper that gathers dust.

**Enterprise.** A logistics company wants route-optimization capability that no vendor sells and its own team cannot build quickly. It runs a staged co-development partnership with an AI startup: a paid pilot on real (anonymized) data, milestone-gated funding, a clear IP split (the startup keeps its core model; the company owns the integration and its own data), and a named internal owner responsible for scaling a successful pilot into production. Because the production path is designed in from the start, the pilot escapes pilot purgatory and ships. The staged structure caps the loss on the earlier pilots that did not.

**Government.** A transport agency needs a congestion-prediction system that does not yet exist. Rather than buy the wrong thing or attempt to build it in-house, it uses an EU-style innovation partnership procedure (or, in the U.S., an SBIR award) to fund several suppliers to develop competing prototypes, then procures the best at scale, legally purchasing an innovation that had to be created. Public-interest guardrails apply throughout: transparency, fair competition, accessibility, and clear IP and data rights that keep the agency from being locked to one vendor (chapters 10.3, 10.5).

## Business case: motivations, ROI, and TCO

The return on innovation partnerships is **optionality and speed**. For the cost of a staged pilot, you buy a real option on a capability you could not have bought or built as fast, and you can walk away cheaply if the bet fails. Compare that with building, which commits full cost up front against uncertain internal capability, and with buying, which cannot acquire what does not yet exist. Partnering often has the best risk-adjusted return when the capability is novel, non-core, or too risky to fund alone. The imported talent and technology also compound: organizations that partner well stay closer to the frontier than those that only build or buy.

On **total cost of ownership**, the visible costs are coordination, governance, and the many bets that do not pay off. The hidden costs are IP leakage, security exposure, and dependence when partnerships are structured carelessly. Staging investment and settling IP, data, and exit up front are what keep TCO in check. The largest silent cost is *pilot purgatory*, real money spent on pilots that never scale, which is why the production path and an accountable internal owner belong in the business case from day one. To make the case to leadership, frame partnerships as a portfolio of cheap, staged options on capability, explicitly budgeted for a high failure rate and a few outsized wins, with a hard rule: no pilot is funded without a named owner for scaling it.

## Anti-patterns and pitfalls

- **Pilot purgatory:** a graveyard of successful pilots that never reach production.
- **Innovation theatre:** partnerships announced for optics, with no real integration intent.
- **Unsettled IP:** deferring ownership questions until they poison a working collaboration.
- **Incentive mismatch:** a signed contract masking parties that want different outcomes.
- **Core leakage:** sharing genuinely differentiating capability or data at the edges.
- **Single-partner dependence:** mission-critical capability locked to one external party.
- **Big-bang commitment:** funding a large partnership in one tranche instead of staging by milestone.
- **Contract over relationship:** trusting clauses to do the work that governance and trust must.

## Maturity model

- **Level 1, Initiate.** Innovation is build-or-buy only; external partnerships are ad hoc, personality-driven, and reactive; IP, incentives, and scaling are figured out case by case, and pilots rarely reach production.
- **Level 2, Develop.** Some pilots, research links, and vendor collaborations run, and a few people have learned to stage funding and settle terms, but the practice is inconsistent from team to team; pilot purgatory is common and depends on who is driving the deal.
- **Level 3, Standardize.** A deliberate partnering playbook is documented and enforced org-wide: model selection, staged milestone funding, IP/data/exit terms, named production owners, and third-party security review are applied consistently to every partnership.
- **Level 4, Manage.** Partnerships are measured against baselines: pilot-to-production conversion rate, cost and time per staged bet, portfolio failure rate versus a few outsized wins, exit and concentration exposure, and IP realized. Milestone gates are enforced on that evidence, and go/no-go and scaling decisions are driven by the metrics rather than by advocacy.
- **Level 5, Orchestrate.** Partnering is integrated with portfolio, procurement, and risk strategy and continuously improved; the organization is a partner of choice that adaptively opens the right edges, retires and re-scopes partnerships as the frontier shifts, and reliably converts external innovation into shipped capability.

## Ideas for discussion

1. For your last "build vs. buy" decision, was "partner" genuinely on the table?
2. How many of your pilots reached production last year, and who owned the path to scale?
3. Do your partnership contracts settle IP, data rights, and exit before work begins?
4. Where might you be sharing core advantage at the edges without realizing it?
5. Are any mission-critical capabilities dependent on a single external partner?
6. In a public-sector context, which innovation instruments (EU partnerships, SBIR, challenges) fit your mission?

## Key takeaways

- Innovation partnership is the deliberate third option beyond build and buy: collaborating to share risk, knowledge, and reward.
- **Choose the model to fit the goal**, from pilots to co-development to public innovation procedures (EU innovation partnerships, SBIR).
- **Align incentives, settle IP/data/exit up front**, and govern the relationship, not just the contract.
- **Stage investment** and design the production path in to escape **pilot purgatory**.
- **Protect the core; open the edges:** import innovation without leaking advantage or creating dependence.
- The ROI is optionality and speed; see chapters 10.3 (procurement), 10.1 (portfolio), 10.2 (third-party risk), and 6.1 (build/buy/partner for AI).

## References and further reading

- Henry Chesbrough, *Open Innovation* and *Open Business Models*.
- Clayton Christensen, *The Innovator's Dilemma* (why incumbents struggle to innovate internally).
- European Union, Directive 2014/24/EU, the *innovation partnership* procurement procedure.
- U.S. Small Business Administration, *Small Business Innovation Research (SBIR/STTR)* programme.
- Vijay Govindarajan and Chris Trimble, *The Other Side of Innovation* (executing innovation, beating pilot purgatory).
- Ronald Adner, *The Wide Lens* (innovation ecosystems and partner dependencies).
- GovTech and public-sector innovation resources (e.g., GDS, USDS, Public Digital); see chapter 10.3.
