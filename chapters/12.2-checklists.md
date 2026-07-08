# 12.2 Checklists

These checklists are practical, ready-to-use quick references. Copy any checklist into a pull request template, a wiki page, a ticket, or a review meeting agenda, and adapt the items to your context. Treat each item as something a person can verify and answer yes or no. A checklist is a memory aid and a shared standard, not a substitute for judgment; delete items that do not apply and add items your domain requires.

Guidance for using these well:

- Keep checklists short enough that people actually complete them. If a checklist is routinely skipped, it is too long or too generic.
- Automate any item a machine can verify (formatting, tests, scans) so humans spend attention on judgment items.
- Version your checklists and review them periodically. A checklist that never changes is probably not being used.
- Distinguish blocking items from advisory items when the distinction matters for your process.

## Code review checklist

For the reviewer examining someone else's change.

- [ ] The change does what its description and linked ticket say it does.
- [ ] The scope is focused on a single logical concern; unrelated changes are split out.
- [ ] The design fits the existing architecture and does not introduce a simpler-to-avoid coupling.
- [ ] Edge cases, error paths, and failure modes are handled, not just the happy path.
- [ ] Tests exist, are meaningful, and would fail if the behavior regressed.
- [ ] Naming, structure, and comments make the code understandable to a future reader.
- [ ] No secrets, credentials, tokens, or personal data are committed.
- [ ] Security-sensitive input is validated, encoded, or parameterized appropriately.
- [ ] Public interfaces, contracts, and backward compatibility are preserved or intentionally versioned.
- [ ] Logging, metrics, and error reporting are adequate to operate the change in production.
- [ ] Documentation, runbooks, and configuration are updated to match the change.
- [ ] Feedback is separated into blocking issues versus suggestions, and phrased about the code.

## Pull request author checklist

For the author before requesting review.

- [ ] The PR is small and focused enough to review carefully in one sitting.
- [ ] The description states what changed, why, and how it was verified.
- [ ] The linked ticket, issue, or design doc gives reviewers the necessary context.
- [ ] All automated checks pass locally or in CI (build, lint, format, tests, scans).
- [ ] New and changed behavior is covered by tests.
- [ ] Mechanical refactors are separated from behavior changes.
- [ ] Self-review is complete: you have read your own diff line by line.
- [ ] No debug code, commented-out blocks, secrets, or stray files remain.
- [ ] Database migrations, feature flags, and config changes are documented and reversible.
- [ ] Breaking changes are called out explicitly with a migration path.
- [ ] Screenshots, recordings, or sample output are included where they aid review.
- [ ] The right reviewers and any required role-based approvers are requested.

## Definition of Done

The shared standard a work item must meet before it is considered complete.

- [ ] Acceptance criteria in the ticket are all met and demonstrable.
- [ ] Code is peer reviewed and approved by the required reviewers.
- [ ] Automated tests are written, passing, and merged with the change.
- [ ] Code is merged to the mainline and deploys cleanly through the pipeline.
- [ ] No known defects of the agreed severity threshold remain open.
- [ ] Documentation, help text, and runbooks are updated.
- [ ] Observability is in place: relevant logs, metrics, and alerts exist.
- [ ] Security and privacy implications have been considered and addressed.
- [ ] Accessibility requirements for the change are met where user-facing.
- [ ] Feature flags are configured and the rollout plan is agreed.
- [ ] The product owner or stakeholder has accepted the outcome.
- [ ] Any follow-up work is captured as tracked tickets, not left implicit.

## Production launch / go-live readiness

Before shipping a significant change or new service to production.

- [ ] Rollout plan is documented, including staged or canary steps and success criteria.
- [ ] Rollback plan is documented, tested, and can be executed quickly.
- [ ] Capacity and load testing show the system meets expected and peak demand.
- [ ] Monitoring, dashboards, and alerts are live and validated before launch.
- [ ] On-call coverage is scheduled and the responders know the system.
- [ ] Runbooks exist for the most likely failure and operational scenarios.
- [ ] Dependencies, integrations, and third parties are confirmed ready and rate limits understood.
- [ ] Security review and required sign-offs are complete.
- [ ] Data migration, if any, is tested end to end with a verified backout.
- [ ] Feature flags allow disabling the change without a redeploy.
- [ ] Legal, privacy, and compliance approvals are obtained where required.
- [ ] Communications plan covers stakeholders, support, and customers.
- [ ] A go/no-go decision is made by named owners against explicit criteria.

## Security review / threat-model checklist

For assessing the security posture of a change or system.

