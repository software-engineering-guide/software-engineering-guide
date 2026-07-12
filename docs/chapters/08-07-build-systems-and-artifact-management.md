# 8.7 Build systems and artifact management

## Overview and motivation

The build is where your source code becomes something you can ship. Every pipeline in chapter 8.1 starts here: before you can test, scan, deploy, or promote anything, a build system has to turn a tree of source files into a concrete artifact, a compiled binary, a package, a container image, or a bundle of static assets. If that first step is slow, flaky, or unreproducible, every step after it inherits the damage. A build that produces different output on two machines undermines every test you run and every approval you collect, because the thing you vetted is not provably the thing you ship.

This chapter is about that first step and its output: the build system that constructs artifacts, and the artifact management that stores, versions, secures, and promotes them. It is deliberately narrower than chapter 8.1, which covers the full continuous integration and continuous delivery (CI/CD) pipeline. Here the subject is the build itself and the artifacts it emits. It complements chapter 2.10 on software configuration management, which governs how you track and control the inputs, and chapter 2.18 on dependency and supply-chain management, which governs the third-party code you pull in. The build is where those inputs meet: your source, your dependencies, and your configuration all converge into one immutable output.

For large teams the stakes are concrete. When hundreds of engineers wait on multi-minute builds many times a day, the aggregate lost time dwarfs almost any other engineering cost. When artifacts are mutable, untracked, or rebuilt per environment, you lose the ability to say with confidence what is running in production. In enterprise and government settings, that traceability is not optional. Auditors and security officers need evidence that the binary in production came from reviewed source, built by a trusted system, with a recorded chain of custody. A disciplined build and artifact practice turns that evidence into a byproduct of normal work rather than a scramble before every audit.

## Key principles

- The build is the first step of delivery: treat its speed and correctness as production concerns.
- Aim for reproducible and, where feasible, hermetic builds: same inputs, same output, every time.
- Build an artifact once, then promote that exact artifact across environments.
- Make artifacts immutable and content-addressed, and version them meaningfully.
- Store artifacts in a managed repository with retention, access control, and provenance.
- Cache aggressively, but treat the cache as a security boundary, not just a speed trick.
- Capture provenance, signatures, and a bill of materials at build time, not after the fact.

## Recommendations

### Treat the build as the first step of delivery

Your build system is production infrastructure, and you should fund and maintain it that way. The fast, correct construction of an artifact is the foundation that CI/CD (chapter 8.1) rests on. When teams treat the build as an afterthought, a pile of shell scripts nobody owns, they pay for it in flaky pipelines, mysterious "works on my machine" defects, and slow feedback that erodes the whole engineering flow described in Part 11. Give the build an owner, a definition kept in version control alongside the code (chapter 2.14 on repository structure), and the same review discipline as any other critical system.

### Make builds reproducible and, where you can, hermetic

