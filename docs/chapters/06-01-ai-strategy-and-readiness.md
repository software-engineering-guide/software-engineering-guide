# 6.1 AI strategy and readiness

## Overview and motivation

[Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) has gone from research novelty to a core capability that large organizations are now expected to deploy responsibly and at scale. For enterprises and government agencies, the real question is no longer whether AI can do something impressive in a demo. It is whether a specific investment solves a real problem better than the alternatives, can be operated safely for years, and can survive audit, procurement, and public scrutiny. AI strategy is the discipline of deciding where to apply AI, where to avoid it, and what foundations you need before the first model reaches production.

For large teams, scale and inertia raise the stakes. A poorly framed initiative can burn budgets, distract talented engineers, and erode trust with regulators and citizens when it fails in public. A well-chosen one can automate drudgery, surface insight from data you could never reach before, and free skilled people for higher-value work. The difference is rarely the model itself. It comes down to how well you frame the problem, how ready your data and talent are, and how honest your business case is.

Government and regulated contexts add more constraints. Public bodies must justify spending, guarantee transparency, avoid unlawful discrimination, and stay accountable to elected officials and the public. Procurement rules may forbid sole-source lock-in, demand explainability, and require that vendors expose model behaviour. Here, treat compliance, auditability, and exit options as first-class requirements, not afterthoughts.

## Key principles

- Start from a problem worth solving, not from a technology looking for a use.
- Prefer the simplest approach that meets the need; AI is one option among many, and often not the best.
- Treat data readiness, talent, and platform maturity as prerequisites, not parallel work streams to sort out later.
- Make build-versus-buy decisions explicitly and revisit them as the market and your capabilities change.
- Quantify the total cost of ownership, including operation, monitoring, and eventual replacement, not just the licence or the pilot.
- Design for exit from day one: avoid architectures that make switching vendors or models prohibitively expensive.
- In regulated and public settings, treat transparency, procurement compliance, and accountability as design constraints.
- Measure the cost of *not* acting alongside the cost of acting.

## Recommendations

### Frame the problem before choosing a technology

Write a one-page problem statement. Name the decision or task you want to improve, the current baseline, the measurable outcome you want, and what happens when the system gets it wrong. Then ask whether the problem even suits AI. Is there enough relevant data? Is the task pattern-based rather than rule-based? Can you tolerate probabilistic answers? Can a human check the output? Many problems are better solved with deterministic software, better process design, or simply better data hygiene. Write down explicitly where AI is *not* a good fit: for example, decisions that must be perfectly explainable by law, or where the cost of a rare error is catastrophic and impossible to catch.

### Use a build-versus-buy-versus-fine-tune-versus-prompt decision tree

Move from cheapest and fastest to most expensive and most controlled:

