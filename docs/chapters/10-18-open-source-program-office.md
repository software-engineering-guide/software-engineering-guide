# 10.18 Open source program office (OSPO) and upstream contribution

## Overview and motivation

Your organization already runs on [open-source software](https://en.wikipedia.org/wiki/Open-source_software): the operating systems, languages, databases, and libraries that carry your product are mostly written by people who do not work for you. Chapter 10.3 covers procurement and license compliance, and chapter 10.12 covers the open-versus-closed decision. This chapter is about the function that makes all of that coherent: an [open-source program office](https://en.wikipedia.org/wiki/Open_Source_Program_Office) (OSPO), the team that owns how the company consumes, contributes to, and releases open source. An OSPO is the center of gravity for a relationship that is otherwise spread across every engineer who types `import`.

Most organizations back into open source one dependency at a time, then discover the accumulated exposure all at once: a license question during acquisition due diligence, a critical library with one exhausted maintainer, a security advisory in code nobody knew they shipped. An OSPO turns that scramble into a managed capability. It sets consumption policy that enables rather than blocks, it decides when contributing upstream serves the business, it stewards the projects you release, and it applies open collaboration inside the company through [InnerSource](https://en.wikipedia.org/wiki/Inner_source). This is a strategic function, connected to your software engineering values (chapter 1.1), not a compliance checkbox.

For enterprises the driver is scale: thousands of dependencies, export and license obligations across jurisdictions, and hundreds of engineers who each make small open-source decisions daily. A single office gives that sprawl a spine. For government the driver is policy and public trust. "Open source by default" and "public money, public code" are increasingly the law, so public bodies need someone who can publish code safely, reuse across agencies, and hold vendors to open standards. In both settings the OSPO pays for itself by converting invisible, unpriced risk into deliberate, budgeted work.

## Key principles

- **Open source is a two-way relationship, not a free warehouse.** You consume, you contribute, and you release, and an OSPO owns all three.
- **Contribution is strategy, not charity.** Upstreaming reduces the cost of carrying private patches and buys you influence.
- **Enable the fast path, do not guard the gate.** A policy slower than copying code will be ignored, so make the compliant path the quickest one.
- **Fund the maintainers you depend on.** The commons is not self-sustaining, and your most critical library may have one unpaid author.
- **Steward what you release, or do not release it.** An abandoned project harms your reputation more than no project ever would.
- **Measure engagement so you can improve it.** Count contributions, dependency health, and time-to-approval, not press releases.
- **In government, default to open and publish by default.** Openness is the norm; closure is the documented exception.

## Recommendations

### Stand up an OSPO sized to your reality

You do not need a large team to start. At a startup an OSPO can be one engineer with a written mandate and a few hours a week. At an enterprise it is a small central group plus a federated network of champions embedded in product teams. Whatever the size, give it a clear charter covering four responsibilities: consumption policy and compliance, upstream contribution, releasing and stewarding your own projects, and community and funding relationships. Place it where it can see both engineering and legal, often reporting into the CTO or a VP of engineering with a dotted line to legal and security. The failure mode is an OSPO that lives entirely inside legal and becomes a brake; the fix is to staff it with engineers who ship, so its guidance carries credibility on the teams it serves.

### Consume responsibly, and make the safe path the easy path

Consumption is where most risk enters, so make good behavior effortless. Provide a curated internal catalog of pre-vetted components, automated license and vulnerability scanning in the pipeline, and clear defaults that a developer can follow without filing a ticket. Lean on the license discipline in chapter 10.3 and the supply-chain and dependency-health practices in chapter 2.18: pin versions, generate a software bill of materials, watch the [software supply chain](https://en.wikipedia.org/wiki/Software_supply_chain) for compromised or abandoned packages, and track end-of-life before it forces a migration. The OSPO's job is not to approve every dependency by hand. It is to build the guardrails so that ninety-five percent of choices are safe automatically and only the genuinely unusual cases reach a human.

### Contribute upstream because it pays, not because it is nice

Treat upstream contribution as an economic decision. Every private patch you carry against a dependency is a tax you pay on every upgrade, forever, until the change lands upstream or the fork diverges so far you own it outright. Contributing the fix back deletes that tax. Upstreaming also buys influence over direction, so the roadmap of a component you rely on bends toward your needs, and it signals competence to the engineers you want to hire. Give your developers a fast, documented path: a pre-cleared contributor license agreement or developer certificate of origin, a lightweight approval that confirms the change is safe to share, and management time budgeted for the work. When the alternative is maintaining a permanent [fork](https://en.wikipedia.org/wiki/Fork_(software_development)) of a project you do not control, contributing back is almost always cheaper.

### Release your own projects with real governance

When you open-source software you built, do it deliberately or not at all. Decide first whether the code is a commodity worth sharing or a differentiator worth keeping closed, using the reasoning in chapter 10.12. If you release, choose a license that matches your intent (permissive to maximize adoption, copyleft to keep the ecosystem reciprocal), document who decides what through a written governance model, and register the [trademark](https://en.wikipedia.org/wiki/Trademark) on the project name so you can protect it from misuse while keeping the code free. Commit to real stewardship: a public issue tracker, a contribution guide, a code of conduct, and a security policy with coordinated disclosure so reporters know how to reach you (chapter 4.2). Name a maintainer and budget their time. A project you launch with fanfare and abandon in a year does more damage to your reputation than one you never shipped.

### Apply InnerSource to collaborate inside the company

The habits that make open source work (public repositories, clear contribution guides, review by merit, low barriers to a first patch) work just as well behind the firewall. InnerSource means any engineer can find, use, and improve any internal project, sending a pull request across team boundaries instead of filing a ticket and waiting. This breaks down silos, spreads code reuse, and trains your people in the exact workflow they will use when they contribute externally. The OSPO is the natural home for InnerSource because it already owns the tooling and the cultural playbook. Start with a few high-value shared libraries, publish their contribution guides internally, and reward teams that accept outside patches gracefully.

### Fund and sustain the maintainers you depend on

Your production system may rest on a library maintained by one person in their spare time. That is a supply-chain risk, and the honest response is to help carry the load. Identify your most critical dependencies from your bill of materials, find the ones with a thin maintainer base, and choose a response for each: sponsor the maintainer directly, contribute engineering time, join a foundation that funds the project, or, as a last resort, prepare to fork or replace. Funding the commons is cheaper than the emergency that follows its collapse, and it keeps the components you rely on healthy and moving in a direction you can influence.

### Set contribution policy that approves fast

A contribution policy exists to say yes quickly, not to say no slowly. Spell out what an engineer may contribute without asking (bug fixes, documentation, small features to projects you already use), what needs a light check (anything touching a differentiator or a patent), and how intellectual property and contributor agreements are handled once, centrally, rather than per contribution. Automate the boring parts: license checks, a pre-signed corporate contributor agreement, and a bot that flags the rare submission needing human eyes. Measure time-to-approval and treat a slow queue as a bug in the policy.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
| --- | --- | --- |
| Central OSPO | Consistent policy, deep expertise, clear ownership | Can become a bottleneck if it only gates and never enables |
| Federated OSPO (champions in teams) | Scales, keeps decisions close to engineers | Needs strong coordination or policy drifts apart |
| Contribute upstream | Deletes private-patch tax, buys influence, aids recruiting | Ongoing effort, IP review, work on someone else's schedule |
| Carry private forks | Full control, ship on your timeline | Permanent maintenance tax, drifts from upstream security fixes |
| Release your own project | Ecosystem, reputation, shared maintenance | Real stewardship cost; abandonment damages reputation |
| Fund maintainers | Protects critical dependencies, buys goodwill | Direct cost, and picking who to fund is political |
| No OSPO (ad hoc) | Zero setup cost | Invisible legal, security, and sustainability debt |

The central tension is between control and enablement. An OSPO that reviews every dependency and every contribution by hand feels safe, but it becomes the thing engineers route around, which produces the invisible shadow dependencies you were trying to prevent. An OSPO that only publishes cheerful guidance without any automated enforcement is ignored the moment a deadline looms. The resolution is the same one that runs through chapter 10.3: automate the common case so the compliant path is the fastest path, and reserve human judgment for the genuinely novel. Get that balance right and the office is a force multiplier; get it wrong in either direction and it is either a brake or a decoration.

## Questions to discuss with your team

1. **Who owns your relationship with open source today, and could they answer a hard question tomorrow?** If a would-be acquirer's lawyers asked for your license inventory, or a reporter asked which unmaintained library sits in your payment path, is there a name attached to the answer? For most organizations the honest response is "no one," which means every engineer is quietly making policy and no one is accountable for the sum. Bring the evidence to the meeting: try to produce the approved-license list, the software bill of materials, and the person who would field a copyleft question during due diligence. If those artifacts do not exist or point to nobody, you have found your first OSPO task. The decision to make is not whether to have the function but who owns it and what mandate they carry, even if the office is one person for one day a week.

2. **Are you carrying private patches you could upstream, and what is that costing you?** Many teams maintain a quiet pile of local modifications against their dependencies, re-applying them by hand on every upgrade and absorbing the merge pain as if it were a law of nature. Each of those patches is a recurring tax, and each is a candidate to contribute back so the tax disappears. Bring the specifics: list the forks and local patches your build actually carries, estimate the engineering hours each one costs per year, and note which upstream projects would likely accept the change. The competing consideration is real, since upstreaming takes effort now and runs on the maintainer's schedule, but the comparison is against paying the patch tax forever. The answer should turn "we always just re-apply it" into a deliberate choice, with a contribution path fast enough that engineers use it.

3. **Which dependency would hurt most if its maintainer walked away, and what will you do about it?** Somewhere in your stack is a component that would stop a revenue or mission-critical service if it broke, maintained by a person or a handful of people you have never funded or thanked. The commons feels free right up until the moment it is not, and the expensive version of that lesson is a scramble after abandonment or an unpatched vulnerability. Bring your bill of materials and rank dependencies by blast radius, then note the maintainer count and funding status of the top few. For each critical, thinly staffed one, decide in advance whether you will sponsor, contribute time, join a foundation, or prepare to replace. That converts a latent single point of failure into a managed relationship, held to the same standard as any other operational risk (chapter 2.18).

## Examples

**Startup.** A twenty-person startup makes its lead platform engineer the part-time OSPO owner with a one-page charter. She sets a simple consumption policy (permissive licenses pre-approved, copyleft reviewed, scanner in the pipeline), and she notices the team carries three private patches against an open-source queue library, re-applied painfully on every upgrade. She upstreams all three; two are accepted within a month, deleting the upgrade tax for good. She open-sources one small internal tool with a real README, a license, and a security contact, mostly to attract engineers, and she sets up a monthly sponsorship for the solo-maintained parser the product depends on. None of this needs headcount, just a named owner and a clear mandate.

**Enterprise.** A global bank runs a central OSPO of six people plus a federated network of open-source champions embedded in each product group. The central team owns policy, the automated license and export-compliance scanning, and the contributor license agreement that every engineer is covered by from day one. The champions handle local review and coach their teams on contribution. The bank funds several foundations whose projects underpin its trading systems, contributes fixes upstream to a widely used data framework so it stops maintaining a fork, and runs InnerSource across two hundred internal repositories so any team can send a pull request to any other. Time-to-approval for a standard contribution is under two days, tracked as a metric the OSPO reports quarterly.

**Government.** A national digital agency operates under an "open source by default" and public-money-public-code mandate. Its OSPO publishes new services in a public repository unless a documented exemption applies for security or privacy, runs a cross-government catalog so agencies reuse code before building it, and writes open-source and open-standards requirements into procurement so vendors deliver reusable, well-documented code with the government keeping rights. The office also handles coordinated security disclosure for the code it publishes and funds maintenance of a shared identity library that several agencies now depend on, so that no single team silently owns a component the whole government relies on.

## Business case: motivations, ROI, and TCO

The clearest return is the elimination of avoidable, expensive surprises. Unmanaged open source produces crises that arrive on their own schedule: a copyleft violation surfaced during acquisition due diligence, an emergency migration off a dead component, a breach traced to a dependency no inventory listed. An OSPO converts those low-probability, high-cost events into steady, budgeted work. Layer on the recurring savings from upstreaming: every private patch you retire stops taxing every future upgrade, and across a large estate that compounds into real engineering capacity returned to product work.

On the [total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership) ledger, the office is cheap relative to what it protects. Its cost is a small team, some scanning and catalog tooling, and modest maintainer funding. Set that against the cost of not having it: legal liability, failed or delayed due diligence, security incidents, duplicated internal builds of things that already exist as open source, and the slow bleed of forks nobody chose to keep. There are upside returns too that are harder to price but real: influence over the direction of components you depend on, a recruiting and reputation advantage from a credible open-source presence, and faster delivery because engineers reuse instead of rebuild. When you make the case to leadership, frame the OSPO as supply-chain management for the majority of your codebase, with a strategic dividend on top. In government, add the compliance dimension, since openness is often mandated and doing it well avoids both non-compliance and duplicated public spending.

## Anti-patterns and pitfalls

- **The OSPO as a gate.** An office that only reviews and blocks, never enables, gets routed around, producing the shadow dependencies it was meant to prevent.
- **Contribution theater.** Announcing an open-source strategy while making the approval process so slow that no one actually contributes.
- **The abandoned release.** Publishing a project with a launch blog post, then never triaging an issue, damaging your reputation more than silence would.
- **Fork-and-forget.** Forking a dependency for one fix and then carrying it forever, drifting away from upstream security patches.
- **Free-riding on fragile maintainers.** Depending on a critical single-maintainer library and never funding, thanking, or helping the person behind it.
- **Trademark neglect.** Releasing a project without protecting its name, then watching a fork or vendor trade on your reputation.
- **Legal-only ownership.** Housing the OSPO entirely in legal so its guidance carries no engineering credibility and teams tune it out.
- **Vanity metrics.** Counting stars and press mentions instead of dependency health, time-to-approval, and retired private patches.

## Maturity model

- **Level 1, Initial:** Engineers add, patch, and occasionally publish open source with no policy and no owner. Contributions happen by accident or personal initiative. Private forks accumulate unnoticed and no one funds any upstream project.
- **Level 2, Managed:** A basic consumption policy and approved-license list exist, and someone is loosely responsible. Contribution is allowed but slow and case-by-case. A few critical dependencies are known, but sustainability and releases are ad hoc.
- **Level 3, Defined:** A chartered OSPO owns consumption, contribution, releasing, and community. Scanning and a bill of materials are automated, a pre-cleared contributor agreement and fast approval path exist, released projects have real governance and security policies, and InnerSource is spreading. Government teams publish by default.
- **Level 4, Optimizing:** Open source is a managed strategic capability. Contribution is routine and measured, critical maintainers are funded, the organization stewards well-run projects and steers ecosystems it depends on, InnerSource is the norm, and engagement metrics feed continuous improvement.

## Ideas for discussion

1. Where is the line between an OSPO that enables and one that gates, and how would you know from the outside which one you have built?
2. Which of your private patches or forks are you carrying out of habit rather than necessity, and what would it take to upstream the top three?
3. How should you decide which maintainers and foundations to fund when the list of critical dependencies is longer than the budget?
4. What would genuinely change in your next release if you had to publish it with real governance, a trademark, and a coordinated disclosure policy from day one?
5. For public-sector readers, what is a defensible process for exempting code from publish-by-default without quietly eroding the principle?
6. Which internal libraries would benefit most from InnerSource, and what is stopping another team from sending you a pull request today?

## Key takeaways

- An OSPO owns the whole relationship with open source: consuming responsibly, contributing upstream, releasing your own projects, and sustaining the maintainers you depend on.
- Contributing upstream is strategy, not charity; it deletes the recurring tax of private patches, buys influence over direction, and helps you recruit.
- Make the compliant path the fastest path through automation and curation, so the office enables engineers instead of gating them.
- Release your own projects only with real governance, a chosen license, a protected trademark, and coordinated security disclosure, or do not release them at all.
- Fund and help the critical maintainers your production system rests on, because the commons is not self-sustaining.
- Apply InnerSource to bring open-source collaboration inside the company, and in government, default to open, publish by default, and reuse before you build.

## References and further reading

- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Nadia Eghbal, *Roads and Bridges: The Unseen Labor Behind Our Digital Infrastructure*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Danese Cooper and Klaas-Jan Stol (editors), *Adopting InnerSource: Principles and Case Studies*
- The Linux Foundation and TODO Group, *OSPO guides and Open Source Program Office resources*
- The Linux Foundation and TODO Group, *State of OSPOs and Open Source Management* (annual survey series)
- Heather Meeker, *Open (Source) for Business*
- Open Source Initiative, *The Open Source Definition* and approved-license list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- U.S. Federal Source Code Policy and Code.gov guidance
