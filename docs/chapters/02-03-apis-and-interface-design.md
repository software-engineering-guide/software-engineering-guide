# 2.3 APIs and interface design

## Overview and motivation

An [API](https://en.wikipedia.org/wiki/API) (application programming interface) is the contract through which one piece of software offers capability to another. It is where teams, systems, and organizations meet, and it is the most durable and expensive thing to get wrong. You can refactor an internal function signature freely. A published API is different: it is a promise to consumers you may never meet, and breaking it breaks them. As organizations split [monoliths](https://en.wikipedia.org/wiki/Monolithic_application) into services and open up capabilities to partners and the public, the API becomes the main product surface and the main integration risk.

For large teams, APIs are what let people work independently. A well-designed interface lets you change your internals without coordinating with every consumer, which is the whole point of a service boundary. A poorly designed one leaks internal detail, forces lockstep deployment, and turns a set of services into a distributed monolith: services split apart yet so coupled they must be built and deployed together. Your API design directly determines how independently your teams can move.

In enterprise and government settings, APIs also carry compliance, security, and longevity obligations. A public-sector API may be required to follow [open standards](https://en.wikipedia.org/wiki/Open_standard), stay stable for years, and serve external developers you cannot coordinate with. Enterprise APIs underpin partner integrations with contractual service levels. All of this raises the bar on versioning discipline, [backward compatibility](https://en.wikipedia.org/wiki/Backward_compatibility), governance, and developer experience.

## Key principles

- Design the contract first. The interface is a deliberate product decision, not a byproduct of implementation.
- Optimize for the consumer's experience, not your own convenience.
- Treat backward compatibility as a promise. Breaking changes need a new version and a migration path.
- Make the easy thing correct: sensible defaults, predictable errors, consistent conventions.
- Design for failure. [Idempotency](https://en.wikipedia.org/wiki/Idempotence) (a repeated request has the same effect as a single one), retries, pagination, and [rate limiting](https://en.wikipedia.org/wiki/Rate_limiting) are first-class concerns, not afterthoughts.
- Choose the protocol style to fit the interaction, not the fashion.
- Govern APIs as products, with owners, lifecycles, and documentation.

## Recommendations

### Work API-first and contract-driven

Define and review the API contract, including its resources, operations, schemas, and error semantics, before you write the implementation. Use a machine-readable specification, so the contract can generate documentation, client and server stubs, mock servers, and validation. Now consumers can start integrating against the mock while you build, and the contract becomes the single source of truth that both sides test against.

### Choose the interaction style deliberately

Choose among [REST](https://en.wikipedia.org/wiki/REST) (representational state transfer), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [gRPC](https://en.wikipedia.org/wiki/GRPC), and [event-driven messaging](https://en.wikipedia.org/wiki/Event-driven_architecture) based on the interaction, not personal preference. Use REST for resource-oriented, broadly interoperable, cacheable interfaces. Use GraphQL when diverse clients need flexible, aggregated reads over a rich graph. Use gRPC for high-performance, strongly-typed calls between internal services. Use event-driven messaging for asynchronous, decoupled workflows and for propagating state changes. Many large systems use several styles at once, each where it fits.

### Version and deprecate with discipline

Adopt an explicit versioning strategy and a published deprecation policy: how you classify changes, how long you support old versions, and how you notify consumers. Draw a clear line between backward-compatible changes (adding optional fields, new endpoints) and breaking changes (removing or renaming fields, changing types or semantics). Never repurpose the meaning of an existing field. Give consumers overlap windows to migrate, and communicate timelines well in advance.

### Make error semantics consistent and machine-readable

Return structured, predictable errors: stable machine-readable codes, human-readable messages, and enough context to act on, without leaking sensitive internals. Use the same status semantics across every endpoint, so clients can handle errors uniformly. Document every error a consumer might run into.

### Build in idempotency, pagination, and rate limiting

Make write operations safe to retry by supporting idempotency keys, so a client that retries after a timeout does not double-charge or double-create. Paginate every list endpoint from day one, and prefer cursor-based pagination for large or changing datasets. Apply and document rate limits, and return the current limit state to clients so they can back off gracefully.

### Govern APIs and invest in developer experience

Treat each API as a product, with an owner, a lifecycle, and a catalogue entry. Set up a design review or an API-standards board so interfaces stay consistent across teams. Invest in developer experience: accurate reference docs, quickstarts, examples, a sandbox, and a changelog. In a large ecosystem, a portal or catalogue that makes APIs discoverable is essential.

## Trade-offs: pros and cons

| Style | Best for | Pros | Cons |
|---|---|---|---|
| REST / HTTP | Public, resource-oriented APIs | Ubiquitous, cacheable, simple, interoperable | Over/under-fetching; many round trips; loose contracts unless specified |
| GraphQL | Flexible reads for varied clients | Client-specified queries; one endpoint; strong schema | Caching and rate-limiting complexity; query-cost risks; server complexity |
| gRPC | Internal high-performance calls | Fast, compact, strongly typed, streaming | Poor browser support; less human-readable; heavier tooling |
| Event-driven | Async, decoupled workflows | Loose coupling; scalable; resilient | Harder to reason about; eventual consistency; operational complexity |

Versioning strategies trade stability against maintenance. Supporting many old versions protects consumers, but it multiplies the code you have to maintain and test. Backward compatibility trades your own freedom for consumer stability, usually the right trade for a widely used API. The big picture: the cost of a bad API decision is paid by every consumer over the entire life of the interface. So it is worth spending more design effort at the boundary than almost anywhere else.

## Questions to discuss with your team

1. **How do you classify a change as backward-compatible versus breaking, and what automated check catches a silent break before it ships?** This chapter draws a hard line: adding optional fields and new endpoints is safe, while removing or renaming fields, changing types, or repurposing a field's meaning breaks consumers. On a large team the person making the change often cannot see every consumer, so a "small" tweak can quietly break partners you never talk to. Bring the concrete signal to the meeting: do you run automated contract-compatibility checks in CI against the published spec, or do you rely on someone remembering the rule. In enterprise and government settings, where a breaking change forces a coordinated migration across every partner and can span vendor and administration changes, the cost scales with consumer count. Decide the classification rules and wire a compatibility gate, so an incompatible change fails the build instead of an integration.

2. **Which reliability primitives, idempotency keys, pagination, and rate limiting, are mandatory on every new endpoint from day one?** The chapter insists these are first-class concerns, because retrofitting an idempotency key onto a live charge endpoint or adding pagination to a list that already ships is itself a breaking change. A large ecosystem amplifies this: an endpoint that works in testing collapses under real data volume, and a non-idempotent write turns one network blip into duplicate charges. Bring the evidence of which current endpoints lack these and what a retry storm would do. Make the defaults non-negotiable for new endpoints: cursor pagination on every list, idempotency keys on every write, documented rate limits that return their current state. That converts a future forced migration into a one-time design habit.

3. **Do you genuinely design and review the contract before writing the implementation, or does the interface leak out of the code?** The API-first recommendation asks for a machine-readable spec, reviewed up front, that generates docs, stubs, and mocks and lets consumers integrate against a mock while you build. When the contract trails the implementation, the interface exposes internal database structure and shifts every time the implementation does, which is the top anti-pattern in this chapter. The signal to examine: can a consumer start integrating against your mock today, or must they wait for a running backend. For public and partner APIs, where the interface is the product surface and the most expensive thing to get wrong, spending a day on the contract saves weeks of support churn. Make contract review a required step before implementation starts.

4. **When two teams need to expose the same capability, which interaction style wins, and who has the authority to say no to a fourth protocol?** This chapter tells you to choose REST, GraphQL, gRPC, or event-driven messaging by interaction fit, but at scale the real risk is that every team picks its own favourite and consumers face a different convention on every endpoint. A large organization pays for that fragmentation in client libraries, gateways, monitoring, and the cognitive load on every integrator who now learns four idioms instead of one. Bring the inventory of protocols already in production, the interaction each was chosen to serve, and the consumers who span more than one. The competing consideration is genuine: a shared default reduces sprawl, yet a rigid mandate forces gRPC-shaped problems into a REST-shaped hole. Name the standards body or architecture review that owns the exception process, because in enterprise and government estates a proliferation of styles becomes a permanent tax on integration and a hard problem to reverse once partners depend on each one.

5. **What is our published deprecation policy, and can we prove we actually honour the support window we advertise?** The chapter treats versioning and deprecation as discipline: a written policy for how long old versions live, how consumers are notified, and what overlap they get to migrate. A promise you cannot enforce is worse than none, because a large ecosystem includes consumers you never speak to who will keep calling a retired version until it breaks in production. Bring the evidence to the discussion: how many live versions you carry today, the real usage on each, whether you can see which consumers still call a deprecated endpoint, and how far in advance your last sunset was announced. The competing pressure is maintenance cost against consumer stability, and both are real. For enterprise partners under contractual service levels and public-sector APIs that must survive across administrations and vendor changes, the support window is a commitment that may outlast the team that made it, so decide who owns it and how a sunset is proven safe before it happens.

6. **How do we know our developer experience is good, or are we assuming it because the API works for us?** This chapter frames each API as a product whose adoption depends on accurate reference docs, quickstarts, examples, a sandbox, a changelog, and a discoverable catalogue. Teams routinely mistake "the API functions" for "the API is usable", and the gap shows up as support tickets, failed integrations, and consumers who quietly give up. Bring measurable signals rather than opinions: time-to-first-successful-call for a new integrator, support-ticket volume per endpoint, how stale the published docs are against the live contract, and whether a newcomer can self-serve from the portal without emailing your team. The tension is that documentation and portals cost real effort that competes with shipping features, yet in a large ecosystem poor developer experience pushes integration cost onto hundreds of consumers at once. In government, where an open API serves external developers you cannot coordinate with and transparency is often mandated, a usable, well-documented, discoverable interface is part of the public accountability obligation, not a nice-to-have.

## Sector lens

**Startup.** With two or three engineers and no time for ceremony, keep the contract lightweight but real: a single machine-readable spec that your first design-partner customers can integrate against while you build. Do not stand up an API gateway, a catalogue, or a governance board yet, but do lock in the two habits that are painful to add later, idempotency keys on writes and cursor pagination on lists, because retrofitting them onto a live endpoint is a breaking change you cannot afford. Favour one interaction style, almost always REST, so you carry no protocol sprawl into your first year.

**Small business.** With no dedicated API specialist and a tight budget, lean on tools that generate docs, mocks, and client stubs from a spec so a generalist can maintain the interface without deep protocol expertise. Weigh buy versus build hard: an off-the-shelf gateway or an API-management platform gives you rate limiting, keys, and a developer portal you would otherwise hand-roll. Keep the surface small and the conventions consistent, since every extra endpoint and every one-off error format is something a thin team has to support forever.

**Enterprise.** Across many autonomous teams, the central problem is consistency without becoming a bottleneck: a shared style guide, an API-standards review, a catalogue that makes interfaces discoverable, and automated backward-compatibility checks in CI so a silent break fails the build rather than an integration. Govern each API as a product with a named owner, a lifecycle, and a published deprecation policy, and measure adoption, support load, and breaking-change frequency so the portfolio stays healthy. Standardize the interaction styles and the versioning rules org-wide, because at this scale fragmentation is the expensive default.

**Government.** Procurement rules, open-standards mandates, and public accountability shape every choice. Publish the contract openly, follow the mandated open standards, and provide a sandbox and reference docs so external developers you cannot coordinate with can self-serve. Treat long-term backward compatibility as a policy requirement, since integrations must survive across administrations and vendor changes, and make breaking changes rare, heavily governed, and announced far in advance. Keep the API and its documentation transparent enough to withstand public and audit scrutiny, and avoid proprietary formats that would trap a future administration.

## Examples

**Startup.** A seed-stage startup shipping its first public API writes the contract as a machine-readable spec before coding, so its two design-partner customers can integrate against a mock while the backend is still being built. Even with only a handful of consumers, it adds idempotency keys to the charge endpoint and cursor pagination to every list, because retrofitting them once partners depend on the API would mean a breaking change it cannot afford. The upfront contract costs a day and saves weeks of support back-and-forth.

**Enterprise.** A large payments company exposes a public REST API to thousands of merchants. Every write endpoint accepts an idempotency key, so a network retry never creates a duplicate charge. Every list endpoint uses cursor pagination. Errors carry stable codes documented in a public reference. A formal deprecation policy guarantees a long support window for any version, with advance notice and migration guides. This discipline is a competitive advantage: integrators trust that the API will not break under them.

**Government.** A national digital service publishes an open API for citizen data, following mandated open standards and an API-first design process. The contract is specified and reviewed before the build, published in a central government API catalogue, and served with a sandbox, so third-party developers, who cannot be individually coordinated, can integrate on their own. Long-term backward compatibility is a policy requirement, because integrations must survive across administrations and vendor changes. So breaking changes are rare and heavily governed.

## Business case: motivations, ROI, and TCO

Good API design lowers integration cost, which is often the biggest cost in connecting systems and onboarding partners. With a clear, stable, well-documented API, consumers integrate in days without a single support ticket. A poor one generates endless support load, failed integrations, and reputational damage. When the API is itself the product, developer experience directly drives adoption and revenue.

The largest hidden cost is breaking changes. Every breaking change forces a coordinated migration across all consumers, internal teams and external partners alike, and the total cost scales with the number of consumers and how hard it is for them to move in lockstep. Investing up front in contract-first design, backward compatibility, and versioning discipline avoids these expensive, organization-wide migration events. When you talk to leadership, frame API quality as the leverage point for team autonomy, partner ecosystem growth, and avoiding costly forced migrations. Track integration time, support-ticket volume, and breaking-change frequency as your evidence.

## Anti-patterns and pitfalls

- **Implementation-first APIs:** the interface leaks internal database structure and changes whenever the implementation does.
- **Silent breaking changes:** repurposing a field or tightening validation without a version bump breaks consumers unpredictably.
- **Chatty interfaces:** designs that require many round trips for one logical operation, hurting performance and usability.
- **Inconsistent conventions:** every endpoint invents its own naming, error format, and pagination, so clients cannot generalize.
- **No pagination or rate limiting:** endpoints that work in testing and collapse under real data volume or load.
- **Non-idempotent writes:** retries cause duplicates; a single network blip corrupts data.
- **Version proliferation:** too many live versions with no deprecation, multiplying maintenance until it is unmanageable.
- **Docs as an afterthought:** undocumented or out-of-date references that push all integration cost onto consumers.

## Maturity model

- **Level 1, Initiate:** APIs emerge from implementation as a byproduct; there are no shared conventions; the interface leaks internal database structure; breaking changes are common, unannounced, and discovered when a consumer's integration fails.
- **Level 2, Develop:** Some teams follow basic REST conventions, version informally, and hand-write docs, but practice is inconsistent across teams; idempotency, pagination, and rate limiting appear on some endpoints and not others; consumers still learn each API's quirks case by case.
- **Level 3, Standardize:** Contract-first design with machine-readable specs is documented and enforced org-wide; a published deprecation policy, consistent error semantics, and mandatory idempotency, cursor pagination, and rate limiting apply to every new endpoint; a shared style guide and an API-standards review keep interfaces consistent across teams.
- **Level 4, Manage:** The API portfolio is measured and controlled against baselines: automated backward-compatibility checks gate every change in CI, and you track time-to-first-successful-call, support-ticket volume per endpoint, breaking-change frequency, live-version count, and per-endpoint usage so deprecation and design decisions rest on evidence rather than opinion. Each API is a governed product in a catalogue with a named owner, and metrics trigger action when a service drifts from its targets.
- **Level 5, Orchestrate:** API strategy is continuously improved and integrated across the organization; the catalogue, gateway, versioning rules, and compatibility gates work as one system; the organization routinely retires, consolidates, and re-scopes interfaces based on measured adoption and cost; interaction-style and versioning standards adapt as the ecosystem, partners, and technology shift, and breaking changes are rare and well-managed.

## Ideas for discussion

- How do you decide when an internal API is stable enough to publish externally?
- What is the right support window for deprecated versions in your context, and who pays for it?
- Where should GraphQL or gRPC replace REST internally, and where would they add more complexity than value?
- How do you enforce API consistency across many autonomous teams without becoming a bottleneck?
- How should AI-consumable APIs and agent tool interfaces change your design conventions?
- What automated checks can catch backward-incompatible changes before they ship?

## Key takeaways

- Design the contract first; the API is a product and a long-lived promise.
- Backward compatibility protects consumers; breaking changes need new versions and migration paths.
- Choose REST, GraphQL, gRPC, or events by interaction fit, not fashion.
- Build in idempotency, pagination, rate limiting, and consistent errors from day one.
- Govern APIs as products with owners, catalogues, and strong developer experience.

## References and further reading

- Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures* (dissertation)
- Arnaud Lauret, *The Design of Web APIs*
- Mike Amundsen, *RESTful Web APIs* and *Design and Build Great Web APIs*
- Sam Newman, *Building Microservices*
- OpenAPI Specification; JSON Schema (as reference standards)
- Martin Kleppmann, *Designing Data-Intensive Applications*
