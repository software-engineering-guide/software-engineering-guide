# 3.13 Networking and connectivity

## Overview and motivation

Every request your application makes crosses a network, and the network does not care about your deadlines. Between your code and the database, the payment provider, or the browser sits a stack of moving parts: name resolution, routing, congestion control, encryption handshakes, load balancers, proxies, and firewalls. Most application engineers treat all of this as a flat, reliable pipe, and that assumption is the single richest source of production incidents. The classic [fallacies of distributed computing](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing) (the network is reliable, latency is zero, bandwidth is infinite, the topology never changes, transport cost is zero) name exactly the beliefs that turn a small hiccup into an outage. This chapter is not a networking certification course. It is the working knowledge an application engineer actually needs to build systems that stay up when the network misbehaves.

For a large organization, connectivity is where architecture meets physics and politics at the same time. A global enterprise stitches together data centers, cloud regions, partner APIs, and legacy systems, and each hop adds latency, failure modes, and a security boundary someone must own. Governments layer on strict rules about how traffic enters and leaves their networks and where citizen data may travel. The difference between a team that understands the network and one that ignores it shows up as availability numbers, page-load times, breach reports, and audit findings. This material connects to distributed systems (chapter 3.3), scalability and resilience (chapter 3.5), infrastructure and cloud security (chapter 4.3), and cryptography and key management (chapter 4.8).

The good news is that you do not need to master routing protocols to build resilient systems. You need to know which layers matter for your decisions, where latency comes from, how names resolve, how connections are secured and balanced, and how to fail gracefully at the network boundary. Get those right and most of the network becomes a dependable substrate.

## Key principles

- **The network is a dependency, not a given.** Treat every remote call as something that can be slow, drop, or lie about whether it finished.
- **Latency is set by distance and round trips.** You cannot beat the speed of light, so cut round trips and move data closer to users.
- **Names fail more than machines do.** Name resolution and certificates cause a startling share of outages, so treat them as first-class operational concerns.
- **Secure and terminate encryption deliberately.** Know exactly where traffic is encrypted, where it is decrypted, and who holds the keys.
- **Every network boundary needs a timeout and a fallback.** Unbounded waits and blind retries turn one slow dependency into a global outage.
- **Default to deny at the edges.** Segment networks, control what can leave, and assume the perimeter is already porous.
- **Observe the connection, not just the code.** Connection errors, retransmits, handshake times, and DNS latency are signals your logs usually miss.

## Recommendations

### Understand the layers that actually affect your decisions

You do not need the full seven-layer model memorized, but you do need a mental map. At the transport layer, [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) (TCP) gives you an ordered, reliable byte stream at the cost of a handshake and head-of-line blocking, while the User Datagram Protocol (UDP) gives you cheap, unordered datagrams with no delivery guarantee. Reliable request/response traffic rides TCP; real-time media, gaming, and some telemetry ride UDP because a late packet is worse than a lost one.