- [ ] Trust boundaries and data flows are identified and documented.
- [ ] Authentication is enforced on every entry point that requires it.
- [ ] Authorization checks enforce least privilege for every action and resource.
- [ ] All external input is validated, and output is encoded for its sink.
- [ ] Secrets are stored in a managed vault, never in code or config, and are rotatable.
- [ ] Data is encrypted in transit and at rest as the classification requires.
- [ ] Dependencies are scanned for known vulnerabilities and kept current.
- [ ] Injection, deserialization, and SSRF risks are mitigated for untrusted input.
- [ ] Security-relevant events are logged without recording sensitive data.
- [ ] Rate limiting, quotas, and abuse protections guard exposed endpoints.
- [ ] Error messages do not leak stack traces, internals, or sensitive detail.
- [ ] Threats identified via STRIDE or similar are recorded with mitigations or accepted risk.
- [ ] Security testing (SAST, DAST, or penetration testing) is planned or complete.

## Privacy and data-protection (DPIA-style) checklist

For processing that involves personal or sensitive data.

- [ ] The personal data collected is inventoried, classified, and minimized to what is needed.
- [ ] The lawful basis or authority for each processing purpose is documented.
- [ ] Purpose limitation is enforced: data is used only for the stated purposes.
- [ ] Retention periods are defined and deletion or anonymization is automated.
- [ ] Data subject rights (access, correction, deletion, portability) can be fulfilled.
- [ ] Consent, where relied upon, is freely given, specific, and revocable.
- [ ] Third parties and processors are bound by adequate data-protection terms.
- [ ] Cross-border transfers have an appropriate legal transfer mechanism.
- [ ] Access to personal data is restricted, logged, and reviewed.
- [ ] Privacy risks to individuals are assessed and mitigated or escalated.
- [ ] Data breach detection and notification processes are defined.
- [ ] Privacy by design and default choices are documented for the feature.
- [ ] The data protection officer or privacy reviewer has signed off where required.

## Accessibility (WCAG) checklist

For user-facing interfaces, aligned to WCAG principles.

- [ ] All content is reachable and operable using only a keyboard.
- [ ] Focus order is logical and a visible focus indicator is present.
- [ ] Text color contrast meets the target ratio (typically 4.5:1 for body text).
- [ ] Images and non-text content have meaningful alternative text.
- [ ] Form fields have associated labels and clear error messages.
- [ ] Headings, landmarks, and structure are marked up semantically.
- [ ] Interactive components expose correct name, role, and state to assistive tech.
- [ ] Content reflows and remains usable at 200% zoom and on small screens.
- [ ] Time limits are adjustable, and motion or auto-playing content can be paused.
- [ ] Color is not the only means of conveying information.
- [ ] Media has captions and, where needed, transcripts or audio description.
- [ ] The interface is tested with a screen reader and automated accessibility tooling.

## API design review checklist

Before publishing or changing an API.

- [ ] Resource and operation naming is consistent and predictable.
- [ ] The contract is specified in a machine-readable schema (for example OpenAPI).
- [ ] Versioning strategy is defined and backward compatibility is preserved or managed.
- [ ] Pagination, filtering, and sorting follow consistent conventions.
- [ ] Error responses use consistent structure, codes, and actionable messages.
- [ ] Authentication and authorization are specified for every operation.
- [ ] Input validation and size limits are defined and enforced.
- [ ] Idempotency is defined for operations where retries are expected.
- [ ] Rate limits, quotas, and throttling behavior are documented.
- [ ] Timeouts, retries, and failure semantics are clear to clients.
- [ ] Sensitive data exposure in responses is minimized and justified.
- [ ] Documentation includes examples for each operation and error case.
- [ ] Deprecation policy and sunset timelines are defined.

## Architecture decision (ADR) review checklist

For reviewing a proposed architecture decision record.

- [ ] The context and problem being solved are stated clearly.
- [ ] The decision is stated unambiguously as a single choice.
- [ ] At least two realistic alternatives were considered and compared.
- [ ] Consequences, both positive and negative, are documented.
- [ ] Non-functional impacts (performance, security, cost, operability) are addressed.
- [ ] The decision aligns with existing principles and prior ADRs, or supersedes them explicitly.
- [ ] Affected teams and stakeholders were consulted.
- [ ] The reversibility and cost of change are assessed.
- [ ] Assumptions and constraints are made explicit.
- [ ] The status (proposed, accepted, superseded) is set and dated.
- [ ] The decision is discoverable and linked from relevant systems.
- [ ] Any follow-up actions or migrations are captured as tracked work.

## Incident response checklist

During an active production incident.

