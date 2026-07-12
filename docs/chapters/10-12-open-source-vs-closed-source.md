# 10.12 Open source vs closed source

## Overview and motivation

Almost every modern system is a blend of software you wrote, software you bought, and software you took for free. Two of those three come with a fundamental choice: is the software **open source** or **closed source**? **[Open-source software](https://en.wikipedia.org/wiki/Open-source_software) (OSS)** is distributed under a license that grants everyone the right to use, study, modify, and redistribute the source code, the human-readable instructions that define the program. **Closed-source software**, also called **[proprietary software](https://en.wikipedia.org/wiki/Proprietary_software)**, is distributed as a finished product whose source code the vendor keeps private. You get the right to run it under a license, but not to inspect or change how it works. A middle category, **[source-available software](https://en.wikipedia.org/wiki/Source-available_software)**, publishes the source for reading but restricts use, modification, or redistribution. It is *visible* but not *open* by the standard definition.

Two clarifications matter before you compare them. First, "free" is ambiguous. The community distinguishes **free-as-in-freedom** (the liberty to modify and share, sometimes written "libre") from **free-as-in-price** (zero cost, "gratis"). Open source is about freedom, not necessarily price. Second, open-source licenses divide into two families. **[Permissive licenses](https://en.wikipedia.org/wiki/Permissive_software_license)** (such as [MIT](https://en.wikipedia.org/wiki/MIT_License), BSD, and Apache 2.0) let you do almost anything, including embedding the code in a closed product. **[Copyleft](https://en.wikipedia.org/wiki/Copyleft) licenses** (such as the [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License), GPL) require that derivative works you distribute also be released under the same open terms, a reciprocity rule sometimes called "viral" by critics and "share-alike" by proponents.

This chapter looks at the choice from two sides. As a **consumer**, you decide whether to adopt an open-source or proprietary component. As a **producer**, you decide whether to open-source software you built. For large enterprises and especially government, both decisions carry weight far beyond the license file. They touch procurement (chapter 10.3), digital sovereignty (chapter 10.11), supply-chain security (chapter 4.2), interoperability (chapter 3.8), and the build-or-buy calculus (chapter 6.1).

## Key principles

- **License, not price, defines "open."** Read the license; free-of-charge and open-source are different claims.
- **Neither model is inherently more secure.** Both can be excellent or negligent; the practices around the code matter more than its openness.
- **Openness is a dependency-reduction lever.** Access to source is the ultimate protection against [vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in).
- **You always own the operational burden.** Free-to-acquire is never free-to-run; [total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership) tells the real story.
- **Differentiators stay closed; commodities can open.** Open-source what does not distinguish you; guard what does.
- **Copyleft has consequences.** Understand reciprocity obligations before you embed copyleft code in a product you distribute.
- **A live community is an asset; an abandoned repository is a liability.** Judge the project, not just the license.

## Recommendations

### Evaluate a component on the project, not just the license

Before you adopt any dependency, open-source or proprietary, assess its health: release cadence, number and diversity of maintainers, responsiveness to security reports, and breadth of adoption. A single-maintainer open-source library and a small proprietary vendor carry the same **bus-factor risk** (the danger that a project collapses if one or a few key people leave). Favour components with a broad contributor base or a financially sound vendor, and record the assessment as part of due diligence (chapters 10.2, 4.2).

### Read and track licenses as a first-class obligation

Maintain an inventory of every component and its license, and enforce a policy on which license families are acceptable for which uses. The critical distinction is copyleft. **Permissive** code (MIT, Apache 2.0) can generally be embedded in closed products freely. **Strong copyleft** (GPL) can obligate you to release your own distributed derivative under the same terms. Use automated **software composition analysis (SCA)**, tools that scan your dependencies to identify components, licenses, and known vulnerabilities, and generate a **software bill of materials (SBOM)**, a formal list of every component in a product (chapters 10.3, 4.2).

### Judge security by practice, not by openness

Do not assume open source is safe because of the **"many eyes" argument** ([Linus's Law](https://en.wikipedia.org/wiki/Linus%27s_law): "given enough eyeballs, all bugs are shallow"). And do not assume proprietary code is safe through **[security-through-obscurity](https://en.wikipedia.org/wiki/Security_through_obscurity)** (the flawed belief that hiding source hides flaws). Many eyes only help if qualified people actually look, and many widely used projects are thinly maintained. Both models carry **supply-chain risk**: open source through compromised or abandoned dependencies, proprietary through opaque code and update channels you cannot inspect. Pin versions, verify provenance, scan continuously, and monitor advisories regardless of model (chapter 4.2).

### Design for exit and interoperability

Prefer components that speak open standards and portable data formats, so you can replace them later (chapters 3.8, 10.11). With open source you gain the ultimate exit: if a project stalls, you can **[fork](https://en.wikipedia.org/wiki/Fork_(software_development))** it (create and maintain your own copy). With proprietary software, negotiate protections up front: data export in open formats, documented APIs, and **[source-code escrow](https://en.wikipedia.org/wiki/Source_code_escrow)** (a legal arrangement where the vendor deposits source with a third party, released to you if the vendor fails). Design so that no single component, of either kind, can hold your system hostage.

### Weigh total cost of ownership, not sticker price

Compare options on **total cost of ownership (TCO)**, the full lifetime cost including acquisition, integration, operation, support, training, upgrades, and eventual replacement, rather than license fees alone. Open source often trades licensing cost for higher operational and staffing cost. Proprietary software often trades predictable subscription fees for lock-in and less control. Include the cost of the model itself: self-supporting open source needs in-house skill, while proprietary software needs vendor-management capacity.

### As a producer, open-source what does not differentiate you

Classify your own software into what gives you competitive or mission advantage and what is undifferentiated plumbing. Keep the differentiators proprietary. Consider open-sourcing the commodity infrastructure, where a community can share maintenance and improvement. For government, weigh **"public money, public code"** (the principle that software funded by taxpayers should be publicly available by default) as a driver of transparency, reuse, and sovereignty (chapters 10.5, 10.11). Choose the license deliberately: permissive to maximize adoption, copyleft to keep the ecosystem open.

## Trade-offs: pros and cons

| Dimension | Open source | Closed / proprietary |
|---|---|---|
| **Acquisition cost** | Usually zero to acquire | License or subscription fee |
| **Total cost of ownership** | Cost shifts to operations and staff | More predictable, but lock-in premium |
| **Control & customization** | Full: you can read and change the source | Limited to what the vendor exposes |
| **Support & accountability** | Community, or paid third party; no single throat to choke | Contractual support and a clear accountable party |
| **Security posture** | Auditable; "many eyes" if truly maintained | Vendor-managed; opaque; obscurity is not protection |
| **Longevity / abandonment** | Can be forked if maintained; may still wither | Depends on vendor viability and roadmap |
| **Vendor lock-in** | Low: source and open formats enable exit | High unless mitigated by standards and escrow |
| **Ecosystem** | Open community and interoperability | Curated, integrated, sometimes walled |

The recurring tension is **control versus convenience and accountability**. Open source maximizes control, auditability, and freedom from lock-in, but it asks you to supply the capability, integration, and support yourself. Proprietary software delivers a supported, integrated, accountable product with a contract to enforce, but it concedes control and invites lock-in. The resolution is rarely all-or-nothing. Most mature estates mix open-source foundations with proprietary systems where support, accountability, or specialized capability justify the trade.

## Questions to discuss with your team

1. **Do we enforce a license policy with automated SCA and SBOMs in the pipeline, especially to catch strong copyleft before it ships?** Embedding a GPL library in a distributed proprietary product can obligate you to release your own source, and that surprise usually surfaces late, when it is expensive to unwind. Maintain an inventory of every component and its license, enforce which license families are acceptable for which uses, and run software composition analysis automatically so the pipeline blocks violations rather than a lawyer catching them at ship time. Generate an SBOM as a matter of course. For a large or government estate, this is also supply-chain hygiene and often a procurement requirement. Bring your current license inventory, or the fact that you do not have one, and decide who owns the policy.

2. **When we adopt a dependency, do we assess project health and bus-factor as due diligence?** A single-maintainer open-source library and a small proprietary vendor carry the same risk: the project collapses if one or a few key people leave. Before you adopt anything, assess release cadence, the number and diversity of maintainers, responsiveness to security reports, and breadth of adoption, and record the assessment. Neither model is safer by default; "many eyes" only helps if qualified people actually look, and many widely used projects are thinly maintained. Bring the three or four dependencies your product most relies on and ask, for each, how many people would have to walk away before it became your problem. If you cannot answer, that is the assessment you owe yourself.

3. **When we buy proprietary, do we secure exit protections up front?** Proprietary software offers accountability and convenience in exchange for control, and the hidden cost is lock-in: switching costs that let a vendor raise prices or degrade service with little recourse. Negotiate the protections before you sign, when you still have leverage: data export in open formats, documented APIs, and source-code escrow that releases the source if the vendor fails. With open source your exit is the ability to fork; with proprietary you must write the exit into the contract. Bring your most critical proprietary systems and ask what actually happens if the vendor doubles the price or goes under. If the answer is "we are stuck," fix the contract at renewal.

4. **For the software we build ourselves, how do we decide what to open-source and what to keep closed, and who holds authority to make that call?** Get this wrong in one direction and you give away the very code that differentiates you; get it wrong in the other and you hoard commodity plumbing whose maintenance a community would gladly share. The competing pressures are real: engineers want the recruiting and reputation upside of a public repository, while product and legal worry about handing rivals an advantage or exposing a security-sensitive heuristic. Bring an honest classification of your systems into mission-differentiating versus undifferentiated infrastructure, and name the person or board that signs off on a release, because an ad hoc decision made by whoever pushed the repository is how crown jewels leak. For a large enterprise the question is portfolio strategy, and for government it collides with "public money, public code," the principle that taxpayer-funded software should be public by default, so decide in advance which exemptions (national security, fraud detection, personal data) justify keeping code closed.

5. **Do our build-or-buy comparisons capture the full total cost of ownership, or do we still treat a zero license fee as a zero cost?** The most common financial mistake with open source is reading "free to acquire" as "free to run," then discovering that integration, operations, security response, and paid support dwarf any license you avoided. The tension is that a proprietary subscription looks expensive on the invoice while hiding a lock-in premium, and an open component looks free on the invoice while shifting cost onto your own staff. Bring a like-for-like TCO model for two or three real decisions: acquisition, integration, operation, support, training, upgrades, security response, and eventual replacement, priced over the full lifetime rather than the first year. In an enterprise or government estate, add the cost of the operating model itself, since self-supporting open source demands in-house skill you must recruit and retain, and treat a comparison that omits those lines as evidence, not analysis.

6. **Do we judge the security of a component by its practices, or do we lean on the openness label, whether "many eyes" or the secrecy of closed code?** Both defaults are traps: "many eyes" only protects you when qualified people actually review the code, and many widely used open projects run on one exhausted maintainer, while closed source that relies on attackers not seeing it is security through obscurity, not a control. The debate matters because it changes where you spend scarce security effort, and the honest answer is that both models carry supply-chain risk, open source through compromised or abandoned dependencies and proprietary through opaque update channels you cannot inspect. Bring evidence for your most critical components: who actually reviews them, how fast advisories are patched, whether versions are pinned and provenance verified, and whether you generate an SBOM. For a large or government estate, tie this to procurement and continuous scanning obligations, because a regulator will ask what you inspected, not whether the source was public.

## Sector lens

**Startup.** With little runway you build on open-source foundations because you cannot afford license fees and you want the freedom to fork if a project stalls. Run a composition-analysis scan before you ship so a strong-copyleft library does not quietly oblige you to publish your own source, and keep your one real differentiator strictly closed. Open-source a small, non-critical tool if it helps recruiting, but do not staff a maintenance burden you cannot carry.

**Small business.** With no in-house legal or platform specialist, treat the license as a risk you must not misread rather than a topic you can master. Prefer supported proprietary tools or commercial open-source distributions where a vendor owns patches and accountability, because self-supporting a stack you cannot operate is a false economy. When you do adopt a free component, check that its license permits your use and that the project is actually maintained, not abandoned.

**Enterprise.** At scale the problem is consistency across many teams: a written license policy, automated software composition analysis and SBOM generation in every pipeline, and TCO-based build-or-buy decisions rather than per-team habit. Manage open and proprietary software as one portfolio, standardize exit protections such as open formats and source-code escrow in procurement, and track the health of critical dependencies so a single abandoned project does not become an incident. Govern the producer side too, with a clear rule on what the organization open-sources versus keeps closed.

**Government.** Procurement rules, transparency duties, and public accountability shape every choice. Weigh "public money, public code," the principle that taxpayer-funded software should be public by default, to advance reuse across agencies and digital sovereignty, while carving out narrow exemptions for security-sensitive or personal-data code. Require any proprietary supplier to provide data export in open formats and source-code escrow so a vendor failure cannot strand a public service, and publish the non-sensitive source so citizens can audit the rules that govern them.

## Examples

**Startup.** A three-founder startup builds its whole product on open-source foundations (Linux, an open-source database, a web framework) because it cannot afford license fees and wants the freedom to fork if a project stalls. Before shipping, one founder runs a composition-analysis scan and catches a strong-copyleft library that would have forced them to publish their proprietary matching algorithm, so they swap it for a permissively licensed equivalent. They keep that algorithm, their sole differentiator, strictly closed, and open-source only a small internal logging tool to build goodwill and attract engineers.

**Enterprise.** A large insurer runs its core platform on open-source foundations: Linux, a widely used open-source database, and a container orchestrator. But it buys a proprietary actuarial-modelling suite, because the vendor's domain expertise, regulatory certifications, and support contract are worth the fee and there is no comparable open alternative. It pays a subscription for **commercial open source** (vendor-supported distributions of the open components) to get accountability and patches on the plumbing, while keeping the pricing algorithm that differentiates it strictly proprietary and in-house. TCO analysis (chapter 10.10) drives each choice rather than ideology.

**Government.** A national tax agency, under a "public money, public code" policy, builds a new benefits-eligibility service on open-source components and open standards (chapter 3.8), so that other agencies can reuse it and citizens can audit the rules. It publishes the non-sensitive code in a public repository, retaining only fraud-detection heuristics as closed for security reasons. This reduces vendor lock-in and advances digital sovereignty (chapter 10.11). Procurement rules (chapter 10.3) require any proprietary component to provide data export in open formats and source-code escrow, to guarantee continuity if the supplier fails.

## Business case: motivations, ROI, and TCO

The financial appeal of open source, its lack of a license fee, is the least reliable part of the case, because acquisition is a small fraction of TCO. The durable returns are strategic: freedom from lock-in (the ability to change or drop a supplier without re-architecting), auditability for security and compliance, faster adoption because engineers can try before committing, and shared maintenance of commodity code across a whole industry. The offsetting costs are real. You must supply integration, operations, security response, and often paid support, and a poorly chosen unmaintained project can cost more in incidents than any license would have.

Proprietary software's business case is accountability and convenience: a single vendor responsible for the product, a support contract you can enforce, integrated features, and predictable budgeting. Its hidden cost is lock-in, the switching costs that let a vendor raise prices or degrade service with little recourse, plus dependency on the vendor's solvency and roadmap. Common **business models** blur the line: **[open core](https://en.wikipedia.org/wiki/Open-core_model)** (an open base with proprietary paid add-ons), **dual licensing** (the same code offered under both a copyleft and a paid commercial license), **[software as a service](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)** (the software runs as a hosted service you rent, where the source may be irrelevant because you never possess the binary), and **support/subscription** models that sell service around otherwise free code.

For a producer, the ROI of **open-sourcing your own non-differentiating software** can be substantial. Outside contributors reduce your maintenance load. The project becomes a recruiting and reputation asset. External adoption makes your standard the de facto one. For government, it delivers transparency and reuse across the public sector. The strategic rule is simple: open-source the commodity to share its cost and grow an ecosystem, and keep the differentiator closed to protect the advantage that funds everything else.

## Anti-patterns and pitfalls

- **"Free means free":** treating zero acquisition cost as zero TCO, then under-funding operation and support.
- **License blindness:** embedding strong-copyleft code in a distributed proprietary product and triggering obligations you never planned for.
- **Faith in "many eyes":** assuming an open project is audited when it has one overworked maintainer and no security review.
- **Security-through-obscurity:** believing closed source is safe simply because attackers cannot read it.
- **Ideological absolutism:** mandating "all open" or "all proprietary" instead of choosing per component on merit and TCO.
- **Ignoring provenance:** pulling dependencies with no SBOM, version pinning, or supply-chain verification (chapter 4.2).
- **Open-sourcing the crown jewels:** releasing the very code that differentiates you, giving away your advantage.
- **Fork-and-forget:** forking an abandoned project without the capacity to actually maintain the fork.

## Maturity model

**Level 1 (Initiate).** Open-source and proprietary components enter the estate ad hoc. Licenses are unread, there is no inventory or SBOM, and the choice between models is made by habit or price alone. Abandonment and license risk surface only when something breaks, and each team reacts on its own.

**Level 2 (Develop).** Some teams begin basic practices: a component and license inventory, a rough view of acceptable licenses, and occasional software composition analysis. Build-or-buy and open-or-closed decisions get written down, but the discipline is patchy and inconsistent from one team to the next, so a copyleft or bus-factor surprise can still slip through where the habit has not taken hold.

**Level 3 (Standardize).** A documented framework governs both consumption and production org-wide. Components are chosen on TCO and project health, licenses are enforced automatically in the pipeline so violations block a build, SBOMs are generated as a matter of course, and an explicit policy states what the organization open-sources versus keeps closed. Exit protections such as open formats and source-code escrow are standard in procurement, and every team follows the same rules rather than its own.

**Level 4 (Manage).** The programme is measured and controlled against baselines. The organization tracks metrics such as SBOM coverage across products, the share of dependencies that violate policy, mean time to patch a disclosed dependency vulnerability, bus-factor and health scores for critical projects, and realized TCO against the estimate that justified each choice. Thresholds trigger action: a component whose maintenance stalls or whose patch latency drifts past target is flagged for replacement on evidence, and open-or-closed and build-or-buy decisions are reviewed against the numbers rather than defended by habit.

**Level 5 (Orchestrate).** Open-source strategy is a deliberate business capability, integrated across the organization and continuously improved. The organization contributes to and sometimes stewards the projects it depends on, open-sources its non-differentiating software as a matter of course, and feeds dependency-health and TCO data back into procurement, security, and product planning. It routinely rebalances its portfolio of open and proprietary software, adapting to shifts in cost, risk, sovereignty, and strategic advantage before they force a crisis.

## Ideas for discussion

- Where in your estate would losing a single vendor or maintainer be existential, and what is your exit plan?
- Which of your own systems are commodities you could open-source, and which are true differentiators to protect?
- Does your organization treat "many eyes" as a real security control or an unexamined assumption?
- For public-sector readers: what would a "public money, public code" default change in your next procurement?
- How well do your TCO comparisons capture the operational and support costs that open source shifts onto you?

## Key takeaways

- **Open vs. closed is defined by the license**, not by price; know the difference between free-as-in-freedom and free-as-in-price, and between permissive and copyleft.
- **Neither model is inherently more secure or cheaper.** Judge the project's practices and its full TCO, not the openness label.
- **Openness is the strongest antidote to lock-in**, delivering auditability, portability, and the ability to fork; proprietary software offers accountability and convenience in exchange for control.
- **Decide per component on merit**, and mix models deliberately rather than by ideology.
- **As a producer, open-source the commodity and keep the differentiator closed**, and in government, weigh "public money, public code" for transparency, reuse, and sovereignty.

## References and further reading

- Eric S. Raymond, *The Cathedral and the Bazaar*
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Adrian Cockcroft and others, various O'Reilly titles on open-source strategy and operations
- Free Software Foundation, *The Free Software Definition* (and the GNU General Public License texts)
- Open Source Initiative, *The Open Source Definition* and approved-license list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- Yochai Benkler, *The Wealth of Networks*
