# 4.3 Infrastructure and cloud security

## Overview and motivation

Applications run on infrastructure, and these days that infrastructure is largely cloud-based, software-defined, and always changing. A single engineer can now provision a database, open a network path, or grant a permission with one command, at a scale and speed traditional change control never anticipated. That power is exactly why misconfiguration, not exotic exploits, is the leading cause of cloud breaches. An accidentally public storage bucket or an over-broad access role can expose an entire organization's data in seconds.

For large enterprises, cloud infrastructure spans multiple providers, thousands of accounts, and a mix of managed services, containers, and serverless functions. The attack surface is not a static perimeter. It is a living, sprawling collection of resources and identities. For government, the same complexity meets strict authorization regimes, data residency mandates, and classification boundaries that shape every architectural choice. In both, the identity layer has become the new perimeter: who can do what, to which resource, under what conditions.

This chapter covers how to secure that foundation: [identity and access management](https://en.wikipedia.org/wiki/Identity_management) (IAM), [network segmentation](https://en.wikipedia.org/wiki/Network_segmentation), [encryption](https://en.wikipedia.org/wiki/Encryption) and [key management](https://en.wikipedia.org/wiki/Key_management), the security of containers and [serverless](https://en.wikipedia.org/wiki/Serverless_computing) workloads, and the continuous posture management that keeps a fast-moving cloud estate from drifting into danger.

## Key principles

- **Identity is the perimeter.** Access decisions hinge on strong identity and fine-grained authorization, not network location.
- **Least privilege, always.** Every identity, human or machine, gets the minimum permissions needed, and no more.
- **Segment to contain.** Divide networks and workloads so a compromise in one area cannot spread freely.
- **Encrypt everywhere.** Protect data in transit and at rest by default, with well-managed keys.
- **Immutable and declarative.** Define infrastructure as code (IaC), deploy immutably, and treat drift as a defect.
- **Continuous verification.** Posture is not a one-time audit; scan and enforce continuously.
- **Secure by default configuration.** The default state of any resource should be locked down, not open.

## Recommendations

### Design identity and access management deliberately

IAM is the most important part of cloud security, and the most frequently mismanaged.

- Use **[role-based access control](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC)** to grant permissions by job function, and **[attribute-based access control](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC)** where finer, context-aware decisions are needed (based on tags, environment, data classification, or time).
- Eliminate long-lived static credentials in favour of short-lived, automatically issued tokens and workload identity federation.
- Enforce [MFA](https://en.wikipedia.org/wiki/Multi-factor_authentication) (multi-factor authentication) for all human access and require strong authentication for privileged actions.
- Apply least privilege rigorously: start from zero and add permissions deliberately. Regularly review and prune unused permissions; access tends to accumulate.
- Separate duties so that no single identity can both make and approve sensitive changes.
- Use dedicated accounts or projects to create hard boundaries between environments (production, staging, development) and between business units.

### Segment networks and micro-segment workloads

Flat networks let attackers roam sideways once they are in. Divide and contain.

- Segment at the network level into tiers and zones, allowing only the traffic each tier legitimately needs.
- Apply **micro-segmentation** so that individual workloads communicate only with the specific peers they require, enforced by identity-aware policy rather than broad subnet rules.
- Default-deny east-west traffic; require explicit allow rules.
- Place sensitive data stores in private subnets with no direct internet exposure, reached only through controlled paths.
- Use private connectivity to managed services instead of routing over the public internet where possible.

### Encrypt data and manage keys properly

Encryption is only ever as strong as the key management behind it.

- Encrypt **in transit** with current [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security) everywhere, including internal service-to-service traffic.
- Encrypt **at rest** by default for all storage, databases, and backups.
- Manage keys with a **Key Management Service (KMS)**, and use a **[Hardware Security Module](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM)** for the highest-assurance keys and for regulatory requirements.
- Rotate keys on a schedule and support rapid rotation on suspected compromise.
- Control and audit who can use and manage keys separately from who can access the data, so key custody enforces separation of duties.
- Consider customer-managed keys where regulation or contractual trust requires the organization to hold the keys rather than the provider.

### Secure containers, Kubernetes, and serverless

Each compute model brings its own risks.

- **Containers:** build from minimal, trusted base images; scan images for vulnerabilities before deployment; run as non-root; make filesystems read-only where possible; and never bake secrets into images.
- **[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes):** enable RBAC and scope service accounts tightly; apply network policies for micro-segmentation; use admission controllers and policy engines to enforce standards; restrict privileged containers; isolate sensitive workloads; and keep the control plane and nodes patched.
- **Serverless:** apply least privilege to each function's execution role (a common source of over-permissioning); validate all event inputs; manage secrets through the platform's secret store; and monitor for anomalous invocation patterns.

Whatever the model, keep the runtime patched and the images fresh. A container is only as secure as the software inside it.

### Manage cloud security posture continuously

The cloud changes far too fast for periodic manual audits to keep up.

- Adopt **Cloud Security Posture Management (CSPM)** tooling to continuously detect misconfigurations, public exposure, and policy violations across accounts.
- Define security policy as code and enforce it at deployment time so bad configurations are blocked before they land.
- Prefer prevention (guardrails that stop misconfiguration) over detection (alerts after the fact), and combine both.
- Maintain an accurate inventory of resources and identities; you cannot secure what you cannot see.
- Track and remediate drift between declared infrastructure-as-code and the actual running state.

## Trade-offs: pros and cons

| Decision | Pros | Cons |
|---|---|---|
| RBAC | Simple, understandable, easy to audit | Coarse, role explosion at scale |
| ABAC | Fine-grained, context-aware, scales with tags | Complex to design and reason about |
| Provider-managed keys (KMS) | Easy, integrated, low operational burden | Provider holds custody; less control |
| Customer-managed keys/HSM | Full control, meets strict mandates | Operational overhead, risk of losing keys |
| Preventive guardrails | Stops misconfiguration before it happens | Can block legitimate work, needs tuning |
| Detective CSPM only | Flexible, non-blocking | Damage may occur before detection |
| Micro-segmentation | Strong lateral-movement containment | Operational complexity, policy sprawl |

The dominant trade-off is control versus operational burden. Tighter controls (customer-managed keys, strict micro-segmentation, ABAC) reduce risk, but they demand expertise and maintenance that small teams struggle to sustain. The right level depends on how sensitive the data is and what regulations apply. A pragmatic approach layers strong secure defaults for everyone, then reserves extra rigour for the highest-risk systems, and it favours automated guardrails that make the secure choice the default rather than a manual discipline.

## Questions to discuss with your team

1. **Where will you draw hard account or project boundaries, and what belongs inside each?** Dedicated accounts and projects create the strongest containment the cloud offers, so a compromise in development cannot reach production and one business unit cannot touch another's data. Decide your boundary scheme before your estate grows to thousands of accounts, because retrofitting isolation onto a flat structure is slow and risky. For enterprise and government work, these boundaries also map cleanly to environment separation, data classification, and the blast-radius limits auditors expect to see. Bring a current diagram of which workloads share an account today and mark where a single over-broad role spans production and non-production. If sensitive data sits in the same account as experimental workloads, that is the boundary to fix first.

2. **What is your standard for who can manage keys versus who can access the encrypted data?** Encryption is only as strong as key management, and separating key custody from data access turns your KMS into an enforcement point for separation of duties. Decide who may create, rotate, and use keys, and make sure that set does not overlap with the people who can read the data those keys protect. For regulated and government systems, this often drives the choice between provider-managed keys and customer-managed keys or HSMs, which carry more control and more operational risk of losing keys. Bring your current key policies and check whether any single identity can both manage a key and read the data behind it, because that is a common silent gap. If custody and access are not split, encryption at rest is protecting you less than the dashboard suggests.

3. **How will you make secure defaults inescapable in your landing zone rather than merely recommended?** Misconfiguration, not exotic exploits, is the leading cause of cloud breaches, and the fix is preventive guardrails that block a public database or an unencrypted bucket before it lands, not alerts after the fact. Decide which policies you will enforce at deploy time (no public storage, encryption on by default, mandatory tags) and which you will only detect and report. For a large team, encoding these into landing zones and infrastructure-as-code templates means every new account inherits protection with no per-team effort, turning security from a recurring tax into a one-time investment. Bring your last month of misconfiguration findings and ask which ones a preventive guardrail would have stopped outright. If your posture management is detective only, damage can occur before anyone sees the alert, so move the highest-impact checks to prevention.

4. **How do you eliminate long-lived static credentials without breaking the automation that quietly depends on them?** Embedded access keys that never expire are among the most common causes of cloud breaches, because a single leaked key in a script, log, or repository hands an attacker durable access. The competing pull is operational: legacy CI jobs, cron tasks, and third-party integrations often assume a static key exists, and cutting it over to short-lived tokens or workload identity federation takes engineering time nobody scheduled. For a large team, a shared migration path (issue tokens automatically, set an expiry standard, and alarm on any new long-lived key) prevents each group from inventing its own weaker answer. Bring an inventory of every static credential in use, its age, its blast radius, and whether the system it feeds can accept federated identity today. In enterprise and government settings, tie the deadline to audit and authorization cycles, because a credential that outlives the person who created it is exactly the finding that stalls a continuous authorization.

5. **When a resource is misconfigured or a key is compromised, how fast can you detect, contain, and remediate it, and have you measured that?** A public bucket or an over-broad role is only as dangerous as the window it stays open, so mean time to detect and remediate is the number that actually bounds your exposure. The tension is between preventive guardrails that stop the mistake at deploy time and detective posture management that catches what slips through, and you need honest figures for both rather than a comforting assumption that guardrails cover everything. Bring your last quarter of misconfiguration and drift findings with timestamps, the median time from introduction to remediation, and the rehearsal record for a key-compromise rotation. For enterprise and government estates spanning thousands of accounts, agree who owns remediation for a finding nobody's team obviously owns, because an alert with no accountable responder is an alert that ages into an incident.

6. **How will you keep security posture consistent across multiple clouds, accounts, and teams without slowing everyone to a crawl?** Multi-cloud and multi-account estates fragment fast: each provider has its own IAM model, its own defaults, and its own posture tooling, so a policy enforced in one place silently lapses in another. The trade-off is between central control that guarantees consistency and local autonomy that lets teams move quickly, and leaning too far either way either bottlenecks delivery or lets standards drift. Bring your current coverage map: which accounts inherit landing-zone guardrails, which are unmanaged, and where the same control is expressed three different ways across providers. For a large or public organization, add the audit angle, because auditors expect one defensible standard applied everywhere, and a control that exists in your primary cloud but not your secondary one is a gap that a determined attacker or assessor will find first.

## Sector lens

**Startup.** Speed and survival win, so lean entirely on secure defaults that ship for free: encryption at rest on, storage private unless a human opens it, MFA on the root account, and the provider's built-in workload identity instead of pasted access keys. Do not stand up a CSPM platform or hand-roll micro-segmentation you cannot maintain; a single guardrail that blocks a database opened to the internet buys most of the protection for an afternoon of work. Keep everything in infrastructure-as-code from the start so hardening scales with you rather than becoming a later rewrite.

**Small business.** With no dedicated security engineer and a tight budget, prefer managed services whose defaults are already hardened and whose key management is handled for you, rather than building your own KMS discipline. Treat cloud security as a configuration-hygiene question: know which buckets and databases exist, keep them private, require MFA, and turn on the provider's native posture checks that come at no extra cost. When you buy tools, favour ones that flag public exposure and unencrypted storage out of the box, because those two mistakes cause most avoidable breaches.

**Enterprise.** The real problem is consistency across thousands of accounts and many teams, so the work is platform work: landing zones that provision every account hardened, guardrails enforced as policy-as-code, and CSPM scanning continuously for drift. Standardize the IAM model, the key-custody rules, and the segmentation baseline so groups stop reinventing weaker versions, and measure posture across the estate rather than trusting each team's word. Budget the ongoing engineering to keep policies current as providers add services and as the estate grows.

**Government.** Procurement rules, data residency mandates, and authorization regimes shape every choice, so security controls double as audit evidence. Favour FIPS-validated key management with custody separated from data access, isolated regions that keep data inside national boundaries, and signed, scanned container images with strict admission control. Publish the safeguards you can, feed continuous posture management directly into ongoing authorization, and require vendors to disclose their configuration defaults and support the segmentation and key-custody controls your classification boundaries demand.

## Examples

**Startup.** A small startup runs everything in one cloud account and cannot staff a platform team, so it leans on defaults that ship secure: encryption at rest on by default, storage buckets private unless a human explicitly opens them, and MFA required on the root account. Instead of long-lived access keys pasted into CI, it uses the provider's built-in workload identity so the pipeline gets short-lived credentials automatically. A single free guardrail that flags any database opened to the internet saves them from the most common and most costly cloud mistake, at a cost of one afternoon to set up.

**Enterprise.** A media company running thousands of accounts across two cloud providers enforces a landing-zone pattern: every account is provisioned from a template with encryption-at-rest on by default, no public access on storage, mandatory tags, and a baseline of guardrail policies. CSPM continuously scans for drift, and workload identity federation has eliminated long-lived keys for CI systems. When a developer accidentally attempts to open a database to the internet, a preventive policy blocks the change and files a ticket automatically.

**Government.** A defence-adjacent agency operates in an isolated cloud region with data residency enforced by policy so no data leaves national boundaries. The most sensitive keys live in FIPS-validated (Federal Information Processing Standards) HSMs, with key custody separated from data access to enforce separation of duties. Kubernetes clusters use strict network policies and admission controls; every container image is scanned and signed before it may run. Continuous posture management feeds directly into the agency's ongoing authorization evidence.

## Business case: motivations, ROI, and TCO

Cloud infrastructure security is where a small investment heads off catastrophic, headline-grade losses. The total cost of ownership includes CSPM tooling, key management services, the engineering time to design least-privilege IAM and segmentation, and the ongoing effort to keep policies current. These costs are real but modest. The cost of skipping them is a single misconfigured resource exposing an entire customer database, along with the regulatory fines, notification costs, and lasting brand damage that follow. Cloud misconfiguration breaches are among the most common and most preventable incidents in the industry.

Automation and reuse amplify the ROI. Encode secure defaults into landing zones and infrastructure-as-code templates, and every new account and workload inherits protection with no per-team effort, turning security from a recurring manual tax into a one-time platform investment. For government and regulated enterprises, strong posture management also lowers the cost of audits and continuous authorization by producing evidence automatically. When you make the case to leadership, stress that the identity and configuration layer is now the primary breach vector, that misconfiguration is preventable, and that guardrails cut both the risk and the friction of manual review.

## Anti-patterns and pitfalls

- **Wildcard permissions.** Granting broad `*` access "to get things working" and never tightening it.
- **Long-lived static keys.** Access keys embedded in scripts and CI that never expire and eventually leak.
- **Flat networks.** No segmentation, so one compromised host reaches everything.
- **Public by accident.** Storage and databases exposed to the internet through default or careless settings.
- **Encryption without key discipline.** Enabling encryption but leaving key access wide open or never rotating.
- **Secrets baked into images.** Credentials embedded in container images that spread everywhere the image runs.
- **Over-permissioned serverless roles.** Functions granted far more than they need because scoping was skipped.
- **Audit-only posture.** Detecting misconfigurations after the fact instead of preventing them at deploy time.
- **Ignoring drift.** Letting the running environment diverge from infrastructure-as-code until no one knows the real state.

## Maturity model

**Level 1: Initiate.** Manual provisioning driven by whoever needs a resource. Broad wildcard permissions and long-lived static keys. Flat networks with no segmentation. Encryption applied inconsistently, if at all. No posture management; misconfigurations surface only after an incident forces the question.

**Level 2: Develop.** Some IAM roles and MFA appear, and encryption at rest is switched on for the major stores, but practice varies team by team. Basic network tiers exist without default-deny. Configuration reviews happen periodically and by hand. Infrastructure is partly defined as code, so hardening depends on which group provisioned the account.

**Level 3: Standardize.** Least-privilege RBAC and ABAC with short-lived credentials are documented and enforced org-wide. Segmentation uses default-deny east-west. Encryption in transit and at rest is on by default, with keys in KMS on a rotation schedule and custody separated from data access. Container and Kubernetes hardening is a standard, and CSPM runs against defined policies applied consistently across every account.

**Level 4: Manage.** The posture is measured, not assumed. You track named metrics against baselines and targets: the share of identities within their least-privilege baseline, mean time to detect and remediate misconfigurations and drift, guardrail and CSPM coverage across accounts, key-rotation compliance, and the count of surviving long-lived credentials. Findings are triaged by blast radius, remediation has an owner and a service-level objective, and trend data on these numbers drives where the next hardening effort goes.

**Level 5: Orchestrate.** Secure defaults are baked into landing zones and infrastructure-as-code so every resource is born hardened, and the controls adapt as the estate and threat picture shift. Micro-segmentation uses identity-aware policy; customer-managed keys and HSMs protect the highest-assurance systems with custody separation. Preventive guardrails block misconfiguration at deploy time, drift is auto-detected and remediated, and posture evidence feeds continuous authorization automatically. Security is integrated with delivery and risk planning, and the organization routinely retires and re-scopes controls as providers, services, and regulations change.

## Ideas for discussion

1. Where is ABAC worth its complexity versus sticking with RBAC in your environment?
2. How do you eliminate long-lived credentials without breaking legacy automation?
3. What is the right split between preventive guardrails and detective posture management?
4. Which systems justify customer-managed keys or HSMs given their operational cost?
5. How do you keep least-privilege permissions from silently accumulating back to over-privilege?
6. How should multi-cloud complexity change your approach to consistent posture and policy?

## Key takeaways

- Identity is the new perimeter; invest in least-privilege IAM with short-lived credentials.
- Segment networks and micro-segment workloads to contain compromise.
- Encrypt in transit and at rest by default, and manage keys with KMS/HSM and separation of custody.
- Harden containers, Kubernetes, and serverless; keep runtimes and images patched.
- Prefer preventive guardrails over after-the-fact detection, and manage posture continuously.
- Bake secure defaults into landing zones and infrastructure-as-code so protection scales automatically.
- Misconfiguration, not exotic exploits, is the leading cause of cloud breaches, and it is preventable.

## References and further reading

- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- Center for Internet Security, *CIS Benchmarks* (cloud providers, Kubernetes, Docker)
- Cloud Security Alliance, *Cloud Controls Matrix* and *Security Guidance for Cloud Computing*
- NIST, *SP 800-190: Application Container Security Guide*
- Liz Rice, *Container Security*
- Marco Lancini and others, *Cloud security posture and detection* engineering literature
- Provider Well-Architected security pillars (as vendor-neutral architectural guidance)