The evolution of the Hypertext Transfer Protocol ([HTTP](https://en.wikipedia.org/wiki/HTTP)) changes your performance ceiling. HTTP/1.1 handles one request per connection at a time, so browsers open many connections and you pay repeated handshakes. HTTP/2 multiplexes many streams over one TCP connection, which removes application-level head-of-line blocking but not the TCP-level kind: one lost packet stalls every stream on that connection. HTTP/3 runs over QUIC, a UDP-based transport that gives each stream independent delivery, faster connection setup, and connection migration across network changes. You rarely implement these yourself, but you choose them in your load balancers, content delivery network, and clients, and the choice shows up in tail latency.

### Treat DNS and certificates as production systems

The [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System) (DNS) translates human names into addresses, and it sits in front of nearly every request. A remarkable number of major outages trace back to DNS: a bad record change, an expired zone, a misconfigured resolver, a caching layer serving stale answers, or a slow authoritative server adding hundreds of milliseconds to the first byte. Treat DNS changes with the same rigor as code deploys. Use sane time-to-live (TTL) values so you can move traffic quickly during an incident without inviting stale caching in normal operation, and monitor resolution latency and failure rates as real metrics.

Certificates deserve the same seriousness. When [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS) certificates expire unnoticed, whole services go dark at once, and the failure looks nothing like a code bug. Automate issuance and renewal, track expiry dates centrally, and alert well before the deadline. Decide deliberately where TLS terminates: at the edge load balancer, at a proxy, or all the way to the service. Terminating at the edge simplifies internal traffic but leaves the internal hop unencrypted unless you re-encrypt. Certificate authorities, key rotation, and cipher choices are covered in chapter 4.8; here the operational point is that DNS and certificates fail quietly and take everything with them, so instrument and automate both.

### Balance load at the right layer and put proxies to work

[Load balancing](https://en.wikipedia.org/wiki/Load_balancing_(computing)) spreads traffic across many backends, and where you do it matters. A layer 4 (L4) load balancer routes by IP address and port without reading the payload, so it is fast, protocol-agnostic, and cheap. A layer 7 (L7) load balancer understands HTTP, so it can route by path or header, terminate TLS, retry idempotent requests, and enforce rate limits, at the cost of more work per request. Most application traffic wants an L7 reverse proxy or API gateway at the edge, giving you one place to handle TLS, authentication, routing, and observability. Reserve L4 for raw throughput or non-HTTP protocols.

Health checks are what make load balancing safe. Configure them to reflect real readiness, not just "the process is up," so a backend that cannot reach its database is pulled from rotation before it serves errors, and drain connections on deploys so in-flight requests finish. An API gateway centralizes cross-cutting concerns (authentication, rate limiting, request shaping, versioning) but becomes a critical dependency and a potential bottleneck, so give it the same availability budget and observability as any core service.

### Move data closer to users with a CDN and edge

Latency is dominated by round-trip time, and round-trip time is dominated by distance. A [content delivery network](https://en.wikipedia.org/wiki/Content_delivery_network) (CDN) caches content in points of presence near users so that static assets, and increasingly dynamic and personalized responses, are served from a few milliseconds away instead of across an ocean. For any user-facing product with a geographically spread audience, a CDN is one of the highest-return performance investments you can make, and it doubles as a shield that absorbs traffic spikes and volumetric attacks.

Push work to the edge where it helps. Terminating TLS at the edge cuts handshake latency because the expensive round trips happen close to the user, and caching API responses at edge locations trims the path length for common requests. The trade is cache invalidation: the closer and more cached your data, the harder it is to guarantee freshness, so be explicit about what may be stale and for how long. This connects to the caching and performance discussion in chapter 3.5.

### Make the network boundary resilient by default

Every remote call is a place the network can hurt you, so wrap each one in the same discipline. Set an explicit timeout on every call, because a hung dependency will exhaust your connection and thread pools and stall everything behind it. Retry only operations that are safe to repeat, use exponential backoff with jitter so a blip does not become a synchronized retry storm, and cap total attempts and total time. Add a circuit breaker so that after a threshold of failures you fail fast for a cooldown instead of piling requests onto a service that is already drowning. These patterns are covered in depth in chapter 3.3; the point here is that they belong at the network boundary specifically, ideally as shared platform defaults rather than something each team reinvents.

Budget your timeouts down the call chain. If a user-facing request has a two-second budget and crosses four hops, each hop must know how little time remains and fail fast rather than retry into the void. Reuse connections through pooling and keep-alive so you are not paying a fresh TCP and TLS handshake per request, and watch tail latency, not just averages, because the slow one percent is what users remember and what cascades under load.

### Design and govern your network topology

In the cloud, your network is software you configure, so configure it on purpose. Put workloads in a virtual private cloud (VPC) and segment it: public-facing tiers, application tiers, and data tiers in separate subnets with rules that allow only the traffic that should exist. Control egress as deliberately as ingress. Uncontrolled outbound access is how data leaves during a breach and how compromised workloads reach command-and-control servers, so route outbound traffic through controlled gateways and allow-list the destinations that genuinely need to be reached. Plan for IPv6 rather than treating it as an afterthought, because address exhaustion and partner requirements will force it eventually and retrofitting is painful.

Adopt a [zero trust security model](https://en.wikipedia.org/wiki/Zero_trust_security_model): stop treating "inside the network" as trusted, and authenticate and authorize every request based on identity rather than network location. In practice this means mutual TLS between services, short-lived credentials, and policy that does not assume a request is safe just because it came from a neighboring subnet. A service mesh can deliver much of this uniformly. By running a sidecar proxy alongside each service, a mesh gives you mutual TLS, consistent retries and timeouts, and per-hop telemetry without changing application code. It adds operational complexity and some latency, so adopt it when your service count makes uniform, code-free enforcement worth the overhead. Zero trust and segmentation are developed further in chapters 4.3 and 8.3.

## Trade-offs: pros and cons

| Decision | Pros | Cons / cost |
|---|---|---|
| L7 load balancer / API gateway | Smart routing, TLS termination, auth, rate limiting, observability | More latency per request, a critical shared dependency |
| L4 load balancer | Fast, protocol-agnostic, cheap | Cannot see or act on HTTP, no content-aware routing |
| Edge TLS termination | Faster handshakes, simpler backends | Internal hop unencrypted unless you re-encrypt |
| CDN and edge caching | Big latency win, absorbs spikes and attacks | Cache invalidation and staleness, extra cost and config |
| Service mesh | Uniform mTLS, retries, telemetry without app changes | Operational complexity, sidecar latency and resource cost |
| HTTP/3 over QUIC | No transport head-of-line blocking, fast setup, connection migration | Newer tooling, UDP sometimes throttled, harder to debug |

The central tension is between control and simplicity. Every capable component you add at the network boundary (an L7 gateway, a mesh, a CDN, an egress proxy) buys you routing intelligence, security enforcement, and visibility, and each one also adds a hop, a failure mode, and something to operate. Resolve it by pushing shared concerns to shared infrastructure only when enough teams need them to justify the operational weight, and by keeping the fast path short. A two-person startup terminating TLS at a managed load balancer and calling it done is making a better trade than the same team hand-rolling a service mesh. A thousand-service enterprise without uniform mutual TLS and egress control is making a worse one.

## Questions to discuss with your team

1. **Where does TLS terminate in each of your request paths, and can everyone draw it the same way?** This sounds like trivia until an incident. If half the team believes traffic is encrypted end to end and the other half knows it is decrypted at the edge and sent in plaintext to the backend, you have both a security gap and a debugging trap. For a large organization this question maps directly to compliance: regulators and auditors will ask where citizen or customer data travels in the clear, and "we are not sure" is a finding. Bring an actual diagram of one real path from client to database, marking every point where encryption starts and stops and who holds each certificate and key. The answer should tell you whether you need internal re-encryption, where mutual TLS belongs, and which certificates would take a service down if they expired. If nobody can draw it confidently, that gap is your first task.

2. **What happens to your system when DNS is slow or wrong, and have you actually tested it?** DNS is upstream of nearly every request, yet most teams have never observed their system under DNS degradation. A slow resolver adds latency to every new connection, a stale cache can send traffic to a decommissioned host, and a bad record change can black-hole a whole service in seconds. In a large enterprise the blast radius is wider because internal service discovery, partner integrations, and cloud endpoints all lean on name resolution. Bring your DNS TTL settings, your resolution-latency metrics if you have them, and the runbook for a bad record change, then ask how fast you could actually shift traffic during an incident. The answer should drive whether you monitor resolution as a first-class metric, tune TTLs for both agility and cache efficiency, and rehearse DNS failover. If you have never induced a DNS failure in a controlled test, that experiment belongs on the calendar.

3. **Which resilience patterns at the network boundary are platform defaults, and which is every team reinventing?** Timeouts, bounded retries with jitter, circuit breakers, connection pooling, and per-hop tracing are cheapest and most reliable when built once and inherited by everyone. Left to individual teams, they drift: some calls have no timeout, some retry non-idempotent operations, some emit no connection-level telemetry, and the gaps surface only under load. For a large team this is an organizational choice about where resilience lives, in a shared library or platform layer versus scattered across services. Bring an audit of a sample of services counting how many set an explicit timeout on every remote call and propagate a correlation identifier end to end. If that number is low, the fix is a platform investment, and standardizing it also makes resilience testable and auditable, which matters increasingly in regulated sectors. The answer should tell you whether to fund a networking platform capability or keep paying for inconsistency in incidents.

## Examples

**Startup.** A ten-person software-as-a-service company runs everything behind a single managed L7 load balancer that terminates TLS with automatically renewed certificates, and it puts a CDN in front of its web application and API. That combination gives them fast global page loads, absorbs the occasional traffic spike from a product launch, and shields their origin without a dedicated operations team. They set an explicit timeout and a bounded retry on every call to their payment provider and their email service, wrapped in a small shared client, so a slow third party never hangs a user request. They resist adding a service mesh: with a dozen services, the operational cost would dwarf the benefit, and managed infrastructure already gives them encrypted, load-balanced traffic.

**Enterprise.** A multinational retailer runs across three cloud regions and a legacy on-premises data center, connected by private links rather than the public internet so that inventory and payment traffic never traverses open networks. Each region sits in a segmented VPC with separate public, application, and data subnets, and all outbound traffic flows through egress gateways that allow-list approved destinations, so a compromised workload cannot quietly exfiltrate data. Hundreds of services communicate through a service mesh that enforces mutual TLS everywhere and applies uniform retries, timeouts, and tracing, letting a central platform team roll out a new retry policy without touching application code. Centralized certificate monitoring flags expiries days ahead and automation rotates them before any customer notices.

**Government.** A national agency operates under network boundary protection rules that funnel all internet-bound traffic through a small set of hardened, monitored gateways, consistent with the trusted internet connections model. Inter-agency traffic runs over private connections, and every external endpoint is inventoried, so security teams know exactly what can enter and leave. The agency runs a zero trust architecture in which services authenticate to each other by identity with short-lived credentials, and no request is trusted merely for originating inside the perimeter. DNS and certificate management are treated as critical infrastructure with dedicated monitoring, because a single expired certificate or bad zone change could take a citizen-facing benefits portal offline and generate both public and legislative scrutiny.

## Business case: motivations, ROI, and TCO

Networking discipline is bought cheaply and its absence is paid for at the worst possible moment. The investment is mostly one-time and platform-shaped: shared clients with timeouts and retries, automated certificate management, DNS monitoring, a sensibly segmented VPC, and edge caching. Each benefits every team that inherits it, so the per-team marginal cost is low while the payoff compounds. A CDN in particular often pays for itself twice, cutting origin bandwidth costs while improving the conversion and engagement numbers that follow from faster page loads.

The cost of skipping this work is measured in outages and breaches. An expired certificate or a bad DNS change can take an entire product offline in minutes, with the fix delayed while engineers chase the wrong layer. A missing timeout can cascade one slow dependency into a full platform stall. Uncontrolled egress turns a single compromised workload into a data exfiltration incident. Frame the case to leadership in terms they already track: availability, mean-time-to-recovery, page-load time, and breach risk. Automated certificate and DNS management prevent a category of self-inflicted outages, edge and CDN investment moves a product performance metric, and segmentation and egress control shrink breach blast radius. The total-cost-of-ownership argument is the one that recurs throughout this guide: building the capability in is a fraction of the cost of retrofitting it after the incident that forces the issue.

## Anti-patterns and pitfalls

- **Assuming the network is reliable and fast.** Coding as if remote calls are local, with no timeouts, no retries, and no handling for "timed out but maybe completed."
- **Manual certificate management.** Tracking expiry in a spreadsheet or someone's memory, guaranteeing an eventual outage when it lapses unnoticed.
- **Ignoring DNS as an operational system.** No resolution monitoring, careless TTLs, and record changes made without the rigor of a deploy.
- **Retrying without idempotency or backoff.** Duplicate side effects and synchronized retry storms that amplify a small blip into an outage.
- **Trusting the internal network.** Treating anything inside the perimeter as safe, with unencrypted internal traffic and no identity-based authorization.
- **Uncontrolled egress.** Allowing workloads to reach any outbound destination, handing attackers an exfiltration path and a channel to command servers.
- **Chatty request paths.** Deep synchronous call chains where each hop adds a round trip, so tail latency balloons under load.
- **Adopting a service mesh too early.** Taking on sidecar complexity and latency for a handful of services that a shared client would serve better.

## Maturity model

- **Level 1, Initial:** Remote calls are treated like local calls. Timeouts and retries are missing or naive. Certificates and DNS are managed by hand and cause surprise outages. There is no segmentation, and internal traffic is trusted by default.
- **Level 2, Managed:** Timeouts and basic retries exist but are inconsistent across services. TLS is terminated at a load balancer and certificates are mostly automated. A CDN fronts static content. Basic network segmentation exists, though egress is largely open.
- **Level 3, Defined:** Timeouts, backoff with jitter, and circuit breakers are standard through shared libraries or a gateway. DNS and certificates are monitored and automated as production systems. VPCs are segmented with controlled ingress and egress, and connection-level telemetry is collected. Zero trust principles are being adopted.
- **Level 4, Optimizing:** Resilient networking is the platform default and is continuously tested, including induced DNS and dependency failures. Mutual TLS and identity-based authorization are uniform, often via a service mesh. Edge and CDN strategy is tuned against real latency data, egress is fully governed, and teams reason explicitly about round trips, tail latency, and boundary failure modes.

## Ideas for discussion

1. If your primary DNS provider or resolver degraded for an hour, how much of your system would still work, and how would you know?
2. Which of your services still send traffic unencrypted once it is "inside" the network, and what would it take to close that gap?
3. Where are the deepest synchronous call chains in your architecture, and how many network round trips does a typical user request actually incur?
4. Do your timeouts compose down the call chain into a coherent budget, or does each layer set its own and hope?
5. What can your workloads reach on the public internet right now, and who approved each of those outbound destinations?
6. At what number of services would a service mesh's uniform enforcement outweigh its operational cost for your organization, and how close are you?

## Key takeaways

- The network is a dependency with its own failure modes; design every remote call for slowness, loss, and ambiguous completion, not just success or clean failure.
- Latency is governed by round trips and distance, so cut hops, reuse connections, and move data closer to users with a CDN and edge.
- DNS and TLS certificates fail quietly and take whole services down; automate and monitor both as production systems.
- Balance load at the layer that fits the traffic, and put shared concerns behind an L7 gateway only when the availability and observability cost is justified.
- Make the network boundary resilient by default with timeouts, bounded retries with jitter, and circuit breakers, ideally as inherited platform defaults.
- Segment your VPC, govern egress, plan for IPv6, and adopt zero trust so that being "inside" the network confers no automatic trust.

## References and further reading

- W. Richard Stevens, *TCP/IP Illustrated, Volume 1: The Protocols*
- Ilya Grigorik, *High Performance Browser Networking*
- Cricket Liu and Paul Albitz, *DNS and BIND*
- Andrew S. Tanenbaum and David J. Wetherall, *Computer Networks*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Evan Gilman and Doug Barth, *Zero Trust Networks: Building Secure Systems in Untrusted Networks*
- Lee Calcote and Zack Butcher, *Istio: Up and Running* (service mesh concepts)
- Internet Engineering Task Force, RFC 9110 (HTTP Semantics) and RFC 9000 (QUIC)
- Peter Deutsch and James Gosling, "The Eight Fallacies of Distributed Computing"
- National Institute of Standards and Technology, *Special Publication 800-207: Zero Trust Architecture*
