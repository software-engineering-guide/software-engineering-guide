# 6.6 AI infrastructure and operations

## Overview and motivation

AI infrastructure and operations is the discipline of provisioning, scheduling, and running the specialized compute, storage, and serving systems that AI workloads demand, doing so cost-effectively, reliably, and observably. Modern AI is expensive to run. Training and serving large models require scarce accelerators ([GPUs](https://en.wikipedia.org/wiki/Graphics_processing_unit) and [TPUs](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), high-bandwidth networking, large-scale vector storage for retrieval (indexing data as numeric vectors so similar items can be found quickly), and serving layers tuned for latency and throughput. Getting this infrastructure right is the difference between AI that scales sustainably and AI that quietly consumes a budget while under-delivering.

For large teams, the core problems are scale, scarcity, and cost. Accelerators are limited and pricey, so scheduling and utilization matter enormously. Idle GPUs are burned money, and poorly batched inference multiplies cost per request. Retrieval-heavy applications need [vector databases](https://en.wikipedia.org/wiki/Vector_database) that stay fast as they grow. Generative AI applications need prompt versioning, evaluation pipelines, and observability (sometimes called LLMOps) to operate safely and improve over time. Without shared infrastructure and operational discipline, every team fights the same battles and costs spiral.

Government and regulated organizations add requirements around data sovereignty, security, and predictable spending. They may need on-premises or sovereign-cloud deployment so sensitive data and models never leave controlled boundaries. They must forecast and justify infrastructure spend, and meet security and availability standards. AI infrastructure decisions in these settings carry multi-year consequences, so make them with procurement, security, and exit in mind.

## Key principles

- Treat accelerator compute as a scarce, expensive resource to be scheduled and utilized, not hoarded.
- Optimize cost per useful unit of work, not raw capacity.
- Right-size models and hardware to the task; the largest option is rarely the most cost-effective.
- Design serving for latency and throughput with batching and caching as first-class techniques.
- Make AI systems observable: track cost, latency, quality, and errors continuously.
- Version and evaluate prompts and models with the same rigour as code.
- Plan for portability and avoid lock-in in infrastructure and serving choices.

## Recommendations

### Plan and control accelerator compute

Forecast demand for training and inference separately, since they have different shapes. Training is bursty and schedulable; inference is continuous and latency-sensitive. Use schedulers and quotas to share scarce GPUs and TPUs across teams, prioritize workloads, and drive up utilization. Measure utilization and treat chronic idleness as a problem to fix. Mix reserved capacity for baseline load with on-demand or spot capacity for bursts to control cost. Consider whether cheaper or smaller accelerators, or CPU inference for lightweight models, would suffice. Choose between cloud, on-premises, and hybrid based on cost at your scale, data-sovereignty needs, and burst patterns, and keep an exit path.

### Build retrieval infrastructure: embeddings and vector databases

For retrieval-augmented applications, stand up infrastructure to generate [embeddings](https://en.wikipedia.org/wiki/Word_embedding) (numeric vector representations that place similar items near each other) and store them in a vector database that supports fast [approximate nearest-neighbor search](https://en.wikipedia.org/wiki/Nearest_neighbor_search) (finding the most similar vectors without exhaustively comparing every one) at your scale. Plan for three things: the cost and latency of embedding generation, index freshness as documents change, and the operational burden of keeping indexes consistent. Evaluate whether a dedicated vector database, a vector-capable extension of an existing database, or a managed service best fits your scale and lock-in tolerance. Monitor retrieval latency and recall, because retrieval quality directly determines application quality.

### Optimize model serving: batching, caching, and latency

Serving is where inference cost and user experience are decided. Use **batching** to process multiple requests together and raise accelerator throughput, balancing batch size against latency. Use **caching** aggressively: cache identical or semantically similar requests, cache embeddings, and exploit prompt or prefix caching where the platform supports it to avoid recomputing shared context. Set clear latency targets, and measure tail latency, not just averages. Route requests to right-sized models: a small model for easy cases, a larger one only when needed. Autoscale serving to demand, and load-test before launch so you know your capacity and cost curve.

### Practice LLMOps: prompt versioning, evaluation pipelines, and observability

Treat prompts as versioned artifacts in source control, with review and the ability to roll back. Build evaluation pipelines that run offline test suites automatically whenever prompts or models change, so you catch regressions before release. Instrument production comprehensively: log inputs, outputs, latency, token usage, cost, and errors, with sampling and privacy safeguards. Track quality signals and user feedback online. This observability lets you catch degradation, control cost, debug failures, and improve systems safely: the operational backbone of generative AI in production.

### Manage cost relentlessly and observably

Attribute AI spend to teams and use cases so cost is visible and owned. Set budgets and alerts, monitor cost per request and per outcome, and review the biggest cost drivers regularly. Pull the levers you have: model right-sizing, caching, batching, prompt and context trimming, and choosing the cheapest deployment that meets requirements. AI costs can scale with usage in surprising ways, so continuous cost observability is essential to avoid unpleasant surprises.

## Trade-offs: pros and cons

| Decision | Option A | Option B | Trade-off |
|---|---|---|---|
| Compute location | Cloud | On-premises | Elasticity and low upfront cost versus control, sovereignty, and steady-state economics |
| Capacity | Reserved | On-demand/spot | Predictable cost versus flexibility and interruption risk |
| Batch size | Large batches | Small batches | Throughput and cost versus latency |
| Model size | Large model | Small model | Quality versus cost and speed |
| Vector store | Dedicated database | Existing database extension | Performance at scale versus simplicity and fewer systems |
| Caching | Aggressive | Minimal | Lower cost and latency versus freshness and complexity |

The dominant trade-off is cost versus latency and quality. Batching, caching, and smaller models cut cost but can add latency or reduce quality. The right balance depends on your application's tolerance. On-premises versus cloud trades control and steady-state economics against elasticity and low commitment, a decision heavily shaped by data-sovereignty needs and scale.

## Questions to discuss with your team

1. **What is our cost per useful outcome today, and which lever would move it most?** Raw capacity and per-request averages hide the number that matters: what it costs to deliver one real unit of value, and how that scales with usage. For a large team, the gap between an optimized and an unoptimized deployment is often several-fold in spend, so this question turns a vague worry about the bill into a ranked list of fixes. Bring current cost attribution by team and use case, per-request and per-outcome trends, and the biggest cost drivers. Discuss the levers in order of payoff: model right-sizing, caching (including prefix and semantic caching), batching, and prompt or context trimming. In government, add the pressure to forecast and justify multi-year spend. The answer should assign each top cost driver an owner and a lever, not a shrug.

2. **If our current inference provider doubled its price or went down tomorrow, how fast could we switch?** Silent lock-in is easy to build and painful to escape, and serving stacks are where it hides most deeply. For enterprises and especially government, portability is a procurement and continuity requirement, not a nicety. Bring your architecture: whether models sit behind an internal interface, whether prompts and evaluation suites are portable, and how much provider-specific serving behaviour you depend on. The signal to watch is whether anyone has ever run your evaluation suite against a second provider or a second deployment target. If switching would take months and rewrite core paths, treat that as a design defect to address now, since sovereign and on-premises options may become mandatory with little notice.

3. **What is our accelerator utilization right now, and how much are idle GPUs and unbatched inference burning?** Accelerators are scarce and expensive, so chronic idleness and per-request serving quietly drain budgets that could fund more capability. For a large organization sharing GPUs across teams, this question exposes whether scheduling, quotas, and priorities actually keep utilization high or whether hoarded, underused hardware is the norm. Bring real utilization numbers, your batching and caching posture, and your tail-latency measurements, not just averages, since users feel the slow tail. Discuss whether training and inference demand are forecast separately, given their different shapes, and whether a smaller model or CPU inference would suffice for lightweight cases. The answer should point at specific idle capacity to reclaim and specific requests to batch or route to a right-sized model.

4. **When a prompt or model change ships, what stops a silent quality or cost regression from reaching users?** A serving stack can look healthy on latency and uptime while the answers it returns quietly get worse or a new prompt doubles token usage per request. For a large team where many groups edit prompts and swap models independently, an ungated change is a production incident waiting to happen, and the blast radius grows with every team on the shared platform. Bring your evaluation coverage: which prompts and models have offline test suites, whether those suites run automatically on every change, what quality and cost thresholds gate a release, and how fast you can roll back. Discuss whether prompts live in source control with review, or whether someone can still edit a live system prompt by hand. In enterprise and government settings, tie each change to an audit trail and a named approver, because a regulator asking "who changed this and what did you test" needs an answer that is recorded, not remembered.

5. **How do we decide between cloud, on-premises, and sovereign deployment, and have we priced the real steady-state economics rather than the pilot?** The compute-location choice sets your cost curve, your data-sovereignty posture, and your exit options for years, yet it is often made on a pilot's cloud bill that looks nothing like production at scale. For a large organization, elastic cloud capacity is cheap to start and can become the largest single line once inference runs continuously, while on-premises trades low commitment for control and steady-state economics. Bring forecast training and inference volumes, the break-even point where reserved or owned hardware beats on-demand, your data-residency and security constraints, and the burst patterns that argue for hybrid. In government and regulated settings, weigh sovereign-cloud or on-premises requirements that may become mandatory with little notice, and confirm the architecture keeps models behind an internal interface so a forced move does not rewrite core paths.

6. **Do we actually own our AI spend, and can each team see and answer for the cost it drives?** AI cost scales with usage in ways that surprise people, and without attribution the bill lands as one opaque number that no team feels responsible for shrinking. In a large organization, cost that nobody owns is cost that nobody optimizes, so the question is whether spend is tagged to teams and use cases with budgets, alerts, and per-outcome trends, or whether it is discovered only when finance escalates. Bring your cost-attribution model, the biggest drivers by team, and the levers each owner controls: right-sizing, caching, batching, and context trimming. For enterprise and government budgets, add the discipline of forecasting and justifying multi-year infrastructure spend, since a public body that cannot explain its compute bill line by line will struggle to defend it in review.

## Sector lens

**Startup.** Own no infrastructure you can avoid. Call a hosted inference API, route easy requests to a small cheap model and reserve a larger one for hard cases, and cache aggressively so repeated prompts cost nothing. Use a managed vector database rather than operating your own, keep prompts in git with a short evaluation script before each change, and log cost per request so a runaway bill shows up before it hurts. Your scarcest resource is engineering attention, so buy operability and keep switching cheap.

**Small business.** With no platform team, treat serving, retrieval, and observability as things you buy inside tools you already use, not systems you staff. Favour managed inference and managed vector search with transparent, predictable pricing, and set a hard spend cap and a billing alert from day one. Frame the decision as buy versus build honestly: operating GPUs or a vector index rarely pays off at your volume, and a small model behind a hosted API usually meets the need at a fraction of the effort.

**Enterprise.** The problem is a shared, paved-road platform across many teams: pooled accelerators with schedulers, quotas, and priorities to drive utilization up, standard batching and caching, right-sizing routers, and cost attributed to each team and use case. Gate prompt and model changes with automated evaluation suites, standardize the interface layer so providers and deployment targets stay swappable, and manage cost per outcome as a first-class metric rather than each group reinventing costly, underused infrastructure.

**Government.** Data sovereignty, security, and predictable spend shape every choice. Favour on-premises or sovereign-cloud deployment so sensitive data and models stay inside controlled boundaries, schedule scarce GPUs across departments with quotas that you can justify in procurement, and forecast capacity to defend multi-year spend line by line. Version and evaluate prompts and models with a recorded audit trail, keep comprehensive observability over cost and quality, and hold models behind an internal interface so a forced move to a new provider or a sovereign platform does not strand you.

## Examples

**Startup.** A small startup running an AI writing feature kept its bill sane without owning any GPUs. It called a hosted inference API, routed easy requests to a cheaper small model and saved the larger one for hard cases, and cached answers to repeated prompts. It stored its prompts in git with a short evaluation script that ran before each change, used a managed vector database for retrieval so it did not have to operate one, and logged cost per request so the founders could see spend climb before it became a surprise.

**Enterprise.** A media company running a high-traffic LLM feature cut inference costs substantially. It routed easy requests to a small model and reserved a larger model for hard ones. It cached responses to repeated queries and enabled prefix caching for its shared system prompt. It ran GPUs through a shared scheduler to keep utilization high, versioned all prompts in git with an automated evaluation suite gating changes, and instrumented cost per request so each product team owned its spend.

**Government.** A national agency with strict data-sovereignty rules deployed its AI systems on-premises so sensitive data and models never left its controlled environment. It scheduled scarce GPUs across departments with quotas and priorities, forecast capacity to justify multi-year procurement, and built a vector-search platform for retrieval over official documents. Prompts and models were versioned and evaluated before release. Comprehensive observability tracked cost and quality, and the architecture kept models behind an internal interface to preserve an exit path and avoid lock-in.

## Business case: motivations, ROI, and TCO

The motivation for disciplined AI infrastructure is straightforward. AI at scale is costly, and the gap between an optimized and an unoptimized deployment is often several-fold in spend. ROI comes from higher accelerator utilization, lower cost per request through batching and caching, right-sized models, and avoiding over-provisioning. Observability and evaluation pipelines pay off by preventing costly incidents and enabling safe iteration.

TCO spans accelerator compute (the largest line for many workloads), vector storage, serving infrastructure, networking, and the platform and operations staff to run it. Weigh this against the cost of not investing: runaway inference bills, poor latency that undermines adoption, and inability to scale. For government, add the cost of failing sovereignty or security requirements. Make the case to leadership by showing cost-per-outcome trends and a paved-road platform that lets many teams deploy AI efficiently, rather than each building costly, underused infrastructure.

## Anti-patterns and pitfalls

- **Idle accelerators.** Dedicating scarce GPUs to teams that leave them underutilized.
- **No batching or caching.** Serving every request individually and recomputing shared context.
- **Largest model by default.** Using an expensive model where a small one would do.
- **Cost blindness.** No attribution, budgets, or per-request cost visibility until the bill arrives.
- **Unversioned prompts.** Changing prompts in production with no versioning or evaluation gate.
- **Tail-latency neglect.** Optimizing average latency while users suffer slow tails.
- **Silent lock-in.** Building deeply on one provider's serving stack with no portability.

## Maturity model

1. **Initiate.** Ad hoc GPU allocation reacting to whoever asks loudest, no batching or caching, no cost visibility until the bill arrives, prompts edited live and unversioned, minimal monitoring.
2. **Develop.** Some teams adopt shared scheduling, caching, and version-controlled prompts, but practice is inconsistent across the organization: one group batches and evaluates while another still serves every request individually and changes prompts by hand.
3. **Standardize.** A documented, paved-road platform is enforced org-wide: shared scheduling with quotas and priorities, standard batching, caching, and right-sizing, vector infrastructure for retrieval, automated evaluation pipelines that gate every prompt or model change, and cost attribution to teams and use cases.
4. **Manage.** The platform is measured and controlled against baselines: accelerator utilization, cost per useful outcome, tail latency, retrieval recall, and per-change quality regressions are tracked with alerts and thresholds, cost is owned by each team, and go or no-go on a change is decided on evidence rather than intuition.
5. **Orchestrate.** Infrastructure continuously improves and adapts: routing, batching, and scaling tune themselves to live cost and quality signals, capacity is rebalanced across teams and between cloud, on-premises, and sovereign targets as demand and constraints shift, portability is rehearsed, and infrastructure planning is integrated with product, security, and procurement.

## Ideas for discussion

- How do you drive accelerator utilization up without starving priority workloads?
- Where is the right batching and caching balance for your latency requirements?
- When does on-premises or sovereign deployment justify its cost over cloud?
- How do you attribute and control AI spend across many teams?
- What should gate a prompt or model change from reaching production?
- How do you keep serving infrastructure portable enough to switch providers?

## Key takeaways

- Accelerators are scarce and expensive; schedule, share, and utilize them deliberately.
- Batching, caching, and model right-sizing are the primary levers for cost and latency.
- Retrieval applications need well-operated embedding and vector-search infrastructure.
- LLMOps (prompt versioning, evaluation pipelines, and observability) is the operational backbone of generative AI.
- Manage cost observably and preserve portability to avoid lock-in.

## References and further reading

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, editors).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
