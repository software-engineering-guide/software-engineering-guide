# 4.7 Identity and access management

## Overview and motivation

Every request that hits your systems carries an implicit claim: *I am allowed to do this*. Identity and access management (IAM) is the discipline of deciding whether that claim is true. It answers two separate questions that people constantly blur. [Authentication](https://en.wikipedia.org/wiki/Authentication) proves who you are. [Authorization](https://en.wikipedia.org/wiki/Authorization) decides what you may do once you have proven it. Keep those two ideas distinct in your head and half of the confusion in this field disappears.

For large teams, identity has quietly become the most important control you own. Chapter 4.3 makes the point that identity is the new perimeter, and chapter 4.1 builds zero trust on top of it: when you stop trusting the network, the only thing left to trust is a verified identity and an explicit policy. That shift means a weak password reset flow or a forgotten service account is no longer a small bug. It is the front door. Most real breaches are not clever exploits of memory-safety flaws; they are stolen credentials, over-broad permissions, and accounts that should have been turned off months ago.

The stakes rise in enterprise and government settings. A global enterprise juggles dozens of overlapping directories, thousands of joiners and leavers a month, and partners who need scoped access to a slice of your systems. A government agency layers on smart-card credentials, mandated identity assurance levels, and auditors who will ask, in writing, exactly who could touch a given record on a given day. This chapter is opinionated about how to build an identity layer that answers those questions well without grinding your people to a halt.

## Key principles

- **Authentication and authorization are different problems.** Proving identity and granting permission need separate designs and separate reviews.
- **One identity, many systems.** Consolidate to a single source of truth per identity population; directory sprawl is a security bug.
- **Least privilege by default.** Start from zero access and add deliberately, for humans and machines alike.
- **Every credential is temporary.** Prefer short-lived, automatically issued credentials over long-lived secrets.
- **Deprovisioning is as important as provisioning.** Access that outlives its need is pure risk.
- **Phishing-resistant beats memorable.** Move authentication toward passkeys and hardware-backed factors.
- **Machines are identities too.** Workloads, pipelines, and services need managed identity, not shared static keys.
- **Access is a lifecycle, not an event.** Grant, review, and revoke on a schedule, and prove you did.

## Recommendations

### Separate authentication from authorization, and centralize both

Authenticate through one identity provider (IdP), a system that verifies identity and issues tokens other systems trust. Then let each application make its own authorization decisions from the identity and attributes that token carries. This split lets you strengthen authentication once, for everyone, while keeping fine-grained permission logic close to the data it protects. Adopt [single sign-on](https://en.wikipedia.org/wiki/Single_sign-on) (SSO), where one authentication grants access to many applications, so your people have one strong login instead of forty weak ones. Federation extends the same trust across organizational boundaries, letting a partner's identities access your systems without you managing their passwords.

### Use the modern protocols for what each is actually for

Three standards do most of the work, and each has a job. **OpenID Connect (OIDC)** is an identity layer built on [OAuth](https://en.wikipedia.org/wiki/OAuth) 2.0; use it to answer *who is this user* for web and mobile sign-in. **OAuth 2.0** is an authorization framework for delegated access; use it to let an application call an API on a user's behalf without ever seeing their password (chapter 2.3). **Security Assertion Markup Language (SAML)** is the older XML-based federation standard; it remains the workhorse for enterprise SSO into established business applications. A common mistake is reaching for OAuth to do authentication directly. OAuth grants access to resources; OIDC sits on top of it to establish identity. Pick OIDC for new user-facing sign-in, keep SAML where your enterprise catalogue demands it, and do not invent your own token format.

### Make authentication phishing-resistant

Passwords alone are indefensible at scale. Require multi-factor authentication (MFA), which combines something you know, something you have, and something you are, for every human account without exception. Then push past the weak factors: one-time codes over SMS are phishable and SIM-swappable. The strong destination is [passkeys](https://en.wikipedia.org/wiki/Passkey) and the underlying WebAuthn standard (a browser API for public-key authentication), which bind a login to a hardware-held private key and to the real site's origin, so a fake page cannot harvest anything worth stealing. Passkeys are also passwordless, which your users will thank you for. Treat account recovery and password reset as part of the authentication surface, because an attacker who cannot beat your MFA will simply attack the reset flow instead.

### Manage the joiner-mover-leaver lifecycle, and deprovision fast

Identity is a lifecycle. A **joiner** needs the right access on day one. A **mover** who changes roles needs new access and, critically, needs the old access removed, or they slowly accumulate the keys to the whole building. A **leaver** must lose all access promptly, ideally within minutes of their final day, across every system. Drive this from an authoritative source, usually the human-resources system, so a status change there automatically provisions and deprovisions downstream. Automate it. Manual offboarding checklists always miss something, and the account they miss is the one that shows up in the incident report.

### Choose an authorization model and express it as policy-as-code

Grant permissions by [role-based access control](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC), where you assign permissions to job-function roles and assign people to roles, because it is simple to reason about and easy to audit. Reach for [attribute-based access control](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) where you need context-aware decisions based on attributes like department, data classification, location, or time of day. Most mature organizations run a hybrid: RBAC for the coarse grants, ABAC for the fine conditions. Whichever you choose, express authorization as **policy-as-code**: rules written in a version-controlled, testable, reviewable form rather than clicked into a console. Policy-as-code makes access decisions auditable, diffable, and consistent across environments, and it lets you test a permission change before it ships.

### Enforce least privilege with just-in-time access and PAM

Apply the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege): every identity gets the minimum access it needs and nothing more. Standing privilege is the enemy, because a permission granted permanently is a permission available to any attacker who lands on that account at any time. Prefer **just-in-time (JIT) access**, where a person requests elevated rights for a bounded window, gets them after approval, and loses them automatically when the window closes. For your most dangerous accounts, adopt **privileged access management (PAM)**: a system that vaults administrative credentials, brokers and records privileged sessions, and issues elevation on demand. The goal is zero standing admin access, so that even a fully compromised laptop yields nothing durable.

### Give machines and workloads real identity

Humans are only half your identities. Services, pipelines, containers, and functions all authenticate to something, and too often they do it with a long-lived secret pasted into a config file. Replace static keys with managed **workload identity**: short-lived credentials issued automatically to a workload based on where it runs and what it is. Use mutual TLS (mTLS), where both sides of a connection present certificates, for service-to-service authentication. Keep any remaining secrets in a dedicated secrets manager with rotation, never in source code or images (chapter 4.2). Short-lived, automatically rotated workload credentials remove the single most common cause of cloud credential leaks.

### Make identity the control plane, and review access continuously

In a zero trust architecture (chapter 4.1), identity is where policy is decided and enforced, so invest there accordingly. Then close the loop with **access reviews**, also called recertification: on a schedule, the owner of each system confirms that every person and machine with access still needs it, and revokes what they cannot justify. Feed every authentication and authorization event into an audit trail that answers *who accessed what, when, and under what policy* (chapter 4.6). Access reviews are how you fight privilege creep, the slow accumulation of permissions that no single grant ever looked unreasonable but that together make an account far too powerful.

## Trade-offs: pros and cons

| Decision | Pros | Cons |
|---|---|---|
| Centralized IdP with SSO | One strong login, consistent policy, easy audit | Single point of failure; outage locks everyone out |
| RBAC | Simple, auditable, familiar | Role explosion; coarse for context-sensitive needs |
| ABAC | Fine-grained, context-aware, scales with attributes | Harder to design, test, and reason about |
| Passkeys / WebAuthn | Phishing-resistant, passwordless, strong | Recovery and device-loss flows need careful design |
| Just-in-time access | Near-zero standing privilege | Friction; needs fast, reliable approval paths |
| Federation with partners | No external password management; scoped trust | Trust depends on the partner's own hygiene |
| Long-lived service keys | Trivially easy to set up | Leak-prone; the top cause of credential breaches |

The central tension is security versus friction. Every control that shrinks the attack surface (MFA on everything, JIT elevation, short credential lifetimes) also adds a step to someone's day, and people route around controls that hurt too much. Resolve it by making the secure path the easy path: SSO so strong authentication is one tap, passkeys so there is no password to type, and automated provisioning so the right access simply appears. Spend your friction budget where the blast radius is largest, on privileged and production access, and keep everyday access nearly frictionless.

## Questions to discuss with your team

1. **How fast can you actually revoke all access for someone who leaves today, and how do you know it worked?** Deprovisioning speed is a direct measure of your identity maturity, because a leaver whose access lingers is an unmonitored account with real permissions. In a large organization with dozens of disconnected systems, the honest answer is often "we are not sure," and the gap is usually the applications that never got wired into the central identity provider. Bring a real recent departure and trace every system they could touch, checking timestamps for when each access actually ended. Decide on a target, such as full revocation within one hour of the human-resources status change, and instrument it so you can prove it rather than hope. If any system relies on someone remembering a manual step, that is the account a future breach will use.

2. **Where do you still have standing privileged access and long-lived static credentials, and what would it take to eliminate them?** Standing admin rights and permanent service keys are the two assets attackers most want, because they are durable and powerful. Inventory every human with always-on production or administrative access and every service authenticating with a static key, then ask honestly which of those could move to just-in-time elevation or short-lived workload identity. The competing consideration is operational fear: teams keep standing access because break-glass moments feel safer with it, so you must make emergency elevation fast and reliable before you take the standing rights away. Bring the list to the discussion and rank items by blast radius, targeting production and administrative access first. The end state to aim for is zero standing admin access and no static key that outlives a single deploy.

3. **Do you have one authoritative identity per person and per workload, or several, and what is the sprawl costing you?** Directory sprawl, where the same human exists as five accounts across five systems with drifting attributes, is where deprovisioning gaps and orphaned access are born. Consolidating to a single source of truth per identity population is one of the highest-leverage investments a large team can make, because every downstream control depends on knowing that two records are the same person. Bring an inventory of your identity stores and map which ones are authoritative versus which are convenient copies nobody governs. The trade-off is that consolidation is a large, unglamorous migration that competes with feature work for attention. Decide whether the ongoing cost of sprawl, in audit pain and breach risk, justifies funding that migration now rather than after the next incident.

4. **Are your strongest authentication factors genuinely phishing-resistant, and what is blocking you from retiring passwords for good?** The factor an attacker cannot phish is the one that ends credential theft as your dominant breach path, and passkeys bound to WebAuthn are the only widely deployable option that clears that bar. In a large organization the honest picture is usually mixed: passkeys for some, one-time codes over SMS for others, and a long tail of legacy applications that still accept a password alone. The competing consideration is real, because passkeys shift the hard problem to recovery and device loss, and a clumsy recovery flow becomes the new soft target an attacker simply pivots to. Bring the coverage numbers by factor type, the list of applications that still fall back to a password, and a designed account-recovery path you would trust against a determined social-engineering attempt. In enterprise and government settings, tie the target to any mandated assurance level, since a high-assurance system that still permits a phishable factor has a compliance gap as well as a security one.

5. **How do you decide what access each identity gets, and can you diff, test, and prove that decision before it ships?** The gap between "someone clicked permissions into a console" and "a reviewed, version-controlled policy" is the difference between an access model you can audit and one you can only apologize for. For a large team the pressure is to let each application grow its own bespoke rules, which quietly produces role explosion on the RBAC side and untestable conditions on the ABAC side, until nobody can say what a given grant actually permits. The competing consideration is delivery speed, because expressing authorization as policy-as-code adds a review step that a console click does not, and teams under deadline resent the friction until the first failed audit or over-broad grant makes the case for them. Bring a real permission change and trace how it would be proposed, tested, reviewed, and rolled back, plus a count of how many roles you have and how many nobody can explain. In enterprise and government settings, an auditor will ask you to show exactly who could access a record and under what rule on a given day, and only a diffable, testable policy answers that without a scramble.

6. **When did an access review last revoke something real, and who is accountable when privilege creep goes unchecked?** Access reviews are the control that fights the slow accumulation of permissions no single grant ever looked unreasonable, and a review that never revokes anything is review theatre that produces paperwork instead of safety. In a large organization the failure mode is the rubber stamp: system owners recertify hundreds of entries in one sitting, approving all of them because genuinely evaluating each one is tedious and the incentive to keep access flowing is stronger than the incentive to cut it. The competing consideration is that meaningful reviews cost owner time and occasionally break someone's workflow when access they quietly relied on disappears, so you must make the review targeted and risk-driven rather than an undifferentiated list. Bring the revocation rate from your last cycle, the average number of entitlements per person, and evidence of who owns each system's recertification. In enterprise and government settings, name the accountable officer for each review and the cadence they are held to, because privilege creep that nobody is responsible for catching is the exact condition auditors and attackers both exploit.

## Sector lens

**Startup.** Buy identity, do not build it. A single hosted identity provider with SSO, passkeys required, and one-click offboarding gives a handful of engineers an enterprise-grade posture for a per-seat fee. Lean on the provider's built-in workload identity so there is not a single long-lived cloud key in your pipeline, and use OIDC and OAuth 2.0 off the shelf rather than inventing token handling you cannot afford to maintain.

**Small business.** With no identity specialist on staff, favour the SSO and MFA already bundled into the tools you pay for, and turn them on rather than shopping for a separate platform. Treat the joiner-mover-leaver problem as a short written checklist tied to whoever owns hiring, and prefer passkeys because they remove the password-reset helpdesk burden you cannot spare anyone to handle. Avoid shared logins, since they are the cheap habit that later makes attribution and revocation impossible.

**Enterprise.** The work is consolidation and governance across many directories and teams: one authoritative identity provider driven by the human-resources system, automated joiner-mover-leaver flows, RBAC for job functions with ABAC for context, and privileged access management with session recording. Express authorization as policy-as-code so changes are diffable and testable, run scheduled access reviews that actually revoke, and standardize the interface so applications wire into central identity instead of each growing its own login.

**Government.** Procurement rules, transparency, and public accountability drive the design. Bind authentication to hardware credentials such as PIV or CAC smart cards, set identity assurance levels per NIST SP 800-63 so higher-risk systems demand higher-assurance factors, and keep immutable audit logs that answer exactly who accessed what and when. Publish plain-language handling of citizen-facing identity, keep customer and workforce identity stacks separate, and ensure every privileged action on a sensitive system is brokered and recorded for the auditors who will ask.

## Examples

**Startup.** A twenty-person startup cannot staff an identity team, so it buys one. Every employee signs in through a single hosted identity provider with SSO into email, code hosting, cloud console, and the internal app, and passkeys are required so there are no passwords to phish. Offboarding is one click: disabling the person in the identity provider cuts access everywhere at once. For their own product, they use OIDC for user sign-in and OAuth 2.0 to let integrations call their API with scoped tokens. Service-to-cloud authentication uses the provider's built-in workload identity, so there is not a single long-lived cloud key anywhere in their pipeline. This costs a modest per-seat fee and buys them an identity posture stronger than many enterprises run.

**Enterprise.** A multinational bank has spent a decade accumulating four directories and hundreds of applications, some federated by SAML, some with their own local logins. It funds a consolidation programme: one authoritative identity provider, driven by the human-resources system, with automated joiner-mover-leaver flows that provision on hire and revoke within minutes of termination. RBAC covers standard job functions while ABAC enforces data-residency and clearance rules for cross-border access. Administrators hold no standing production access; they request just-in-time elevation through a privileged access management system that records every session. Quarterly access reviews force system owners to recertify or revoke, and every decision is expressed as policy-as-code so auditors can diff exactly what changed and when.

**Government.** A federal agency issues personal identity verification (PIV) smart cards, and the military equivalent, the common access card (CAC), to its workforce, so authentication is bound to a hardware credential rather than a password. Its identity programme follows the federal identity, credential, and access management (FICAM) approach and sets identity assurance levels per the National Institute of Standards and Technology guideline NIST SP 800-63, so higher-risk systems demand higher-assurance credentials. Citizen-facing services use a separate customer identity stack at a lower assurance level with strong MFA. Access reviews and immutable audit logs feed directly into the agency's continuous authorization evidence (chapter 4.6), and every privileged action on a classified system is brokered and recorded.

## Business case: motivations, ROI, and TCO

The return on identity investment comes from moving your dominant breach vector out of the danger zone. Stolen credentials and over-permissioned accounts drive a large share of real incidents, and each one carries a heavy tail: incident response, regulatory fines, breach notification, and lasting reputational damage. Phishing-resistant MFA alone eliminates the most common intrusion path, and automated deprovisioning closes the orphaned-account gap that turns a routine departure into an exposure. These are among the cheapest risk reductions available per dollar spent.

The total cost of ownership is real but bounded. It includes identity provider licensing, a privileged access management and secrets platform, the engineering to wire every application into central identity, and the ongoing effort of access reviews. The larger cost is organizational: consolidating directories and retrofitting SSO onto legacy applications is slow, unglamorous work that competes with features. Weigh it against the alternative. Fragmented identity spends the same money forever in the form of manual offboarding, audit scrambles, and helpdesk password resets, plus the eventual cost of the breach that fragmentation makes likely. When you make the case to leadership, frame identity as the control plane for zero trust: consolidation and automation are a one-time investment that lowers both breach risk and the recurring cost of audits, offboarding, and access support.

## Anti-patterns and pitfalls

- **Orphaned accounts.** Access that outlives the person or purpose, especially unmonitored service accounts and forgotten contractors.
- **Standing admin everywhere.** Always-on privileged access instead of just-in-time elevation, giving any compromised admin account durable power.
- **Long-lived static keys.** Service credentials pasted into config or CI that never expire and eventually leak.
- **Directory sprawl.** The same person as many ungoverned accounts, so no change ever fully propagates.
- **Shared accounts.** Credentials used by several people, destroying attribution and making revocation impossible.
- **SMS as your strong factor.** Treating phishable, SIM-swappable one-time codes as sufficient MFA.
- **Role explosion.** So many narrow RBAC roles that the model becomes unauditable and nobody knows what a role grants.
- **Deprovisioning as a manual checklist.** Human offboarding steps that inevitably miss the one account that matters.
- **OAuth used for authentication.** Treating an access token as proof of identity instead of using OIDC.
- **Review theatre.** Access recertifications rubber-stamped without anyone genuinely evaluating need.

## Maturity model

- **Level 1, Initiate:** Each application has its own login. Passwords with no consistent MFA. Provisioning and offboarding are manual, reactive, and slow; orphaned accounts accumulate. Service credentials are long-lived static keys. No access reviews; permissions granted and never revisited.
- **Level 2, Develop:** SSO covers major applications through a central identity provider, but coverage is uneven across teams. MFA is required for most human access. Basic RBAC exists. Joiner-mover-leaver is partly automated from the human-resources system. Some privileged accounts are vaulted. Access reviews happen occasionally and inconsistently.
- **Level 3, Standardize:** A consolidated identity provider is authoritative for the workforce, with automated provisioning and prompt deprovisioning enforced org-wide. Phishing-resistant MFA is standard and documented. RBAC plus ABAC is expressed as policy-as-code. Privileged access management with session recording is in place. Workload identity replaces most static keys. Scheduled access reviews are enforced and audited to a written policy every team follows.
- **Level 4, Manage:** The identity programme is measured against baselines and controlled with data. You track deprovisioning time from human-resources status change to full revocation, MFA and passkey coverage by population, the count of accounts with standing privileged access, the number of long-lived static keys still in use, orphaned-account counts, and access-review revocation rates. Metrics carry targets, such as full revocation within one hour and zero net new standing admin grants, and breaches of a threshold trigger investigation rather than a shrug. Authorization changes are tested in the pipeline and each go or no-go on an access grant is driven by evidence, not habit.
- **Level 5, Orchestrate:** Identity is the continuously improved control plane for zero trust, integrated with security, risk, and joiner-mover-leaver planning across the organization. Passkeys are the default and passwords are being retired. Zero standing privilege is achieved through just-in-time elevation, and all workloads use short-lived, automatically rotated credentials and mTLS. Authorization is fully policy-as-code. Access reviews are continuous and risk-driven, deprovisioning is near-instant, and every decision produces audit evidence automatically. The model adapts as risk signals shift, tightening or relaxing access dynamically rather than on a fixed cadence.

## Ideas for discussion

1. What would it take to reach zero standing administrative access, and what break-glass path would make that safe?
2. Where is ABAC worth its complexity in your environment versus staying with plain RBAC?
3. How aggressively should you retire passwords in favour of passkeys, and what recovery flow replaces them?
4. Which applications are still outside your central identity provider, and what keeps them there?
5. How do you give partners and customers scoped access without inheriting their security hygiene?
6. What single metric best captures your deprovisioning speed, and are you measuring it today?

## Key takeaways

- Authentication proves who you are; authorization decides what you may do. Design and review them separately.
- Consolidate to one authoritative identity provider with SSO; directory sprawl is a security defect, not a convenience.
- Automate the joiner-mover-leaver lifecycle and make deprovisioning fast and provable.
- Use OIDC for user sign-in, OAuth 2.0 for delegated API access, and SAML where the enterprise catalogue needs it; do not use OAuth as authentication.
- Move authentication toward phishing-resistant passkeys and WebAuthn; require MFA everywhere and treat weak factors as a stopgap.
- Enforce least privilege with just-in-time access and privileged access management; aim for zero standing admin rights.
- Give machines real identity with short-lived workload credentials and mTLS; eliminate long-lived static keys.
- Make identity the control plane for zero trust (chapter 4.1), and close the loop with continuous access reviews and audit evidence (chapter 4.6).

## References and further reading

- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines* (identity assurance, authentication, and federation levels)
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *SP 800-162: Guide to Attribute Based Access Control (ABAC) Definition and Considerations*
- National Institute of Standards and Technology, *SP 800-53: Security and Privacy Controls*, Access Control (AC) and Identification and Authentication (IA) families
- The OAuth 2.0 Authorization Framework, IETF RFC 6749, and the OAuth 2.0 Security Best Current Practice
- OpenID Connect Core 1.0 specification, OpenID Foundation
- Security Assertion Markup Language (SAML) 2.0 specification, OASIS
- Web Authentication (WebAuthn) Level 2, W3C Recommendation, and FIDO2 / FIDO Alliance passkey specifications
- Federal Identity, Credential, and Access Management (FICAM) architecture and playbooks, U.S. General Services Administration
- FIPS 201, *Personal Identity Verification (PIV) of Federal Employees and Contractors*
- Open Policy Agent (OPA) documentation, Cloud Native Computing Foundation (policy-as-code for authorization)
