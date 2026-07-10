# 8.2 Infrastructure as code and configuration

## Overview and motivation

[Infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC) means defining and provisioning infrastructure (networks, servers, databases, load balancers, permissions) through machine-readable definition files rather than manual console clicks or ad hoc scripts. [Configuration management](https://en.wikipedia.org/wiki/Configuration_management) extends the same idea to the settings and state of systems once they exist. Together they turn infrastructure from a hand-crafted, fragile artifact into a versioned, reviewable, reproducible product of the same engineering discipline you use for application code.

For large teams, IaC is not a convenience but a necessity. When hundreds of engineers need environments and thousands of resources must stay consistent across regions and accounts, manual provisioning cannot keep up and cannot stay correct. Human-configured infrastructure drifts, sooner or later, into unique "snowflake" servers that no one fully understands and that cannot be reliably rebuilt after a failure. Codifying infrastructure makes it consistent, auditable, and disposable. Any environment can be recreated from its definition, and any change is a reviewable diff.

Enterprise and government organizations gain one more, decisive benefit: enforceable governance. Security and compliance requirements, such as encryption at rest, network segmentation, approved regions, and tagging for cost allocation, can be embedded directly into the code and checked automatically before anything is provisioned. Instead of auditing infrastructure after the fact and chasing violations, you keep non-compliant infrastructure from ever existing. This shift from detection to prevention is the core reason IaC has become foundational to modern platform practice.

## Key principles

- Prefer declarative definitions that describe desired state over imperative scripts that describe steps.
- Store all infrastructure definitions in version control, reviewed like any other code.
- Treat infrastructure as immutable: replace rather than modify in place.
- Make provisioning idempotent so applying the same definition repeatedly yields the same result.
- Detect and reconcile drift, the live environment diverging from its declared definition, continuously; the code, not the live system, is the source of truth.
- Compose infrastructure from reusable, versioned modules rather than copying and pasting.
- Encode policy as code, organizational rules expressed as machine-checkable code, so guardrails are automatic, not advisory.
- Keep secrets out of definitions; reference them from a dedicated secrets manager.

## Recommendations

### Choose declarative tooling and structure it around modules

Adopt a declarative IaC tool, such as [Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), Pulumi, or a cloud-native option like CloudFormation, and standardize on it across the organization so you avoid a fragmented tooling landscape. The key architectural practice is modularity: build small, well-documented, versioned modules that capture common patterns (a compliant network, a hardened database, a standard service). Teams then compose environments from these modules rather than authoring raw resources. This spreads good defaults and security settings automatically and dramatically reduces duplication.

### Manage state deliberately

Declarative tools track the mapping between code and real resources in a state file. Store state remotely in a shared, encrypted, access-controlled backend, and use locking so concurrent modifications cannot corrupt it. Never keep state on a laptop, and never edit it by hand except as a last-resort recovery action. State is sensitive, because it can contain resource metadata and secrets, so protect it accordingly.

### Build immutable infrastructure with golden images

Rather than patching running servers, bake a versioned "golden image" (a pre-configured, hardened machine or container image) and deploy fresh instances from it. When you need a change or patch, build a new image and roll it out, retiring the old instances. This eliminates configuration drift, makes rollback trivial, and keeps every instance identical and traceable to a known-good build. Automated image pipelines should include security hardening and scanning, so compliance is built in at the image level.

### Detect and reconcile configuration drift

Drift happens when the live environment diverges from its definition, usually because someone made an emergency manual change. Run regular drift detection that compares actual state to declared state and flags the differences. Treat drift as a defect: reconcile by updating the code and re-applying, not by leaving the manual change in place. For systems that need ongoing configuration enforcement, use a configuration management tool that continuously converges hosts to their declared state.

### Adopt GitOps and pull-based deployment

In the GitOps model, a Git repository holds the declared desired state of the system, and an automated agent running inside the target environment continuously pulls that state and reconciles the live system to match. This flips the traditional push model. No external system needs standing credentials to change the environment, because the environment pulls its own configuration. GitOps gives you a complete audit trail (every change is a commit), easy rollback (revert the commit), and strong drift correction (the agent continuously re-asserts the desired state). It is especially powerful for [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) and for organizations that want a single, reviewable source of truth.

### Enforce guardrails with policy as code

Express organizational rules, such as allowed regions, mandatory encryption, required tags, and prohibited public exposure, as machine-checkable policies using a tool such as Open Policy Agent (OPA) or a platform-native policy engine like Sentinel. Run these checks in the pipeline before provisioning, so violations are blocked automatically. Policy as code turns a security team's intent into an executable, uniformly applied control, and it scales to thousands of changes in a way that manual review never could.

## Trade-offs: pros and cons

| Choice | Pros | Cons | Best fit |
|---|---|---|---|
| Declarative IaC (Terraform/Pulumi) | Reproducible, reviewable, drift-detectable | Learning curve; state management complexity | Almost all teams at scale |
| Imperative scripts | Familiar; flexible for one-offs | Not idempotent; hard to audit and repeat | Narrow, transitional cases |
| Immutable + golden images | No drift; trivial rollback | Image build pipeline overhead | Fleets needing consistency |
| Mutable config management | Fine-grained ongoing control | Drift risk; slower convergence | Legacy or long-lived hosts |
| GitOps (pull-based) | Strong audit trail; self-healing | Requires in-cluster agent and Git discipline | Kubernetes and cloud-native |
| Policy as code | Automatic, uniform guardrails | Upfront policy authoring effort | Regulated environments |

The main tension is between flexibility and control. Manual and imperative approaches feel faster for a single change, but they accumulate hidden inconsistency that becomes crippling at scale. Declarative, immutable, policy-governed infrastructure asks for more upfront investment and a real cultural shift, since engineers have to stop making quick console changes, but it repays that investment many times over in reliability, auditability, and the ability to rebuild anything on demand.

## Questions to discuss with your team

1. **Who owns the shared module library, and how does an improvement in a module reach every team using it?** Modules only pay off if fixes and hardened defaults propagate, and that requires clear ownership and real versioning, not a folder everyone copies from. Decide who maintains the compliant-network and hardened-database modules, how you version them (semantic versioning with a changelog), and how teams pull upgrades without a fire drill. At scale this is the difference between fixing a misconfiguration once and chasing it across a thousand hand-edited resources. Bring evidence: how many distinct copies of the same pattern exist today, how long a security fix takes to reach every environment, and whether teams pin module versions or float them. If a critical patch cannot reach the whole estate in days, your modularity is cosmetic.

2. **What is your drift-detection cadence, and what actually happens when drift is found?** Drift is the live environment quietly diverging from its declared state, usually from an emergency console change, and tolerating it turns your code into fiction. Decide how often you compare actual state to declared state (nightly is a reasonable default) and, more importantly, decide the response: reconcile by updating the code and re-applying, never by leaving the manual change in place. In regulated settings this is a control requirement, because auditors need the declared state to match reality continuously. Bring your current numbers: how many resources drift each week, how long they stay drifted, and whether anyone is accountable for closing them. Treat every drift as a defect with an owner, or the source-of-truth guarantee erodes until nobody trusts the code.

3. **Have you moved to GitOps and pull-based reconciliation, or does an external system still hold standing credentials to change production?** In the pull model an agent inside the target environment continuously reconciles the live system to Git, which removes the need for any outside system to hold write access, and it re-asserts desired state so drift self-corrects. That is a strong security and audit posture, since every change is a commit and no operator needs standing production credentials. The cost is real: an in-cluster agent to run and strict Git discipline, so weigh it against your current push-based automation. Bring the list of who and what can currently mutate production directly, and what audit trail those changes leave. For Kubernetes and high-assurance enclaves this shift is usually worth it; for a handful of static resources it may be overkill.

## Examples

**Startup.** A five-person startup defines its whole AWS setup, meaning the VPC, database, and container service, in a single Terraform repository with state kept in an encrypted S3 backend and locking through DynamoDB. Every change goes through a pull request, so even a solo on-call engineer can see exactly what will change before running apply. When they need a fresh staging environment for a big demo, they copy a small module and stand it up in minutes, and tear it down just as fast to keep the cloud bill low.

**Enterprise.** A multinational retailer manages infrastructure across several cloud accounts and regions. A central platform team publishes versioned Terraform modules for compliant networks, databases, and service scaffolding, and enforces OPA policies that reject any resource lacking encryption or cost-allocation tags. Product teams provision their own environments self-service, but every change flows through the pipeline, where policy is checked automatically. Drift detection runs nightly and opens tickets for any manual change, keeping thousands of resources continuously in a known, compliant state.

**Government.** A defense agency operating in a high-assurance environment builds hardened golden images that embed the required security baseline, and deploys only immutable instances from those images. All infrastructure is declared in Git and reconciled by a GitOps agent inside the accredited enclave, so no operator holds standing credentials to change production directly. Every change is a signed commit. This gives auditors a complete, tamper-evident history and satisfies continuous-monitoring and configuration-control requirements without manual evidence gathering.

## Business case: motivations, ROI, and TCO

The ROI of IaC comes from speed, reliability, and risk reduction. Environments that once took weeks of ticket-driven manual provisioning can be created in minutes, which frees engineers and accelerates projects. Reproducibility slashes recovery time after failures, because any environment can be rebuilt from code. Automated policy enforcement reduces the frequency and cost of security incidents and audit findings, which for regulated organizations can be substantial.

On the TCO ledger, adoption costs include tooling, training, building a module and policy library, and the discipline to stop making manual changes. The cost of not adopting is steeper and compounds over time: snowflake infrastructure that no one can rebuild, slow and error-prone provisioning, security misconfigurations that lead to breaches, and audits that consume weeks of manual effort. For leadership, frame IaC as converting infrastructure from an unmanaged liability into a governed, reproducible asset, and as the mechanism that makes security and compliance automatic rather than aspirational.

## Anti-patterns and pitfalls

- **ClickOps in production.** Making changes by hand in the console guarantees drift and destroys reproducibility.
- **Secrets in code.** Hardcoding credentials in definition files leaks them into version history and state.
- **Monolithic, un-modularized definitions.** One enormous configuration that no one dares change becomes as brittle as the manual setup it replaced.
- **Unmanaged state.** Local or unlocked state files lead to corruption and lost infrastructure.
- **Drift tolerated.** Leaving manual changes in place erodes the source-of-truth guarantee until the code is fiction.
- **Policy as documentation.** Rules that live in a wiki instead of an automated check are routinely violated.
- **Copy-paste proliferation.** Duplicating configuration across teams means fixes and improvements never spread.

## Maturity model

**Level 1: Initial.** Infrastructure is provisioned manually. Environments are inconsistent, undocumented, and cannot be reliably reproduced. Recovery from failure is slow and uncertain.

**Level 2: Managed.** Some infrastructure is scripted or codified, but practices vary by team. State management is inconsistent, drift is common, and policy is enforced through manual review.

**Level 3: Defined.** Declarative IaC is standard, built from shared versioned modules with managed remote state. Policy as code enforces guardrails in the pipeline, and drift detection runs regularly.

**Level 4: Optimizing.** Infrastructure is immutable and GitOps-driven, self-healing against drift. Compliance evidence is produced automatically, and the module and policy library continuously improves based on real usage and incidents.

## Ideas for discussion

- Where should the line sit between centrally governed modules and team autonomy to define custom infrastructure?
- How do you handle the genuine emergency change that must bypass the pipeline, without normalizing ClickOps?
- What is the right strategy for managing and securing state across many accounts and teams?
- When is mutable configuration management still justified versus fully immutable infrastructure?
- How do you keep the policy-as-code library aligned with evolving security and regulatory requirements?
- What does a realistic migration path look like for legacy infrastructure that predates IaC?

## Key takeaways

- Define infrastructure declaratively, version it, and treat it as reviewable, reproducible code.
- Build from small, versioned modules to spread good defaults and eliminate duplication.
- Prefer immutable infrastructure and golden images to abolish drift and simplify rollback.
- Manage state deliberately and keep secrets out of definitions.
- Adopt GitOps for a strong audit trail and self-healing reconciliation.
- Enforce guardrails with policy as code so compliance is prevented into existence, not audited after the fact.

## References and further reading

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Weaveworks, "GitOps" foundational writings (Alexis Richardson et al.).
- Open Policy Agent documentation and the Rego policy language.
- NIST Special Publication 800-53, security and privacy controls (configuration management family).
