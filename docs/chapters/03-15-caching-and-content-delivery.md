# 3.15 Caching and content delivery

## Overview and motivation

A [cache](https://en.wikipedia.org/wiki/Cache_(computing)) is a copy of data kept somewhere faster or closer than the original, so you can answer a request without doing the full, expensive work again. Almost every system that feels fast is fast because of caching. The database query that would take 40 milliseconds returns in under one when its result already sits in memory. The image that would cross an ocean is served from a machine in the same city. Caching is the single highest-leverage performance technique you have, and it is also the one most likely to hand you a subtle, maddening bug.

This chapter goes deep on caching strategy. Chapter 3.4 (data architecture and storage) introduces caches and content delivery networks as one storage concern among many, and chapter 3.13 (networking and connectivity) covers the network path they ride on. Here you get the decisions: where to place a cache, how to key it, when to invalidate it, how to protect it under load, and how to reason about the staleness you are trading for speed. Caching touches performance engineering (chapter 2.16), scalability and resilience (chapter 3.5), the partial-failure realities of distributed systems (chapter 3.3), and, because a poisoned cache can serve an attack to thousands of users, application security (chapter 4.2).

The motivation comes down to three levers. Caching cuts latency, so users wait less. It cuts load, so your origin serves more traffic on the same hardware. And it cuts cost, because a request answered at the edge never touches your database, your compute, or your egress bill. For large teams, a shared caching strategy is the difference between a platform that scales predictably and one where every service reinvents invalidation and gets it wrong. In enterprise and government systems, where traffic spikes on filing deadlines and launch days, a well-designed cache is often what stands between a working portal and a public failure.

## Key principles

- Cache to cut latency, load, and cost, and know which one you are buying.
- Place caches at the right layer of the hierarchy, closest to where they help most.
- Treat invalidation as the hard part; design keys and lifetimes before you cache.
- Protect the cache under load with coalescing, jitter, and stampede defences.
- Choose a write pattern deliberately: consistency and speed pull against each other.
- Measure hit rate, staleness, and origin load; an unmeasured cache is a liability.
- Treat cached content as an attack surface; a poisoned cache serves everyone.

## Recommendations

### Understand the cache hierarchy

Caching is not one thing in one place. It is a hierarchy of copies, each closer to the user than the last, and you design across all of it. Nearest the user is the client cache: the browser's HTTP cache, a mobile app's local store, an in-process memory cache. Next is the [content delivery network](https://en.wikipedia.org/wiki/Content_delivery_network) (CDN), a fleet of servers distributed around the world that hold copies of your content at the network edge, near users. Behind that sits the reverse proxy or gateway cache, a shared cache in front of your servers. Then the application cache: a fast key-value store such as an in-memory data grid holding computed results, sessions, and rendered fragments. Finally the database's own query and buffer cache, which keeps hot pages in memory so the disk is touched less.

Each layer serves a distinct job: the client cache eliminates the request entirely, the CDN absorbs global read traffic, the reverse proxy shields your origin from repeated identical work, the application cache saves recomputation, and the database cache keeps the store responsive. A request that misses every layer and reaches the database is the slowest, most expensive path you have, so the point of the hierarchy is to answer as far up and out as you safely can. Design it as a system, because a cached fragment at the application layer and a stale CDN copy above it can disagree in ways that confuse users.

### Treat invalidation as the hard problem

There is an old joke that the two hardest problems in computer science are naming things, [cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation), and off-by-one errors. The joke endures because invalidation genuinely is hard: a cache is a copy, and the instant the original changes, every copy is a potential lie. You have three broad strategies. Time-based expiration with a time to live (TTL), the duration an entry stays valid before it is considered stale, is the simplest: you accept bounded staleness and let entries age out. Explicit invalidation purges or updates entries when the underlying data changes, which is precise but requires you to know every place a copy lives. Event-driven invalidation subscribes caches to change events so they refresh themselves, which scales better across many caches but adds a messaging dependency.

Most real systems blend these: short TTLs for data that changes often and tolerates seconds of staleness, longer TTLs plus explicit purge for data that changes rarely but must be correct when it does, and versioned cache keys for content that is immutable once published. The versioned-key trick is worth internalizing: instead of invalidating, you change the key. A stylesheet served as `app.v187.css` never needs purging, because a new version is a new key and the old one simply stops being requested. Whenever you can turn an invalidation problem into a naming problem, do it.

### Design cache keys and TTLs on purpose

A cache is only as good as its key. The [cache key](https://en.wikipedia.org/wiki/Cache_(computing)) is the identifier under which a value is stored and looked up, and getting it wrong causes two opposite failures. Too coarse, and you serve one user's data to another: a personalized page cached under a URL that ignores the user identity is a data leak. Too fine, and your hit rate collapses because no two requests share a key. Decide deliberately what belongs in the key: the resource identity plus whatever legitimately varies the response (language, currency, device class) and nothing that does not. Normalize keys so trivial differences like query parameter order do not fragment the cache.

TTLs deserve the same thought. A TTL is a promise about the maximum staleness you will serve, so set it from the data's real tolerance, not a round number someone guessed: a stock ticker tolerates seconds, a product catalogue minutes, a published regulation hours or a versioned key and no expiry at all. Add a small random spread, called jitter, so a batch of entries written together does not all expire in the same instant and stampede the origin. Write these choices down, because a TTL with no rationale is a number the next engineer will be afraid to change.

### Protect against stampedes and coalesce requests

When a popular cached entry expires, every request that wanted it misses at once and rushes the origin together. This is the [cache stampede](https://en.wikipedia.org/wiki/Cache_stampede), also called the thundering herd, and it can knock over the very database the cache was protecting. Build the defences once and reuse them everywhere. Request coalescing (single-flight) lets only the first request for a missing key recompute the value while the others wait for its result, so a thousand simultaneous misses cause one origin call. Probabilistic early recomputation refreshes a hot entry at random slightly before it expires, so one background request renews it before the crowd sees a miss. A stale-while-revalidate policy serves the slightly stale copy immediately and refreshes it asynchronously, so users never wait on a miss at all.

These patterns matter most exactly when you need the cache most, under peak load, so validate them at realistic scale: a defence that works with ten users can still fail at ten thousand. Pair them with the resilience patterns of chapter 3.5, especially timeouts and circuit breakers, so that when the origin is genuinely slow your cache layer shields it rather than piling on. The goal is a cache that behaves best under pressure, not one that amplifies a spike into an outage.

### Choose a write pattern deliberately

How you handle writes decides how fresh your cache stays and how much you risk on failure. There are four common patterns. In [cache-aside](https://en.wikipedia.org/wiki/Cache_(computing)) (lazy loading), the application checks the cache, and on a miss reads the origin, populates the cache, and returns the value; writes go to the origin and invalidate the entry. It is the default for good reason: simple, and the cache holds only what is requested. In write-through, every write goes to cache and origin together, so the cache is always current, at the cost of write latency and caching data that may never be read. In write-back (write-behind), writes hit the cache first and flush to the origin asynchronously, making writes fast but risking loss if the cache dies before the flush. In write-around, writes go straight to the origin and skip the cache, avoiding churn from write-heavy data that is rarely read, at the cost of a guaranteed first-read miss.

Pick per workload, not once for the whole system. A read-heavy catalogue suits cache-aside or write-through. A write-heavy log or metrics stream suits write-around, so the cache is not churned by data no one re-reads. Write-back suits high-throughput writes where a small, understood risk of loss is acceptable and durability is handled elsewhere. State the pattern for each cache explicitly, because a reader who assumes cache-aside when the code does write-back will misjudge both freshness and failure behaviour.

### Match eviction policy to your access pattern

A cache has a fixed size, so when it fills, something must go. The eviction policy decides what. [Least recently used](https://en.wikipedia.org/wiki/Cache_replacement_policies) (LRU) evicts the entry untouched for the longest, betting that recent use predicts future use, and it is a sensible default. Least frequently used (LFU) evicts the entry with the fewest hits, which suits stable hot sets where a few items are perennially popular but can cling to entries that were hot once and never adapt. Variants such as segmented LRU and adaptive policies blend recency and frequency; first-in-first-out and simple time-based expiry are cheaper but blunter.

Match the policy to how your data is accessed: LFU or a frequency-aware policy for a small hot set that rarely shifts, LRU where popularity moves over time as with news or trending content. Whatever you choose, size the cache so the hot set fits, because a cache too small to hold the working set thrashes, evicting entries just before they are needed again. Watch the eviction rate as a first-class metric, since a sudden rise usually means the cache is undersized or a key explosion is fragmenting it.

### Use HTTP caching semantics correctly

The web has a mature, standardized caching model built into [HTTP](https://en.wikipedia.org/wiki/HTTP), and using it well gets you client and CDN caching for free. The `Cache-Control` header is the control surface: `max-age` sets the freshness lifetime, `public` and `private` say whether shared caches may store the response, `no-store` forbids caching, and `stale-while-revalidate` permits serving a stale copy while refreshing. Validation lets a cache check freshness cheaply without refetching the body. An [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) (entity tag) is an opaque version identifier the server attaches to a response; the client sends it back in an `If-None-Match` header, and the server replies `304 Not Modified` with no body if nothing changed. `Last-Modified` with `If-Modified-Since` does the same using timestamps.

The practical discipline is to be explicit. Set `Cache-Control` on every response rather than leaving caches to guess with heuristics. Mark private, per-user responses `private` or `no-store` so a shared proxy never stores them, a common and dangerous mistake. Use versioned URLs with long max-age and the `immutable` directive for static assets, and validation with ETags for content that changes unpredictably. Getting these headers right turns the entire client and CDN tier into a correct, standards-based cache you did not have to build.

### Push work to the edge with CDNs and edge computing

A CDN started as a way to cache static files near users, and it still does that superbly: images, scripts, video, and downloads served from an edge location milliseconds away instead of a distant origin. Modern CDNs go further. They cache dynamic and personalized content with fine-grained keys, terminate TLS at the edge, absorb traffic spikes and distributed denial-of-service attacks, and increasingly run your code. [Edge computing](https://en.wikipedia.org/wiki/Edge_computing) executes logic at the edge locations themselves, so you can personalize a response, check authorization, or assemble a page fragment without a round trip to a central region.

Lean on this for the reads that dominate most systems. Put static assets behind the CDN with long-lived versioned URLs, cache API responses at the edge where freshness allows (keyed carefully so personalization does not leak), and use edge compute for latency-sensitive, lightweight logic close to users. The trade-off is reach versus control: the edge is fast and close but far from your data and harder to debug, so keep anything requiring strong consistency or fresh authoritative state in the origin and let the edge handle the vast, cacheable read traffic.

### Treat the cache as an attack surface

A cache serves the same stored response to many users, which makes it a target. [Cache poisoning](https://en.wikipedia.org/wiki/Cache_poisoning) is an attack where a request is crafted so the cache stores a harmful or attacker-controlled response and then serves it to everyone who follows. It usually exploits an unkeyed input: a header the application reflects into the response but the cache ignores when building the key. The related web cache deception attack tricks a cache into storing a victim's private response under a public URL. Both are failures of keying and of trusting inputs, covered more broadly in chapter 4.2.

Defend deliberately. Include in the cache key every input that can change the response, and refuse to reflect unkeyed headers into cached bodies. Never let a shared cache store authenticated, per-user responses under a shared key. Normalize and validate request paths and parameters before caching. Set `Vary` correctly so caches partition responses by the headers that actually matter, such as content encoding or language. Because a single poisoned entry harms every downstream user, treat cache configuration as security-sensitive code and review it as such.

### Make cache behaviour observable

You cannot manage a cache you cannot see. The headline metric is the hit rate: the fraction of requests served from cache rather than the origin. A hit rate that quietly drops from 95 to 70 percent can multiply origin load severalfold and precede an outage, and you will only catch it early if you watch it. Instrument each layer separately, since a healthy CDN hit rate can hide a collapsing application-cache hit rate underneath. This is the caching-specific face of the observability practices in chapter 9.2.

Track more than hits: eviction rate and memory pressure to catch undersizing, latency at each layer to confirm the cache is actually faster, origin request rate to see how much load the cache absorbs, and staleness (how old served entries are) to confirm you honour your freshness promises. Alert on the ratios that predict trouble, especially a falling hit rate or a rising eviction rate, so you learn about a degrading cache from a dashboard rather than from users. An observed cache is an asset you can tune; an unobserved one is a hidden dependency waiting to surprise you.

## Trade-offs: pros and cons

Caching buys speed and scale with the currency of freshness and complexity. Every cache is a bet that stale-but-fast beats fresh-but-slow for this particular data, and the art is placing that bet consciously rather than by default. The table below summarizes the main choices.

| Choice | Pros | Cons |
|---|---|---|
| Cache-aside | Simple; caches only what is read | First read always misses; risk of brief staleness after writes |
| Write-through | Cache always current on write | Slower writes; caches data that may never be read |
| Write-back | Very fast writes; absorbs bursts | Data loss risk if cache fails before flush |
| Write-around | Avoids churning cache with write-heavy data | Guaranteed miss on first read |
| Short TTL | Bounded, small staleness | Lower hit rate; more origin load |
| Long TTL / versioned keys | High hit rate; low origin load | Staleness unless invalidated; needs disciplined keys |
| CDN and edge | Global low latency; absorbs spikes | Far from data; harder to debug and invalidate |
| LRU eviction | Adapts to shifting popularity | Can evict a stable hot set under scan-heavy load |
| LFU eviction | Protects a stable hot set | Slow to adapt; clings to formerly hot entries |

The recurring tension is consistency versus performance. A cache with a long TTL and high hit rate is fast and cheap and can serve stale data; a cache with a short TTL and aggressive invalidation is fresh and correct and works the origin harder. There is no universal right answer, only a right answer per piece of data, set by its real tolerance for staleness. The second tension is simplicity versus reach: an application cache is close to your data and easy to reason about, while the edge is far, fast, and harder to invalidate. Resolve both by classifying your data by freshness need and read volume, then placing and configuring each class on purpose.

## Questions to discuss with your team

1. **What is the real staleness tolerance of each kind of data we cache, and have we set TTLs and invalidation from that tolerance rather than from habit?** Most teams cache with a TTL someone picked once and never revisited, so some data is served staler than the business can accept while other data expires so aggressively that the cache barely helps. Bring your top ten cached resources and, for each, ask the people who own that data how stale it may safely be: seconds, minutes, hours, or never once published. You will usually find the answers vary widely and that your current TTLs do not match them. The outcome you want is a short freshness classification, each class mapped to an approach (short TTL, long TTL plus purge, or versioned immutable keys), so caching decisions follow from data semantics instead of guesswork.

2. **If our most popular cache entry expired right now under peak traffic, what would happen to the origin?** This question exposes whether you have real stampede protection or only hope. Many systems run fine until a hot key expires during a traffic peak and every request stampedes the database at once, turning the cache from a shield into a trigger. Walk through the path concretely for your busiest endpoint: is there request coalescing so only one miss reaches the origin, is there jitter so entries do not expire in lockstep, is there a stale-while-revalidate policy so users never wait on a refill? Bring load-test evidence, not intuition, because a stampede defence that holds at ten users can still collapse at ten thousand. If you cannot answer with confidence, your next resilience investment just found you.

3. **Are we certain no shared cache ever stores one user's private data under a key another user can hit?** This is the caching mistake that becomes a security incident and a headline. It happens when a personalized or authenticated response is cached under a key that omits the user identity, or when a `Cache-Control` header meant to keep a response private is missing, so a shared proxy or CDN stores it and serves it to the next person. Audit which responses are cacheable at shared layers, confirm every per-user response is marked `private` or `no-store`, and confirm every cache key includes every input that changes the response. Treat this as security review, because the blast radius is every downstream user, and connect it to the practices in chapter 4.2.

4. **Which write pattern does each of our caches actually use, and did anyone choose it on purpose?** Cache-aside, write-through, write-back, and write-around make opposite promises about freshness and about what you lose when the cache fails, yet in most codebases the pattern is whatever the first author happened to copy. For a large team this matters because one service assuming cache-aside freshness while another quietly runs write-back can produce data that looks corrupted but is only stale, and the on-call engineer wastes hours chasing a ghost. Bring a per-cache inventory: the write pattern, the freshness it guarantees, and what happens to unflushed writes if the process dies. Where any cache uses write-back, bring the durability story that backs it. In enterprise and government systems handling financial or records data, a write-back cache with no backing guarantee is an audit finding waiting to happen, so the discussion should end with each cache's pattern named, justified, and written down.

5. **When we deploy or change data, does every relevant cache layer invalidate correctly, or do we rely on someone remembering to purge?** Invalidation is the hard part, and the failure mode is silent: a corrected value that stays wrong for hours because one layer of the hierarchy, a CDN, a reverse proxy, or an application cache, never got the message. A large organization multiplies this risk, because a single logical change may need to propagate across many caches in many regions owned by different teams. Bring a concrete trace of one recent data change and follow it through every cache layer, asking at each: what triggered invalidation here, and how long did it take? Favour designs that turn invalidation into naming (versioned keys) or into events (a change publishes a purge) over manual runbooks. In public-sector systems where a wrong published figure, a tax rate or a benefit amount, can carry legal weight, an invalidation gap is not a nuisance but a compliance exposure, so the outcome should be a mapped invalidation path for every class of cached data.

6. **Are we treating caching as shared platform infrastructure, or is every team reinventing keys, invalidation, and stampede protection on their own?** Caching done well is a small set of hard problems solved once: normalized keys, event-driven invalidation, request coalescing, correct HTTP semantics, and per-layer observability. When each team improvises these, a large organization pays for the same mistakes repeatedly, and a poisoning bug or a private-data leak fixed in one service silently persists in ten others. Bring an honest map of who owns caching conventions today and how much duplicated caching code exists across services. The competing consideration is autonomy: teams resist a mandated shared library, so weigh a paved-road default that is easy to adopt against a hard standard that is enforced. For an enterprise or government platform group, a shared, well-tested caching capability is also the cheapest way to make security and audit requirements hold uniformly, so the discussion should decide what becomes shared infrastructure and who funds it.

## Sector lens

**Startup.** Caching is your cheapest path to surviving a traffic spike you cannot yet afford to scale for, so spend the little time you have on a few high-leverage placements: a CDN with versioned URLs for static assets, and a single cache-aside layer with short TTLs and jitter in front of your hottest query. Lean on managed CDN and cache services rather than running your own, and add request coalescing early, because a launch-day stampede against a small database is the failure most likely to end a good day badly. Skip elaborate invalidation schemes until you have data telling you they matter.

**Small business.** With no caching specialist and a tight budget, prefer buying caching you get for free inside tools you already run: a CDN bundled with your hosting, HTTP `Cache-Control` headers on your web framework's responses, and your database's built-in query cache. The build-versus-buy call almost always favours buy here, since a mis-keyed cache that leaks one customer's data to another costs far more than the managed service you avoided. Get the two cheap wins right, correct HTTP headers and never caching authenticated pages at shared layers, and leave the exotic patterns alone.

**Enterprise.** At scale across many teams the risk shifts from any single cache to inconsistency between them: divergent key schemes, uneven invalidation, and private-data leaks that appear in one service and not another. Provide caching as shared platform infrastructure with paved-road defaults for keys, invalidation, stampede protection, and per-layer observability, so hit rate, eviction, and staleness are visible in one place and governed uniformly. Make cache configuration reviewable as security-sensitive code, and treat invalidation across regions as a first-class design problem rather than a per-team runbook.

**Government.** Procurement and transparency constraints shape what you can cache and how you prove it is safe. Cache public content aggressively, guidance, forms, and rate tables behind a CDN with long TTLs, so a filing-deadline surge is absorbed far from the origin, and document that configuration for audit. Authenticated pages showing a citizen's own records must never touch a shared cache, and that rule should be verifiable, not merely asserted. Where a CDN or caching service is procured from a vendor, require the contract to expose the controls you need (keying, purge, and logging) and avoid lock-in that would trap public data behind proprietary cache formats.

## Examples

**Startup.** A small consumer app runs its product catalogue through a cache-aside layer backed by an in-memory store, with a 60-second TTL and jitter so entries do not expire together. Static assets go to a CDN with versioned filenames and a one-year max-age, so a deploy that changes a stylesheet serves a new URL and never needs a purge. When a launch on a popular podcast sends a traffic spike, single-flight coalescing means the thousands of simultaneous homepage misses cause one database read, not thousands. The founders spend almost nothing on caching yet handle a spike that would have melted their small database, because they placed a few well-chosen caches on purpose.

**Enterprise.** A global retailer serves millions of shoppers through a layered cache: a CDN for images and cacheable API responses, a shared reverse-proxy cache in each region, and an application cache for computed pricing and inventory fragments. Cache keys are normalized and include currency, language, and device class, so personalization never leaks and hit rates stay high. Product data uses short TTLs with event-driven invalidation, so a price change publishes to a message bus that purges the affected keys across regions within seconds. Every layer reports hit rate, eviction rate, and staleness to the observability platform of chapter 9.2, and an alert on a falling hit rate once caught an undersized cache before it became a checkout outage.

**Government.** A national tax agency runs a filing portal that is quiet for most of the year and overwhelmed near the deadline. The team caches aggressively where it is safe and never where it is not. Public content (guidance pages, forms, rate tables) is served from a CDN with long TTLs and versioned URLs, absorbing the deadline-day read surge far from the origin. Authenticated pages showing a citizen's own filing are marked `no-store` and never touch a shared cache, so no taxpayer is ever served another's data. Cache configuration is reviewed as security-sensitive code against the practices in chapter 4.2, and stampede protection is load-tested at deadline scale months ahead, so the portal that used to buckle on the busiest day of the year now holds.

## Business case: motivations, ROI, and TCO

The return on caching is unusually direct and easy to quantify. A cache that raises hit rate from 80 to 95 percent cuts origin traffic by three-quarters, which can mean postponing a database upgrade, running fewer application servers, or surviving a traffic spike that would otherwise have required emergency scaling. Latency improvements convert to revenue in commerce and to satisfaction and completion rates in public services, where research has long linked faster pages to higher conversion and lower abandonment. Egress and compute costs fall because a request served from the edge never pays for origin bandwidth or processing. For read-heavy systems, which most systems are, caching is often the cheapest performance you can buy.

Weigh the total cost of ownership honestly. The direct costs are modest: CDN and cache infrastructure are cheap relative to the origin capacity they save. The real cost is engineering discipline, because a cache that is wrong is worse than no cache. Staleness bugs, invalidation mistakes, and cache-poisoning vulnerabilities all carry real cost, and they grow when caching is improvised per team instead of provided as a shared, well-tested capability. The strongest business case funds a small amount of shared caching infrastructure and convention (standard keys, invalidation, stampede protection, and observability) so every team gets the benefit without repeating the mistakes. Framed for leadership, caching connects to metrics they already track: infrastructure cost, page latency, conversion and completion rates, and incident frequency during peak events.

## Anti-patterns and pitfalls

- **Caching without invalidation:** setting a long TTL with no way to purge, so a corrected value stays wrong for hours.
- **Keys too coarse:** caching personalized responses under a shared key, leaking one user's data to another.
- **Keys too fine:** including volatile inputs in the key so no two requests ever match and the hit rate collapses.
- **No stampede protection:** a hot key expires under load and every request rushes the origin at once.
- **Synchronized expiry:** a batch of entries written together all expire in the same instant with no jitter, causing a periodic thundering herd.
- **Caching private data at shared layers:** missing `Cache-Control: private` or `no-store`, so a proxy or CDN stores authenticated responses.
- **Ignoring unkeyed inputs:** reflecting a header into the response body but omitting it from the key, opening the door to cache poisoning.
- **Undersized cache:** a cache too small to hold the working set thrashes and evicts entries just before they are needed.
- **Unmeasured cache:** no hit-rate or eviction metric, so a degrading cache is invisible until it becomes an outage.
- **Write-back without durability:** fast writes that vanish when the cache dies before flushing, with no backing guarantee.

## Maturity model

- **Level 1, Initiate:** Caching is ad hoc and per-developer, added reactively when something feels slow. TTLs are guessed, keys are inconsistent, invalidation is manual or absent, and stale data and mysterious bugs are common. No one tracks hit rate, and a traffic spike that a cache should have absorbed instead causes an outage.
- **Level 2, Develop:** Teams cache in obvious places and use a CDN for static assets. Basic TTLs and cache-aside appear, but conventions vary from service to service, invalidation is inconsistent, stampede protection is missing, private-versus-shared caching rules are informal, and observability is limited to occasional spot checks.
- **Level 3, Standardize:** A caching strategy is documented and enforced across the organization. Cache keys are normalized, TTLs follow a shared freshness classification, invalidation is event-driven where it matters, stampede protection and correct HTTP semantics are standard, private data is never cached at shared layers, and every layer reports hit rate and eviction to a common observability pipeline.
- **Level 4, Manage:** Caching is measured and controlled against baselines. Each layer has target hit rates, staleness budgets, and eviction thresholds, and dashboards alert when a hit rate falls or an eviction rate rises past its baseline. Stampede defences are load-tested at peak scale, origin-load reduction is quantified per cache, TTLs and eviction policies are tuned from measured access patterns, and cache configuration is reviewed as security-sensitive code before release.
- **Level 5, Orchestrate:** Caching is continuously improved and integrated across the organization. Placement, keys, and TTLs adapt to shifting traffic, edge compute is used where it earns its keep, capacity planning and cost models draw on cache metrics, and lessons from one team's incidents feed shared conventions. The organization treats caching as a designed, measured, adaptive capability rather than a collection of local hacks.

## Ideas for discussion

1. Which single cache in your system, if it went cold right now, would most endanger your origin, and what protects it?
2. For each layer of your cache hierarchy, can you name its current hit rate from memory, and if not, what does that tell you?
3. Where have you turned an invalidation problem into a naming problem with versioned keys, and where could you still do so?
4. Which of your write paths uses cache-aside, write-through, write-back, or write-around, and was each chosen on purpose?
5. If an attacker controlled one request header, could they poison any cached response your users share?
6. How would you know, within minutes, that your hit rate had quietly dropped by twenty points?

## Key takeaways

- Caching cuts latency, load, and cost, and the cache hierarchy (client, CDN and edge, reverse proxy, application, database) lets you answer as far up and out as you safely can.
- Invalidation is the hard part; design cache keys and TTLs deliberately, and turn invalidation problems into naming problems with versioned keys wherever you can.
- Protect the cache under load with request coalescing, jitter, and stale-while-revalidate, because a cache is most needed exactly when a stampede could break it.
- Choose write patterns and eviction policies per workload, and use HTTP caching semantics (`Cache-Control`, ETags, validation) explicitly rather than leaving caches to guess.
- Treat cached content as an attack surface and measure hit rate, eviction, and staleness, because an unobserved or mis-keyed cache is a hidden liability, not an asset.

## References and further reading

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Andrew S. Tanenbaum and Herbert Bos, *Modern Operating Systems*
- John L. Hennessy and David A. Patterson, *Computer Architecture: A Quantitative Approach*
- Roy T. Fielding and Julian Reschke, "Hypertext Transfer Protocol (HTTP/1.1): Caching," RFC 7234, IETF
- Mark Nottingham, "Caching Tutorial for Web Authors and Webmasters"
- James Kettle, "Practical Web Cache Poisoning," PortSwigger Research
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems*
- Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software*
