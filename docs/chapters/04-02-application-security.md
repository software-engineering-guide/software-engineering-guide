# 4.2 Application security

## Overview and motivation

Application security is where abstract threats meet concrete code. Most breaches that reach the headlines trace back to an application-layer flaw: an injection, a broken authentication flow, an exposed secret, or a compromised dependency. For large teams shipping many services, the hard part is not knowing these flaws exist. It is preventing them consistently across a sprawling codebase written by thousands of hands over many years.

For enterprises, application security is a matter of customer trust and regulatory obligation. A flaw in a login flow or a payment path can trigger fraud, fines, and mandatory breach disclosure. Government systems face the same technical risks with higher-stakes data: benefits eligibility, tax records, criminal justice data, and national infrastructure. In both settings, the application is the front door, and attackers probe it constantly and automatically.

This chapter covers the practices that keep applications resilient: knowing and defending against the common vulnerability classes, validating input and encoding output, getting authentication and authorization right, managing secrets, and securing the software supply chain that increasingly determines your real attack surface.

*See also:* chapter 4.1 (security foundations, threat modeling, and the secure development lifecycle), chapter 10.3 (open-source supply chain and licensing), and chapter 10.2 (SBOMs, risk, and assurance).

## Key principles

- **Never trust input.** Treat all data crossing a trust boundary as hostile until validated.
- **Secure defaults.** The safe path should be the easy path; insecure behavior should require deliberate, visible effort.
- **Fail closed.** When a security check cannot complete, deny access rather than allow it.
- **Defense in depth at the app layer.** Combine validation, encoding, parameterization, and framework protections; do not rely on one.
- **Least privilege for identities and tokens.** Scope credentials narrowly and expire them quickly.
- **Your dependencies are your code.** You are responsible for the security of everything you ship, including third-party and open-source components.
- **Standards over improvisation.** Use vetted frameworks such as the [OWASP](https://en.wikipedia.org/wiki/OWASP) (Open Worldwide Application Security Project) ASVS rather than inventing your own security controls.

## Recommendations

### Know and defend the OWASP Top 10, verify with ASVS

The OWASP Top 10 is the industry baseline list of the most critical web application risks: broken access control, cryptographic failures, injection, insecure design, security misconfiguration, vulnerable components, authentication failures, data integrity failures, logging failures, and server-side request forgery. Treat it as required knowledge for every engineer, not just a compliance reference to file away.

For a rigorous, testable standard, adopt the **OWASP Application Security Verification Standard (ASVS)**. ASVS defines security requirements at three levels of assurance, giving you concrete, auditable controls to design and test against. Pick the level that fits each application's risk, and verify against it.

### Validate input and encode output

Injection flaws stay among the most damaging precisely because they are so easy to introduce. Defend with layered controls:

- **Validate input** against strict allow-lists (expected type, length, format, range). Reject rather than sanitize where you can.
- **Use parameterized queries** and [prepared statements](https://en.wikipedia.org/wiki/Prepared_statement) for all database access; never build SQL by string concatenation. Use safe query builders and ORMs (object-relational mappers) correctly.
- **Encode output** contextually. HTML, HTML attributes, JavaScript, URLs, and CSS each require different encoding. Rely on framework auto-escaping and understand its limits.
- **Prevent [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** with output encoding plus a strong Content Security Policy as a second layer.
- **Prevent command and template injection** by avoiding shelling out with untrusted data and by using logic-less or sandboxed templates.

### Get authentication and authorization right

Authentication proves who a user is. Authorization decides what they may do. Both fail often, so get them right.

- Prefer established protocols: **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** for delegated authorization and **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** for authentication. Do not build these from scratch.
- Enforce **[multi-factor authentication](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)**, especially for privileged and administrative access.
- Store passwords only as salted hashes using a modern, slow, memory-hard algorithm (such as [Argon2](https://en.wikipedia.org/wiki/Argon2) or [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Never store or log plaintext credentials.
- Manage **sessions** carefully: generate cryptographically strong tokens, set secure and HttpOnly cookie flags, rotate on privilege change, and expire idle sessions.
- Enforce **authorization on the server for every request**, checking that the authenticated principal owns or may access the specific resource. Broken object-level authorization (accessing another user's record by changing an ID) is one of the most common and severe API flaws.
- Centralize authorization logic where practical so policy is consistent and auditable.

### Manage secrets and rotate keys

Hardcoded secrets in source code are a perennial cause of breaches. Build a disciplined habit around secret management:

- Store secrets in a dedicated secrets manager or vault, never in source, config files, or environment variables checked into version control.
- Scan commits and repositories for leaked secrets automatically, and block merges that introduce them.
- Rotate keys and credentials regularly and immediately upon any suspected exposure. Prefer short-lived, automatically issued credentials over long-lived static ones.
- Apply least privilege to every secret: scope it to exactly what it needs.
- Encrypt secrets at rest and in transit, and audit access to them.

### Secure the software supply chain

Modern applications are mostly assembled from third-party components, which makes the supply chain a primary attack surface.

- Maintain a **[Software Bill of Materials](https://en.wikipedia.org/wiki/Software_bill_of_materials) (SBOM)** for every application so you know exactly what you ship and can respond fast when a new vulnerability lands.
- Continuously scan dependencies (Software Composition Analysis, or SCA) and remediate known-vulnerable components promptly.
- Pin and verify dependency versions; use lockfiles and trusted registries.
- Adopt **SLSA** (Supply-chain Levels for Software Artifacts) to raise build integrity, and generate **provenance** attestations describing how artifacts were built.
- **Sign artifacts** and verify signatures before deployment so you can trust that what runs is what you built.
- Secure the build system itself; a compromised CI pipeline can inject malicious code into every downstream consumer.

## Trade-offs: pros and cons

| Decision | Pros | Cons |
|---|---|---|
| Buy/adopt identity provider (OIDC) | Battle-tested, MFA built in, less code to secure | Vendor dependency, integration effort, cost |
| Build custom auth | Full control, no external dependency | Extremely easy to get wrong, high maintenance |
| Strict allow-list validation | Blocks whole vulnerability classes | Can break legitimate edge cases, more upfront work |
| Short-lived credentials | Small breach window, auto-revocation | Requires robust issuance infrastructure |
| Aggressive dependency updates | Fewer known vulnerabilities | Churn, potential breaking changes, test burden |
| SBOM + signing + provenance | Fast incident response, verifiable trust | Tooling and process investment, cultural change |

The recurring trade-off is upfront rigor versus ongoing exposure. Building custom authentication or skipping dependency hygiene feels faster today and costs you enormously later. Adopting vetted standards and automated supply-chain controls costs effort now, but it turns an unbounded, unpredictable risk into a managed, bounded one. For large teams, the automation multiplier matters most: a control applied once in a paved-road template protects every service that uses it.

## Questions to discuss with your team

1. **Which ASVS controls will you bake into your paved-road framework so engineers get them for free?** The highest-leverage move for a large team is to make the safe path the default, so a control written once in a shared framework protects every service that adopts it. Decide which ASVS requirements (parameterized queries, output encoding, secure session flags, server-side authorization checks) belong in the template rather than in each engineer's memory. For enterprise and government portfolios, also decide which applications need ASVS Level 2 versus Level 3, and tie that to the sensitivity of the data each one touches. Bring a list of your services and mark which ones already inherit these defaults and which reimplement security by hand, because the hand-rolled ones are where injection and broken access control hide. If secure defaults live only in a wiki page, they will be skipped under delivery pressure, so put them in code.

2. **How will you find and fix broken object-level authorization across every API, not just the new ones?** Accessing another user's record by changing an ID is one of the most common and severe API flaws, and it hides in older endpoints that predate your current standards. Server-side authorization on every request and every object is the rule, but the hard part is verifying it holds across a sprawling, years-old codebase written by many hands. Decide whether you will centralize authorization logic, add automated tests that attempt cross-tenant access, or run targeted testing against your highest-risk APIs first. Bring your inventory of endpoints that expose object identifiers and rank them by the sensitivity of what they return. Without a deliberate sweep, you will keep shipping this flaw and discover it only when a researcher or an attacker does.

3. **What is your plan for the next widespread dependency vulnerability: how fast can you find and patch every affected service?** When a critical flaw lands in a popular library, the companies with an accurate SBOM identify affected services in hours while others spend weeks searching, and that speed gap decides how much damage you take. Decide now whether you produce a Software Bill of Materials for every artifact, whether dependency scanning runs in every pipeline, and who owns the emergency patch decision. For regulated and government buyers, SBOMs and signed provenance are increasingly a condition of doing business, so this readiness also protects revenue. Bring the honest answer to a drill: pick a library you use widely and time how long it takes to list every service that ships it. If the answer is measured in days, invest in inventory and signing before the next incident forces you to.

## Examples

**Startup.** A three-engineer SaaS team skips building its own login and adopts a managed OIDC provider on day one, gaining MFA and safe password resets without writing security-critical code it cannot afford to get wrong. It relies on the framework's ORM so queries are parameterized by default, keeps secrets in the platform's secret manager rather than in `.env` files a teammate might commit by accident, and turns on automated dependency scanning that opens a pull request when a library needs patching. None of this slows the team down, and it means one leaked key or one injected query does not end the company before it has customers.

**Enterprise.** A retail platform serving tens of millions of shoppers standardizes authentication on OIDC through a single identity provider, enforcing MFA for staff and step-up authentication for high-value account changes. All database access goes through an ORM configured to parameterize queries, and a Content Security Policy backs up output encoding. After a widely publicized vulnerability in a popular logging library, the company's SBOM lets it identify every affected service within hours and patch them in two days, while competitors without inventories spent weeks searching.

**Government.** A federal benefits agency builds citizen-facing services verified against OWASP ASVS Level 2, with Level 3 for the components handling the most sensitive records. Secrets live in a central vault issuing short-lived credentials; commit scanning blocks any leaked key. Every deployed artifact is signed and its provenance attested per SLSA, satisfying a federal mandate for verifiable software supply chains and giving auditors a clear chain of custody from source to production.

## Business case: motivations, ROI, and TCO

Application security spending buys down the most likely and most expensive category of breach. The total cost of ownership includes tooling (scanners, secret managers, identity providers), engineer time to remediate findings, and the mild friction of secure defaults. Against that, weigh the cost of skipping it: injection and broken-access-control breaches routinely expose millions of records, triggering regulatory fines, mandatory notification, fraud losses, remediation sprints, and reputational damage that suppresses revenue for years.

The ROI is strongest when controls are automated and reused. A single well-configured identity integration, one hardened query layer in a shared framework, and one pipeline that blocks vulnerable dependencies protect the whole fleet at marginal cost per service. Supply-chain controls in particular have gone from optional to essential: a compromised dependency can turn every one of your customers into a victim, and regulators and enterprise buyers increasingly require SBOMs and signed provenance as a condition of doing business. When you make the case to leadership, tie the investment to specific, named risks and to procurement and compliance requirements that block revenue if you fail to meet them.

## Anti-patterns and pitfalls

- **Rolling your own crypto or auth.** Almost always produces subtle, exploitable flaws.
- **Client-side-only validation.** Trivially bypassed; the server must revalidate everything.
- **Blocklist sanitization.** Trying to strip "bad" characters instead of allow-listing good ones; attackers find the gaps.
- **Secrets in source or environment files.** The single most common cause of credential leaks.
- **Ignoring authorization on object access.** Assuming an authenticated user may access any object whose ID they can guess.
- **Set-and-forget dependencies.** Never updating third-party components until a breach forces it.
- **Treating the Top 10 as the finish line.** It is a floor, not a comprehensive standard; use ASVS for depth.
- **Logging sensitive data.** Passwords, tokens, and PII (personally identifiable information) in logs become a breach waiting to happen.

## Maturity model

**Level 1: Initial.** Security depends on individual developer knowledge. No standard controls. Secrets in code. Dependencies rarely updated. Custom, ad hoc authentication.

**Level 2: Repeatable.** OWASP Top 10 awareness. Some framework-level protections. A secrets manager exists but is unevenly used. Occasional dependency scanning. Standard auth for new systems.

**Level 3: Defined.** ASVS-based requirements per risk tier. Parameterized queries and output encoding are the norm. Central identity with MFA. Secrets managed and scanned automatically. SBOMs produced; dependency scanning in the pipeline.

**Level 4: Optimizing.** Secure defaults built into paved-road frameworks so the safe path is automatic. Short-lived credentials everywhere. Full supply-chain assurance with signing and provenance (SLSA). Continuous verification and rapid, measured response to new vulnerabilities.

## Ideas for discussion

1. Where should authorization logic live to be both consistent and maintainable across many services?
2. How aggressively should you update dependencies given the trade-off between exposure and churn?
3. What ASVS level is appropriate for each class of application in your portfolio?
4. How do you eliminate long-lived secrets without creating fragile issuance infrastructure?
5. What would it take for your organization to produce and consume SBOMs and provenance for every artifact?
6. How do you keep secure defaults from being disabled under delivery pressure?

## Key takeaways

- The OWASP Top 10 is essential knowledge; ASVS provides the testable standard.
- Layer input validation, parameterization, and output encoding to defeat injection and XSS.
- Use vetted protocols (OAuth 2.0, OIDC) and enforce MFA; never build auth from scratch.
- Enforce authorization server-side for every request and every object.
- Keep secrets out of source, manage them centrally, and rotate to short-lived credentials.
- The supply chain is a primary attack surface; use SBOMs, SCA, signing, and provenance (SLSA).
- Automated, reusable controls protect the whole fleet at marginal cost per service.

## References and further reading

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorization, Secrets Management)
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation and OpenSSF, *SLSA framework* and *Supply-chain Security guidance*
