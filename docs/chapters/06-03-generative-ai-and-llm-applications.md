# 6.3 Generative AI and LLM applications

## Overview and motivation

[Generative AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), and [large language models](https://en.wikipedia.org/wiki/Large_language_model) (LLMs) in particular, can produce fluent text, code, summaries, and structured data from natural-language instructions. That makes them powerful building blocks for assistants, search, document processing, and automation. But those strengths come with a distinctive risk profile. LLMs are probabilistic. They can produce confident falsehoods ([hallucinations](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))). They are sensitive to how you prompt them. And they open new attack surfaces such as [prompt injection](https://en.wikipedia.org/wiki/Prompt_injection) (malicious instructions smuggled into inputs to hijack the model's behaviour). So building dependable LLM applications is less about the model and more about the engineering around it: how you supply context, ground answers in trusted knowledge, constrain outputs, and evaluate quality.

For large teams, LLM applications call for new patterns that differ from both traditional software and classical machine learning. There is often no training step. Instead, behaviour is shaped by prompts, retrieved context, tool definitions, and guardrails (runtime checks that constrain the model's inputs and outputs). That shifts the engineering effort toward context management, retrieval quality, orchestration, and evaluation. Enterprises adopting LLMs at scale need shared patterns so that every team does not rediscover the same failure modes the hard way.

Government and regulated organizations face extra demands. An LLM that fabricates a policy citation or leaks sensitive data is not merely a bug; it can be a legal or safety incident. These settings need grounding in authoritative sources, strict output validation, human oversight for consequential outputs, and clear records of what the system was asked and what it produced. The techniques in this chapter (retrieval-augmented generation, guardrails, and rigorous evaluation) are what make LLMs safe enough to deploy in high-stakes contexts. Anthropic's Claude models are one leading option among several capable providers; the practices here apply regardless of which model you choose.

## Key principles

- Ground the model in trusted knowledge rather than relying on what it memorized.
- Treat prompts and context as engineered, versioned artefacts, not throwaway strings.
- Assume the model can be wrong or manipulated; validate outputs and constrain actions.
- Give the model only the context and tools it needs, no more, to reduce error and attack surface.
- Evaluate continuously with offline test sets, online metrics, and human judgment.
- Keep humans in the loop for consequential outputs.
- Design for the model as an untrusted component within a trusted system.

## Recommendations

### Engineer prompts and manage context deliberately

Treat prompts as code: store them in version control, review changes, and test them against a suite of examples. Structure each prompt clearly: role and task, constraints, format requirements, and examples where they help. Treat the context window (the fixed span of text the model can consider at once) as a scarce resource. Include the most relevant information, order it thoughtfully, and strip out noise, because irrelevant or excessive context degrades quality and raises cost. For multi-turn applications, manage conversation state explicitly, summarizing or truncating history to stay within limits while keeping what matters. Prefer clear instructions and few-shot examples (a handful of worked demonstrations included in the prompt) over elaborate tricks that break the moment a model changes.

### Ground answers with retrieval-augmented generation (RAG)

For knowledge-intensive tasks, retrieve relevant documents from a trusted corpus and supply them to the model as context, telling it to answer only from that material and to cite its sources. RAG keeps knowledge current without retraining, confines answers to approved content, and enables citation and verification. Invest in retrieval quality: chunk documents sensibly, choose [embeddings](https://en.wikipedia.org/wiki/Word_embedding) (numeric vector representations that place similar meanings close together) suited to your domain, and check whether the retrieved passages actually contain the answer, because a fluent answer built on the wrong passage is worse than no answer. And when nothing relevant turns up, have the system say so rather than invent content.

### Build agents and tool use with restraint

LLMs can call tools (search, databases, calculators, internal APIs) and can be composed into agents that plan and act over multiple steps. This adds real capability, but it also multiplies risk: every tool is another way for a wrong or manipulated model to cause harm. Define tools with precise schemas, validate every argument, apply least privilege, and require confirmation or human approval for consequential actions such as sending communications or moving money. Keep agent loops bounded, observable, and interruptible. Start with tightly scoped, single-purpose tools before you reach for open-ended autonomy.

### Add guardrails and validate outputs

Wrap the model in layers of defence. On the way in, filter and detect prompt injection, especially when untrusted content (web pages, user documents) enters the context. On the way out, validate structure against a schema, check claims against sources, filter unsafe or non-compliant content, and reject or retry when validation fails. For structured outputs, parse and verify rather than trust the model's formatting. Never let raw model output trigger irreversible actions without validation. Treat hallucination mitigation as a system property you achieve through grounding, citation, validation, and human review, not something the model manages on its own.

### Evaluate offline, online, and with humans

Build an evaluation suite of representative inputs with known-good or rubric-scored outputs, and run it on every prompt or model change (offline evaluation). Measure real behaviour in production with metrics such as task success, escalation rate, and user feedback (online evaluation). For subjective quality, use human reviewers and, carefully, model-based grading. Evaluation is the safety net that lets you change prompts and models with confidence. Without it, you are flying blind.

## Trade-offs: pros and cons

| Choice | Pros | Cons | Best when |
|---|---|---|---|
| Pure prompting | Simple, fast, cheap to change | Limited grounding, can hallucinate | Broad tasks, low stakes |
| RAG | Current, grounded, citable | Retrieval is hard to get right | Knowledge-heavy, factual tasks |
| Agents with tools | Powerful, can act | Larger attack surface, harder to control | Well-scoped automation with guardrails |
| Larger, stronger model | Better quality and reasoning | Higher cost and latency | Complex or high-stakes tasks |
| Smaller, cheaper model | Fast and inexpensive | Weaker on hard tasks | High volume, simple tasks |

The core tension is capability versus control and cost. More autonomy and larger models deliver more value, but they demand more guardrails, more evaluation, and more money. Grounding via RAG improves trustworthiness at the cost of retrieval engineering. The right balance depends on the stakes: high-stakes applications lean toward grounding, validation, and human oversight, even when that costs more.

## Questions to discuss with your team

1. **What accuracy and grounding bar must an LLM feature clear before it faces the public, and who signs off?** A fluent answer that cites the wrong source or invents a policy is worse than no answer, and in government a fabricated citation is a legal incident, not a bug. For a large team, an explicit bar stops each group from setting its own private threshold by vibe. Bring your definition of "grounded enough": whether every claim must trace to a retrieved, verified source, whether the system must refuse when retrieval comes up empty, and what your adversarial evaluation set actually covers. The signal to watch is whether anyone can currently ship a prompt change straight to users with no regression run. If the stakes are legal or safety-related, the answer should route the highest-risk outputs through a human reviewer with real authority before release.

2. **Which of our LLM features are secretly agents, and has each tool been given least privilege and a human gate on irreversible actions?** Any feature that lets the model call tools or act over multiple steps has crossed into agent territory, and every tool is another way a wrong or manipulated model causes harm. For enterprises wiring LLMs into internal APIs, this question surfaces risk that a "simple assistant" label hides. Bring an inventory of every tool the model can invoke, its argument validation, its privilege scope, and which actions (sending communications, moving money, changing records) require confirmation. Discuss whether agent loops are bounded, observable, and interruptible. The answer should tighten scopes and add human approval gates wherever a consequential or irreversible action is currently reachable without one.

3. **How would we know within a day that our retrieval quality has dropped, given a confident answer built on the wrong passage looks fine?** RAG makes answers trustworthy only when retrieval actually surfaces the passage that contains the answer, and retrieval silently rots as documents change, chunks go stale, or embeddings drift from your domain. Because the model still writes fluently over bad context, users may not complain until trust is already lost. Bring your current measures of retrieval latency and recall, how you check whether retrieved passages truly contain the answer, and how index freshness keeps pace with document changes. For high-stakes or public deployments, discuss logging retrieved sources for audit so you can trace a bad answer to its bad passage. If you have no retrieval evaluation at all, you are grounding on faith.

4. **Do we treat prompts, context, and evaluation sets as versioned, reviewed artefacts, or as strings scattered across notebooks and chat logs?** When prompts sprawl across teams unversioned and duplicated, a fix in one place never reaches the others, and nobody can reproduce what the system was asked to do last quarter. For a large team, a shared prompt registry and a regression suite that runs on every change are what let you swap a model or edit an instruction without silently breaking a feature two teams over. The competing pull is speed: engineers iterate fastest when they paste a prompt and ship, so agree where the line sits between quick experiments and anything that touches users. Bring where your prompts actually live today, whether an evaluation set gates changes, and how you version the retrieval corpus alongside the prompt. In enterprise and government settings, add the audit requirement: you may have to show exactly which prompt and which sources produced a given output months later, and a prompt you cannot reconstruct is a record you cannot defend.

5. **As volume grows, how will we control inference cost without silently degrading quality, and who owns the model-selection decision?** TCO for LLM features is dominated by per-call inference, and costs that look trivial in a pilot compound fast at production scale, tempting teams to quietly drop to a weaker model and hope nobody notices the quality slide. For a large organization, letting each team pick models and cost limits by feel produces both surprise bills and inconsistent quality. The genuine trade-off is capability versus cost and latency: a larger model reasons better on hard tasks, a smaller one is cheaper and faster on simple ones, and caching, routing, and retrieval scope all move the number. Bring cost per resolved task, quality by model tier on your evaluation set, and where prompt or context bloat is inflating token spend. In enterprise and government budgeting, name who approves the model choice and the spend ceiling, because a cost line nobody owns is one nobody controls when traffic triples.

6. **What sensitive data can reach the model, where does that data go, and can we prove it stayed within bounds?** Every prompt, retrieved document, and tool result may carry personal or confidential data into the model and, with a hosted provider, out of your perimeter, and a leak here is a legal or safety incident, not a defect ticket. For a large team wiring LLMs into internal systems, the risk hides in the plumbing: a retrieval corpus that includes records a given user should never see, or logs that capture raw inputs. The tension is capability versus exposure, since redaction and tight scoping can blunt the feature you are trying to build. Bring a data-flow map of what enters the context, the provider's retention and training terms, and how you redact, scope, and log sensitive fields. In regulated and public settings, tie this to data-residency rules, records-retention duties, and contractual limits on how a vendor may use your data, because oversight you cannot evidence is oversight you do not have.

## Sector lens

**Startup.** Ship one narrow LLM feature that touches your core value, built on a hosted model with retrieval over your own content, and keep prompts in git behind a thin interface so you can swap providers. Run a small evaluation file of real questions before each change, filter pasted user text to blunt prompt injection, and cap monthly spend hard. Resist agents and self-hosting: an unbounded tool-calling loop you cannot supervise is a liability, not a demo.

**Small business.** You likely have no ML specialist, so buy LLM features embedded in tools you already use rather than staffing a build. Frame the risk as a plain question: where would a confident wrong answer cost you a customer, and who checks the output before it goes out. Prefer vendors that show their sources, let you keep a human in the loop, and make the AI easy to turn off when it misbehaves.

**Enterprise.** The problem is scale across many teams: publish shared patterns for RAG, guardrails, and tool schemas, plus a common evaluation harness and prompt registry so each group stops rediscovering the same failure modes. Budget inference cost and human review explicitly, standardize the interface layer so models stay swappable, and govern agents centrally with least privilege, bounded loops, and audit logging. Manage LLM features as a portfolio with metrics and kill criteria, not a scatter of pilots.

**Government.** Transparency, procurement rules, and accountability shape every choice. Ground strictly in approved sources with citations, refuse when retrieval comes up empty, and forbid the model from stating law it cannot cite. Keep an accountable officer reviewing consequential outputs, log inputs and retrieved sources for audit, run an adversarial evaluation set before each release, and demand disclosure of model limitations and data-handling terms in the contract.

## Examples

**Startup.** A three-person developer-tools startup added a chat helper over its own docs so users could stop emailing basic questions. It used RAG so every answer cited a specific doc page, instructed the model to say "I'm not sure, here's who to ask" when retrieval came up empty, and kept its prompts in git. Before each change it ran the prompts against a small file of real user questions to catch regressions, and it filtered user-pasted text to blunt prompt injection. The helper handled the common questions and quietly passed the rest to the founders' shared inbox.

**Enterprise.** A software company built an internal support assistant over its product documentation. It used [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) so answers cite specific doc pages, told the model to say "I don't know" when retrieval failed, and verified that every cited source actually existed. Prompts were version-controlled and tested against a suite of real support questions on each change. The assistant deflected routine tickets and escalated anything low-confidence to human agents, while online metrics tracked resolution and correction rates.

**Government.** A public agency deployed an LLM assistant to help staff draft responses to citizen inquiries. Grounding was strict: the model could only compose replies from approved guidance with citations, and it was forbidden from stating policy that was not present in the retrieved sources. An accountable officer reviewed every draft before it went out. Input filtering guarded against prompt injection from citizen-submitted documents, outputs were logged for audit, and an evaluation set of adversarial and edge-case queries ran before each release to confirm the system refused to speculate on matters of law.

## Business case: motivations, ROI, and TCO

LLM applications deliver ROI by automating language-heavy work: answering questions, summarizing documents, drafting content, and extracting structure from unstructured text. Value shows up as deflected tickets, faster drafting, less manual review, and new self-service capabilities. Because there is often no training step, time to first value is short, a major draw.

TCO, though, is dominated by ongoing inference cost, retrieval infrastructure, evaluation pipelines, guardrail systems, and human review. Per-call costs add up quickly at scale, and an unmonitored application can drift into unsafe or expensive behaviour. The cost of not adopting is falling behind on service quality and staff productivity. The cost of adopting carelessly is a public hallucination incident or a data leak. Make the case to leadership by pairing a concrete productivity target with a concrete safety and evaluation plan, and by budgeting for the guardrails and human oversight that keep the value durable.

## Anti-patterns and pitfalls

- **Trusting fluent output.** Mistaking confident, well-written text for correct text.
- **RAG without retrieval evaluation.** Assuming retrieval works and never checking whether it surfaces the right passages.
- **Prompt injection blindness.** Feeding untrusted content into prompts without defences.
- **Unbounded agents.** Letting agents take consequential actions without limits or human approval.
- **No evaluation harness.** Changing prompts and models by vibe, with no regression testing.
- **Prompt sprawl.** Prompts scattered, unversioned, and duplicated across teams.
- **Over-automation.** Removing humans from decisions that carry legal or safety weight.

## Maturity model

1. **Initiate.** Ad hoc prompting in isolated projects; no grounding, guardrails, or evaluation; prompts live wherever someone pasted them, and hallucinations are discovered in production.
2. **Develop.** Some teams add RAG and prompt versioning, basic output validation, and a small manual evaluation set, but practices vary team to team and rest on individual champions rather than shared expectation.
3. **Standardize.** Documented patterns for RAG, guardrails, tool schemas, and prompt versioning are enforced org-wide; automated offline evaluation runs on every prompt or model change; high-stakes flows carry online metrics and human review.
4. **Manage.** The portfolio is measured against baselines: retrieval recall, hallucination and refusal rates, injection-defence coverage, per-call cost and latency, and escalation and correction rates are tracked on dashboards; release gates and kill criteria fire on evidence rather than opinion, and a regression run blocks any change that moves a metric the wrong way.
5. **Orchestrate.** Continuous offline and online evaluation is tied to business outcomes; injection defences, agents, and grounding are governed and observable; the organization routinely retires, retunes, and re-scopes LLM features, and swaps models as quality, cost, and risk shift.

## Ideas for discussion

- How do you decide which outputs require human review before use?
- What is your standard for "grounded enough" before an answer can be shown to users?
- How do you defend against prompt injection when untrusted content must enter the context?
- When is an agent worth its added risk versus a simpler, single-call design?
- How do you evaluate subjective quality at scale without over-relying on model-based grading?
- How do you keep prompts maintainable and consistent across many teams?

## Key takeaways

- Dependability comes from the engineering around the model: context, grounding, guardrails, and evaluation.
- RAG grounds answers in trusted sources and enables citation and verification.
- Treat the model as an untrusted component; validate outputs and constrain tool use.
- Give agents least privilege, bounded loops, and human approval for consequential actions.
- Evaluate offline, online, and with humans continuously; it is what makes change safe.

## References and further reading

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (engineering guidance).
- Louis-François Bouchard and Louie Peters, *Building LLMs for Production*.
