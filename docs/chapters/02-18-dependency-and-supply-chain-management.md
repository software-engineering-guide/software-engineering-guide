# 2.18 Dependency and supply-chain management

## Overview and motivation

Open your project's lockfile and count the packages. If you are like most teams, the code you wrote is a thin layer on top of hundreds or thousands of [dependencies](https://en.wikipedia.org/wiki/Coupling_(computer_programming)) you did not write, do not fully understand, and cannot easily audit. A modern web service pulls in a framework, a database driver, a logging library, and a serialization format, and each of those pulls in more. The result is that most of your running software, often the large majority of it, came from strangers on the internet. That is not a failure. It is the deal that lets a small team ship in weeks what once took years. The point is to take the deal with your eyes open.

Managing that borrowed code well is an engineering discipline in its own right, and this chapter is about the craft of it: how you choose dependencies, pin them, update them, reproduce your builds, and keep the whole graph legible as it grows. The security threat side, where an attacker deliberately poisons that graph, gets its full treatment in chapter 4.2 on application security. Here the concern is the everyday engineering: version constraints, lockfiles, transitive conflicts, update cadence, and knowing what is in your software. Get this right and security becomes far easier, because you cannot defend a supply chain you cannot see.

For large teams, and especially for enterprise and government, the stakes rise with scale. When five hundred repositories each choose their own libraries, you get five hundred slightly different versions of the same logging framework, a licence nobody approved, and no way to answer "are we affected?" when a serious vulnerability lands. Enterprises answer this with approved libraries and shared registries. Governments increasingly answer it with mandates: the United States Executive Order 14028 pushed a [software bill of materials](https://en.wikipedia.org/wiki/Software_supply_chain) (SBOM) and build provenance into the baseline for software they buy. The organizations that stay calm during the next dependency crisis are the ones who did this work before they needed it.

## Key principles

- Most of your software is code you did not write; own the responsibility even though you did not write it.
- Every dependency is a permanent liability as much as an asset; add them deliberately, not reflexively.
- Pin versions with lockfiles so builds are reproducible and deterministic, not "whatever was latest that day."
- Update on a steady cadence, in small automated increments, rather than in rare terrifying leaps.
- Know exactly what is in your software; you cannot secure or license what you cannot enumerate.
- Prefer fewer, well-maintained dependencies over many convenient ones.
- Control where packages come from; an unverified registry is an open door.

## Recommendations

### Understand versioning and constrain it deliberately

Learn how your ecosystem expresses versions, because your update behaviour rides entirely on it. Most package managers use some form of [semantic versioning](https://en.wikipedia.org/wiki/Software_versioning) (SemVer), where a version reads as MAJOR.MINOR.PATCH: a patch bump promises bug fixes only, a minor bump adds backward-compatible features, and a major bump signals breaking changes. Your dependency declarations then set a constraint, such as "compatible with 4.x" or "at least 2.3.0," which tells the resolver how far it may roam when it picks versions.

Be intentional about how loose or tight those constraints are. Loose ranges pick up fixes automatically, at the cost of letting a minor release you never reviewed slip into production; tight pins give control at the cost of manual effort. The pragmatic answer for most teams is to declare reasonably permissive ranges in your manifest, then freeze the exact resolved versions in a lockfile so the range is only re-evaluated when you deliberately update. Treat SemVer as a promise maintainers try to keep, not a guarantee they always do; a "patch" release can still break you, which is exactly why you test updates rather than trust them.

### Commit lockfiles and demand reproducible builds

A lockfile records the exact version and cryptographic hash of every package in your dependency graph, direct and transitive alike. Commit it to version control (chapter 2.6) and treat it as a first-class part of your source. Its job is to make your build a function: the same inputs produce the same output every time, on every machine, this year and next. Without it, two engineers running "install" a week apart can get different code, and a bug that appears in production may be impossible to reproduce on the laptop that built it.

Aim for genuinely [reproducible builds](https://en.wikipedia.org/wiki/Reproducible_builds), where a given commit always yields a behaviour-identical artifact. In continuous integration (chapter 8.1), install strictly from the lockfile and fail the build if the lockfile and manifest disagree, rather than silently resolving fresh versions. The hashes in the lockfile do double duty: they pin behaviour and they detect tampering, because a package whose content no longer matches its recorded hash will not install. Reproducibility is the foundation everything else in this chapter stands on.

### Manage transitive dependencies and diamond conflicts on purpose

Your direct dependencies are only the ones you named. Beneath them sits a much larger graph of transitive dependencies, the packages your packages depend on, and that is where most of your risk and most of your surprises live. A classic failure is the diamond dependency: library A needs version 1 of a shared utility, library B needs version 2, and now the resolver must reconcile an impossible request. Some ecosystems allow multiple versions to coexist, trading disk and memory for peace; others force a single version and leave you to broker the conflict.

Make these conflicts visible instead of letting them fester. Use your tooling to print the full dependency tree and to explain why a given package is present and who pulled it in. When a conflict appears, resolve it deliberately: upgrade the laggard, pin an override, or drop a dependency whose demands you cannot satisfy. Watch the graph's growth over time, because unchecked sprawl in transitive dependencies is a slow accumulation of [technical debt](https://en.wikipedia.org/wiki/Technical_debt) that eventually shows up as an unsolvable upgrade or a vulnerability you cannot patch without a rewrite.

### Update on a steady cadence with automated pull requests

The riskiest update strategy is the one most teams drift into by accident: never update, then update everything at once under emergency pressure when a critical vulnerability forces your hand. By then you are years behind, the changelogs are a wall, and the upgrade is a multi-week project instead of a routine chore. The fix is cadence. Adopt an automated dependency updater (the Dependabot and Renovate tools are common examples) that opens a pull request whenever a dependency has a new version, complete with the changelog and your test results attached.

Then tune the flow so it helps rather than drowns you. A firehose of individual pull requests every morning trains people to ignore them, which is worse than no automation at all. Batch low-risk updates such as patch releases, let them merge automatically when tests pass, and reserve human attention for major-version bumps and anything that touches a sensitive library. Set a rhythm the team can sustain, perhaps a weekly review, so updating stays a small steady tax rather than a rare painful bill. This is exactly where a strong testing strategy (chapter 2.4) pays off, because automated updates are only safe if your tests can catch what they break.

### Minimize your footprint and evaluate before you adopt

Every dependency you add is a standing commitment: to its bugs, its vulnerabilities, its licence, its maintainer's continued interest, and its own growing graph of sub-dependencies. The cheapest dependency to manage is the one you did not add. Before reaching for a package, ask whether a few dozen lines of your own code would do, especially for trivial functionality. The history of package ecosystems is full of cautionary tales where a tiny, widely-depended-upon package was removed or hijacked and broke half the internet.

When you do adopt, evaluate the candidate like the long-term relationship it is. Check maintenance health: recent commits, responsive maintainers, a real release history, and more than one person with the keys. Check the licence and confirm it is on your approved list (chapter 10.3). Check its security track record, its size, and its own transitive footprint, because a small feature is not worth dragging in a hundred packages. Write these criteria down so "should we add this?" is a checklist your whole team applies consistently, not a mood.

### Produce an SBOM and capture build provenance

You cannot answer "are we affected by this vulnerability?" quickly unless you already know what is in your software. An SBOM is the answer: a machine-readable inventory of every component in a build, with versions and licences, in a standard format such as SPDX or CycloneDX. Generate one automatically as part of your build pipeline, store it alongside the artifact, and keep it for as long as that artifact runs anywhere. When the next headline vulnerability drops, a query against your SBOMs turns a week of frantic grep into a five-minute report.

Go one step further and capture provenance: a signed, tamper-evident record of how an artifact was built, from which source commit, by which pipeline. The [open-source software](https://en.wikipedia.org/wiki/Open-source_software) community has converged on the SLSA framework (Supply-chain Levels for Software Artifacts) as a graded model for exactly this, moving from "we can describe our build" up to "we can prove it, and the proof resists a compromised build system." Attestation lets a consumer verify that an artifact really came from your pipeline. For government work this is increasingly not optional; provenance and SBOM sit inside procurement mandates, so building the capability early keeps you eligible to bid.

### Control your sources with registries, mirrors, and vendoring

Where your packages come from is as important as which packages you choose. Pull directly from the public internet on every build and you inherit its outages, its yanked versions, and its attackers. Stand up an internal package registry or a caching mirror that proxies the public ecosystem, so builds are fast, repeatable, and insulated from upstream disappearing. The registry also becomes the natural place to enforce policy: block known-bad versions, quarantine new releases for a short soak, and refuse packages that fail your licence or security gates.

Configure that registry carefully to avoid two specific traps. Dependency confusion happens when a build tool, offered both a private internal package and a public package of the same name, fetches the attacker's public one; you defend against it by scoping internal names and pinning internal packages to the internal source explicitly. [Typosquatting](https://en.wikipedia.org/wiki/Typosquatting) happens when a malicious package uses a name one keystroke away from a popular one and waits for a fat finger; a curated registry with an allowlist blocks it at the door. For a small set of critical or slow-moving dependencies, consider vendoring, checking the actual dependency source into your own repository, so your build has zero external dependencies at all. It trades update convenience for total control, which is sometimes exactly right.

## Trade-offs: pros and cons

| Approach | Pros | Cons |
| --- | --- | --- |
| Loose version ranges | Automatic fixes; low manual effort | Unreviewed code reaches production; nondeterministic without a lockfile |
| Strict pinning plus lockfile | Reproducible, auditable builds | Requires deliberate update work; can lag on fixes |
| Aggressive update cadence | Small, safe steps; always near current | Constant churn; steady reviewer attention needed |
| Rare, batched big upgrades | Fewer interruptions day to day | Terrifying, risky, expensive when forced |
| Many convenient dependencies | Fast to build features | Large attack surface; heavy maintenance load |
| Minimal footprint plus vendoring | Control, small surface, no upstream risk | More code you own; you carry the updates yourself |
| Public registry direct | Zero setup | Outages, yanks, confusion and typosquatting exposure |
| Internal registry and mirror | Speed, policy enforcement, insulation | Infrastructure to run and maintain |

The central tension runs between velocity and control. Every choice above is the same dial viewed from a different angle: how much of your borrowed code will you actively govern, and how much will you let flow in on trust? Lean too far toward control and you drown in manual review, fall behind on security fixes, and slow the team that dependencies were supposed to speed up. Lean too far toward velocity and you wake up one day with an unauditable, unupgradeable graph and a licence violation you cannot explain to counsel. The resolution is a posture, not a fixed point: lock and reproduce everything, update continuously in small steps, minimize what you take on, and enforce policy at a chokepoint you control. That combination buys you both speed and safety, which is the trade worth making at scale.

## Questions to discuss with your team

1. **What is your real update cadence, and would a forced emergency upgrade take hours or weeks?** Most teams cannot answer this honestly until a critical vulnerability forces the issue. The chapter treats steady, automated, small-step updating as the safe path and the rare big-bang upgrade as the dangerous one, because the gap you let open is the gap you must sprint across under pressure later. Bring the evidence: how many of your dependencies are more than one major version behind, and how long your last significant upgrade actually took. Discuss whether you can adopt an automated updater, how you will batch low-risk changes so people do not tune out, and what testing you need for auto-merge to be safe. The answer should change how you budget engineering time, turning a rare crisis into a routine weekly tax. If the honest answer is "weeks," that is a risk to name now, not to discover mid-incident.

2. **If a serious vulnerability were announced in a common library right now, how fast could you list every affected artifact you run?** This is the question an SBOM exists to answer, and the speed of your answer is a direct measure of your supply-chain maturity. Without an inventory you are reduced to grepping repositories and interviewing teams, which takes days you may not have while the clock runs. Bring the concrete signal: do you generate an SBOM per build, where is it stored, and can you actually query across all of them today? Discuss whether you know not just direct dependencies but the transitive graph, since the vulnerable package is usually one you never named. The answer determines whether your next incident is a query or a fire drill, and it is worth building the capability before you need it. Governments now mandate this for exactly that reason.

3. **How do you decide whether a new dependency is worth adopting, and does everyone apply the same bar?** The chapter argues that every dependency is a permanent liability as well as a convenience, and that the cheapest one to manage is the one you never added. Yet on most teams the decision is invisible: an engineer needs a feature, finds a package, and it is in the lockfile by lunch with no review of its maintenance, licence, security history, or footprint. Bring examples from your own graph of packages nobody remembers adopting and could not defend today. Discuss whether a written evaluation checklist and an approved-library list (chapter 10.3) would help or just add friction, and where the line sits between trivial helpers you should write yourself and real infrastructure worth depending on. The answer shapes the long-term weight your team carries, one small decision at a time.

4. **Do you actually govern your transitive dependencies, or only the ones you named?** Most of your risk lives one level down, in the packages your packages pulled in, and a diamond conflict where two libraries demand incompatible versions of a shared utility can block an upgrade at the worst possible moment. This matters at scale because a single unpatchable transitive package can freeze a security fix across hundreds of repositories, and the competing pull is real: surfacing and pinning the full graph costs ongoing effort, while ignoring it trades that effort for a slow accumulation of debt that surfaces as an unsolvable upgrade. Bring the evidence: can your tooling print the full tree and explain why any given package is present and who pulled it in, and how many distinct versions of your most common libraries coexist today? For enterprise and government, add whether your inventory and policy reach transitive components at all, because a mandate to know what is in your software is meaningless if half the graph is invisible to you. The answer tells you whether your next forced upgrade is a routine merge or a multi-team excavation.

5. **Where do your packages actually come from, and what stops an attacker from slipping one in?** Every build that pulls directly from the public internet inherits its outages, its yanked versions, and two specific attacks: dependency confusion, where a build tool fetches a public package that shadows your private one, and typosquatting, where a malicious package sits one keystroke away from a popular name. This matters for a large team because a single poisoned fetch can propagate through your whole estate before anyone notices, and the trade-off is genuine: an internal registry or caching mirror gives you a policy chokepoint and insulation from upstream, but it is infrastructure someone has to run and keep current. Bring the concrete signal: do internal package names get scoped and pinned to the internal source explicitly, is there an allowlist, and does any new release get a short quarantine before it can be used? For government and regulated buyers, tie this to the approved-software-list and no-direct-internet posture that procurement increasingly demands, and be honest about whether your current setup would pass that bar today.

6. **Can you actually reproduce and prove how your artifacts were built?** A committed lockfile with cryptographic hashes should make your build a function, the same inputs yielding the same output on every machine this year and next, and provenance should let anyone verify that an artifact really came from your pipeline and source commit. This matters because an unreproducible build turns a production bug into an unsolvable mystery and leaves you unable to prove tampering did not occur, and the competing consideration is effort versus assurance: strict lockfile installs, signed attestation, and SLSA-aligned provenance cost setup and discipline that a "just install latest" flow avoids. Bring the evidence: does continuous integration fail when the lockfile and manifest disagree, do you generate and store an SBOM and a signed provenance record per build, and has anyone ever verified one? For enterprise and especially government work, provenance and SBOM increasingly sit inside procurement mandates, so the honest answer here decides whether you stay eligible to bid or get shut out.

## Sector lens

**Startup.** With a tiny team and no platform group, lean on defaults and automation instead of process. Commit lockfiles from the first day, turn on an automated updater that batches patch releases and auto-merges on green tests, and keep one lightweight rule for adding packages: prefer boring, well-maintained libraries and think twice about tiny ones. You will not build an internal registry yet, and that is fine, but the committed hashes alone already protect you: a poisoned version simply will not install.

**Small business.** You have no dependency specialist and a tight budget, so buy the discipline rather than build it. Rely on the update automation your hosting and code platform already provide, favour a small set of mature libraries so upgrades stay cheap, and use a free SBOM generator in your pipeline so you can answer "are we affected?" without staffing for it. Spend your scarce attention on licence checks and on not adopting trivial packages you could write in a dozen lines yourself.

**Enterprise.** The problem is consistency across many teams: a shared internal registry that mirrors the public ecosystem and enforces licence, source, and version policy at one chokepoint, plus a curated set of golden libraries as the default and a documented exception path for anything else. Emit an SBOM per build into a central store so one query answers your exposure across the whole estate, roll coordinated upgrades through automated pull requests, and treat dependency health as a measured, governed portfolio rather than a per-repo accident.

**Government.** Procurement rules and public accountability shape everything. Require vendors to deliver a machine-readable SBOM and SLSA-aligned build provenance with every release, install internally only from an approved software list served by a mirror with no direct path to the public internet, and favour dependencies with stable maintenance and clear licensing because a system may run for fifteen years and must be patchable for all of them. Plan end-of-life migrations deliberately rather than as emergencies, and keep the records that let an auditor trace any shipped artifact back to its source.

## Examples

**Startup.** A six-person startup ships a web application built on a framework, a payment library, and roughly nine hundred transitive packages they have never inspected. They cannot afford a platform team, so they lean on automation: lockfiles committed from day one, an automated updater that batches patch releases and merges them on green tests, and a monthly hour to review the major-version bumps that piled up. Their one-paragraph rule for adding dependencies is mostly "prefer boring, well-maintained libraries, and think twice about tiny ones." When a popular package was compromised, their committed lockfile hashes meant the poisoned version simply would not install, and they read about the incident rather than living it.

**Enterprise.** A bank with four hundred repositories runs an internal package registry that mirrors the public ecosystem and enforces policy at that chokepoint. A curated set of golden libraries, one approved logging framework, one HTTP client, one JSON parser, is the default, and anything else requires a documented exception. An inner-source model lets any team contribute to those shared libraries while a small platform group owns their health. Coordinated upgrades roll a security patch across all four hundred repositories through automated pull requests in a matter of days, and every build emits an SBOM into a central store. When a critical vulnerability is announced, they run one query and know their exposure before the news cycle finishes.

**Government.** A federal agency procures software under provenance and SBOM requirements traceable to Executive Order 14028. Vendors must deliver a machine-readable SBOM with every release and demonstrate build provenance aligned to the SLSA framework, so the agency can verify that each artifact came from the claimed source. Internally, developers may install only from an approved software list served by an internal mirror with no direct path to the public internet. Long-term supportability drives the choices: they favor dependencies with stable maintenance and clear licensing, because a system may run for fifteen years and must be patchable for all of them. When a component reaches end of life, a planned migration replaces it rather than an emergency.

## Business case: motivations, ROI, and TCO

The return on dependency discipline is mostly measured in disasters that never happen. A committed lockfile and reproducible build cost almost nothing to adopt and eliminate an entire class of "works on my machine" defects and unreproducible production bugs, each of which can burn days of senior engineering time. An automated update cadence converts the occasional multi-week emergency upgrade, the kind that stalls a roadmap and exhausts a team, into a steady low hum of small merged changes. Across a portfolio of many repositories, that shift from rare-and-huge to frequent-and-tiny is one of the highest-leverage process changes available to an engineering organization.

The total cost of ownership argument is about what you carry over years, not what you spend this sprint. Unmanaged dependencies accrue quietly: outdated versions that can no longer be upgraded without a rewrite, licences that create legal exposure nobody priced in, and a graph so tangled that a single required patch triggers a cascade of breaking changes. The cost of not doing this arrives all at once and at the worst time, during a security incident or an audit or a forced migration, when the bill for years of deferred maintenance comes due with interest. To make the case to leadership, frame it in their language: reproducible builds reduce incident cost, SBOMs cut vulnerability-response time from days to minutes, and approved libraries plus provenance keep you eligible for regulated and government contracts you would otherwise be shut out of.

## Anti-patterns and pitfalls

- **No lockfile, or an uncommitted one:** builds resolve fresh each time, so nobody can reliably reproduce what shipped or what broke.
- **Floating "latest" in production:** whatever the registry served that minute becomes your release, unreviewed and untraceable.
- **Never updating until forced:** years of drift collapse into one terrifying, high-risk emergency upgrade under vulnerability pressure.
- **Update-bot fatigue:** an unbatched firehose of pull requests trains the team to ignore them all, including the urgent ones.
- **Dependency sprawl:** adding packages reflexively for trivial features, growing an unmaintainable graph and a wide attack surface.
- **No inventory:** without an SBOM, answering "are we affected?" means days of manual archaeology across repositories.
- **Trusting the public registry blindly:** direct pulls expose you to outages, yanked versions, dependency confusion, and typosquatting.
- **Ignoring transitive dependencies:** governing only what you named while most of your risk hides one level down.
- **Unvetted licences:** pulling in code whose licence conflicts with how you ship, discovered only during an audit or acquisition.

## Maturity model

- **Level 1, Initiate:** Dependencies are added freely with no evaluation. There is no committed lockfile, builds are not reproducible, updates happen only in forced emergencies, and nobody can enumerate what the software contains.
- **Level 2, Develop:** Some teams commit lockfiles and get mostly reproducible builds, and a little automation opens update pull requests, but practice is inconsistent from repository to repository. Awareness of licences and transitive risk is informal, with no shared policy, inventory, or control over where packages come from.
- **Level 3, Standardize:** Practices are documented and enforced org-wide. An automated updater runs on a steady cadence with sensible batching, builds install strictly from lockfiles and fail when the lockfile and manifest disagree, an SBOM is generated per build, an internal registry enforces source and licence policy, and new dependencies are evaluated against a written checklist that every team applies.
- **Level 4, Manage:** The dependency estate is measured and controlled with data against baselines. You track version lag (how many dependencies sit more than one major version behind), mean time to patch a critical vulnerability across all artifacts, automated-update merge rates, SBOM coverage as a percentage of shipped builds, and the count of unresolved diamond conflicts and policy exceptions. These metrics gate releases and drive where you spend effort, so upgrades and remediation are managed by evidence rather than by whoever shouts loudest.
- **Level 5, Orchestrate:** Dependency management is continuously improved and integrated across the organization. Build provenance and attestation are captured and verified, SBOMs are queryable across the whole portfolio for instant vulnerability response, coordinated upgrades roll across many repositories automatically, golden libraries are curated and inner-sourced, and the whole system adapts as the ecosystem, threats, and procurement mandates shift.

## Ideas for discussion

1. Where is the right line for your team between writing a small utility yourself and taking on a dependency for it?
2. How loose or tight should your version constraints be, and does that answer differ for applications versus published libraries?
3. Should low-risk patch updates auto-merge on green tests, and what would your test suite need to make that safe?
4. Is an internal registry or mirror worth the operational cost for your organization's size and risk profile?
5. How would you prioritize which dependencies to vendor for maximum control, and which to leave on the public registry?
6. What would it take to generate and actually use an SBOM for every artifact you ship, starting this quarter?

## Key takeaways

- Most of your software is borrowed code; managing it well is a core engineering discipline, not an afterthought.
- Commit lockfiles and demand reproducible, deterministic builds so the same inputs always produce the same output.
- Update continuously in small automated steps instead of rare, forced, terrifying leaps.
- Add dependencies deliberately against a written bar; the cheapest one to manage is the one you never took on.
- Generate an SBOM and capture provenance so you always know what is in your software and where it came from.
- Control your sources with an internal registry to defend against confusion, typosquatting, and upstream failure.

## References and further reading

- U.S. Executive Order 14028, *Improving the Nation's Cybersecurity* (2021)
- National Institute of Standards and Technology (NIST), *Secure Software Development Framework* (SP 800-218)
- SLSA (Supply-chain Levels for Software Artifacts) framework specification, Open Source Security Foundation
- OWASP CycloneDX specification and the SPDX specification, for SBOM formats
- Tom Preston-Werner, *Semantic Versioning Specification (SemVer)*
- The Reproducible Builds project documentation
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
