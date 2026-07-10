# 10.11 Digital sovereignty

## Overview and motivation

[Digital sovereignty](https://en.wikipedia.org/wiki/Digital_sovereignty) is the degree to which an organization, nation, or bloc keeps meaningful control over its own data, software, and infrastructure. That means control over where data physically resides, which laws and governments can compel access to it, and whether critical systems can keep operating without depending on a foreign power or a single vendor. It has several dimensions: **[data sovereignty](https://en.wikipedia.org/wiki/Data_sovereignty)** (whose jurisdiction and laws govern the data), **operational sovereignty** (the ability to run and administer systems without a third party's permission or presence), **software sovereignty** (access to and control over the source and its evolution), and **supply-chain sovereignty** (freedom from chokepoints in hardware, services, and dependencies). This chapter sits in the management part because sovereignty is fundamentally a strategy, procurement, and risk decision (chapters 10.1–10.3) with deep technical consequences.

The motivation has moved from theoretical to urgent. [Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing) concentrated much of the world's infrastructure in a handful of providers, mostly under a single country's jurisdiction. Extraterritorial laws such as the U.S. [CLOUD Act](https://en.wikipedia.org/wiki/CLOUD_Act) (which can compel a provider to disclose data regardless of where it is stored) collide with regimes such as the EU's [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation), a tension crystallized by the *[Schrems II](https://en.wikipedia.org/wiki/Schrems_II)* ruling that invalidated the EU–US Privacy Shield. Add geopolitical shocks, sanctions, and the risk of a provider being cut off, and dependency becomes a strategic vulnerability, not just a vendor-management footnote. Sovereignty is the discipline of deciding, deliberately, how much of that dependency your most critical systems and data can safely carry.

For enterprise and especially government the stakes are direct. Multinationals must reconcile conflicting data-protection regimes and avoid a lock-in that a regulator or a geopolitical event could turn into an existential migration. Governments hold data (health records, tax, defense, citizen identity) whose exposure to a foreign jurisdiction is a national-security and public-trust question. That is why "sovereign cloud" offerings, initiatives like the EU's [Gaia-X](https://en.wikipedia.org/wiki/Gaia-X), and national certifications such as France's SecNumCloud have emerged. The goal is not autarky. It is proportionate control matched to the sensitivity of what is at stake.

## Key principles

- **Sovereignty is a spectrum, not a switch.** Match the degree of control to the sensitivity of the data and workload.
- **Location is not jurisdiction.** Data stored locally can still be legally reachable by a foreign government; residency alone is not sovereignty.
- **Design for exit.** The ability to leave a provider is the truest measure of sovereignty.
- **[Open standards](https://en.wikipedia.org/wiki/Open_standard) and [open source](https://en.wikipedia.org/wiki/Open-source_software) reduce dependency:** they are strategic autonomy tools, not just cost savers.
- **Control the keys.** Who holds and controls encryption keys often matters more than where bytes sit.
- **Avoid trading one lock-in for another.** A single "sovereign" vendor can be as captive as a hyperscaler.
- **Be proportionate.** Sovereignty has real costs; over-rotating everywhere wastes money and slows delivery.

## Recommendations

### Classify data and workloads by sovereignty sensitivity

Not everything needs the same protection. Classify data and systems by the consequence of foreign-jurisdiction access or provider loss. Public and low-risk workloads can sit on global hyperscale infrastructure for scale and cost. Highly sensitive data (national security, health, citizen identity, regulated records) warrants stronger sovereignty controls. This tiering, the same risk-based logic as data classification in chapter 4.5, is what keeps sovereignty affordable, focusing expensive controls where they are justified rather than localizing everything.

### Understand jurisdiction, not just residency

**Data residency** (the physical or geographic location where data is stored) is necessary but not sufficient. What matters legally is *jurisdiction*: which governments can compel disclosure, and under which laws. A dataset held in an in-country data center operated by a foreign-headquartered provider may still be reachable under that provider's home-country law (the CLOUD Act problem). Map each system's legal exposure: provider headquarters, applicable laws, and any adequacy decisions or transfer mechanisms (Standard Contractual Clauses, the EU–US Data Privacy Framework). Then treat that legal map as a first-class part of the architecture (chapters 4.5, 4.6).

### Design for portability and reversibility

The most durable sovereignty control is a credible exit. Prefer open standards and portable formats (chapter 3.8). Containerize workloads so they can move. Keep infrastructure as code (chapter 8.2) so an environment can be rebuilt elsewhere. Avoid deep reliance on a single provider's proprietary services for your most critical systems. Maintain and periodically *test* an exit plan, an escrow of data and configuration plus a rehearsed path to an alternative, so that "we could leave if we had to" is a demonstrated fact, not a hope. This is the antidote to **[vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in)**, the condition of being unable to switch providers without prohibitive cost or disruption.

### Use sovereign infrastructure and key control where warranted

For the most sensitive tier, stronger technical controls exist: **sovereign cloud** offerings (cloud regions operated by or partnered with in-jurisdiction entities, sometimes certified like SecNumCloud), **[confidential computing](https://en.wikipedia.org/wiki/Confidential_computing)** (hardware-based trusted execution that keeps data encrypted even while it is being processed), and customer-controlled encryption keys: **bring your own key (BYOK)** and, more strongly, **hold your own key (HYOK)**, where the provider never has access to the keys that unlock the data. Controlling the keys can deliver much of the practical benefit of sovereignty even on shared infrastructure. Data a provider cannot decrypt is data it cannot meaningfully disclose.

### Favor open source and open ecosystems for strategic autonomy

Open source software and open standards are among the strongest sovereignty levers, because they remove the single-vendor kill switch. The source can be run, audited, forked, and maintained independently of any one supplier (chapters 10.3, 3.8). Public-sector "public money, public code" policies and initiatives like Gaia-X reflect this. Open source is not automatically sovereign. It still needs skilled people to run and support it, and its supply chain needs securing (chapter 4.2). But it converts dependency on a vendor into dependency on a community and your own capability, which is far easier to control.

### Govern sovereignty as a proportionate risk, not an absolute

Stand up a sovereignty risk framework alongside your other governance (chapters 10.2, 1.5). Assess the concentration and jurisdictional risk of major platforms. Decide target sovereignty levels per data tier, and weigh them against cost, capability, and delivery speed. The aim is a defensible, documented position ("these workloads accept hyperscale dependency; these require in-jurisdiction control; here is our exit posture"), reviewed as geopolitics and regulation change, not a one-time absolute stance.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
|---|---|---|
| **Global hyperscale cloud** | Scale, features, low cost, speed | Jurisdictional exposure; concentration and lock-in risk |
| **Sovereign cloud / in-jurisdiction provider** | Legal control; national-security fit; trust | Higher cost; fewer features; often smaller scale; new lock-in |
| **Key control (BYOK/HYOK) on shared infra** | Much of the benefit at lower cost; keeps scale | Operational complexity; key-management risk; not absolute |
| **Open source / self-hosted** | Auditability, forkability, no vendor kill switch | Needs in-house capability; you own the operations and security |
| **Data localization mandates** | Regulatory compliance; political assurance | Costly; fragments data; can reduce resilience and utility |

The defining tension is **control versus capability and cost**. Maximum sovereignty (self-hosted, in-jurisdiction, open source, fully portable) sacrifices the scale, features, and velocity of global platforms. Maximum capability accepts dependency and jurisdictional exposure. The resolution is tiering: pay for sovereignty where the consequence justifies it, and take pragmatic dependency where it does not.

## Questions to discuss with your team

1. **Have we tiered our data and workloads by sovereignty sensitivity, so expensive controls land only where they are justified?** Sovereignty is a spectrum, not a switch, and localizing everything burns money, forfeits capability, and can even reduce resilience by shrinking your options. Classify each system by the consequence of foreign-jurisdiction access or provider loss: public and low-risk workloads can sit on global hyperscale infrastructure, while national-security, health, or citizen-identity data warrants stronger controls. This is the same risk-based logic as data classification, and it is what keeps sovereignty affordable. Bring your crown-jewel systems and their current hosting, and ask whether the protection matches the sensitivity. If you are protecting everything equally, you are almost certainly overpaying somewhere and exposed somewhere else.

2. **Are open standards and open source part of our sovereignty strategy, or do we treat them as cost savers only?** Source you can run, audit, fork, and maintain removes the single-vendor kill switch, which is one of the strongest autonomy levers you have. Open standards and portable formats are what make a credible exit possible, and a credible exit is the truest measure of sovereignty. The subtler trap is escaping a hyperscaler only to become wholly captive to one "sovereign" vendor with no exit: you traded one lock-in for another. Bring your most critical platforms and ask how tightly each is bound to one provider's proprietary services. Where the answer is "very," open standards and containerized, rebuildable environments are the cheapest way to loosen the grip.

3. **Who owns our sovereignty risk framework, and how often do we revisit the stance as law and geopolitics shift?** A sovereignty position set once and never reviewed becomes fiction the moment a ruling, sanction, or new law lands, and those shocks now arrive regularly. Stand up a living framework alongside your other governance: assess the concentration and jurisdictional risk of major platforms, set target sovereignty levels per data tier, and document a defensible position you can show a regulator. Name the owner and the review cadence. Bring the question of how a sanction or adverse ruling against your main provider would hit your critical services next week; if no one can answer, the framework does not exist yet.

## Examples

**Startup.** A small health-tech startup lands its first hospital customer in Germany, which requires patient data to stay under EU jurisdiction. Instead of over-building a sovereign stack it cannot afford, the founders deploy to their existing cloud provider's EU region, hold their own encryption keys so the provider cannot decrypt the sensitive records, and keep the workload containerized so it stays portable. This buys most of the sovereignty benefit the customer needs at a cost a seed-stage team can carry, and it closes the deal without a wholesale re-architecture.

**Enterprise.** A multinational bank must keep certain customer data within the EU and beyond the reach of foreign disclosure law. Rather than abandon its global cloud provider, it tiers its estate. General workloads stay on hyperscale regions for scale. Regulated customer data runs in EU regions with **hold your own key** encryption (the provider cannot decrypt it) and a tested exit plan to an alternative provider. This satisfies regulators and the bank's own concentration-risk appetite (chapter 10.2) without a wholesale, capability-destroying migration.

**Government.** A national health service holds citizens' medical records and judges exposure to foreign jurisdiction unacceptable. It procures a sovereign cloud, meaning infrastructure operated by an in-country entity under national certification (e.g., SecNumCloud-style), with confidential computing for the most sensitive processing, and mandates open standards (chapter 3.8) and open-source components so the platform can be maintained independently of any single supplier. The higher cost and narrower feature set are accepted as the price of national-security control and public trust. Meanwhile, less-sensitive services (a public information portal) remain on cheaper global infrastructure.

## Business case: motivations, ROI, and TCO

The economics of digital sovereignty are asymmetric, and best framed as insurance against low-probability, high-impact events. The costs are visible and recurring: sovereign and in-jurisdiction infrastructure is typically more expensive, offers fewer managed services, and demands more in-house operational capability, all of which raise total cost of ownership and can slow delivery. The benefits are mostly avoided catastrophes: regulatory fines and forced re-architecture after a ruling like *Schrems II*, a business-ending loss of access if a provider is sanctioned or cut off, or the reputational and national-security damage of foreign disclosure of sensitive data. Because those tail risks are severe and increasingly plausible, proportionate investment in sovereignty, especially cheap-but-powerful controls like key ownership, portability, and open standards, is often strongly positive expected value, even though it looks like pure cost on a steady-state spreadsheet.

The trap on both sides is disproportion. *Under*-investing leaves critical data and systems exposed to a single jurisdiction or vendor with no exit, turning a manageable risk into an existential one. *Over*-investing, by localizing everything and refusing all global platforms, burns money, forfeits capability, and can *reduce* resilience by shrinking your options. To make the case to leadership, tie sovereignty spending to a data-and-workload risk tiering. Quantify the concentration and jurisdictional exposure of the crown-jewel systems. Price the cheap controls (keys, portability, exit rehearsals) that de-risk them. Reserve expensive sovereign infrastructure for the tier that genuinely warrants it.

## Anti-patterns and pitfalls

- **Sovereignty theater:** advertising in-country data residency while a foreign-headquartered provider retains legal access to the data.
- **Conflating encryption with sovereignty:** encrypting data but letting the provider hold the keys, so it can still be compelled to decrypt.
- **Over-rotation:** localizing and self-hosting everything at ruinous cost and reduced capability, regardless of sensitivity.
- **New single lock-in:** escaping a hyperscaler by becoming wholly captive to one "sovereign" vendor with no exit.
- **No tested exit:** an exit plan that exists on paper but has never been rehearsed, so portability is unproven.
- **Ignoring the human supply chain:** assuming open source or self-hosting grants sovereignty without the skilled people to run it.
- **Static stance:** setting a sovereignty position once and never revisiting it as law and geopolitics shift.

## Maturity model

- **Level 1 (Initial):** Sovereignty is unconsidered; data and critical systems sit wherever is cheapest, with no map of jurisdictional or concentration risk.
- **Level 2 (Managed):** Data residency is addressed for obvious regulated data, but jurisdiction, keys, and exit are not; reliance on single providers is unexamined.
- **Level 3 (Defined):** Data and workloads are tiered by sovereignty sensitivity; jurisdiction is mapped; key control, portability, and open standards are applied to sensitive tiers; exit plans exist.
- **Level 4 (Optimizing):** A living sovereignty risk framework tied to data tiers and geopolitics; exits are rehearsed; sovereign controls are applied proportionately; sovereignty is a routine input to architecture and procurement, not a crisis response.

## Ideas for discussion

1. For your most sensitive dataset, which governments could legally compel access to it today, and do you know?
2. Is your data residency real sovereignty, or does a foreign-headquartered provider still hold the keys and the legal exposure?
3. Could you actually leave your primary cloud provider if you had to, and have you ever tested it?
4. Which of your workloads genuinely need sovereign infrastructure, and which are you over-protecting at needless cost?
5. Where would controlling your own encryption keys give you most of the sovereignty benefit at a fraction of the cost?
6. How would a sanction, outage, or legal ruling against your main provider affect your critical services next week?

## Key takeaways

- Digital sovereignty is proportionate control over your data, software, and infrastructure, across data, operational, software, and supply-chain dimensions.
- **Location is not jurisdiction:** residency alone doesn't prevent foreign legal access; map who can compel disclosure.
- **Design for exit** and **control your keys:** portability and key ownership are the highest-leverage, lowest-cost controls.
- **Open standards and open source** are strategic autonomy tools; reserve expensive **sovereign cloud** for the tier that warrants it.
- Govern sovereignty as a **proportionate, living risk** (chapters 10.2, 10.3, 4.5, 4.6, 3.8), avoiding both under-protection and ruinous over-rotation.
- The ROI is insurance against severe tail risks (regulatory, geopolitical, and lock-in) priced against real, recurring cost.

## References and further reading

- European Court of Justice, *Data Protection Commissioner v. Facebook Ireland and Maximillian Schrems* ("Schrems II", 2020).
- Regulation (EU) 2016/679, *General Data Protection Regulation (GDPR)*; Regulation (EU) 2023/2854, *Data Act*.
- U.S. *Clarifying Lawful Overseas Use of Data (CLOUD) Act* (2018).
- ANSSI, *SecNumCloud* qualification framework (France).
- Gaia-X European Association for Data and Cloud (Gaia-X initiative).
- ENISA, reports on cloud security and EU cybersecurity certification (EUCS).
- Julia Pohle and Thorsten Thiel, "Digital Sovereignty" (*Internet Policy Review*, 2020).
- Bert Hubert, writings on European digital autonomy and dependency on foreign providers.
- Kai Zenner and others, analyses of EU digital sovereignty policy (for context; verify current sources).
