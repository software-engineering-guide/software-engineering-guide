# 6.8 AI evaluation and testing

## Overview and motivation

Testing ordinary software rests on a comforting assumption: given the same input, the program returns the same output, and you can assert exactly what that output should be. Artificial intelligence breaks that assumption. A model can answer the same question two different ways, both acceptable. It can be graded on a spectrum from wrong to brilliant rather than pass or fail. And there is often no single correct answer to assert against. So the discipline of evaluation, measuring how well a model behaves across many representative cases rather than checking one output against one expected value, becomes the backbone of any trustworthy AI system. When teams ship AI features that embarrass them, the root cause is almost always that they had no serious way to measure quality before release.

For large teams, evaluation is what makes change safe. You will swap models, rewrite prompts, tune retrieval, and add tools, and every one of those changes can silently degrade behavior you thought was solid. Without a repeatable way to measure quality, each change is a gamble and each regression is discovered by a user. This chapter is the measurement companion to the building chapters: generative AI and LLM applications (chapter 6.3), AI agents and agentic systems (chapter 6.7), and machine learning engineering and MLOps (chapter 6.2). It extends your general testing strategy (chapter 2.4) into the probabilistic world.

Enterprise and government settings raise the stakes further. An enterprise running dozens of AI features needs a shared evaluation platform so every team does not reinvent grading from scratch. A government agency needs evaluation that is documented and auditable, because "we tested it" must become "here is the evidence, the dataset, the metric, and the sign-off." Evaluation is where responsible and trustworthy AI (chapter 6.5) stops being a value statement and becomes something you can show a regulator.

## Key principles

- Treat evaluation as a first-class product, not an afterthought bolted on before launch.
- Measure with representative data that mirrors real usage, not toy examples that flatter the model.
- Combine offline evaluation for fast iteration with online evaluation for ground truth.
- Use human judgment as your anchor, and calibrate every automated grader against it.
- Guard your evaluation sets from contamination, or your numbers will lie to you.
- Wire evaluations into continuous integration as gates, so quality cannot silently regress.
- Keep measuring in production, because quality drifts even when your code does not.

## Recommendations

### Adopt eval-driven development

Before you tune a prompt or pick a model, write the evaluation. This mirrors test-driven development: you define what "good" means in measurable terms, then build toward it. An evaluation here means a dataset of inputs paired with a scoring method that returns a number or grade for each output. Start small. Twenty carefully chosen cases that reflect real user intent beat a thousand random ones. Grow the set as you learn where the system fails, adding every production failure back as a permanent case so the same mistake cannot return unnoticed.

Eval-driven development changes team behavior. When the definition of good is written down and runnable, arguments about whether a change helped become checkable rather than a matter of taste. Make the eval set a reviewed artifact in version control, right next to the prompts and code it measures.

### Separate offline and online evaluation, and use both

Offline evaluation runs a fixed dataset through your system in a controlled setting, fast, cheap, and repeatable, so you can compare versions before anything ships. Online evaluation measures the live system with real users through metrics such as task completion, escalation rate, thumbs-up and thumbs-down feedback, and downstream business outcomes. Offline tells you whether a change is likely safe; online tells you whether it actually worked. You need both, because offline sets never fully capture reality and online signals arrive too late to be your only guardrail.

Connect the two into a loop. When online metrics dip or users flag a bad answer, capture that case, label it, and fold it into the offline set. Route experiments through the same controlled comparison you use for any product change, which is the territory of product analytics and experimentation (chapter 7.4). An A/B test showing a new model lifts task success is worth more than any offline score, yet the offline score is what let you dare to run the test.

### Build representative eval sets and guard against contamination

Your evaluation is only as honest as its data. Build golden datasets, curated collections of inputs with vetted expected outputs or scoring rubrics, that mirror the real distribution of what users ask: the common cases, the rare-but-critical cases, the adversarial cases, and the ones your system currently gets wrong. Stratify them so you can read quality per segment rather than hiding a failing category inside a decent average. Have domain experts vet the expected answers, because a golden set built on wrong answers is worse than none.

Then protect that data from contamination. Test-set contamination happens when your evaluation examples leak into a model's training data or into the prompt itself, so the model appears to perform well because it has effectively seen the answers. This is why a model can score brilliantly on a public benchmark and stumble on your real traffic. Keep a portion of your eval data private and never send it to a third party you cannot trust. Refresh sets over time. Watch for the subtler leak where developers hand-tune prompts against the eval set until the score is meaningless, a form of overfitting to the test rather than genuine improvement. Hold out a fresh set that you only look at occasionally.

