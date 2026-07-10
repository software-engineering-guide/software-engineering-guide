# 2.6 Version control and source management

## Overview and motivation

Think of [version control](https://en.wikipedia.org/wiki/Version_control) as your codebase's system of record. It captures every change, including who made it, when, and why, and it lets many people work on the same software without overwriting each other. For a large organization, it is far more than a backup. It is the foundation that collaboration, [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), auditing, and release management all rest on. The choices you make about branching, repository structure, and commit discipline shape how fast your team can move, and how safely.

For large teams, source management is really a coordination problem at scale. When hundreds of engineers push changes into shared code, they need a strategy that keeps merges small, keeps the mainline releasable, and keeps history readable. A team that integrates continuously flows smoothly. A team that lets branches diverge for weeks lurches from one integration crisis to the next. Your repository structure, one big repo or many, shapes how teams share code and coordinate too.

Enterprise and government settings add a few more demands: traceability, access control, and retention. A change may need to link to an approved work item for audit. Secrets must never enter history. Repository access must respect security boundaries. Here, your version-control practices become part of the organization's control framework, and a mistake such as a leaked secret or an unauditable history can have serious consequences.

## Key principles

- Integrate small changes frequently; long divergence is the root of merge pain.
- Keep the mainline always releasable.
- History is documentation; write commits for the future reader who must understand why.
- Never commit secrets; treat any secret that reaches history as compromised.
- Automate enforcement of hygiene (hooks, CI checks) rather than relying on discipline alone.
- Choose repository structure (mono vs poly) by how teams actually share code and coordinate, not by fashion.
- Link changes to their rationale (work items, tickets, or decisions) for traceability.

## Recommendations

### Prefer trunk-based development with short-lived branches

Lean toward [trunk-based development](https://en.wikipedia.org/wiki/Trunk-based_development): integrate to a shared mainline often, using short-lived feature branches measured in hours or days, not weeks. Short branches keep merges small and integration continuous, and that habit is strongly associated with high delivery performance. When work isn't finished yet, don't park it on a long-lived branch. Use [feature flags](https://en.wikipedia.org/wiki/Feature_toggle), runtime switches that hide unfinished work, so you can merge it safely instead. Save long-lived release branches for genuine multi-version support, and go in knowing the maintenance cost they carry.

### Choose a branching model that fits release cadence

Match your [branching model](https://en.wikipedia.org/wiki/Branching_(version_control)) to how you actually release. If you deploy continuously, trunk-based development with minimal branching serves you well. If you ship versioned releases to customers, or support several live versions at once, you may need release branches and back-porting. Steer clear of heavyweight models with many long-lived branches unless your release model truly demands them, because they multiply merge and maintenance overhead.

### Decide monorepo vs polyrepo deliberately

Reach for a [monorepo](https://en.wikipedia.org/wiki/Monorepo), a single repository holding many projects, when teams share code heavily, need atomic cross-project changes, and want unified tooling and visibility. In return, you accept the need for scaled build tooling and access controls. Reach for polyrepos, separate repositories per project or service, when teams and services are genuinely independent, want isolated access and release cycles, and don't need atomic cross-repo changes. In return, you accept the cost of coordinating changes that span repositories. Both work at scale. It's the wrong choice for your coupling pattern that creates constant friction.

### Enforce commit hygiene and conventional commits

Ask for commit messages that explain why a change was made, not just what. Adopt a convention such as conventional commits so messages are structured and machine-parseable, which lets you automate changelogs and versioning. Keep commits atomic, one logical change each, so history stays bisectable and easy to revert. Let hooks and CI checks enforce message format and basic hygiene, rather than leaning on memory.

### Keep large binaries and generated code out of ordinary history

Don't commit large binary assets straight into the main history, because they bloat every clone forever. Use a large-file storage mechanism or an artifact repository instead. As a rule, avoid committing generated code too; generate it in the build. When you genuinely must commit a generated artifact, isolate it and mark it clearly so it doesn't pollute reviews and diffs.

### Prevent secrets from ever entering the repository

Put automated secret scanning in your pre-commit hooks and CI so credentials get blocked before they ever land. Give engineers a proper secrets-management system, so they never need to hardcode a credential in the first place. And treat any secret that does reach history as compromised: rotate it right away. Once a secret has been pushed and cloned, removing it from history is difficult and unreliable.

### Establish access control and traceability

Set up repository access to respect security boundaries and [least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Link commits or pull requests to work items, so every change traces back to its rationale, which helps both day-to-day engineering context and audit. Protect your key branches with required checks and reviews, so nothing merges without clearing the gates you agreed on.

## Trade-offs: pros and cons

| Choice | Pros | Cons |
|---|---|---|
| Trunk-based development | Continuous integration; small merges; high flow | Requires feature flags and discipline; less isolation |
| Long-lived feature branches | Strong isolation of in-progress work | Painful merges; delayed integration; drift |
| Monorepo | Atomic cross-project changes; shared tooling; visibility | Needs scaled build tooling; coarse access control by default |
| Polyrepo | Independent releases; isolated access; simple per-repo tooling | Hard cross-repo changes; version coordination overhead |
| Conventional commits | Automated changelogs and versioning; consistent history | Upfront convention; enforcement needed |

The big trade-off here is integration frequency versus isolation. Long-lived branches feel safer because your work sits off on its own, but that very isolation is what causes the expensive merges and integration surprises later. Trunk-based development gives up that feeling of isolation in exchange for continuous, cheap integration, and asks you to bring feature flags and discipline. The monorepo/polyrepo decision trades cross-project ease against team independence. Pick the one that matches how tightly your code is actually coupled.

## Questions to discuss with your team

1. **What checks must pass before anything merges to your protected mainline, and is that mainline truly always releasable?** This chapter treats a releasable mainline as a core principle and calls an unprotected mainline, where broken or unreviewed code reaches the branch everyone depends on, an anti-pattern. On a large team a red mainline blocks everyone at once, so the gate you require is a shared safety property, not a personal one. Bring the evidence: what your branch protection actually enforces today, and how often the mainline is currently broken. Decide the required set, passing tests, security scans, and review, and make the mainline releasable by policy rather than by hope. That gate is what lets many people integrate continuously without fear.

2. **Is adopting conventional commits worth the convention overhead for your team, given what it automates?** The chapter recommends structured, machine-parseable commit messages precisely because they let you automate changelogs and versioning, and it asks for atomic commits so history stays bisectable and revertible. The trade-off is real: you pay an upfront convention and need enforcement, in exchange for generated release notes and reliable history. Bring the signal of what you do manually today, such as hand-writing changelogs or hunting for which commit introduced a regression. If you release often or maintain multiple versions, the automation usually pays for itself; if you rarely cut releases, a lighter convention may be enough. Let hooks and CI enforce the format so it does not rely on memory.

3. **Have you accepted the operational cost your repository structure demands, whether monorepo tooling or cross-repo coordination?** This chapter says both monorepo and polyrepo work at scale, and that the wrong choice for your coupling pattern is what creates constant friction. A monorepo needs scaled build tooling and finer-grained access control, while polyrepos make any change spanning repositories a coordination project with version-skew risk. Bring the concrete signal: how often your changes cross project boundaries, and whether your build and access tooling can carry the structure you have. If cross-project atomic changes are common, invest in monorepo tooling; if teams and services are genuinely independent, accept the cross-repo coordination cost deliberately. The point is to match structure to how tightly your code is actually coupled, then fund the tooling that structure requires.

## Examples

**Startup.** A three-person startup works trunk-based out of both habit and necessity, merging short-lived branches into main several times a day and hiding half-finished features behind simple flags. They turn on secret scanning in CI from the first commit, because a leaked API key in a public repo could sink a company that has no security team to contain the fallout. One repository, a protected main branch, and meaningful commit messages give them enough discipline to move fast without tripping over their own history.

**Enterprise.** A large technology company runs a monorepo with hundreds of services and shared libraries. Scaled build tooling and code-ownership rules route each change to the right reviewers. A single commit can atomically update a shared library and every consumer at once, sidestepping the version-skew problems that plague distributed repositories. Trunk-based development with feature flags keeps the mainline releasable, and secret scanning blocks credentials at commit time across the whole repository.

**Government.** A national defense contractor holds to strict traceability. Every commit must reference an approved work item. Branch protection requires passing security scans and independent review, and access is tightly controlled per classification boundary. Secret scanning is mandatory, and any exposed credential triggers immediate rotation under an incident process. Long-lived release branches support multiple deployed versions across sites that can't all upgrade at once, with disciplined back-porting of security fixes.

## Business case: motivations, ROI, and TCO

Sound source management is nearly free to adopt and expensive to go without. Trunk-based development and continuous integration are among the practices most strongly associated with high software-delivery performance, which in turn correlates with better organizational outcomes. Clean, traceable history cuts the time it takes to diagnose incidents and satisfy audits, and disciplined branching spares you the recurring, unbudgeted cost of integration crises and merge marathons.

The biggest lopsided risk is secrets in version control. A single leaked credential can cause a breach whose cost dwarfs any tooling investment, and history makes such leaks stick around. Preventing them is cheap; cleaning up after them is not. Poor structure choices show up as chronic friction: every cross-repo change becomes a coordination project, or every monorepo build becomes a bottleneck. To make the case to leadership, tie your branching strategy to delivery metrics and incident-diagnosis time, and frame secret scanning and access control as low-cost controls against high-cost breach and audit risk.

## Anti-patterns and pitfalls

- **Long-lived divergent branches:** weeks of isolated work that merge into painful, risky integration events.
- **Secrets in history:** hardcoded credentials that persist in clones forever and require rotation once exposed.
- **Committing large binaries to main history:** permanently bloating every clone and slowing all operations.
- **Meaningless commit messages:** "fix", "wip", "changes" that destroy the value of history as documentation.
- **Committing generated code as if handwritten:** noisy diffs, merge conflicts, and confusion about the source of truth.
- **Wrong repo structure for the coupling:** polyrepos for tightly coupled code, or monorepos without scaled tooling.
- **Unprotected mainline:** no required checks, so broken or unreviewed code reaches the branch everyone depends on.

## Maturity model

- **Level 1, Initial:** Ad hoc branching; long-lived branches; poor messages; no secret scanning; frequent merge pain.
- **Level 2, Repeatable:** A consistent branching model and message conventions exist, but branches still live too long and enforcement is partial.
- **Level 3, Defined:** Trunk-based development with short branches, protected mainline, enforced commit conventions, secret scanning, and a deliberate repo structure.
- **Level 4, Optimizing:** Source practices are measured against delivery metrics, automation enforces hygiene end to end, and structure and branching evolve with the organization's needs.

## Ideas for discussion

- Is your team's branch lifetime actually short, and if not, what is preventing continuous integration?
- Does your monorepo or polyrepo choice match how coupled your code really is?
- How do you handle large binaries and generated artifacts today, and what does it cost you?
- What would happen if a live credential were committed right now, and how fast would you detect and rotate it?
- How much commit-message and traceability discipline is worth enforcing for your context?
- How do feature flags change your branching strategy, and what new risks do they introduce?

## Key takeaways

- Integrate frequently with short-lived branches; long divergence causes the pain it seems to avoid.
- Keep the mainline releasable and protected by required checks.
- Never let secrets enter history; scan automatically and rotate immediately if they do.
- Choose monorepo or polyrepo by your real coupling and coordination needs.
- Treat commit history as documentation, with meaningful, conventional, atomic commits.

## References and further reading

- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Jez Humble and David Farley, *Continuous Delivery*
- Scott Chacon and Ben Straub, *Pro Git*
- Paul Hammant and others, writings on trunk-based development
- Conventional Commits specification (as a reference standard)
- Martin Fowler, articles on branching patterns and continuous integration
