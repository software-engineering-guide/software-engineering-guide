# 6.2 Machine learning engineering (MLOps)

## Overview and motivation

Machine learning engineering, usually called [MLOps](https://en.wikipedia.org/wiki/MLOps), is the discipline of taking [machine learning](https://en.wikipedia.org/wiki/Machine_learning) out of notebooks and experiments and into reliable, observable, maintainable production systems. Traditional software behaves the way its code says it will. An ML system behaves the way its code, its data, and its learned model parameters together say it will. That makes ML systems harder to test, harder to reproduce, and prone to failing quietly as the world drifts away from the data they were trained on. MLOps brings the rigour of software engineering (version control, testing, continuous delivery, and monitoring) to this three-part reality of code plus data plus models.

For large teams, MLOps is what separates a one-off model that dazzles in a demo from a fleet of models many teams can build, deploy, and operate safely. Without shared platforms and practices, every team reinvents data pipelines, training loops, and deployment, and you end up with brittle systems no one can reproduce six months later. Enterprises rely on MLOps to scale across dozens of models, meet service-level objectives, and satisfy auditors who ask how a given prediction was produced.

In government and regulated industries, MLOps is often a compliance requirement in disguise. Reproducibility, lineage, and versioning are what let an agency answer a legally significant question: exactly which model, trained on which data, with which code, produced the decision that affected a citizen? A mature MLOps practice keeps that question answerable years later, which is both good engineering and a legal safeguard.

*See also:* chapter 8.1 (CI/CD and delivery), chapter 9.2 (observability and monitoring), and chapter 6.6 (AI infrastructure and operations).

## Key principles

- Treat data, code, and models as jointly versioned artefacts; changing any one changes system behaviour.
- Automate the path from data to trained model to deployment so it is repeatable and auditable.
- Make every model traceable to the exact data, code, and configuration that produced it.
- Evaluate models against representative, held-out data before deployment, and keep evaluating after.
- Assume models degrade; monitor for drift (the gradual divergence of live data or input-output relationships from what the model was trained on), data quality problems, and performance decay from day one.
- Prefer boring, reproducible pipelines over clever, irreproducible experiments.
- Separate the concerns of experimentation speed and production reliability, and bridge them deliberately.

## Recommendations

### Manage the full ML lifecycle explicitly

Define and instrument each stage: data ingestion and validation, [feature engineering](https://en.wikipedia.org/wiki/Feature_engineering), training, evaluation, deployment, and monitoring. Make the boundaries between stages explicit so each one can be tested, retried, and audited. Avoid the common failure where a model is trained in an ad hoc notebook and thrown over the wall to operations. Instead, wrap the lifecycle in an orchestrated pipeline that any authorized engineer can run from a clean checkout.

### Use feature stores, experiment tracking, and model registries

A **feature store** centralizes feature definitions so the same transformations run in both training and serving. This eliminates training-serving skew (inconsistencies between how features are computed for training versus for live predictions) and lets teams reuse features rather than recompute them. **Experiment tracking** records every training run's parameters, code version, data version, and metrics, so results are comparable and reproducible. A **model registry** is the system of record for trained models, holding versions, lineage, evaluation results, approval status, and deployment stage. Together, these let you answer "what changed?" when behaviour shifts, and promote or roll back models through governed stages.

### Make data and models reproducible and versioned with lineage

Version your datasets, not just your code. Use content-addressable storage or data-versioning tools so a training run references an immutable snapshot. Pin code with git commits, and pin environments with locked dependencies and container images. Capture lineage end to end: which raw data fed which features, which features and code produced which model, and where that model is deployed. When an incident or audit hits, lineage turns a forensic nightmare into a simple query. Record randomness (seeds) and hardware wherever results depend on them.

### Choose deployment patterns to match the workload

- **Batch** scoring runs on a schedule over large datasets; simplest to operate, tolerant of latency, ideal for reports and periodic decisions.
- **Online (real-time)** serving responds to individual requests within tight latency budgets; needs low-latency feature retrieval and careful capacity planning.
- **Streaming** scores events continuously as they arrive; suits fraud detection and monitoring where freshness is critical.
- **Edge** runs models on devices or on-premises hardware for latency, privacy, connectivity, or data-sovereignty reasons, common in government and field settings.

Pick the simplest pattern that meets the requirement, and design your rollout with shadow deployments, canaries, and instant rollback.

### Monitor for drift, degradation, and data quality

Instrument inputs and outputs in production. Watch for **data drift** (input distributions shifting), **[concept drift](https://en.wikipedia.org/wiki/Concept_drift)** (the relationship between inputs and the target changing), **data quality** failures (nulls, schema changes, broken upstream sources), and **performance degradation** measured against delayed ground truth where you have it. Set alert thresholds, write runbooks, and wire monitoring to your retraining triggers. Silent degradation is the classic ML failure mode, and monitoring is your only defence against it.

## Trade-offs: pros and cons

| Decision | Option A | Option B | Trade-off |
|---|---|---|---|
| Serving pattern | Batch | Online | Simplicity and cost versus freshness and latency |
| Feature computation | Feature store | Per-model pipelines | Consistency and reuse versus setup overhead |
| Platform | Buy a managed MLOps platform | Assemble open-source tools | Speed and support versus flexibility and lock-in |
| Retraining | Scheduled | Triggered by drift | Predictability versus responsiveness and complexity |
| Reproducibility rigour | Full data versioning | Lightweight tracking | Audit strength versus storage and effort |

The overarching trade-off is investment now versus fragility later. Heavy reproducibility and monitoring infrastructure cost effort up front, but they prevent the far larger cost of unexplainable failures, unreproducible models, and eroded trust. Managed platforms speed teams up but can create lock-in; open-source stacks offer control at the price of integration work. Large organizations usually benefit from a shared platform team that hides this complexity behind paved-road defaults.

## Questions to discuss with your team

1. **How would we learn that a deployed model has silently degraded before a customer or citizen is harmed, and who owns that alert?** Silent decay is the classic ML failure mode: the code still runs, the model still returns confident scores, and quality slides as the world drifts from the training data. For a large team running many models, you need this answered per model, not once for the fleet, because each has its own drift profile and its own ground-truth delay. Bring your current monitors for data drift, concept drift, and data-quality breaks, the alert thresholds, and the runbook that says who responds. In regulated settings where labels arrive weeks late, discuss proxy signals you can watch in the meantime, because waiting for delayed ground truth means waiting to discover harm. If no single owner is named for a model's drift alert, that model is effectively unmonitored.

2. **If an auditor asked us to reproduce a specific prediction from eighteen months ago, could we actually do it end to end?** Reproducibility is the compliance requirement hiding inside good engineering: it lets an agency answer exactly which model, trained on which data, with which code, produced a decision that affected someone. Bring a real example and try to trace it: the immutable data snapshot, the git commit, the locked dependencies and container image, the recorded seeds, and the lineage from raw data through features to the deployed model. The signal is whether any link in that chain is missing or manual. For government and regulated industries, decide the retention period the law actually requires and confirm your storage keeps lineage answerable for that whole window, since a gap turns a routine query into a forensic emergency.

3. **What is our rule for promoting a model to production and rolling it back, and is it enforced by the registry or only by trust?** Ungoverned promotion is how notebook experiments leak into production and how a bad model lingers because nobody can revert it cleanly. For many teams, the difference between mature and fragile is whether the model registry gates promotion with mandatory approval and evaluation, or whether an engineer can push weights by hand. Bring your current promotion path, your rollback mechanism, and evidence that shadow deployments or canaries actually run before full traffic. Discuss whether retraining is scheduled or drift-triggered, and whether retrained models pass validation gates before deployment, because retraining on live data without validation amplifies drift or poisoning. The answer should be enforced in the platform, not in a wiki page people are trusted to follow.

4. **Do we build our MLOps platform on open-source tools, buy a managed one, or blend the two, and who has weighed the lock-in?** This choice sets the ceiling on how fast every future model ships and how much control you keep over your data and pipelines. A managed platform gets teams to production quickly and carries support, but it can trap your feature definitions, lineage records, and model artefacts in a proprietary format you cannot easily leave; an assembled open-source stack keeps you portable at the price of real integration and maintenance labour. Bring the total cost of ownership for each path (license or build, storage, compute for retraining, and the platform staff to operate it), an honest read on your team's capacity to run infrastructure, and a concrete exit test: could you export your registry, feature store, and lineage and rebuild elsewhere? In enterprise and government settings, add procurement constraints and data-sovereignty rules, since a platform that stores training data in a region or format your regulator forbids is disqualified no matter how convenient it is.

5. **Should our feature store and model registry be one centralized platform or federated per team, and what does training-serving skew cost us today?** Centralizing feature definitions eliminates the skew where a feature is computed one way in training and another way in serving, which is a silent and expensive source of accuracy loss, but a single platform can become a bottleneck that slows every team. Federating gives teams autonomy while multiplying the plumbing and the chances that two teams define the same feature inconsistently. Bring evidence of where skew has already bitten you, how many teams reuse features versus rebuild them, and the paved-road defaults a shared platform team could offer. For a large organization, weigh the governance benefit of one auditable system of record against the delivery cost of a central queue, and in regulated settings favour the centralized lineage that lets an auditor trace any prediction to the exact feature code that produced it.

6. **Have we matched each model's deployment pattern to its real latency, freshness, and sovereignty needs, or defaulted everything to one shape?** Batch, online, streaming, and edge each carry very different operational cost and complexity, and picking the wrong one either overspends on real-time infrastructure a nightly report never needed or starves a fraud scorer of the freshness it depends on. Decide per workload which pattern the requirement actually justifies, and resist standardizing on the most complex option because it feels modern. Bring the latency budget, the volume, the cost of a stale answer, and the ground-truth delay for each model. In government and field settings, weigh edge and on-premises deployment deliberately, because data-sovereignty rules or intermittent connectivity may force models onto local hardware, and that choice reshapes how you version, monitor, and roll back every model you push there.

## Sector lens

**Startup.** Your scarcest resource is engineering attention, so keep MLOps lightweight and buy it. Track experiments in a simple hosted tool, pin each deployed model to its training data snapshot and code commit in git, and add one cheap drift check rather than a platform. Skip the feature store and bespoke pipelines until a second or third model makes the reuse worth it; a fragile stack you cannot maintain will sink you faster than a missing capability.

**Small business.** You likely have no ML platform specialist and a tight budget, so treat MLOps as something embedded in the tools you already run rather than a system you staff. Prefer a managed service that handles versioning, deployment, and monitoring for you, and frame the discipline as a data-hygiene and reproducibility question: know which model and data produced a given result, and keep the ability to roll back. Favour vendors who let you export your data and models so a later switch stays possible.

**Enterprise.** The problem is scale across dozens of models and many teams: a shared feature store, experiment tracking, and a model registry with governed promotion so groups stop reinventing pipelines. Budget a platform team that offers paved-road defaults, standardize lineage and monitoring so every model is auditable and every incident explainable, and manage build-versus-buy and lock-in deliberately behind an interface that keeps the underlying tools swappable. Enforce validation gates and rollback in the platform, not in convention.

**Government.** Reproducibility, lineage, and versioning are compliance requirements in disguise, so treat them as first-class from day one. Version the exact dataset and code behind every deployed model, retain that lineage for the legally required period, and be able to reproduce any historical prediction that affected a citizen. Keep a human reviewing consequential decisions, weigh edge and on-premises deployment where data-sovereignty rules demand it, and require that any vendor platform grant full portability of your data, features, and lineage.

## Examples

**Startup.** A small analytics startup shipped its first churn-prediction model with one data scientist and a lightweight setup. It tracked experiments in a simple hosted tool, pinned each deployed model to its training data snapshot and code commit in git, and added a basic weekly job that compared recent inputs against the training distribution. When a data source changed its date format and predictions started drifting, that simple check caught it in days rather than after an angry customer call, and the team could reproduce the last good model and roll back.

**Enterprise.** A retail bank runs dozens of credit and fraud models. It standardized on a feature store shared across teams, an experiment-tracking service, and a model registry with mandatory approval gates. Every model in production traces back to its training data snapshot and code commit. Fraud models deploy as streaming scorers; credit models run in batch. A monitoring layer watches input drift and alerts when a data source schema changes, which once caught a broken upstream feed before it corrupted decisions.

**Government.** A public benefits agency uses an ML model to prioritize case reviews. Because those decisions affect citizens' access to services, the agency versions the exact dataset and code behind every deployed model, keeps this lineage for the legally required period, and can reproduce any historical prediction on demand. Models deploy in batch with a human reviewing flagged cases, and a drift monitor forces a mandatory re-evaluation whenever the incoming population shifts, so the model is never quietly applied outside the conditions it was validated for.

## Business case: motivations, ROI, and TCO

MLOps pays for itself by turning fragile experiments into dependable assets. ROI comes from faster time-to-production for new models, fewer costly incidents, less duplicated infrastructure, and the ability to operate many models with a small platform team. A shared feature store and registry can cut per-model delivery time dramatically, because teams stop rebuilding the same plumbing.

TCO covers platform build or license, storage for versioned data and models, compute for retraining, and the staff to operate it all. Weigh that against the cost of not adopting: models you cannot reproduce or audit, silent failures that harm customers or citizens, and regulatory findings. In regulated settings, the cost of an unexplainable model in an audit can dwarf the entire MLOps investment. Make the case to leadership by framing MLOps as risk reduction and delivery acceleration, not overhead: a paved road that every future model will travel.

## Anti-patterns and pitfalls

- **Notebook-to-production leaps.** Deploying models trained in ungoverned notebooks with no reproducibility.
- **Training-serving skew.** Different feature code in training and serving, causing silent accuracy loss.
- **No data versioning.** Versioning code but not data, so runs cannot be reproduced.
- **Deploy and forget.** Shipping a model with no monitoring, discovering degradation only when users complain.
- **Retraining on autopilot.** Automatically retraining on live data without validation, amplifying drift or poisoning.
- **One-off infrastructure.** Every team building its own pipeline, multiplying cost and fragility.
- **Ignoring delayed labels.** Assuming you can measure accuracy instantly when ground truth arrives weeks later.

## Maturity model

1. **Initiate.** Models built ad hoc in notebooks; manual deployment; no versioning of data or models; no monitoring; reproducing a past prediction is guesswork.
2. **Develop.** Some experiment tracking and a model registry appear, but practices vary by team; deployment is semi-automated; basic monitoring covers a few models; data versioning is partial and lineage has gaps.
3. **Standardize.** A shared platform with a feature store, registry, reproducible pipelines, and end-to-end lineage is documented and enforced org-wide; monitoring for drift and data quality runs across models; promotion and rollback follow a governed path every team uses.
4. **Manage.** The fleet is measured against baselines: drift rates, data-quality breaks, model accuracy against delayed ground truth, training-serving skew, time-to-production, and per-model operating cost are tracked as metrics; alert thresholds and validation gates are enforced on evidence, and each model's health is reviewed on a fixed cadence with a named owner.
5. **Orchestrate.** The lifecycle is fully automated, auditable, and adaptive; drift-triggered retraining runs behind validation gates; self-service paved roads let teams ship safely; continuous evaluation ties model performance to business metrics, and the platform integrates with delivery, risk, and compliance so models are routinely retired, replaced, and re-scoped as data and conditions shift.

## Ideas for discussion

- How do you balance experimentation freedom with production reproducibility?
- What is the right retraining trigger (schedule, drift, or performance decay) for your use cases?
- How long must you retain data and model lineage, and what drives that requirement?
- Should feature stores and registries be centralized platforms or federated per team?
- How do you monitor accuracy when ground-truth labels arrive with long delays?
- When is edge deployment worth its added operational complexity?

## Key takeaways

- ML behaviour comes from code plus data plus models; version and govern all three together.
- Feature stores, experiment tracking, and registries are the backbone of reproducible ML.
- Lineage makes models auditable and incidents explainable: essential in regulated settings.
- Choose batch, online, streaming, or edge to match latency, freshness, and sovereignty needs.
- Models degrade; monitoring for drift, data quality, and decay is not optional.

## References and further reading

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson, and Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