A [reproducible build](https://en.wikipedia.org/wiki/Reproducible_builds) produces bit-for-bit identical output from the same source, so anyone can independently rebuild and verify that an artifact matches its source. This is the property that lets you trust that a binary was not tampered with between commit and deployment. Getting there means eliminating sources of nondeterminism: embedded timestamps, absolute file paths, build-order randomness, and network fetches whose results drift over time.

A hermetic build goes further by declaring every input up front and running in an isolated environment that cannot reach the network or the host's ambient state. Nothing enters the build except what you declared: pinned toolchain versions, pinned dependencies, explicit source files. Hermeticity is what makes reproducibility reliable rather than lucky. Full hermeticity has a real cost in tooling and discipline, so treat it as a direction rather than a binary. Even partial progress, pinning your compiler version, vendoring or locking dependencies, stripping timestamps, buys you most of the trust for a fraction of the effort.

### Resolve dependencies deterministically with lockfiles

Every build pulls in third-party code, and how you resolve it decides whether your build is deterministic. A [lockfile](https://en.wikipedia.org/wiki/Lock_file) records the exact resolved version and cryptographic hash of every direct and transitive dependency, so a build months from now resolves to precisely the same graph. Commit the lockfile, treat changes to it as reviewable events, and verify hashes on every fetch so a mutated upstream package cannot slip in unnoticed. This is the build-time face of the supply-chain discipline in chapter 2.18. Without a lockfile, "it built yesterday" tells you nothing about what it will build today, because a floating version range can silently pull a new release, or an attacker can publish a malicious one.

### Use incremental builds and caching, locally and remotely

Nobody should rebuild what has not changed. Incremental builds track which inputs feed which outputs and rebuild only the parts affected by a change. A build cache stores the outputs of previous work keyed by a hash of their inputs, so an unchanged target is fetched instead of recomputed. A local cache speeds up one developer's loop; a remote or distributed build cache shares results across the whole team and the CI fleet, so the first person to build a given input pays the cost and everyone else gets a cache hit. On a large monorepo this is the difference between a ten-minute build and a ten-second one.

The payoff is developer feedback speed, which is one of the highest-leverage investments you can make. Fast, correct feedback keeps engineers in flow and shortens the loop between writing code and knowing whether it works. Guard the correctness of the cache carefully, though: a cache key that omits a real input (an environment variable, a tool version) produces stale results that are maddening to debug. The cache is only as trustworthy as the completeness of its input hashing.

### Choose build tooling that matches your scale

Build tools sit on a spectrum. At the light end, [Make](https://en.wikipedia.org/wiki/Make_(software)) and language-native tools model a simple dependency graph and are enough for a single service or a small repo. In the middle, ecosystem tools such as Gradle and Maven for the Java world, or the standard toolchains for Go, Rust, and JavaScript, add dependency resolution and conventions. At the heavy end, graph-based systems such as [Bazel](https://en.wikipedia.org/wiki/Bazel_(software)) and similar monorepo build tools model the entire build as a fine-grained, hermetic [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) of targets, which enables precise incrementality, remote caching, and remote execution across a large codebase.

Heavier tooling pays off when you have many interdependent projects, a large monorepo (chapter 2.14), or build times that throttle your teams. It costs real investment: a steeper learning curve, migration effort, and a dedicated team to maintain the build definitions. Do not adopt Bazel-class tooling because it is fashionable. Adopt it when your build graph is large enough that fine-grained caching and parallelism recover more engineering time than the tool costs to run. For most small and mid-size systems, a good ecosystem tool with a remote cache is the sweet spot.

### Store artifacts in a managed repository

Once you have built an artifact, it needs a home. An [artifact repository](https://en.wikipedia.org/wiki/Software_repository) (also called a registry) stores your packages, container images, and binaries with versioning, access control, and metadata. It is the counterpart to your source repository: source in, artifacts out, both managed. A good repository gives you a single trusted place to publish and retrieve internal artifacts, proxies and caches external ones so you are not reaching to the public internet on every build, and records who published what and when. Container images have their own registry conventions, and other package types have theirs, but the discipline is the same: nothing runs in production that did not come from a managed, access-controlled store.

### Version artifacts and make them immutable and content-addressed

Give every artifact a meaningful version. [Semantic versioning](https://en.wikipedia.org/wiki/Software_versioning) (major.minor.patch) communicates the nature of a change to consumers: a major bump signals a breaking change, a minor adds compatible features, a patch fixes bugs. Alongside the human-readable version, identify each artifact by a cryptographic hash of its content, so it is content-addressed. A content address, often called a digest, is a fingerprint that changes if a single byte changes, which lets you refer to an exact artifact unambiguously and detect any tampering.

Make published artifacts immutable: once a version is published, it never changes. Republishing different bytes under the same version is a supply-chain hazard and a debugging nightmare, because two people can hold "version 1.4.2" and have different software. Mutable tags such as "latest" are convenient for humans but must always resolve, for anything that matters, to a specific immutable digest that you record. Deploy by digest, not by floating tag, so what you tested is provably what you run.

### Build once, promote everywhere

Build an artifact one time, then move that same artifact through your environments: development, staging, production. This "build once, promote everywhere" rule is the single most important artifact-management practice. If you rebuild per environment, you have thrown away your guarantee that the tested artifact is the deployed one, because each rebuild can pull a different dependency or run on a slightly different machine. Promotion is a metadata operation: you mark an already-built, already-tested digest as approved for the next environment, and you configure it for that environment through externalized configuration (chapter 2.10) rather than by rebuilding. This keeps the binary constant and the configuration variable, which is exactly the separation you want for both reliability and auditability.

### Capture provenance, sign artifacts, and generate an SBOM

At build time, record where the artifact came from and prove it has not been altered. Provenance is a signed statement of how an artifact was built: which source commit, which builder, which inputs. Signing an artifact lets consumers verify authenticity and integrity before they run it, and verifying signatures at deploy time closes the loop. A [software bill of materials](https://en.wikipedia.org/wiki/Software_supply_chain) (SBOM), a complete inventory of the components and dependencies inside an artifact, lets you answer "are we affected?" within minutes when a new vulnerability is disclosed, rather than spending days spelunking through build logs.

Frameworks such as SLSA (Supply-chain Levels for Software Artifacts) give you a graded model for build-time integrity: higher levels require hermetic, isolated builds and unforgeable provenance. Generate all of this in the build, where the information is authoritative and cheap to collect, not reconstructed afterward when it is expensive and unreliable. This work directly serves the secure software development lifecycle of chapter 4.9 and the supply-chain concerns of chapter 2.18.

### Secure the cache and manage retention and cost

A shared build cache is a shared trust boundary. If an attacker can write a poisoned entry, every consumer that fetches it runs compromised code, and the speed advantage becomes an attack surface. Protect the cache with authentication, scope write access narrowly (often only trusted CI, never developer laptops), and make sure cache keys hash every real input so a poisoned or stale entry cannot masquerade as a legitimate one. Treat cache poisoning as a real threat model, especially for remote caches shared across teams.

Artifacts also accumulate cost. Container images and build outputs are large, and an unbounded registry grows until storage bills and slow lookups force the issue. Define retention policies: keep every production-promoted artifact and everything referenced by a running system, expire old development and pull-request builds automatically, and record what you deleted. The goal is a store that keeps what you need for reproducibility and audit while shedding the noise, at a cost you consciously choose rather than one that surprises you.

## Trade-offs: pros and cons

| Decision | Pros | Cons |
|---|---|---|
| Heavy graph build tool (Bazel-class) | Fine-grained incrementality, remote cache and execution, scales to huge monorepos | Steep learning curve, migration cost, needs a dedicated build team |
| Light build tool (Make, native) | Simple, low overhead, fast to adopt | Poor incrementality and caching at scale, weak hermeticity |
| Remote/distributed build cache | Shared results, dramatic speedups across the fleet | Cache-poisoning surface, correctness depends on complete input hashing |
| Full hermetic builds | Reliable reproducibility, strong provenance | Real tooling and discipline cost, harder local workflows |
| Build once, promote everywhere | Tested artifact equals shipped artifact, clean audit trail | Requires externalized config and disciplined promotion |
| Immutable, content-addressed artifacts | Tamper-evident, unambiguous references | Less convenient than floating tags, more storage to manage |
| Long artifact retention | Full reproducibility and audit history | Storage cost, slower lookups without cleanup policy |

The recurring tension is between speed and trust. Caching, shared build farms, and floating tags all make builds faster and more convenient, and each one, used carelessly, weakens your ability to say exactly what you built and prove it was not tampered with. Resolve it by making the trustworthy path the fast path. A complete input hash makes the cache both fast and correct. Deploying by digest is as quick as deploying by tag and far safer. Generating an SBOM in the build costs seconds and saves days. You rarely have to choose speed over integrity if you engineer the integrity into the fast path from the start.

## Questions to discuss with your team

1. **Can we rebuild last quarter's production artifact today and get the same bytes, and if not, what is missing?** This is the sharpest test of your build discipline, because reproducibility depends on pinned toolchains, locked dependencies, and eliminated nondeterminism all working together. Pick a specific artifact that shipped a few months ago and actually try to rebuild it from the recorded source commit. What you learn from the attempt is more valuable than any policy document: maybe a dependency range floated, maybe the compiler version was never pinned, maybe a timestamp is baked in. The gaps you find are your reproducibility backlog, and closing them is what lets you trust that the thing you audited is the thing you run, which matters enormously in regulated and government settings where that chain of custody is a legal requirement.

2. **Do we build each artifact once and promote it, or do we rebuild per environment, and how would we prove which?** Many teams believe they promote a single artifact but discover, when they look closely, that staging and production each trigger a fresh build with subtly different inputs. Trace one real release from commit to production and confirm whether the exact same digest moved through every environment or whether new bytes were produced along the way. If you find rebuilds, you have found a place where your testing guarantees are weaker than you thought, because the tested artifact and the deployed artifact are not provably identical. The fix, externalizing configuration so the binary stays constant while settings vary, pays off in both reliability and a much cleaner audit story.

3. **If a critical vulnerability were announced in a common library tomorrow, how fast could we list every artifact that contains it?** This question tests whether your build-time provenance and SBOM practice is real or aspirational. When a widely used component turns out to be exploitable, the organizations that recover in hours are the ones that generate a bill of materials at build time and store it with each artifact; the ones that recover in weeks are grepping through build logs and interviewing engineers. Walk through the scenario concretely with a library you actually depend on and time how long the answer would take today. The gap between that time and "minutes" is a direct measure of your supply-chain exposure, and it connects straight to the secure development lifecycle work in chapter 4.9.

4. **How much engineering time do our builds cost each day, and what is the business case for making them faster?** Build latency is a tax paid on every change by every engineer, and at the scale of a large team the aggregate is easy to underestimate because no single wait feels expensive. Agreeing to measure it turns a vague complaint into a number you can weigh against the cost of a remote cache, better incrementality, or heavier build tooling. Bring your median and worst-case local and CI build times, the number of builds per day, and an honest estimate of how often a slow build pushes someone out of flow into a context switch. The competing consideration is that faster builds are not free: a remote cache and distributed execution add infrastructure to run and secure, and heavier tooling adds a maintenance team. For an enterprise or government organization, count the throughput and morale cost of slow feedback across many teams, which usually dwarfs the infrastructure bill and is exactly the framing leadership already funds.

5. **Who can write to our shared build cache, and what stops a poisoned entry from reaching production?** A shared cache trades a speed win for a new trust boundary, and the same mechanism that lets one engineer's result serve the whole fleet lets one corrupted or malicious entry compromise everyone who fetches it. For a large team the blast radius is the whole organization, so this deserves a deliberate decision rather than whatever a tool's defaults happen to be. Bring the list of who and what holds write access to each cache, whether writes are scoped to trusted CI rather than developer laptops, and whether your cache keys hash every real input so a stale or poisoned entry cannot masquerade as legitimate. The tension is that the tightest controls slow down the convenient path where developers push cache entries from their own machines. In enterprise and government settings, treat cache poisoning as an explicit threat in your supply-chain model and require the same access controls, logging, and review you apply to any other production system that can inject code into a release.

6. **At what point does our build graph justify heavier tooling, and how will we know we have crossed it?** The choice between a light ecosystem tool and a graph-based system such as Bazel is one of the more expensive and hard-to-reverse decisions in this area, because migrating a large codebase to fine-grained build definitions costs months and a dedicated team. Deciding the threshold in advance keeps you from either adopting complexity you do not need because it is fashionable, or clinging to a light tool long after your build times throttle every team. Bring the size and interdependence of your build graph, current build and cache-hit metrics, and a realistic estimate of the migration and ongoing maintenance cost against the engineering time the tool would recover. The competing pull is that heavy tooling delivers precise incrementality and remote execution that nothing else matches at scale, but only if your graph is genuinely large enough to repay it. For a large enterprise or agency, weigh also whether the tool's hermeticity and provenance guarantees help satisfy audit and supply-chain requirements, which can shift the calculus beyond raw speed.

## Sector lens

**Startup.** With a tiny team and no runway for build infrastructure, keep it light: use language-native build tools, adopt lockfiles from day one, and deploy container images by digest rather than the "latest" tag, since those habits cost almost nothing and spare you a whole class of "works on my machine" pain later. Resist heavy graph build tools; your scarcest resource is engineering attention. A remote build cache is the one upgrade worth reaching for once builds start creeping past a few minutes.

**Small business.** With no dedicated build engineer, lean on managed services rather than running your own artifact infrastructure: a hosted registry and your CI provider's built-in cache give you versioning, retention, and access control without a platform team. Frame the choice as buy over build, set an automatic expiry policy so storage costs stay predictable, and make sure the basics are in place, locked dependencies and immutable, digest-pinned deploys, because those protect you even when nobody watches the pipeline full-time.

**Enterprise.** Across many teams the problem is consistency: a shared, owned build platform, a common artifact repository, and enforced standards for lockfiles, signing, SBOMs, and build-once-promote so no group reinvents an unreliable pipeline. Invest in a remote cache and, where the build graph justifies it, graph-based tooling, and treat the cache as a governed trust boundary with scoped write access and audit logging. Manage artifacts as a controlled estate with retention policies and provenance so any production component traces back to reviewed source on demand.

**Government.** Procurement rules, transparency, and public accountability make build-time integrity a compliance requirement, not a nicety. Align the pipeline to a graded framework such as SLSA, run builds in isolated, network-restricted environments from pinned toolchains, and proxy third-party dependencies through an internal repository that scans and approves them before use. Store signed SBOMs and provenance immutably for the years that records-retention law requires, deploy only signed, digest-identified artifacts, and be ready to attest to auditors and the public that the software in production is exactly what was reviewed and approved.

## Examples

**Startup.** A fifteen-person startup running a small monorepo starts with language-native build tools and fast feedback, which is the right call at their scale. As they grow, build times creep past five minutes and engineers start context-switching while they wait. Rather than jumping to a heavy graph build tool, they add a remote build cache shared between developer machines and CI, which cuts most builds to seconds because unchanged targets are fetched, not rebuilt. They adopt lockfiles for every language, deploy container images by digest instead of the "latest" tag, and turn on automatic expiry for pull-request image builds so their registry bill stays flat. The whole effort takes a couple of weeks and buys back hours of engineering time every day.

**Enterprise.** A global financial-services company runs a large monorepo across hundreds of engineers and adopts a graph-based build system with remote caching and remote execution, because at their scale fine-grained incrementality recovers far more engineering time than the build team costs. Every artifact is built hermetically in an isolated environment, signed, and published to a managed registry with an SBOM and signed provenance attached. Deployments happen by content digest, and a policy engine refuses to run any image whose signature does not verify. Artifacts are promoted, never rebuilt, from staging to production, so the binary that passed testing is provably the one that serves customers. When auditors ask to trace a production component back to reviewed source, the chain of custody is a query, not an investigation.

**Government.** A national tax agency modernizing its systems treats build-time supply-chain integrity as a compliance requirement, aligning its pipeline with a graded framework like SLSA. Builds run in isolated, network-restricted environments from pinned toolchains and locked dependencies, so the output is reproducible and independently verifiable. Every artifact carries a signed SBOM and provenance, stored immutably for years to satisfy records-retention law. Third-party dependencies are proxied through an internal repository that scans and approves them before any build can use them, keeping unvetted code off the network entirely. Because the agency deploys only signed, promoted artifacts identified by digest, it can attest to regulators and to the public that the software processing citizens' returns is exactly what was reviewed and approved.

## Business case: motivations, ROI, and TCO

The return on build and artifact discipline shows up first as recovered engineering time. Slow builds tax every engineer on every change, and the cost compounds across a large organization: shaving minutes off a build that runs thousands of times a day recovers person-years annually and, harder to quantify but just as real, keeps engineers in flow instead of context-switching. A remote cache and good incrementality often pay for themselves within weeks. Reproducible, promote-once artifacts reduce a whole class of "it worked in staging" incidents, lowering change-failure rate and mean time to recovery, the delivery metrics leaders already watch.

The larger, less visible return is risk reduction. Signed artifacts, SBOMs, and provenance turn a supply-chain incident from a multi-week emergency into a scoped, hours-long response, and they turn audits from a fire drill into a query. In regulated and government contexts, that traceability is a precondition for operating at all, so the investment is not optional but structural. The total cost of ownership runs the other way when you neglect this: mutable artifacts and unreproducible builds accrete into an estate nobody can fully account for, storage grows unbounded without retention policy, and every audit and every incident costs more than it should. To make the case to leadership, connect build speed to engineering throughput and connect artifact integrity to audit cost and breach exposure, both of which they already fund.

## Anti-patterns and pitfalls

- **Rebuild per environment:** producing fresh bytes for staging and production, discarding the guarantee that the tested artifact is the deployed one.
- **Deploying by floating tag:** running "latest" or a mutable tag instead of an immutable digest, so what runs is unpredictable and untraceable.
- **No lockfile:** floating version ranges that let a build silently pull different or malicious dependencies over time.
- **Incomplete cache keys:** omitting a real input from the cache key, producing stale results that waste days of debugging.
- **Unsecured shared cache:** letting untrusted writers poison a remote cache so consumers fetch and run compromised outputs.
- **Nondeterministic builds:** embedded timestamps, absolute paths, and unpinned tools that make output vary and defeat verification.
- **Adopting heavy tooling prematurely:** taking on Bazel-class complexity before the build graph is large enough to justify it.
- **SBOM and provenance as afterthought:** reconstructing supply-chain metadata after the build, when it is expensive and unreliable, instead of generating it in the build.
- **Unbounded retention:** never expiring old artifacts until storage cost and slow lookups force a panicked cleanup.

## Maturity model

- **Level 1, Initiate:** Builds are ad hoc scripts nobody owns, often run from developer machines. Output is nondeterministic, dependencies float without lockfiles, artifacts are rebuilt per environment and deployed by mutable tag, and there is no shared cache, no signing, and no bill of materials.
- **Level 2, Develop:** Some teams have moved builds into CI from a checked-in definition and adopted lockfiles, but practice is inconsistent across the organization. Artifacts may land in a managed repository with basic versioning, and a local or simple remote cache speeds up common builds, yet rebuilds per environment still happen and provenance is patchy.
- **Level 3, Standardize:** Reproducible, largely hermetic builds are documented and enforced org-wide, with pinned toolchains and a shared remote cache whose keys hash all real inputs. Artifacts are immutable, content-addressed, versioned semantically, built once and promoted everywhere, signed, and shipped with an SBOM. Cache access is controlled and retention policies are applied consistently across teams.
- **Level 4, Manage:** The build estate is measured and controlled against baselines. Build times, cache-hit rates, developer feedback time, and storage cost are tracked with explicit targets, regressions trigger action, and signature and provenance verification is enforced at deploy time so a failed check blocks release. Build-time supply-chain integrity is assessed against a graded framework such as SLSA, and the numbers drive where you invest next.
- **Level 5, Orchestrate:** Build, cache, artifact, and supply-chain practice is continuously improved and integrated across the organization. Tooling, retention, and security posture adapt as you learn from incidents and audits, remote execution and caching are tuned as the codebase evolves, and build-time integrity is woven into the wider secure development lifecycle rather than bolted on afterward.

## Ideas for discussion

1. What is your current median and worst-case local build time, and what would a remote cache do to each?
2. Which of your artifacts are deployed by mutable tag today, and what would it take to deploy every one by digest?
3. Where does your build graph justify heavier tooling, and where would that tooling cost more than it saves?
4. Who can write to your shared build cache, and what stops a poisoned entry from reaching production?
5. Can you produce a signed SBOM for the last thing you shipped, and if not, what is the smallest step toward that?
6. What is your retention policy for build artifacts, and what does storage cost you today versus what it should?

## Key takeaways

- The build is the first step of delivery: fund its speed and correctness as production concerns, because everything downstream inherits its flaws.
- Make builds reproducible and, where feasible, hermetic, with pinned toolchains and lockfiles, so the artifact you audit is provably the one you ship.
- Cache and build incrementally, locally and remotely, but hash every real input and secure the cache, because a shared cache is a shared trust boundary.
- Build each artifact once, make it immutable and content-addressed, version it meaningfully, and promote that exact artifact across environments.
- Generate provenance, signatures, and an SBOM at build time and store artifacts with retention and access control, turning supply-chain integrity and audit readiness into a byproduct of normal work.

## References and further reading

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google: Lessons Learned from Programming Over Time*
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems*
- Peter Smith, *Software Build Systems: Principles and Experience*
- The Open Source Security Foundation, *SLSA: Supply-chain Levels for Software Artifacts* (specification)
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- Tom Preston-Werner, *Semantic Versioning Specification (SemVer)*