1. **Prompt an existing hosted model.** If a general-purpose model (such as Anthropic's Claude, or comparable offerings from other providers) solves the problem with careful prompting and retrieval, do that first. Lowest cost, fastest iteration, no training infrastructure.
2. **Augment with retrieval or tools.** If the gap is knowledge or actions, add [retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG), which fetches relevant documents at query time and supplies them to the model as context, and tool use before touching model weights.
3. **Fine-tune or adapt.** If prompting cannot achieve the needed accuracy, tone, or format consistently, [fine-tune](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) a smaller model on your data: that is, further-train a pretrained model on your examples to specialize it. This buys control at the cost of an [MLOps](https://en.wikipedia.org/wiki/MLOps) (machine learning operations) pipeline.
4. **Buy a specialized product.** For well-defined domains (document processing, fraud scoring), a mature vendor product may beat anything you build.
5. **Build from scratch.** Reserve training [foundation models](https://en.wikipedia.org/wiki/Foundation_model) (large models pretrained on broad data and adaptable to many tasks) for organizations with unique data, deep talent, and strategic reasons. For almost all enterprises and agencies, this is the wrong choice.

### Establish data, talent, and platform prerequisites

Audit your data for availability, quality, labelling, lineage, and legal basis for use. Confirm you actually have the right to use it for AI, including any personal or third-party data. Assess talent honestly: you need data scientists, and also ML engineers, data engineers, product managers who understand probabilistic systems, and reviewers who can evaluate outputs. Before you scale, stand up a platform baseline: experiment tracking, a model registry (the system of record for trained model versions and their approval status), monitoring, and secure serving, so each new use case does not reinvent operations.

### Handle regulated and government contexts deliberately

Bring in procurement, legal, and risk teams early. Require vendors to disclose model provenance, training-data practices, evaluation results, and known limitations. Prefer contracts that grant portability of your data and prompts, and avoid proprietary formats that trap you. Where appropriate, publish the purpose and safeguards of public-facing AI systems, and give people a channel to contest automated decisions. Align to recognized frameworks (see chapter 6.5) so audits find a documented, defensible process.

### Compute total cost of ownership and guard against lock-in

Model the full lifecycle cost: inference or licensing, data pipelines, human review, monitoring, retraining, incident response, and decommissioning. Compare it to the cost of the status quo and of the alternatives. Reduce lock-in by putting the model behind an internal interface, keeping prompts and evaluation datasets portable, and testing a second provider from time to time.

## Trade-offs: pros and cons

| Approach | Pros | Cons | Best when |
|---|---|---|---|
| Prompt hosted model | Fast, cheap, no infra, easy to switch | Less control, per-call cost, data-sharing questions | Prototypes, broad tasks, uncertain requirements |
| Retrieval augmentation | Grounds answers in your data, updatable | Retrieval quality is hard, adds infra | Knowledge-heavy tasks |
| Fine-tune smaller model | Control, lower per-call cost at scale, on-prem option | Needs MLOps, data, and upkeep | Stable, high-volume, specialized tasks |
| Buy a product | Proven, supported, fast to value | License cost, lock-in, limited fit | Well-defined commodity problems |
| Build foundation model | Maximum control and differentiation | Enormous cost, rare talent, high risk | Almost never, outside frontier labs |

The dominant trade-off is control versus cost and speed. Prompting gives you the most speed and flexibility but the least control; building gives you the most control but demands resources few organizations should spend. Most large teams should live in the middle: prompt and retrieve first, fine-tune selectively, and buy for commodity needs. Lock-in trades short-term convenience for long-term risk, and that matters especially in government, where multi-year exit obligations are common.

## Questions to discuss with your team

1. **Where does each of our top three candidate use cases sit on the prompt-then-retrieve-then-fine-tune-then-buy-then-build ladder, and what evidence would move it a rung?** This matters because most wasted AI spend comes from starting a rung too high: training a model when careful prompting would have worked. For a large team, agreeing the ladder as a shared default stops each group from reinventing an expensive pipeline. Bring the one-page problem statement for each candidate, the current baseline, and an honest read on whether the gap is knowledge (retrieval), consistency (fine-tuning), or a solved commodity (buy). In enterprise and government settings, add the procurement and audit cost of each rung, since a fine-tuned model drags along an MLOps burden that a hosted call does not. The answer should let you kill or downgrade at least one over-scoped project in the room.

2. **What is our concrete exit plan for the vendor or model we depend on most, and have we actually tested it?** Lock-in is cheap to accept and expensive to unwind, and in government you may carry multi-year exit obligations you cannot meet if you never rehearsed. Bring the list of proprietary features you rely on, whether prompts and evaluation datasets are portable, and how the model sits behind an internal interface (or does not). The signal to watch is whether anyone has ever run your evaluation suite against a second provider; if not, your exit plan is a hope, not a plan. If the honest answer is that switching would take months and rewrite core code, treat that as a design defect to fix now, not a bridge to cross later.

3. **What does an honest readiness scorecard say about our data rights, and which use cases does it disqualify today?** Skipping data readiness is the failure that sinks pilots quietly: the model works, but you never had the legal basis to use the data, or it is unlabelled and unlineaged. For a large organization, personal and third-party data raise consent and contractual limits that vary by jurisdiction and by dataset. Bring an audit of availability, quality, labelling, lineage, and legal basis for each candidate, and be willing to mark some use cases as blocked until data foundations exist. In regulated and public settings, an unusable legal basis is not a delay, it is a hard stop, and funding the readiness work should be an explicit line in the plan rather than an afterthought.

4. **How will we know a live AI use case is actually working, and what evidence would make us kill it?** Most AI portfolios accumulate zombies: pilots that shipped, impressed someone, and now run forever without anyone checking whether they still earn their cost. Agree the baseline and the success metric before launch, then set an explicit kill threshold, so the decision to stop is made in advance rather than defended in the moment. Bring the current metric, the human-oversight cost per outcome, and the drift you have seen since launch. For enterprise and government portfolios, name who reviews each system on a fixed cadence and who holds authority to retire it; a use case nobody is accountable for reviewing is one nobody will ever switch off.

5. **Where does a human stay in the loop, what does that oversight cost, and have we actually budgeted it?** The cheapest-looking AI use cases are the ones that quietly assume full automation, then leak cost through the review, correction, and escalation that reality forces back in. Decide deliberately which decisions a person must confirm, which the model may take alone, and which it may never take, then price the human time that implies. Bring the volume of low-confidence cases, the cost of a wrong answer, and the current escalation path. In regulated and public settings, tie each automated decision to an accountable officer and a route of appeal, because oversight you cannot describe is oversight you do not have.

6. **Do we have the talent and platform to run what we are proposing, or are we quietly assuming capacity we lack?** Ambitious AI plans fail less on the model than on the unglamorous foundations: nobody to maintain the pipeline, no one who can evaluate outputs, no platform to deploy on. Match each candidate use case to the skills and infrastructure it actually needs, and be honest where the gap is a hire, a partner, or a reason not to build. Bring an inventory of who can own each system in production, what platform it will run on, and which capabilities you would have to buy. For a large or public organization, add the procurement and hiring lead times, since a plan that depends on talent you cannot recruit in the relevant window is a plan to under-deliver.

## Sector lens

**Startup.** Speed and survival dominate. Pick one narrow use case that touches your core value, ship it on a hosted model behind a thin interface, and cap spend hard. Avoid building infrastructure or training models: your scarcest resource is engineering attention, and a fine-tuned pipeline you cannot maintain is a liability, not a moat. Keep switching cheap so you can follow a fast-moving market.

**Small business.** You likely have no data scientists and a tight budget, so treat AI as something you buy embedded in tools you already use, not a programme you staff. Frame readiness as a data-hygiene and privacy question rather than a machine-learning project: know what customer data you hold, what you are allowed to do with it, and where a wrong automated answer would cost you a customer. Prefer vendors who make the AI optional, transparent, and easy to turn off.

**Enterprise.** The problem is portfolio governance across many teams: a shared build-versus-buy ladder, consistent readiness assessments, and lock-in and total-cost analysis so groups stop reinventing expensive pipelines. Budget the MLOps and human-oversight burden explicitly, standardize the interface layer so providers stay swappable, and manage AI use cases as a portfolio with clear metrics and kill criteria rather than a scatter of pilots.

**Government.** Transparency, procurement rules, and accountability shape every choice. Favour systems that cite official sources rather than generate policy, keep a human accountable for consequential decisions, and demand data portability and disclosure of model limitations in contracts. Publish a plain-language description and an appeals route, honour any multi-year exit obligations you sign, and keep AI out of final assessment decisions that must rest with an accountable officer.

## Examples

**Startup.** A five-person scheduling startup wanted to add a natural-language "book me a meeting" feature without pulling its two engineers off the core product. It picked the smallest problem that mattered, parsing a request into a proposed time, and shipped it with a hosted model behind a thin internal API so it could switch providers later. The team set a hard monthly spend cap, tracked whether users accepted the suggested times, and agreed to revisit a fine-tuned model only if volume ever justified the extra work.

**Enterprise.** A multinational insurer wanted to speed up claims triage. Instead of training a bespoke model, it framed the problem narrowly (route and summarize incoming claims), prototyped with a hosted model plus retrieval over its policy documents, and measured against human handling time and accuracy. Only after proving value did it fine-tune a smaller model for the highest-volume claim type to cut per-call cost. It kept the model behind an internal API so it could swap providers, and it modelled a three-year TCO that included human review of low-confidence cases.

**Government.** A national tax authority considered an AI assistant to help staff answer citizen queries. Because those answers touched legal obligations, the agency insisted on transparency: the system could only surface official guidance with citations, never invent policy, and a human reviewed every automated suggestion before it went out. Procurement required the vendor to disclose model limitations and grant data portability, and the agency published a plain-language description of the system and an appeals route. It kept AI out of final assessment decisions entirely, reserving those for accountable officers.

## Business case: motivations, ROI, and TCO

AI strategy exists to help you avoid two mirror-image failures: over-investing in AI that never pays off, and under-investing while competitors or peer agencies pull ahead. ROI comes from labour saved, cycle time reduced, error rates lowered, and new capabilities enabled. Measure these against a genuine baseline, and discount for the real cost of human oversight, which rarely disappears.

TCO has to include the unglamorous line items: data pipelines, monitoring, retraining as the world drifts, security review, and eventual decommissioning. A pilot that looks cheap can turn expensive once it runs at scale for years. Present the cost of *not* adopting too: slower service, higher manual cost, and strategic drift. Make the case to leadership with a portfolio view: a few high-confidence bets, clear success metrics, kill criteria for failures, and a readiness assessment showing that data and talent foundations exist. Ask leaders to fund readiness explicitly; skip it, and you guarantee expensive rework.

## Anti-patterns and pitfalls

- **Solution in search of a problem.** Buying AI because peers did, then hunting for a use case.
- **Skipping data readiness.** Launching models on data that is unavailable, unlabelled, or legally unusable.
- **Demo-driven decisions.** Committing based on a polished demo without a production-quality evaluation.
- **Ignoring the human loop.** Assuming full automation and under-budgeting review, which is where most cost hides.
- **Silent lock-in.** Building deeply on one vendor's proprietary features with no exit plan.
- **Underestimating operations.** Treating deployment as the finish line rather than the start of a maintenance obligation.
- **Compliance as an afterthought.** Retrofitting transparency and auditability after design, at multiples of the cost.

## Maturity model

1. **Initiate.** Ad hoc experiments, no shared strategy, decisions driven by hype and individual enthusiasm.
2. **Develop.** Problem framing exists for some projects; a first platform baseline appears; build-versus-buy is discussed but inconsistent.
3. **Standardize.** A portfolio of AI use cases with clear metrics, a documented decision tree, readiness assessments, and lock-in and TCO analysis, applied consistently across teams.
4. **Manage.** The portfolio is measured: readiness, ROI, TCO, and human-oversight cost are tracked against baselines; kill criteria are enforced on evidence; delivery and quality impact drive each go or no-go decision.
5. **Orchestrate.** AI strategy is integrated with business and risk planning; readiness is continuously maintained; the organization routinely retires, replaces, and re-scopes AI systems based on evidence, rebalancing the portfolio as the market and the risk picture shift.

## Ideas for discussion

- How do you decide when a problem is genuinely unsuited to AI, and who has authority to say no?
- What readiness threshold should gate a project from pilot to production?
- How much lock-in is acceptable in exchange for faster time to value?
- In government, how should transparency obligations shape the build-versus-buy choice?
- How do you keep TCO estimates honest when vendors and enthusiasts have incentives to understate them?
- Who owns the AI portfolio, and how are kill decisions made?

## Key takeaways

- Strategy starts with a real problem and an honest baseline, not with a technology.
- Prefer the simplest option: prompt, then retrieve, then fine-tune, then buy, and rarely build from scratch.
- Data, talent, and platform readiness are prerequisites; funding them is part of the plan.
- Regulated and government contexts require transparency, procurement compliance, and exit options by design.
- Model full TCO and the cost of inaction, and guard against vendor lock-in from the first architecture decision.

## References and further reading

- Ajay Agrawal, Joshua Gans, and Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Organisation for Economic Co-operation and Development, *OECD AI Principles*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.
