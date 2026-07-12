# 8.1 CI/CD and delivery

## Overview and motivation

[Continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) and [continuous delivery](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) are the connective tissue between writing code and putting it in front of users safely. Continuous integration means every change is merged frequently into a shared mainline, then automatically built and tested, so integration problems surface within minutes rather than at the end of a long release cycle. Continuous delivery means every change that passes the pipeline is kept in a deployable state, so releasing to production becomes a business decision rather than an engineering scramble. [Continuous deployment](https://en.wikipedia.org/wiki/Continuous_deployment) goes one step further and releases every passing change automatically, with no human gate.

For large teams, these distinctions matter enormously. When hundreds of engineers commit to overlapping systems, the cost of manual integration and manual testing grows non-linearly. A shared, automated pipeline is the only practical way to give many contributors fast, trustworthy feedback and to keep one team's change from silently breaking another's. The pipeline becomes the single source of truth about whether the software is healthy, and it enforces a consistency that no amount of documentation or good intentions can guarantee at scale.

Enterprise and government contexts add one more dimension: auditability and change control. Regulators, security officers, and auditors need evidence that changes were reviewed, tested, and approved, and that the artifact running in production is exactly the one that was built and vetted. A well-designed CI/CD pipeline turns these compliance obligations from a paperwork burden into an automatic byproduct of the normal engineering workflow. Done well, delivery becomes faster and safer at the same time, which is the outcome that matters most to leadership.

*See also:* chapter 8.4 (platform engineering and developer experience), chapter 8.5 (test and process automation), and chapter 7.4 (product analytics and experimentation) for the [feature-flag](https://en.wikipedia.org/wiki/Feature_toggle) (runtime switches that expose functionality to users without redeploying) and experimentation practices that progressive delivery (releasing a change gradually while automatically monitoring its health metrics) enables.

## Key principles

- Integrate small changes frequently; long-lived branches are the enemy of continuous integration.
- Build the artifact once and promote the identical artifact through every environment.
- Make the pipeline the authoritative gate: if it is green, the change is shippable; if it is red, work stops until it is fixed.
- Optimize relentlessly for fast feedback so developers stay in flow and defects are caught while context is fresh.
- Automate everything that is repeated, including tests, security scans, provisioning, and deployment.
- Treat pipeline definitions as version-controlled code subject to review, not as clickable console configuration.
- Design for safe, reversible releases so that any deployment can be undone quickly.
- Separate deployment (installing the code) from release (exposing it to users) using feature flags.

## Recommendations

### Design the pipeline as a series of quality gates

Structure the pipeline into stages that progress from cheap and fast to expensive and thorough: compile and unit tests first, then integration tests, security and licence scanning, and finally deployment to staging and production. Each stage is a gate that a change must pass. Order the gates so the fastest, most likely-to-fail checks run first, which gives developers feedback in the shortest possible time. Keep the commit-stage feedback loop under ten minutes wherever you can. Beyond that, developers context-switch and productivity falls.

### Build once, promote everywhere

Produce a single immutable artifact in the build stage and promote that exact artifact through test, staging, and production. Never rebuild per environment, because a rebuild can silently introduce differences. Configuration that varies by environment should be injected at deploy time, not baked into separate builds. This practice is also what lets you tell an auditor, with certainty, that the binary in production is the one that passed every gate.

### Make the pipeline the enforcement point for policy

Encode required checks (code review approval, test coverage thresholds, security scan results, signed commits) directly into the pipeline and branch protection rules. Manual policy that lives in a wiki gets routinely bypassed under deadline pressure. Policy encoded in the pipeline is applied uniformly and automatically to every change.

### Keep the mainline releasable at all times

Use trunk-based development, which integrates all work into a single shared branch with few or no long-lived branches, or use short-lived feature branches, and rely on feature flags to hide incomplete work rather than long-lived branches. This keeps merge conflicts small and keeps the mainline always in a deployable state, which is the precondition for genuine continuous delivery.

### Choose deployment strategies deliberately

Match the deployment strategy to the risk and blast radius of the service:

- **Rolling** deployments replace instances gradually and are a sensible default for stateless services.
- **[Blue-green](https://en.wikipedia.org/wiki/Blue-green_deployment)** maintains two identical environments and switches traffic all at once, giving an instant rollback path.
- **Canary** releases route a small percentage of traffic to the new version, watch health metrics, and expand only if the signals are good.
- **Feature flags** decouple release from deployment, letting you enable functionality for specific users or cohorts without redeploying.

### Adopt progressive delivery with automated rollback

Progressive delivery combines canary releases with automated analysis of metrics such as error rate, latency, and saturation. Define objective health criteria in advance, then let the system promote or roll back automatically based on those signals. Automated rollback removes the human hesitation that turns a small incident into a major one.

### Provide release management and change control for regulated environments

In regulated settings, keep a lightweight but real change-management record. Automatically capture who approved each change, what tests ran, and what artifact was deployed. Use change advisory processes for genuinely high-risk changes, but reserve them for those cases. Routing every routine change through a weekly board destroys the value of automation. Aim instead for standard, pre-approved change types that flow through the pipeline without ceremony.

## Trade-offs: pros and cons

| Approach | Pros | Cons | Best fit |
|---|---|---|---|
| Continuous delivery (manual release gate) | Business controls timing; strong for regulated release windows | Requires discipline to keep mainline shippable | Enterprises with change windows |
| Continuous deployment (fully automatic) | Fastest feedback; smallest batches | Demands mature tests and observability | High-trust, high-frequency teams |
| Blue-green | Instant rollback; simple mental model | Doubles environment cost during switch | Critical services needing fast revert |
| Canary + progressive delivery | Limits blast radius; data-driven | Complex to build; needs good metrics | Large-scale user-facing systems |
| Feature flags | Decouples deploy from release | Flag debt if not cleaned up | Teams shipping incomplete work safely |

The central trade-off is speed versus control, but that is often a false choice. Mature automation delivers both: releases are faster because they are smaller, and safer because each one is verified and reversible. The real cost is the upfront investment in test coverage, observability, and pipeline engineering, plus the ongoing discipline to keep them healthy. Organizations that skimp on that investment get the speed without the safety, which is worse than a slow manual process.

## Questions to discuss with your team

1. **What is your target for commit-stage feedback time, and what gets cut when the suite outgrows ten minutes?** A slow commit stage quietly kills continuous integration, because developers stop waiting for green and start batching changes. Decide the number now (this chapter argues for under ten minutes) and decide the mechanism for holding it: parallel workers, a strict test pyramid, and moving slow integration checks into a later stage. At enterprise scale this is a platform decision, since hundreds of engineers share the same pipeline and every added minute multiplies across every commit. Bring real data to the meeting: current p50 and p95 pipeline duration, the slowest ten tests, and how often people re-run rather than wait. If you cannot state the target and defend it with numbers, your pipeline is drifting toward a batch process wearing a CI costume.

2. **Which deployment strategy does each service use, and who is accountable for that choice?** Rolling, blue-green, and canary are not interchangeable: they trade cost, rollback speed, and complexity differently, and the right pick depends on the blast radius of the service. Blue-green buys instant rollback at the price of a doubled environment during the switch, which is worth it for a payment system and wasteful for an internal dashboard. Canary limits exposure but demands good health metrics and more pipeline engineering. For a large or regulated estate, leaving this to each team's habit produces inconsistency that surfaces during an incident, so agree on defaults per service tier and record the decision. Bring your service catalogue and tag each service with its strategy, its rollback path, and the person who owns that call.

3. **How do you prove the artifact in production is exactly the one that passed every gate?** Build once and promote the identical artifact is the whole game for auditability, and it breaks the moment anyone rebuilds per environment or patches a running box. In enterprise and government settings an auditor will ask you to trace a running binary back to its commit, its review, and its approvals, and you want that answer to take seconds, not a week. Decide how you enforce it: immutable artifacts, signed images, signature verification at deploy time, and configuration injected at deploy rather than baked into separate builds. Bring the current gaps to the table, such as any stage that rebuilds, any manual hotfix path, and anywhere config forks the artifact. The answer determines whether your compliance evidence is a byproduct of the pipeline or a manual scramble before every audit.

4. **When the mainline goes red, what actually stops, and how do you handle flaky tests?** A pipeline is only an authoritative gate if a red build genuinely halts work, yet many organizations quietly tolerate a broken mainline and a backlog of intermittent failures, which trains developers to re-run until green and to ship on top of failures. For a large team this rot compounds, because one team's ignored flake becomes everyone's excuse to bypass the gate, and trust in the pipeline is far cheaper to keep than to rebuild. Weigh the competing pulls: a strict stop-the-line rule protects quality but can block hundreds of engineers on a single bad commit, while a lenient policy preserves throughput and erodes the gate. Bring evidence to the discussion: your current mainline red time, the number of quarantined or flaky tests, the re-run rate, and how often changes merge over a failing check. In enterprise and government settings, name who owns flake triage and who has authority to freeze merges, because a gate nobody is accountable for enforcing is one auditors will find has been routinely overridden.

5. **What is your lifecycle for feature flags, and who is on the hook to retire them?** Flags are what let you separate deployment from release and hide incomplete work, but every flag is a branch in your code that never gets cleaned up on its own, and unmanaged flags accumulate into conditional complexity that no one dares touch. In a large estate this debt is dangerous, because a stale flag can silently gate a security fix or flip untested code paths into production, and the person who created it has often moved on. Balance the tension: flags bought you safe, incremental delivery, so the goal is not fewer flags but a disciplined lifecycle with an owner, an expiry expectation, and tooling that surfaces stale ones. Bring the current inventory to the meeting: how many flags are live, how old the oldest is, which have no owner, and whether any long-lived flag now functions as permanent configuration that belongs elsewhere. For regulated environments, add who can change a flag in production and whether that change is logged with the same rigour as a deployment, since a flag flip is a release even when the pipeline never runs.

6. **Where is the boundary between continuous delivery with a human gate and full continuous deployment, and who sets the rollback thresholds?** Continuous delivery keeps a person in control of release timing, which suits statutory change windows and high-blast-radius systems, while continuous deployment ships every passing change automatically and demands mature tests, observability, and automated rollback to be safe. For a large or regulated organization the answer is rarely uniform: your marketing site can deploy continuously while your payments core keeps a documented human gate, and drawing that line per service tier prevents both needless friction and reckless automation. The competing considerations are speed and batch size against control and auditability, plus the engineering cost of the health metrics that automated rollback requires. Bring the evidence: per-service change-failure rate, mean time to recovery, current release cadence, and the objective signals (error rate, latency, saturation) you would trust to promote or roll back without a human. In government and enterprise settings, tie each tier to who owns the rollback thresholds and who signs off on any move from a gated release to full automation, so the decision is deliberate rather than drifting.

## Sector lens

**Startup.** Lean on managed CI/CD from day one: a hosted runner, one pipeline, one immutable image, and automatic deploy to staging on merge. Do not build pipeline infrastructure you then have to maintain. Feature flags let two or three engineers merge half-finished work safely and ship several times a day, and a one-click production deploy plus a fast flag-off is all the change control you need until scale forces more.

**Small business.** With no dedicated platform or release engineer, favour the pipeline your source host gives you (built-in Actions or equivalent) and its default deployment strategy over anything custom. Frame the buy-versus-build choice honestly: a managed pipeline and a hosting platform with built-in rollback cost less than the engineer-hours a bespoke setup consumes. Keep the essentials, which are build once, promote the same artifact, and an easy revert, and skip the progressive-delivery machinery until volume justifies it.

**Enterprise.** The core problem is consistency across many teams: standardize a shared pipeline template that enforces review, scanning, signed immutable artifacts, and per-tier deployment strategies, so quality does not vary team by team. Treat pipeline definitions as reviewed code, capture change-control evidence automatically, and manage feature flags and rollback thresholds as governed assets rather than each team's private habit. The payoff is faster delivery and audit evidence produced as a byproduct instead of a quarterly scramble.

**Government.** Procurement rules, statutory change windows, and public accountability shape the pipeline. Prefer continuous delivery with a documented human release gate over full automation for consequential systems, classify routine work as pre-approved standard changes, and keep an instant rollback path (blue-green or automated canary) for services citizens depend on during narrow annual windows. Ensure the pipeline records who approved each change, what tests ran, and which artifact deployed, so transparency and audit obligations are met by the normal workflow rather than by manual paperwork.

## Examples

**Startup.** A four-person SaaS startup wires up a single GitHub Actions pipeline that runs unit tests, builds one Docker image, and deploys that same image to staging automatically on every merge to main. A production deploy is one click, and the founders lean on feature flags so they can merge half-finished work behind a flag instead of keeping a branch alive for weeks. When a bad release slips through, they flip the flag off in seconds and fix it calmly, which keeps their tiny team shipping several times a day without a dedicated ops person.

**Enterprise.** A global bank consolidates dozens of team-specific Jenkins jobs into a standardized pipeline template that every product team inherits. The template enforces static analysis, dependency scanning, and a signed, immutable artifact, and it deploys via canary with automated rollback keyed to error-rate and latency thresholds. Because the same artifact is promoted from test to production and every gate is logged, the bank's auditors can trace any production binary back to its commit, review, and approval in seconds, replacing a quarterly manual evidence-gathering exercise.

**Government.** A national tax agency modernizing a filing system adopts continuous delivery with an explicit human release gate, so it can respect statutory change windows during filing season. Routine changes are classified as standard pre-approved changes that flow automatically to staging. Production release requires a single documented approval that the pipeline records. Blue-green deployment gives the agency an instant rollback path if a defect reaches production, which is critical when millions of citizens depend on the service during a narrow annual window.

## Business case: motivations, ROI, and TCO

The return on CI/CD investment shows up as reduced lead time for changes, lower change-failure rate, and faster recovery when incidents occur: the metrics that research consistently links to both delivery performance and organizational outcomes. Faster, smaller releases cut the coordination overhead that consumes engineering capacity at scale, and automated verification cuts the expensive, morale-sapping work of firefighting production defects.

The total cost of ownership weighs adoption cost against the cost of not adopting. Adoption costs include building and maintaining pipelines, growing test coverage, and investing in observability and platform staff. The cost of not adopting is larger but less visible: slow manual releases, integration pain, production incidents that damage reputation, and, in regulated settings, failed audits and remediation. For leadership, the argument is best framed in terms of risk reduction and capacity. Automation converts scarce senior-engineer time from repetitive release toil into product work, while making outages rarer and shorter.

## Anti-patterns and pitfalls

- **Snowflake pipelines.** Every team hand-builds a unique pipeline, so improvements and fixes cannot be shared and quality varies wildly.
- **Rebuild per environment.** Rebuilding for each stage breaks the "build once" guarantee and lets subtle differences reach production.
- **Ignored red builds.** Tolerating a persistently broken mainline destroys trust in the pipeline and normalizes shipping on top of failures.
- **Flaky tests left unaddressed.** Intermittent failures train developers to re-run until green, defeating the purpose of the gate.
- **Manual approval theatre.** A change advisory board that rubber-stamps everything adds delay without adding safety.
- **Flag debt.** Feature flags that are never removed accumulate into unmaintainable conditional complexity.
- **Deploy equals release.** Coupling the two means every user-facing change requires a risky redeploy.

## Maturity model

**Level 1: Initiate.** Builds and deployments are largely manual, ad hoc, and reactive. Integration happens late, releases are infrequent and stressful, rollback means redeploying an old version by hand, and there is no shared notion of a pipeline gate.

**Level 2: Develop.** Automated builds and unit tests run on each commit, but practices vary team by team. Deployments are scripted yet still triggered and supervised manually, some environments are consistent, and artifacts may still be rebuilt per stage. Where a pipeline exists it is often a snowflake that cannot be shared.

**Level 3: Standardize.** A documented, standardized pipeline template is enforced across teams. It promotes a single immutable artifact through all environments, applies automated quality and security gates, encodes required checks such as review approval and scan results, and captures change records automatically. Deployment strategies such as canary or blue-green are chosen deliberately per service tier.

**Level 4: Manage.** Delivery is measured and controlled against baselines. The organization tracks lead time for changes, deployment frequency, change-failure rate, and mean time to recovery, along with pipeline p50 and p95 duration, flaky-test and re-run rates, and feature-flag age. Rollback thresholds are set from observed error-rate, latency, and saturation data, gates are enforced on evidence rather than habit, and each metric has an owner who acts when it drifts from target.

**Level 5: Orchestrate.** Delivery continuously improves and is integrated across the organization. Progressive delivery with automated, metric-driven rollback is the norm, release is decoupled from deployment via well-governed flags, and compliance evidence is produced automatically as a byproduct. The pipeline adapts as the estate changes, and delivery metrics feed business and risk planning so investment flows to the highest-leverage improvements.

## Ideas for discussion

- Where is the right boundary between continuous delivery with a human gate and full continuous deployment for your most critical systems?
- How do you keep a mandatory change-management process meaningful without turning it into rubber-stamp theatre?
- What objective health metrics should govern automated rollback, and who owns their thresholds?
- How should platform teams balance standardized pipeline templates against the legitimate needs of teams with unusual requirements?
- What is your policy and tooling for retiring feature flags before they become debt?
- How do you measure whether faster delivery is actually improving business outcomes rather than just shipping more?

## Key takeaways

- CI, CD, and continuous deployment are distinct; choose the level of automation that matches your risk tolerance and maturity.
- Build the artifact once and promote the identical artifact through every environment.
- Design the pipeline as ordered quality gates optimized for fast feedback, and treat it as the authoritative shipping decision.
- Pick deployment strategies deliberately, and adopt progressive delivery with automated rollback to limit blast radius.
- Decouple release from deployment with feature flags, and manage flag debt.
- In regulated environments, capture change-control evidence automatically rather than through manual paperwork.

## References and further reading

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr, and George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (essay).
- ITIL (Information Technology Infrastructure Library), change management guidance.