- [ ] Declare the incident and assign a single incident commander.
- [ ] Assess and communicate severity, scope, and customer impact.
- [ ] Open a dedicated communication channel and incident record.
- [ ] Assign clear roles: commander, communications lead, and operations lead.
- [ ] Prioritize mitigation and restoring service over root-cause analysis.
- [ ] Post regular status updates to stakeholders on a set cadence.
- [ ] Capture a timeline of events, actions, and decisions as they happen.
- [ ] Escalate to additional responders or vendors when needed.
- [ ] Notify legal, security, and compliance if data or regulation is involved.
- [ ] Verify the fix and confirm the system has fully recovered.
- [ ] Formally close the incident and communicate resolution.
- [ ] Schedule the blameless postmortem before people disperse.

## Postmortem checklist

For the retrospective review after an incident.

- [ ] The review is blameless and focuses on systems and contributing factors.
- [ ] A factual, timestamped timeline of the incident is documented.
- [ ] Customer and business impact is quantified (duration, scope, cost).
- [ ] Detection is analyzed: how and when the issue was noticed.
- [ ] Response is analyzed: what helped and what slowed recovery.
- [ ] Contributing causes are identified, not just a single root cause.
- [ ] What went well is recorded, as well as what went wrong.
- [ ] Action items are specific, assigned to owners, and have due dates.
- [ ] Action items address prevention, detection, and mitigation.
- [ ] Follow-up items are tracked to completion in the normal backlog.
- [ ] The postmortem is shared broadly so others can learn from it.
- [ ] Systemic patterns across incidents are reviewed periodically.

## On-call readiness checklist

Before someone takes an on-call shift.

- [ ] The responder has access to all systems, dashboards, and tools they need.
- [ ] Alerting reaches the responder reliably and is tested.
- [ ] Escalation paths and secondary on-call contacts are known and current.
- [ ] Runbooks exist for the most common and most severe alerts.
- [ ] The responder has completed onboarding or shadowing for these systems.
- [ ] Recent changes, ongoing incidents, and known issues are handed off.
- [ ] Alert thresholds are tuned to minimize noise and false pages.
- [ ] The responder knows how to declare an incident and reach the commander.
- [ ] Access to production is possible from the responder's working environment.
- [ ] Communication channels and stakeholder contacts are documented.
- [ ] The on-call schedule is published and coverage has no gaps.
- [ ] Compensation, expectations, and workload limits for on-call are clear.

## SLO definition checklist

When defining a service level objective.

- [ ] The user journey or capability the SLO protects is clearly identified.
- [ ] Service level indicators (SLIs) are defined as clear, measurable quantities.
- [ ] SLIs are measured from the user's perspective where possible.
- [ ] The objective target is set at a level users actually need, not 100%.
- [ ] The measurement window (for example rolling 28 days) is specified.
- [ ] The error budget derived from the target is calculated and understood.
- [ ] A policy defines what happens when the error budget is exhausted.
- [ ] Data sources for the SLIs are reliable and instrumented.
- [ ] Alerting is tied to burn rate, not just threshold breaches.
- [ ] Owners and stakeholders agree the SLO is realistic and meaningful.
- [ ] The SLO is documented and visible on a dashboard.
- [ ] A schedule exists to review and revise SLOs as the service evolves.

## CI/CD pipeline checklist

For a continuous integration and delivery pipeline.

- [ ] Every commit triggers an automated build and test run.
- [ ] The pipeline fails fast and reports results clearly to authors.
- [ ] Linting, formatting, and static analysis run automatically.
- [ ] Unit, integration, and relevant end-to-end tests run in the pipeline.
- [ ] Security and dependency scanning run on every build.
- [ ] Build artifacts are versioned, immutable, and stored in a registry.
- [ ] Secrets are injected securely and never printed in logs.
- [ ] Deployments are automated and repeatable across environments.
- [ ] Deployment strategy (canary, blue-green, rolling) is defined and used.
- [ ] Rollback is automated or a single documented action.
- [ ] Pipeline permissions follow least privilege and are auditable.
- [ ] Pipeline configuration is stored in version control as code.
- [ ] Build provenance and a software bill of materials are produced where required.

## Infrastructure-as-code review checklist

For reviewing infrastructure defined as code.

- [ ] Changes are expressed entirely in code and applied through the pipeline.
- [ ] A plan or dry-run output is reviewed before apply.
- [ ] State is stored securely with locking to prevent concurrent changes.
- [ ] Resources follow naming, tagging, and ownership conventions.
- [ ] Least-privilege IAM roles and policies are used, with no wildcards where avoidable.
- [ ] Network exposure is minimized; no unintended public access.
- [ ] Secrets and sensitive values are referenced from a vault, not hardcoded.
- [ ] Encryption is enabled for storage, databases, and transit.
- [ ] Changes are idempotent and safe to re-apply.
- [ ] Blast radius is understood; destructive changes are called out.
- [ ] Cost impact of the change is considered.
- [ ] Modules are reusable, versioned, and tested.
- [ ] Drift detection is in place to catch out-of-band changes.

