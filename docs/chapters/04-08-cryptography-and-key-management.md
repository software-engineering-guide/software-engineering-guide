# 4.8 Cryptography and key management

## Overview and motivation

Almost every system you build already depends on [cryptography](https://en.wikipedia.org/wiki/Cryptography), the practice of protecting information using mathematical techniques so that only the intended parties can read or trust it. Your web traffic rides encrypted channels, your passwords are hashed, your software updates are signed, and your customer data sits encrypted on disk. The good news for most engineers is that you are not asked to invent any of this. The hard part is not the mathematics. It is using vetted building blocks correctly and, above all, managing the keys those building blocks depend on.

This chapter is written for engineers who are not cryptographers, which is nearly all of us. You need enough understanding to make sound choices, to know what each tool guarantees, and to avoid the mistakes that turn strong algorithms into false comfort. Chapter 4.3 (infrastructure and cloud security) mentions encryption and key management in passing; here we go deeper into what to encrypt, how, and how to run the key lifecycle that makes it real.

For large enterprises, cryptography sprawls across thousands of services, certificates, and keys, and a single expired certificate or lost key can take down a critical system or leak a data store. For government, cryptography is often mandated, validated, and audited, with data classification rules that dictate exactly which keys protect which secrets and who may hold them. In both settings, the recurring failure is the same: good algorithms undone by sloppy key management.

## Key principles

- **Do not roll your own crypto.** Use vetted, widely reviewed libraries and standard algorithms. Novel schemes fail in ways only experts catch.
- **Algorithms are the easy part; keys are the hard part.** The lifecycle of a key is where most real-world failures live.
- **Know what each primitive guarantees.** Confidentiality, integrity, and authenticity are different properties requiring different tools.
- **Encrypt in transit and at rest by default.** Make protection the standard, not an opt-in.
- **Separate key custody from data access.** Whoever manages a key should not automatically be able to read the data it protects.
- **Plan for change.** Algorithms weaken, keys leak, and standards evolve. Build for rotation and migration from day one.
- **Prefer validated implementations where it matters.** For regulated and government work, choose modules with recognized validation.

## Recommendations

### Do not roll your own crypto

This is the golden rule, and it is worth stating first. Never design your own encryption algorithm, invent your own protocol, or hand-implement a primitive from a paper. Working cryptography looks simple and hides subtle failure modes (timing side channels, padding oracles, weak randomness) that only survive years of expert review. Use established libraries such as your platform's standard crypto module or a well-regarded library, and use them at the highest level of abstraction available. Reach for authenticated encryption modes and "easy" interfaces that make the safe choice the default, rather than assembling low-level pieces yourself.

### Match the primitive to the guarantee you need

Different tools provide different guarantees, and confusing them is a common and dangerous mistake. Learn the three main families.

- **[Symmetric-key](https://en.wikipedia.org/wiki/Symmetric-key_algorithm) cryptography** uses one shared secret key to both encrypt and decrypt. It is fast and protects **confidentiality**, but both parties must already share the key. AES is the standard workhorse.
- **[Public-key](https://en.wikipedia.org/wiki/Public-key_cryptography) cryptography** uses a mathematically linked key pair: a public key anyone can hold and a private key you keep secret. It solves key distribution and enables **digital signatures**, which prove **authenticity** (who sent it) and **integrity** (that it was not altered).
- A **[cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)** produces a fixed-size fingerprint of data and provides **integrity** checking. Hashing is one-way and is not encryption. For storing passwords, use a slow, salted password-hashing function, never a plain fast hash (see chapter 4.2 on application security).

The practical lesson: encryption hides data but does not prove who sent it, and a hash detects tampering but does not hide anything. Most real systems combine them, which is exactly why you should lean on libraries that bundle these correctly.

### Encrypt in transit with current TLS

Protect every network hop with [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS), the protocol that secures data as it moves between systems. Require modern TLS versions, disable obsolete ones, choose strong cipher suites, and validate certificates properly rather than disabling checks to "make it work." Encrypt internal service-to-service traffic too, not just the public edge, because a zero-trust posture assumes the internal network is hostile. Automate certificate issuance and renewal so TLS is the effortless default everywhere.

### Encrypt at rest with envelope encryption

Encrypt stored data by default: databases, object storage, backups, and logs. The standard pattern is **envelope encryption**, where a **data encryption key (DEK)** encrypts the actual data, and a **key encryption key (KEK)** held in a key management service encrypts the DEK. This lets you rotate the master key without re-encrypting terabytes of data, and it keeps the powerful root key inside a hardened boundary. Store only the wrapped DEK next to the data, and fetch and unwrap it at use time.

### Run the key lifecycle deliberately

The lifecycle of a key is the genuinely hard part of cryptography, and where most breaches and outages originate. Manage every stage on purpose:

- **Generation:** create keys from a strong random source, at appropriate strength.
- **Distribution:** get keys to the systems that need them without exposing them in code, config files, or chat.
- **Rotation:** replace keys on a schedule, and be able to rotate fast on suspected compromise.
- **Revocation:** invalidate a compromised key or certificate quickly, and make sure systems honour the revocation.
- **Destruction:** securely retire old key material so it cannot be recovered.

Use a **key management service (KMS)** to centralize this, and use a [hardware security module](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM), a tamper-resistant device that generates and guards keys so they never leave in plaintext, for your highest-assurance keys. Separate who can manage keys from who can read the protected data, so key custody enforces separation of duties. This connects directly to data classification and custody rules in chapter 4.5 (privacy and data protection).

### Distinguish secrets management from key management

These overlap but are not the same. **Key management** governs cryptographic keys and their lifecycle, usually inside a KMS or HSM that performs crypto operations for you so the raw key never leaves. **Secrets management** governs application credentials (database passwords, API tokens, certificates) that services need to retrieve and use in plaintext, usually from a secrets vault with short-lived, audited access. Use a KMS for keys, a secrets manager for credentials, and never paste either into source code or environment files checked into version control.

### Automate PKI and certificate lifecycles

**Public key infrastructure (PKI)** is the system of certificate authorities, certificates, and trust chains that binds public keys to identities. At scale, the dominant PKI risk is the surprise certificate expiry that takes down a service. Maintain an inventory of every certificate, monitor expirations, and automate issuance and renewal so no human has to remember. Short-lived certificates renewed automatically are safer than long-lived ones nursed by hand, because automation removes the human single point of failure. Standard protocols here support interoperability across vendors (chapter 3.8 on interoperability and open standards).

### Build for cryptographic agility and post-quantum migration

Algorithms weaken over time, and standards move. **Cryptographic agility** means designing systems so you can swap algorithms and key sizes without a painful rewrite: abstract crypto behind a small interface, version your encrypted data so you know which algorithm produced it, and keep a crypto inventory of what you use where. This matters now because of [post-quantum cryptography](https://en.wikipedia.org/wiki/Post-quantum_cryptography), the new family of algorithms designed to resist future quantum computers. Adversaries can harvest encrypted data today to decrypt later, so long-lived secrets need a migration plan. You do not need to panic, but you should know your inventory and be ready to adopt the standardized post-quantum algorithms as platforms ship them.

### Prefer validated implementations where required

For regulated and government systems, using a strong algorithm is not enough; the implementation must be validated. **FIPS 140** (Federal Information Processing Standard 140) is the U.S. standard for validating cryptographic modules, and many contracts require FIPS-validated crypto. Government work may also follow national guidance such as the NSA's Commercial National Security Algorithm (CNSA) suite for classified systems. Check which regime applies before you build, because retrofitting validated modules late is expensive. This ties into compliance evidence and governance (chapter 4.6).

## Trade-offs: pros and cons

| Decision | Pros | Cons |
|---|---|---|
| Provider-managed KMS | Easy, integrated, low operational burden | Provider holds custody; less direct control |
| Customer-managed keys / HSM | Full custody, meets strict mandates | Operational overhead, risk of losing keys |
| Automated short-lived certificates | No surprise expiries, fast revocation | Requires automation investment upfront |
| Long-lived certificates | Simple, fewer moving parts | Human-managed expiries cause outages |
| Envelope encryption | Cheap key rotation, protects master key | More moving parts to understand |
| Cryptographic agility up front | Cheap future migrations | Extra abstraction and design effort now |
| Early post-quantum adoption | Guards long-lived secrets | Immature tooling, larger keys, some risk |

The central tension is control versus operational burden. Holding your own keys in an HSM gives maximum custody and satisfies the strictest mandates, but it demands expertise and creates a new catastrophic risk: lose the key and you lose the data, irrecoverably. Provider-managed services remove that burden but place custody with the provider. Resolve it by layering: use managed services with sensible defaults for most systems, and reserve customer-managed keys and HSMs for the highest-classification data where the extra control is worth the cost and risk.

## Questions to discuss with your team

1. **Do you have a complete inventory of your keys, certificates, and the algorithms you rely on?** You cannot rotate, migrate, or audit what you cannot see, and most organizations discover they have far more cryptographic material scattered across services than anyone tracks. An inventory is the prerequisite for every later decision: certificate-expiry monitoring, key rotation, FIPS scoping, and post-quantum planning all depend on it. Bring a list of your current certificates and their expiry dates, and ask who owns each and what breaks when it lapses. For a large estate, the honest answer is usually that no single source of truth exists, and building one is the highest-leverage first step. If you cannot enumerate your crypto today, agility and rotation are aspirations, not capabilities.

2. **Can you rotate or revoke a compromised key fast, and have you ever practised it?** Rotation and revocation are the parts of the key lifecycle that only matter under pressure, and teams routinely discover during an incident that a key is hard-coded in a dozen places or that revocation does not actually propagate. Decide your target time to rotate a key and revoke a certificate, then rehearse it before you need it. Bring the story of your last credential exposure and walk through what rotation required in practice. For enterprise and government systems, an unrehearsed rotation can mean choosing between a prolonged exposure and a self-inflicted outage. If rotation has never been tested, assume it does not work.

3. **Where does key custody sit, and does it enforce separation of duties?** Whoever can manage a key and whoever can read the data it protects should not be the same person, because merging those powers quietly defeats the purpose of encryption at rest. This choice also drives whether you use provider-managed keys, customer-managed keys, or HSMs, each with different control and different operational risk. Bring your current key policies and check whether any single identity can both administer a key and access the plaintext behind it, which is a common silent gap. For regulated and classified data, custody rules may be dictated by data classification (chapter 4.5) and by mandate. If custody and access are not separated, your encryption is protecting you less than the dashboard suggests.

4. **How would you recover if the master key that protects your envelope encryption were lost or destroyed?** Customer-managed keys and HSMs give you custody, but they hand you a new catastrophic failure mode: lose the key encryption key and every data encryption key it wraps becomes permanently unreadable, along with the data behind them. Weigh this against the opposite risk of an over-broad backup that quietly recreates the very custody problem you were trying to solve. Bring your current key-backup and escrow arrangements, the blast radius of each master key, and evidence that a restore has actually been performed rather than merely documented. For enterprise and government estates, tie this to your data-classification rules: the most sensitive keys often forbid casual copies, so recovery has to be designed deliberately, tested on a schedule, and reconciled with any regulatory requirement to prove that retired key material was destroyed.

5. **How ready are your systems for a post-quantum migration, and which long-lived secrets would you migrate first?** Adversaries can harvest encrypted traffic and archives today and decrypt them once quantum computers mature, so any secret that must stay confidential for years is already exposed to a future you cannot see. The competing pressure is that post-quantum tooling is still young, the keys are larger, and moving too early risks betting on an algorithm that shifts before it settles. Bring your crypto inventory, a list of secrets ranked by how long they must remain confidential, and an honest read on whether your architecture can swap algorithms without a rewrite. For government and regulated work, records with multi-decade confidentiality mandates make this concrete rather than theoretical, and procurement may soon require a documented migration plan and support for the standardized post-quantum algorithms.

6. **When regulation requires validated cryptography, do you know exactly which modules are in scope and whether they qualify?** Using a strong algorithm is not the same as using a validated implementation, and teams routinely discover late that a library, a language runtime, or a cloud service is not covered by the FIPS 140 boundary a contract demands. The tension is that validated modules can lag behind current libraries in features and speed, so choosing them constrains your stack in ways that matter for engineering. Bring the list of cryptographic modules each regulated system actually calls, the validation certificates that cover them, and the specific mandate (FIPS 140, CNSA, or a sector rule) that applies. For enterprise and government programmes, decide this before you build, because retrofitting validated modules and re-authorizing a system after the fact is expensive, slow, and often forces a redesign of the very components you thought were finished.

## Sector lens

**Startup.** Lean entirely on your platform's vetted defaults and spend zero engineering time on custom crypto. Turn on managed encryption at rest, terminate TLS with automatically renewed certificates, hash passwords with a standard slow function, and keep secrets in the platform's secrets manager rather than the repository. Your one design decision is a thin interface around the handful of fields you encrypt in the application, so a future move off provider-managed keys is not a rewrite.

**Small business.** You have no cryptographer and little appetite for operating an HSM, so buy custody rather than build it: use the provider-managed KMS and secrets manager that come with your cloud or SaaS tools. Frame the work as hygiene, that is, no keys in code, encryption switched on everywhere by default, and certificate expiries monitored so nothing lapses by surprise. Reserve customer-managed keys for the rare data that a contract or regulator genuinely requires them for.

**Enterprise.** The problem is scale and consistency across thousands of services, certificates, and keys. Run a centralized KMS with envelope encryption, automate the full certificate lifecycle so no expiry is nursed by hand, and maintain a single crypto inventory that feeds rotation, FIPS scoping, and post-quantum planning. Separate key custody from data access as an organization-wide control, and make encryption a platform capability every team inherits rather than a task each team reinvents.

**Government.** Procurement, validation, and audit shape every choice. Use FIPS 140-validated modules and follow national guidance such as CNSA for classified systems, tie key custody to data classification so the most sensitive keys sit with cleared personnel under strict separation of duties, and generate continuous evidence of validated crypto for ongoing authorization. Document a post-quantum migration plan for records that must stay confidential for decades, and require vendors to disclose which modules are validated before you commit.

## Examples

**Startup.** A small team building a health-tracking app leans entirely on vetted defaults. They terminate TLS with automatically renewed certificates, enable encryption at rest on their managed database and object storage with the provider's KMS, and hash passwords with a slow, salted function from a standard library. Rather than writing any crypto themselves, they use a high-level authenticated-encryption call for the one field they must encrypt in the application. Secrets live in the platform's secrets manager, never in the repository. It costs a few afternoons and removes an entire category of catastrophic mistakes.

**Enterprise.** A global bank runs a centralized KMS and a fleet of HSMs, with a crypto inventory that tracks every key and certificate across thousands of services. Envelope encryption protects customer data, with data keys wrapped by master keys that rotate on a schedule while the data stays put. Certificate issuance and renewal are fully automated after a public-facing outage taught them the cost of a single expired certificate. Key administrators are a separate team from application engineers, so custody enforces separation of duties, and a cryptographic-agility layer lets them begin piloting post-quantum algorithms for long-lived archives.

**Government.** A national agency handling classified records uses only FIPS 140-validated cryptographic modules and follows NSA CNSA guidance for its highest-classification systems. Keys are generated and held in HSMs that never release plaintext key material, and custody is tied to data classification so that the most sensitive keys sit with cleared personnel under strict separation of duties. Certificates run on a managed internal PKI with automated lifecycles, and continuous evidence of validated crypto feeds the agency's ongoing authorization. A documented post-quantum migration plan protects records that must stay confidential for decades.

## Business case: motivations, ROI, and TCO

Cryptography is another area where a modest investment prevents catastrophic, headline-grade losses. The total cost of ownership includes a KMS or HSM, secrets and certificate management tooling, and the engineering time to design lifecycles and keep an inventory current. These costs are real but bounded. The cost of skipping them is a breach of unencrypted data, a multi-hour outage from an expired certificate, or an irrecoverable data loss from a mishandled key, each carrying regulatory fines, notification costs, and lasting reputational harm.

The strongest ROI comes from automation and reuse. Automated certificate lifecycles eliminate the single most common self-inflicted outage. Centralized key management with sensible defaults means every new service inherits encryption in transit and at rest with no per-team effort, turning cryptography from a recurring tax into a platform capability. For regulated and government work, validated modules and automated evidence also lower the cost of audits and authorization. When you make the case to leadership, frame it plainly: the algorithms are free and proven, the risk lives in key management and certificate operations, and a small, automated investment there prevents the expensive failures.

## Anti-patterns and pitfalls

- **Rolling your own crypto.** Custom algorithms or hand-built protocols that fail in subtle, expert-only ways.
- **Hard-coded keys and secrets.** Credentials pasted into source code, config files, or chat, where they leak and cannot be rotated.
- **Encryption without key discipline.** Turning on encryption but leaving key access wide open or never rotating.
- **Confusing hashing with encryption.** Treating a hash as reversible, or storing passwords with a fast hash instead of a slow, salted one.
- **Certificate roulette.** No inventory, no expiry monitoring, and periodic surprise outages when a cert lapses.
- **Merged key custody and data access.** One identity that can both manage a key and read the data it protects.
- **No rotation plan.** Keys that have never been rotated and cannot be rotated quickly under pressure.
- **Crypto with no agility.** Algorithms wired so deeply that swapping them requires a rewrite, blocking any future migration.
- **Ignoring validation mandates.** Using strong algorithms in unvalidated modules where FIPS or similar validation is required.

## Maturity model

- **Level 1, Initiate:** Encryption is inconsistent and often absent, applied reactively when someone notices a gap. Keys and secrets are hard-coded or shared informally over chat and config files. There is no inventory, no rotation, and certificates expire by surprise, and teams occasionally write their own crypto.
- **Level 2, Develop:** TLS and encryption at rest are switched on for the major systems, and a KMS or secrets manager exists, but adoption is uneven and varies team by team. Some certificates are monitored while others are not, rotation is manual and rare, and no complete crypto inventory ties it together.
- **Level 3, Standardize:** Encryption in transit and at rest is the documented default enforced org-wide. Keys live in a KMS with scheduled rotation and envelope encryption, key custody is separated from data access, certificate lifecycles are automated, a crypto inventory is maintained, and validated modules are used wherever regulation requires them.
- **Level 4, Manage:** The crypto estate is measured and controlled against baselines. You track certificate-expiry lead time, the percentage of keys rotated on schedule, mean time to revoke a compromised key, secrets-in-code detections per period, and inventory coverage, and you review these metrics against targets. Rotation and revocation are rehearsed on a cadence with recorded timings, and deviations trigger corrective action rather than going unnoticed.
- **Level 5, Orchestrate:** Cryptography is a platform capability every service inherits by default, and it is continuously improved and integrated across the organization. Rotation and revocation are fast and routinely exercised, HSMs protect the highest-assurance keys, and cryptographic agility plus an active post-quantum migration plan keep the estate adaptive as algorithms and mandates shift. Compliance evidence is produced automatically and feeds ongoing authorization.

## Ideas for discussion

1. Which systems in your estate justify customer-managed keys or HSMs given their operational cost and catastrophic-loss risk?
2. How would you build and maintain a single source of truth for every key and certificate you own?
3. What is your realistic time to rotate a compromised key today, and what makes it slow?
4. Where does your architecture make swapping a cryptographic algorithm hard, and how would you fix that before a forced migration?
5. Which of your long-lived secrets would matter if an adversary harvested them now and decrypted them years later?
6. Do secrets and keys ever end up in code, config, or logs, and how would you know?

## Key takeaways

- **Do not roll your own crypto.** Use vetted libraries and standard algorithms at the highest safe abstraction.
- **Algorithms are easy; key management is hard.** The lifecycle of a key (generation, distribution, rotation, revocation, destruction) is where real failures live.
- **Know your guarantees:** symmetric and public-key encryption protect confidentiality, signatures prove authenticity and integrity, and hashing detects tampering but is not encryption.
- **Encrypt in transit with current TLS and at rest with envelope encryption**, as the default for every system.
- **Separate key custody from data access**, use a KMS for keys and a secrets manager for credentials, and never hard-code either.
- **Automate certificate lifecycles** to kill the surprise-expiry outage, and keep a crypto inventory.
- **Build for cryptographic agility** and start a post-quantum migration plan for long-lived secrets.
- **Prefer validated implementations** (FIPS 140 and applicable national guidance) where regulation or classification requires them.

## References and further reading

- National Institute of Standards and Technology, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- National Institute of Standards and Technology, *SP 800-57: Recommendation for Key Management*.
- National Institute of Standards and Technology, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- National Institute of Standards and Technology, post-quantum cryptography standards (FIPS 203, 204, and 205).
- Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Open Web Application Security Project, *Cryptographic Storage Cheat Sheet* and *Transport Layer Protection Cheat Sheet*.
- National Security Agency, *Commercial National Security Algorithm (CNSA) Suite* guidance.
