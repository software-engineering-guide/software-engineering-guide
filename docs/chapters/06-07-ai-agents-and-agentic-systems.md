# 6.7 AI agents and agentic systems

## Overview and motivation

An **AI agent** is a [large language model](https://en.wikipedia.org/wiki/Large_language_model) (LLM) wrapped in a loop: it is given a goal, it can call tools, it keeps some memory of what it has done, and it decides its own next step until the goal is met or it gives up. That loop is the whole difference between an agent and the plain prompt-response calls of chapter 6.3. A single call answers a question. An agent reads its email, searches a database, files a ticket, checks the result, and tries again. The model is no longer just producing text; it is choosing actions in your systems.

That shift changes the engineering problem. When a model only writes words, a bad output is a bad sentence. When a model drives tools, a bad output can send a wrong message, delete a record, or move money. So an [intelligent agent](https://en.wikipedia.org/wiki/Intelligent_agent) is best understood as an untrusted planner sitting inside a trusted system, and most of your work goes into bounding what that planner is allowed to do. This chapter builds directly on the LLM foundations of chapter 6.3, the trust and accountability concerns of chapter 6.5, and the platform practices of chapter 6.6.

For large teams the stakes are organizational as much as technical. Enterprises want agents wired into real internal systems (ticketing, finance, customer records), which means agents inherit real access controls and real change-management obligations. Government adds public accountability: an autonomous action that affects a citizen must be explainable, overseeable, and auditable after the fact. The pattern is powerful. Deployed without discipline, it is a fast way to automate mistakes.

## Key principles

- An agent is a model plus a loop, tools, memory, and a goal. The risk lives in the loop, not the prose.
- Bound autonomy to the task. Give the smallest amount of freedom that gets the job done.
- Prefer a fixed workflow when the steps are known. Reach for open-ended autonomy only when they are not.
- Treat every tool as attack surface and grant it the least privilege it can work with.
- Put a human in the loop for consequential or irreversible actions, and make reversal cheap.
- Evaluate on task success, not on how the transcript reads.
- Trace every run. An action you cannot reconstruct is an action you cannot govern.
- The simplest design that works is usually the right one. Often that is not an agent at all.

## Recommendations

### Start with a workflow, add autonomy only where you must

The most common mistake is reaching for an autonomous agent when a fixed pipeline would do. If you already know the steps (extract fields, validate them, look up a record, draft a reply), write that as an orchestrated workflow with the model filling specific slots. Autonomy earns its keep when the path genuinely cannot be predetermined, for example open-ended research or triage across many possible tools. Bound the autonomy to the task: cap the number of steps, restrict the tool set to what this goal needs, and set a clear stopping condition. A good rule is to give the model exactly as much freedom as the problem demands and not one degree more.

### Make tool use the core capability, and make it safe

Tool use (also called function calling) is what turns a model into an agent. Define each tool with a precise schema, validate every argument the model supplies, and apply the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege): a read-only reporting agent gets read-only credentials, never write access it might misuse. Run tools inside a [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) so a bad call cannot reach beyond its blast radius. Prefer many narrow, single-purpose tools over a few broad ones, because a narrow tool is easier to reason about, permission, and audit. This is the same restraint chapter 6.3 urges for LLM tool use, made central.

### Use explicit reasoning and planning patterns

Agents work better when their thinking is structured. In a reason-and-act pattern (popularized by the ReAct research), the model alternates between reasoning about the situation and taking an action, then observes the result before reasoning again. For harder goals, have the model plan first (decompose into subtasks) and then execute, so you can inspect and even approve the plan before any tool runs. Keep these loops observable and interruptible. A plan you can read is a plan you can stop.

### Keep humans in the loop for consequential actions

Decide, per tool and per action, whether the model may act alone or must ask first. Reversible, low-stakes actions (searching, drafting) can run unattended. Consequential or irreversible ones (sending external communications, moving money, changing production data, deciding a citizen's case) need a [human-in-the-loop](https://en.wikipedia.org/wiki/Human-in-the-loop) gate with real authority to say no. Design for reversibility wherever you can: prefer staging a change over committing it, and make undo a first-class feature so a mistaken action costs minutes, not an incident.

### Treat the security model as adversarial

Agents widen the attack surface described in chapter 4.2. The headline threat is [prompt injection](https://en.wikipedia.org/wiki/Prompt_injection): malicious instructions hidden in a web page, document, or email that the agent reads and obeys. Closely related is the [confused deputy problem](https://en.wikipedia.org/wiki/Confused_deputy_problem), where an attacker tricks a privileged agent into misusing its own legitimate access, for instance exfiltrating data through a tool the agent is allowed to call. Assume any content the agent ingests may be hostile. Separate trusted instructions from untrusted data, constrain tools so a hijacked agent cannot reach sensitive systems, and never let raw model output trigger an irreversible action without validation.

### Evaluate on task success and regression-test the non-determinism

Judge agents by whether they accomplish the task, not by whether the transcript sounds smart. Build an evaluation set of representative goals with checkable success criteria (did the ticket get the right priority, did the refund match policy) and run it on every prompt, model, or tool change. Because agents are non-deterministic, a single pass proves little: run each case multiple times and track a success rate, not a pass or fail. This extends the offline and online evaluation discipline of chapters 6.3 and 6.2 (machine learning engineering and MLOps) to systems whose output is a sequence of actions.

### Instrument runs for observability, cost, and failure handling

You cannot govern what you cannot see. Trace every agent run end to end (chapter 6.6): the goal, each reasoning step, every tool call with its arguments and result, the tokens spent, and the final outcome. This tracing is your debugger, your audit trail, and your cost meter at once. Set hard budgets on steps, time, and spend, because an agent that loops can burn latency and money fast. Handle failure explicitly: retry transient tool errors with backoff, but detect loops where the model repeats a failing action, and fail safe rather than thrash.

## Trade-offs: pros and cons

| Choice | Pros | Cons | Best when |
|---|---|---|---|
| Fixed workflow (model fills slots) | Predictable, cheap, easy to test and audit | Rigid; breaks on unforeseen paths | Steps are known in advance |
| Autonomous single agent | Flexible; handles open-ended goals | Harder to control, evaluate, and bound | The path cannot be predetermined |
| Multi-agent orchestration | Parallelism; specialized roles | Coordination cost, compounding errors, higher spend | A task truly decomposes into independent parts |
| Unattended action | Fast, low friction | Mistakes execute without a check | Actions are reversible and low-stakes |
| Human-in-the-loop gate | Safety, accountability, reversibility | Slower; needs reviewer capacity | Actions are consequential or irreversible |

The central tension is autonomy versus control. More autonomy handles more situations but demands more guardrails, more evaluation, and more money, and it fails in ways that are harder to predict. Multi-agent designs tempt teams with elegance, yet each additional agent adds coordination overhead and another place for a small error to compound into a wrong result. Resolve the tension by starting with the least autonomy that solves the problem and adding freedom only when a concrete task forces you to, always paired with a matching guardrail.

## Questions to discuss with your team

1. **Does this feature actually need an agent, or would a fixed workflow be safer and cheaper?** Autonomy is seductive, but most jobs have knowable steps that an orchestrated pipeline handles with far less risk. For a large team, defaulting to agents means every group takes on evaluation, tracing, and security burdens that a simpler design would avoid. Bring the specific task and ask whether its steps can be predetermined; if they can, an agent is likely over-engineering. Reserve open-ended autonomy for goals where the path genuinely varies per case. The answer should push most features towards a workflow and leave a small, deliberate set as true agents.

2. **For every tool our agent can call, what is the worst thing a hijacked agent could do with it, and what stops that?** Prompt injection and confused-deputy attacks turn the agent's own legitimate access against you, so the right lens is adversarial (chapter 4.2). Inventory each tool, its privilege scope, and whether a malicious instruction smuggled through ingested content could reach it. For enterprises wiring agents into internal systems, this is where least privilege, sandboxing, and human gates on irreversible actions get real. Bring the list of tools and the credentials each one holds. If any consequential action is reachable without validation or a human check, that is the first thing to fix.

3. **How would we know an agent's success rate dropped, given every run looks plausible?** Agents are non-deterministic, so a transcript that reads well can still have taken the wrong action, and one green run proves nothing. Ask whether you have an evaluation set of goals with checkable outcomes, run many times per case to produce a success rate rather than a single pass. For high-stakes or public deployments, discuss how run traces let you reconstruct exactly what happened when something goes wrong (chapters 6.5 and 6.6). If your only signal is user complaints, you are already too late. The answer should fund an evaluation harness before scale, not after an incident.

4. **Which of this agent's actions are truly irreversible, who holds authority to approve them, and do we have the reviewer capacity to staff that gate?** The temptation is to let the model act unattended everywhere, but a human gate is only real if a named person with authority to say no is available when the agent asks. For a large team, an approval queue that no one owns quietly becomes a rubber stamp, and the safety you designed evaporates under volume. Bring the full list of actions the agent can take, mark each reversible or irreversible, and estimate the daily volume of low-confidence cases that would land on a reviewer. Weigh the friction and staffing cost of a gate against the blast radius of an unattended mistake, and prefer redesigning an irreversible action into a staged, undoable one over adding another reviewer. In enterprise and government settings, tie each consequential action to an accountable officer and a change-management record, because an autonomous action affecting a citizen or a customer that no human approved is exactly the failure an audit will find.

5. **Are we reaching for a multi-agent design because the task genuinely decomposes, or because it looks elegant?** Splitting work across specialized agents is seductive, yet each extra agent adds coordination overhead and another place where a small error compounds into a wrong result. For a large organization the cost is not just spend and latency: a multi-agent system is far harder to trace, evaluate, and reason about when it fails, so the governance burden multiplies with every role you add. Bring the task and show, concretely, which parts run independently and in parallel, then compare the measured success rate and cost of a multi-agent version against a single agent on the same evaluation set. If the single agent wins or ties, the elegant design is over-engineering. For regulated or public deployments, remember that every agent in the chain is another component an oversight body must be able to inspect, so added structure you cannot justify is added liability.

6. **What are the hard budgets on an agent's steps, time, and spend, and how would a looping agent be caught before it runs up cost or latency?** An agent that repeats a failing action can burn money and time without warning, so unbounded autonomy is a financial risk as much as a safety one. For a large team running many agents, a single misbehaving loop can spike a cloud bill or exhaust a rate limit that starves every other workload, which makes per-run caps a shared operational concern rather than one team's problem. Bring the current step, time, and token budgets for each agent, the alerting that fires when a run exceeds them, and the loop-detection that fails safe rather than thrashing. Weigh tight budgets, which may cut off a legitimately hard task, against loose ones that let cost run away. In enterprise and government settings where spend must be forecast and justified, an agent whose cost is unbounded is a line item you cannot defend in a budget review or an audit.

## Sector lens

**Startup.** Ship one narrow agent that touches your core value, on a hosted model, with the smallest tool set that does the job and a hard cap on steps and spend. Resist the multi-agent demo: your scarce engineering attention is better spent bounding a single agent's autonomy and tracing its runs than coordinating roles you cannot maintain. Keep every consequential action behind a single "draft, never send" gate so a mistake costs a click to undo, not an incident.

**Small business.** You have no one to run an evaluation harness or a sandbox, so prefer agents embedded in tools you already trust, and turn on only the autonomy you can supervise by eye. Treat any agent that can send, pay, or delete on your behalf as something to keep off until a person confirms each action, because a wrong automated message to a customer costs you the relationship. Favour vendors who show you what the agent did and let you switch the automation off.

**Enterprise.** The problem is governing agents across many teams: shared patterns for bounding autonomy, least-privilege tool credentials, sandboxing, human-in-the-loop gates, and end-to-end tracing so no group reinvents the guardrails. Wire agents into internal systems under the same access controls a human would hold, gate irreversible actions behind named approvers and change management, and manage the portfolio with success-rate metrics, per-run budgets, and adversarial injection testing. Standardize the tracing and evaluation layer so any agent's behaviour can be reconstructed and audited.

**Government.** Procurement, transparency, and public accountability bound every choice. Keep agents to gathering facts and drafting, and reserve every decision that affects a citizen for an accountable human, because responsibility for a public-sector decision cannot be delegated to a model. Log every run so an oversight body can see which sources were consulted and what was done, demand that vendors disclose the agent's tools and limitations, and prove through an adversarial evaluation set that the agent refuses to act beyond its bounded remit.

## Examples

**Startup.** A five-person analytics startup builds a support triage agent. It reads an incoming ticket, searches the docs, and either drafts a reply or routes the ticket to a human, and that is the whole tool set. The credentials are read-only plus a single "create draft" action that never sends without a person clicking send. Every run is traced so the founders can see why a ticket was routed where it was, and a nightly evaluation set of fifty real tickets runs the agent five times each to track a routing-accuracy rate. When a competitor's clever multi-agent demo tempts them, they stay single-agent because their task does not decompose.

**Enterprise.** A bank builds an agent to help operations staff reconcile failed payments. It integrates with internal systems under the same access controls a human clerk has, granted through least-privilege service credentials scoped to reconciliation only. The agent may investigate freely (read ledgers, search transaction history) but any action that moves money or edits a record is staged and requires a named human approver, satisfying change management. Ingested documents are treated as untrusted to blunt prompt injection, tools run sandboxed, and every run is traced end to end for audit. An offline evaluation set gates each model or prompt change, and per-run budgets cap steps and spend so a looping agent cannot run up cost or latency.

**Government.** A benefits agency pilots an agent to help caseworkers assemble the facts for a claim: pulling records, checking eligibility rules, and drafting a summary. The agency draws a hard line: the agent gathers and drafts, but a human caseworker makes and owns every decision that affects a citizen, because accountability for public-sector decisions cannot be delegated to a model (chapter 6.5). Each run is fully logged, showing which sources were consulted and what was drafted, so an oversight body can audit any case. Autonomy is deliberately bounded to read-and-draft, tools are least-privilege and sandboxed, and an adversarial evaluation set confirms the agent refuses to act beyond gathering facts.

## Business case: motivations, ROI, and TCO

Agents deliver return by automating multi-step work that used to need a person to click between systems: triage, reconciliation, research, and routine operations. The value shows up as work completed without a human in every step, faster cycle times, and staff freed for judgement-heavy tasks. Because agents build on existing LLMs and tools, time to a working prototype is short, which is exactly why teams overbuild.

The total cost of ownership is where agents differ from plain LLM features. On top of inference cost you pay for the tool integrations, the sandboxing and permission plumbing, the evaluation harness, the tracing and observability stack (chapter 6.6), and the human reviewers who staff the approval gates. A looping or poorly bounded agent adds a variable cost that can spike without warning, so budgets on steps and spend are part of the design, not an afterthought. The cost of not adopting is slower operations and manual toil your competitors automate. The cost of adopting carelessly is an autonomous action that sends the wrong message, leaks data, or makes an unaccountable decision. Make the case to leadership by pairing one concrete automation target with a concrete plan for guardrails, evaluation, and human oversight, and by being honest that the guardrails are most of the cost.

## Anti-patterns and pitfalls

- **Agent when a workflow would do.** Taking on autonomy's full risk for a task whose steps were knowable.
- **Over-broad tools and credentials.** One "do anything" tool instead of narrow, least-privilege ones.
- **Prompt-injection blindness.** Feeding untrusted content to an agent that holds real privileges.
- **No human gate on irreversible actions.** Letting the model send, pay, or delete without a check.
- **Multi-agent theatre.** Splitting a simple task across agents, paying coordination cost for no gain.
- **Vibes-based evaluation.** Judging by how the transcript reads instead of task success rate.
- **Unbounded loops.** No cap on steps, time, or spend, so a stuck agent burns money and latency.
- **Untraced runs.** No record of what the agent did, leaving you unable to debug, audit, or account.

## Maturity model

- **Level 1, Initiate:** Agents are prototyped ad hoc with broad tool access and no bounds. Success is judged by demos, reactively, after something breaks. There is no evaluation set, no tracing, and no human gate on consequential actions.
- **Level 2, Develop:** Some agents have bounded loops and least-privilege tools, and basic tracing exists, but practice varies team by team. A manual evaluation set catches gross regressions in a few projects while others have none. Human approval guards the most obvious irreversible actions, yet coverage is uneven and undocumented.
- **Level 3, Standardize:** Shared patterns govern autonomy, tool permissions, sandboxing, and human-in-the-loop gates, documented and enforced across every team. Every consequential action is gated or validated, agents are traced end to end, and an automated evaluation set with success-rate scoring runs on every change. Prompt injection is treated as a standing threat with a defined response.
- **Level 4, Manage:** The agent portfolio is measured and controlled against baselines. Success rate per task, prompt-injection defence pass rate, cost and step count per run, human-approval latency, and loop or failure incidents are tracked as metrics; rollback and kill thresholds are enforced on that evidence rather than on complaints. Per-run budgets on steps, time, and spend are monitored, and a regression in any metric triggers action before scale, not after an incident.
- **Level 5, Orchestrate:** Autonomy is matched to task risk by policy and adjusted continuously as results come in. Ongoing offline and online evaluation ties agent behaviour to business outcomes, and the organization routinely retires, re-scopes, or re-permissions agents as the risk picture shifts. Tracing, cost budgets, and audit trails are uniform across the portfolio; injection and confused-deputy defences are tested adversarially; accountability for autonomous actions is clear and auditable.

## Ideas for discussion

1. Which of your current LLM features have quietly become agents, and has each one's autonomy been bounded on purpose?
2. For each agent tool, what is the cheapest way an attacker could abuse it through injected content, and what stops that?
3. Where have you chosen multi-agent designs, and can you show the coordination cost paid off versus a single agent?
4. Which agent actions are truly irreversible, and could every one of them be redesigned to be reversible or staged?
5. If an agent took a harmful action tomorrow, could you reconstruct exactly what it did and who was accountable?

## Key takeaways

- An agent is an LLM in a loop with tools, memory, and a goal. The risk lives in the loop and the tools, not the text.
- Prefer a fixed workflow when the steps are known; reserve autonomy for genuinely open-ended goals and bound it tightly.
- Tool use is the core capability. Give each tool least privilege, a validated schema, and a sandbox.
- Gate consequential and irreversible actions behind a human with real authority, and design for cheap reversal.
- Treat agents as adversarial: defend against prompt injection and confused-deputy abuse (chapter 4.2).
- Evaluate on task success rate across many runs, and trace every run for debugging, cost control, and audit (chapters 6.5 and 6.6).
- Often the right answer is not to build an agent at all.

## References and further reading

- Shunyu Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (engineering guidance on workflows versus agents).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (including prompt injection and excessive agency).
- Simon Willison, writing on prompt injection and the "lethal trifecta" for AI agents.
- Norman Hardy, *The Confused Deputy* (the classic statement of the confused-deputy problem).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (intelligent agents and rational action).