## AI/ML model release checklist

Before releasing a machine learning model to production.

- [ ] The model's intended use, scope, and limitations are documented.
- [ ] Training and evaluation data provenance, licensing, and consent are verified.
- [ ] Data and model are versioned and reproducible.
- [ ] Performance is evaluated on representative, held-out test data.
- [ ] Fairness and bias are assessed across relevant subgroups.
- [ ] The model is evaluated against the incumbent or a baseline.
- [ ] Failure modes, edge cases, and out-of-distribution behavior are understood.
- [ ] Safety, misuse, and harmful-output risks are assessed and mitigated.
- [ ] Monitoring for drift, data quality, and performance degradation is in place.
- [ ] A rollback or fallback to a previous model or rule-based path exists.
- [ ] Human oversight or appeal is provided for consequential decisions.
- [ ] Privacy review covers training data and inference inputs and outputs.
- [ ] A model card or equivalent documentation is published for stakeholders.

## Data pipeline quality checklist

For a data pipeline that feeds analytics or products.

- [ ] Source data schemas are validated and schema changes are detected.
- [ ] Ingestion handles late, duplicate, and out-of-order records correctly.
- [ ] Data quality checks (completeness, uniqueness, ranges) run automatically.
- [ ] Failed records are quarantined and surfaced, not silently dropped.
- [ ] Transformations are tested with representative and edge-case inputs.
- [ ] The pipeline is idempotent and safe to re-run after failure.
- [ ] Freshness and latency of outputs are monitored against expectations.
- [ ] Lineage is documented so consumers know where data comes from.
- [ ] Personal and sensitive data is classified, masked, or restricted appropriately.
- [ ] Backfills and reprocessing are supported and documented.
- [ ] Alerting notifies owners of failures and quality breaches.
- [ ] Retention and deletion policies are enforced on stored data.
- [ ] Downstream consumers and SLAs are documented.

## Open source intake and license review checklist

Before adopting an open source component.

- [ ] The component's license is identified and is on the approved list.
- [ ] License obligations (attribution, copyleft, notices) are understood and met.
- [ ] License compatibility with your distribution model is confirmed.
- [ ] The project is actively maintained and has a healthy community.
- [ ] Known vulnerabilities are checked and the version is current.
- [ ] The dependency and its transitive dependencies are inventoried.
- [ ] Security posture and past incident history are reviewed.
- [ ] The component fills a real need without significant duplication.
- [ ] The exit cost and replaceability of the component are considered.
- [ ] The component is recorded in the software bill of materials.
- [ ] A named owner is responsible for tracking updates and advisories.
- [ ] Contribution-back and internal-fork policies are followed if modified.

## Vendor / third-party risk checklist

Before onboarding an external vendor or service.

- [ ] The business need and data the vendor will access are clearly defined.
- [ ] The vendor's security posture is assessed (certifications, audits, questionnaire).
- [ ] Data processing terms, ownership, and deletion on exit are contractually clear.
- [ ] The vendor's subprocessors and data locations are disclosed and acceptable.
- [ ] Compliance with relevant regulations is verified.
- [ ] Uptime, support, and SLA commitments are documented.
- [ ] Breach notification obligations and timelines are in the contract.
- [ ] Access is scoped to least privilege and revocable.
- [ ] Business continuity and the impact of vendor failure are assessed.
- [ ] An exit and data-migration plan exists to avoid lock-in.
- [ ] Costs, renewal terms, and price-change clauses are understood.
- [ ] The vendor is added to the risk register with a review date.

## Government compliance (ATO / FedRAMP-style) readiness checklist

For systems requiring formal authorization to operate.

- [ ] The system boundary and data flows are defined and diagrammed.
- [ ] Data is categorized by impact level and sensitivity.
- [ ] The applicable control baseline is selected and tailored.
- [ ] A system security plan documents how each control is implemented.
- [ ] Controls are implemented, evidenced, and mapped to the plan.
- [ ] Continuous monitoring and vulnerability scanning are operational.
- [ ] A plan of action and milestones tracks open findings to remediation.
- [ ] Access control, audit logging, and identity management meet requirements.
- [ ] Encryption uses approved algorithms and validated modules.
- [ ] An incident response plan is documented and tested.
- [ ] A contingency and disaster recovery plan is documented and tested.
- [ ] An independent assessment or audit of controls is completed.
- [ ] The authorizing official has the risk assessment needed to grant authorization.
- [ ] Reauthorization triggers and the ongoing authorization cadence are defined.