### Choose metrics that fit the task

Match your measurement to the shape of the output. For classification and extraction, where there is a correct label, classic metrics apply: [precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall) (of the items you flagged, how many were right, and of the right items, how many you found), the [F-score](https://en.wikipedia.org/wiki/F-score) that balances them, and exact-match accuracy. For anything where a confident probability matters, measure [calibration](https://en.wikipedia.org/wiki/Calibration_(statistics)), whether a stated 80 percent confidence is right about 80 percent of the time, because a well-calibrated model that knows when it is unsure is far safer than an overconfident one.

Generative outputs are harder. Reference-based metrics like [BLEU](https://en.wikipedia.org/wiki/BLEU) and ROUGE, originally built for machine translation and summarization, compare generated text against reference text by counting overlapping words and phrases. They are cheap and repeatable, and they are weak proxies for quality: they reward surface overlap and punish a correct answer phrased differently from the reference. Use them as coarse regression signals, not as your definition of good. For open-ended tasks, rubric-based scoring works better: define explicit criteria (is it grounded, complete, safe, and correctly formatted) and score each one. Rubrics make subjective quality legible and reviewable.

### Use LLM-as-a-judge, but calibrate it against humans

Grading generative output by hand does not scale, so teams increasingly use a strong [large language model](https://en.wikipedia.org/wiki/Large_language_model) as an automated judge, prompting it with the input, the output, and a rubric, and asking it to score. This LLM-as-a-judge approach is fast and surprisingly capable, and it carries real biases you must manage. Judges tend to prefer longer answers, favor the first option shown in a pairwise comparison (position bias), reward their own writing style, and can be swayed by fluent but wrong reasoning. Left unchecked, a biased judge gives you confident, precise, wrong numbers.

Calibrate the judge against human labels. Have people grade a sample, then check how well the model judge agrees with them, and keep tuning the judge prompt until agreement is high enough to trust. Reduce known biases deliberately: randomize option order, control for length, and ask for a rubric-anchored score with reasons rather than a bare number. Treat the judge as a measuring instrument that needs periodic recalibration, not a fixed oracle. When you build the judge, default to the most capable model available, since a weak judge is a weak ruler.

### Keep humans in the loop for the ground truth

Human evaluation remains the anchor that every automated metric is measured against, so invest in doing it well. Write clear annotation guidelines, train your annotators, and measure inter-annotator agreement, the degree to which independent reviewers give the same case the same grade. Low agreement usually means your rubric is ambiguous, not that your reviewers are careless, so fix the rubric. For high-stakes domains, use qualified experts, not crowd workers who lack the context to judge a legal or medical answer.

### Red-team for safety and adversarial robustness

Standard eval sets measure whether the system does the right thing on reasonable inputs. [Red teaming](https://en.wikipedia.org/wiki/Red_team), deliberately attacking your own system to find where it misbehaves, measures what happens under pressure. Probe for prompt injection, jailbreaks, unsafe content, privacy leaks, and biased outputs. Make it a repeatable suite, not a one-time exercise: turn every successful attack into a permanent regression case so a fixed vulnerability stays fixed. This work connects directly to responsible and trustworthy AI (chapter 6.5), and in regulated settings it is often the evidence that satisfies a safety review.

### Evaluate agents by end-to-end task success

Agents that plan and act over many steps cannot be judged one output at a time. What matters is whether the whole task succeeded: did the agent book the meeting, resolve the ticket, or complete the workflow correctly and safely. Build task-level evaluations in a sandboxed environment where the agent can act against realistic but safe fixtures, and score final outcomes plus the trajectory, meaning the sequence of steps and tool calls it took to get there. A correct answer reached through a dangerous or wasteful path is still a problem. This is essential to AI agents and agentic systems (chapter 6.7), where a single wrong action can have real consequences.

### Wire evaluations into CI and monitor production

Make evaluation automatic. Run your offline suite in [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI) on every prompt, model, or retrieval change, and gate merges on it just as you gate on unit tests, a practice rooted in your broader testing strategy (chapter 2.4). Because scores are noisy, gate on thresholds and trends rather than demanding a perfect run, and fail the build when a key metric drops below its floor or regresses beyond a set margin. Then keep watching in production: monitor quality signals, output distributions, and input drift so you catch the slow degradation that offline tests miss, which ties into the observability practices of machine learning engineering and MLOps (chapter 6.2). A model that was accurate at launch can decay as the world it describes changes underneath it.

## Trade-offs: pros and cons

| Evaluation approach | Pros | Cons | Best when |
|---|---|---|---|
| Human evaluation | Highest fidelity, captures nuance | Slow, costly, hard to scale | Ground truth, high-stakes, calibrating judges |
| LLM-as-a-judge | Fast, cheap, scales to large sets | Biased, needs calibration | Frequent offline runs on generative output |
| Reference-based metrics (BLEU, ROUGE) | Cheap, deterministic, repeatable | Weak proxy for real quality | Coarse regression signals, not final verdicts |
| Classic metrics (precision, recall, F-score) | Objective, well understood | Only fit tasks with correct labels | Classification, extraction, retrieval |
| Public benchmarks | Comparable across models, no setup | Contamination, poor fit to your task | Early model shortlisting, not release gates |
| Online evaluation (A/B, feedback) | Reflects real users and outcomes | Slow, arrives after exposure | Confirming a change actually helped |

The central tension is speed versus fidelity. Human evaluation is the most trustworthy and the least scalable; automated grading is the reverse. The resolution is to layer them: use fast, cheap methods for constant iteration, anchor those methods to human judgment through regular calibration, and reserve full human review for the highest-stakes decisions and for checking that your cheap metrics still track reality. A second tension is offline convenience versus online truth. Offline sets let you move fast but never fully mirror production, so treat a strong offline score as permission to run a careful online test, not as proof you are done.

## Questions to discuss with your team

1. **What is our bar for "good enough," and who owns the eval set that defines it?** Every AI feature has an implicit quality threshold, and when it stays implicit, each engineer sets their own by feel and disputes get settled by whoever is most senior in the room. Writing the bar down as a runnable eval set with target scores per segment turns those disputes into measurable questions. Bring your current definition of success, the data behind it, and an honest account of who actually maintains it, because an eval set with no owner rots as fast as any other untended code. Decide whether the bar differs by risk tier, since a public-facing legal answer should clear a higher bar than an internal brainstorming aid. The answer should tell you whether anyone can currently ship an AI change with no measurement standing between them and users.

2. **How do we know our evaluation numbers are honest rather than contaminated or overfit?** A score is only useful if it predicts real-world quality, and there are many ways for it to stop doing that: benchmark data leaking into training, developers tuning prompts against the test set until the number is meaningless, or a golden dataset built on answers that were never verified. Bring evidence about where your eval data came from, how much of it is held private, and how often it is refreshed. Discuss whether you keep a fresh holdout that you look at rarely, so you have at least one number nobody has been optimizing against. If you cannot explain why your scores would still hold on data the model has never influenced, you are measuring your own reflection.

3. **Where do humans stay in the loop, and how do we keep our automated judges calibrated to them?** LLM-as-a-judge and reference metrics let you grade at scale, and they drift from human judgment in ways that are invisible unless you check. Bring your current agreement rate between automated grading and human review, how recently you measured it, and which biases (length, position, style) you have tested for. Decide which decisions require a human grader regardless of cost, typically the highest-stakes and the ones used to recalibrate the automated judge. Talk about annotation quality too, because a judge calibrated against inconsistent human labels inherits that inconsistency. The answer should produce a schedule for recalibration, not a one-time blessing.

## Examples

**Startup.** A four-person company building an AI contract-review assistant started with a spreadsheet of forty real clauses, each labeled by their in-house lawyer with the risk it should flag. Every prompt change ran against that set in a script before merging, and the score printed in the pull request. When users flagged a missed clause, it went straight into the sheet, so the set grew with the product. As volume rose they added an LLM-as-a-judge to grade explanation quality, but only after checking it agreed with the lawyer on a sample. Cheap, private, and honest beat any public benchmark for their niche.

**Enterprise.** A large bank ran a dozen AI features across support, search, and internal tooling, and each team had been grading differently. They built a shared evaluation platform: a common place to store golden datasets, run offline suites in CI, register LLM-judge prompts with their calibration scores, and track online metrics per feature. Governance sat on top, with risk tiers that set the required bar and the sign-off needed before release. A new fraud-explanation feature could not ship until its eval set was reviewed, its red-team suite passed, and its accountable owner signed the results. Reusing the platform meant teams argued about their domain, not about how to measure.

**Government.** A public health agency deployed an assistant to help staff answer benefits questions from approved guidance. Because a wrong answer could affect someone's eligibility, evaluation had to be auditable. Every release ran a documented eval set covering common questions, edge cases, and adversarial prompts, and the results, the dataset version, the metrics, and the reviewer's name were archived as accountability evidence. A red-team suite checked that the system refused to invent policy or state law absent from its sources. When an oversight body asked how the agency knew the tool was safe, the answer was a dated record, not a reassurance.

## Business case: motivations, ROI, and TCO

Evaluation pays for itself by making every other AI investment safer and faster. Its return on investment (ROI) shows up as fewer production incidents, faster iteration because teams can change prompts and models with confidence, and the ability to adopt better models the day they arrive because you can prove whether they help. The clearest way to value it is the cost of its absence: a single public hallucination, biased output, or data leak can cost far more in remediation, lost trust, and regulatory exposure than years of evaluation infrastructure. It is the difference between finding a regression in CI for free and finding it in the newspaper.

The total cost of ownership (TCO) is real and worth naming. You pay for annotation labor, for the compute that automated judges consume, and for the ongoing work of keeping eval sets representative as usage shifts. At enterprise scale, a shared platform amortizes most of this across many teams, which is the strongest argument for building one rather than letting every group improvise. Make the case to leadership by pairing a concrete risk (the cost of one bad public answer in your domain) with a concrete capability (the speed to safely adopt each new model), and by framing evaluation as the control that lets the organization move fast without moving recklessly.

## Anti-patterns and pitfalls

- **Vibes-based shipping.** Judging AI changes by trying a few prompts by hand, with no dataset and no repeatable score.
- **Benchmark theater.** Trusting a strong public benchmark score as proof the system fits your task, ignoring contamination and distribution mismatch.
- **Overfitting to the eval set.** Tuning prompts against the same fixed set until the number is high and meaningless, with no fresh holdout.
- **Uncalibrated judges.** Deploying an LLM-as-a-judge and trusting its scores without ever checking agreement with human graders.
- **Metric worship.** Optimizing BLEU or ROUGE as if it were quality, and shipping worse answers that happen to overlap the reference text.
- **One-shot red teaming.** Attacking the system once before launch and never turning findings into permanent regression tests.
- **Offline-only confidence.** Believing a good offline score means the feature works, with no online measurement of real outcomes.
- **Orphaned eval sets.** Datasets nobody owns, that never absorb production failures and slowly stop reflecting reality.

## Maturity model

- **Level 1, Initial:** AI changes are judged by hand on a few examples. There is no dataset, no repeatable score, and no gate. Regressions are found by users, and nobody can say whether the system is better or worse than last month.
- **Level 2, Managed:** Teams keep small golden datasets and run them manually before big changes. Some classic metrics and reference-based scores exist. Human review happens for important features, but grading is inconsistent and evaluation is not yet automated or gated.
- **Level 3, Defined:** Offline suites run in CI on every change and gate merges. LLM-as-a-judge is calibrated against human labels, red teaming is a repeatable suite, and online metrics track real outcomes. Datasets are owned, versioned, and fed by production failures, with contamination actively guarded.
- **Level 4, Optimizing:** A shared evaluation platform serves the whole organization with governance and risk tiers. Offline and online evaluation form a continuous loop tied to business outcomes, judges are recalibrated on a schedule, drift is monitored in production, and evaluation evidence is auditable for regulators and oversight.

## Ideas for discussion

1. How do you decide when an offline score is strong enough to justify an online experiment, and when it is not?
2. What is the right ratio of human evaluation to automated grading for your risk profile, and how often should you revisit it?
3. When a public benchmark and your private eval set disagree about which model is better, which do you trust and why?
4. How do you keep an eval set representative as user behavior shifts, without letting it balloon into something too slow to run in CI?
5. What belongs in a red-team suite for your domain, and who is qualified to design the attacks?
6. How do you evaluate an agent's trajectory, not just its final answer, without drowning in the cost of grading every step?

## Key takeaways

- AI evaluation differs from software testing because outputs are non-deterministic and there is rarely one correct answer, so you measure quality across representative cases instead of asserting exact values.
- Practice eval-driven development: define measurable quality first, then build toward it, and fold every production failure back into the set.
- Layer methods by speed and fidelity: cheap automated grading for constant iteration, human judgment as the anchor, and calibration to keep them aligned.
- Guard against contamination and overfitting, or your numbers will flatter you while the real system disappoints users.
- Wire offline evaluation into CI as a gate and keep measuring quality and drift in production, because a model that was good at launch can decay.

## References and further reading

- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Lianmin Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
- Kishore Papineni et al., *BLEU: A Method for Automatic Evaluation of Machine Translation*.
- Chin-Yew Lin, *ROUGE: A Package for Automatic Evaluation of Summaries*.
- Percy Liang et al., *Holistic Evaluation of Language Models (HELM)*.
- Deep Ganguli et al., *Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- National Institute of Standards and Technology, *AI Risk Management Framework*.
