# Appendix C. Templates

These templates are copy-paste-ready starting points. Lift any template into your wiki, repository, or ticketing system and fill in the bracketed placeholders. Italicized notes and inline comments explain what belongs in each section; delete them once the section is filled. Keep templates lightweight: a template that is faster to skip than to complete will not be used. Adapt headings and sections to your organization, but preserve the intent of each part.

A few conventions used below:

- Text in `[square brackets]` is a placeholder to replace.
- Text in _italics_ or `<!-- comments -->` is guidance to delete.
- Keep the finished document as short as it can be while still answering its questions.

## Architecture Decision Record (ADR)

```markdown
# ADR [NNNN]: [Short title of the decision]

- Status: [Proposed | Accepted | Deprecated | Superseded by ADR-XXXX]
- Date: [YYYY-MM-DD]
- Deciders: [names or roles]
- Consulted: [names or roles]

## Context

<!-- What is the problem, force, or constraint driving this decision?
     State the facts and requirements neutrally. Include only what a
     future reader needs to understand why a decision was necessary. -->

## Decision

<!-- State the choice in one or two clear sentences: "We will ..." -->

## Alternatives considered

<!-- List the realistic options you weighed and why each was or was
     not chosen. At least two alternatives should appear here. -->

- Option A — [summary]; rejected because [reason].
- Option B — [summary]; rejected because [reason].
- Chosen option — [summary]; chosen because [reason].

## Consequences

<!-- Honest results of the decision, both good and bad. -->

- Positive: [benefits gained]
- Negative: [costs, risks, or limitations accepted]
- Follow-up: [migrations, new work, or decisions this triggers]

## Related

<!-- Links to prior ADRs, RFCs, tickets, or docs this relates to. -->
```

## RFC / design doc

```markdown
# RFC: [Title]

- Author(s): [names]
- Status: [Draft | In review | Approved | Rejected | Implemented]
- Reviewers: [names or roles]
- Created: [YYYY-MM-DD]
- Last updated: [YYYY-MM-DD]
- Ticket / tracking: [link]

## Summary

<!-- One paragraph: what this proposes and why it matters. A reader
     should grasp the essence from this section alone. -->

## Problem and motivation

<!-- What problem are we solving? Who is affected? What happens if we
     do nothing? Include relevant background and constraints. -->

## Goals and non-goals

- Goals: [what success looks like, measurable where possible]
- Non-goals: [explicitly out of scope, to prevent scope creep]

## Proposed design

<!-- The core of the document. Describe the approach, architecture,
     data model, interfaces, and key flows. Use diagrams where they
     clarify. Explain how it works, not just what it is. -->

## Alternatives considered

<!-- Other approaches and why they were not chosen. Shows the reader
     the design space was explored. -->

## Impact and risks

- Security and privacy: [implications and mitigations]
- Performance and scale: [expected load and behavior]
- Operability: [monitoring, failure modes, rollout, rollback]
- Cost: [infrastructure or licensing impact]
- Backward compatibility: [migration and deprecation]

## Testing and rollout plan

<!-- How the change will be validated and released safely. -->

## Open questions

<!-- Unresolved issues you want reviewers to weigh in on. -->
```

## Postmortem / incident review (blameless)

```markdown
# Postmortem: [Incident title]

- Incident ID: [ID]
- Date of incident: [YYYY-MM-DD]
- Authors: [names]
- Status: [Draft | Final]
- Severity: [SEV1 | SEV2 | SEV3]

> This review is blameless. We focus on systems and contributing
> factors, not on individuals. The goal is to learn and to prevent
> recurrence.

## Summary

<!-- Two or three sentences: what happened, the impact, and the
     resolution, readable by a non-expert. -->

## Impact

- Duration: [start time to recovery time, with timezone]
- Users affected: [scope and number]
- Business impact: [revenue, SLA, reputation, or other]

## Timeline

<!-- Timestamped, factual sequence of events. Include detection,
     escalation, key actions, and recovery. -->

- [HH:MM] [event]
- [HH:MM] [event]

## Contributing factors

<!-- The chain of conditions that led to the incident. Prefer
     "contributing factors" over a single root cause. -->

## Detection and response

- How was it detected? [alert, customer report, etc.]
- What helped the response?
- What slowed the response?

## What went well

<!-- Recognize effective actions and safeguards that worked. -->

## Action items

<!-- Specific, owned, and dated. Address prevention, detection, and
     mitigation. Track these in the normal backlog. -->

| Action | Owner | Due date | Type (prevent/detect/mitigate) | Ticket |
|--------|-------|----------|--------------------------------|--------|
| [action] | [name] | [date] | [type] | [link] |

## Lessons learned

<!-- What the wider organization should take away. -->
```

## Threat model (STRIDE-based)

```markdown
# Threat model: [System or feature name]

- Author(s): [names]
- Date: [YYYY-MM-DD]
- Reviewers: [security contact, owners]
- Scope: [what is and is not covered]

## System overview

<!-- Brief description of the system, its purpose, and its users. -->

## Assets

<!-- What is worth protecting: data, credentials, functionality,
     reputation. Note the sensitivity of each. -->

## Trust boundaries and data flow

<!-- Describe or diagram components, data stores, external entities,
     and the boundaries where trust changes. -->

## Threats (STRIDE)

<!-- For each element, consider the STRIDE categories. Record each
     credible threat, its risk, and the mitigation or accepted risk. -->

| Threat | STRIDE category | Affected element | Risk (L/M/H) | Mitigation | Status |
|--------|-----------------|------------------|--------------|------------|--------|
| [threat] | Spoofing | [element] | [risk] | [control] | [open/mitigated/accepted] |
| [threat] | Tampering | [element] | [risk] | [control] | [status] |
| [threat] | Repudiation | [element] | [risk] | [control] | [status] |
| [threat] | Information disclosure | [element] | [risk] | [control] | [status] |
| [threat] | Denial of service | [element] | [risk] | [control] | [status] |
| [threat] | Elevation of privilege | [element] | [risk] | [control] | [status] |

## Assumptions and dependencies

<!-- Security assumptions relied upon and external controls trusted. -->

## Open issues and follow-up

<!-- Threats needing further work, tracked as tickets. -->
```

## Runbook

```markdown
# Runbook: [Task or scenario name]

- Service: [service name]
- Owner: [team]
- Last reviewed: [YYYY-MM-DD]
- Related alerts: [alert names]

## Purpose

<!-- When to use this runbook and what it accomplishes. -->

## Prerequisites

<!-- Access, tools, and permissions needed before starting. -->

## Detection / symptoms

<!-- What the operator observes: alerts, error signatures, dashboards. -->

## Diagnosis

<!-- Step-by-step checks to confirm the problem and narrow the cause.
     Include the exact commands, queries, or dashboard links. -->

1. [step and expected result]
2. [step and expected result]

## Resolution

<!-- Concrete, ordered steps to fix or mitigate. Note any step that is
     risky or irreversible, and how to verify success. -->

1. [step]
2. [verify recovery]

## Rollback

<!-- How to undo the actions if resolution makes things worse. -->

## Escalation

<!-- Who to contact and when to escalate. Secondary on-call, owning
     team, and vendor contacts. -->

## References

<!-- Dashboards, related runbooks, architecture docs. -->
```

## Service README / service catalog entry

```markdown
# [Service name]

- Owner team: [team]
- On-call: [rotation link]
- Tier / criticality: [Tier 1 | 2 | 3]
- Repository: [link]
- Status: [Active | Deprecated]

## What it does

<!-- One paragraph on the service's responsibility and its consumers. -->

## Architecture

<!-- Key components, dependencies (upstream and downstream), and a
     link to the design doc or diagram. -->

## Interfaces

- APIs / endpoints: [link to spec]
- Events published / consumed: [topics]
- Data stores: [databases, caches, buckets]

## Runtime and deployment

- Environments: [dev, staging, prod]
- How to deploy: [pipeline link and process]
- Configuration and feature flags: [where and how]

## Observability

- Dashboards: [links]
- Alerts: [links]
- Logs: [where to find them]
- SLOs: [link]

## Operations

- Runbooks: [links]
- Common tasks: [scaling, restart, backfill]
- Known issues and limitations: [notes]

## Getting started (for new contributors)

<!-- How to build, test, and run locally. -->

## Contacts

- Slack / chat channel: [link]
- Escalation: [path]
```

## SLO / error-budget policy

```markdown
# SLO and error-budget policy: [Service or journey name]

- Owner: [team]
- Effective date: [YYYY-MM-DD]
- Review cadence: [e.g. quarterly]

## Service level indicators (SLIs)

<!-- Define each SLI precisely: the measured quantity, how it is
     measured, and from where (ideally the user's perspective). -->

| SLI | Definition | Data source |
|-----|-----------|-------------|
| Availability | [e.g. successful requests / total requests] | [source] |
| Latency | [e.g. proportion of requests under Xms] | [source] |

## Objectives (SLOs)

| SLI | Target | Measurement window |
|-----|--------|--------------------|
| Availability | [e.g. 99.9%] | [e.g. rolling 28 days] |
| Latency | [e.g. 95% under 300ms] | [rolling 28 days] |

## Error budget

<!-- The allowed unreliability: 100% minus the target, over the
     window. State the budget in concrete terms (e.g. minutes/month). -->

- Budget: [derived allowance]

## Policy when the budget is exhausted

<!-- The agreed consequences. Make them concrete and enforceable. -->

- [e.g. Freeze non-critical feature releases until the budget recovers.]
- [e.g. Prioritize reliability work in the next planning cycle.]
- [e.g. Escalate to engineering leadership if breached two windows running.]

## Policy when the budget is healthy

<!-- What extra risk the team may take, e.g. faster rollouts. -->

## Alerting

<!-- Burn-rate alerts and thresholds tied to this SLO. -->
```

## Risk register entry

```markdown
## Risk: [Short risk title]

- Risk ID: [ID]
- Date raised: [YYYY-MM-DD]
- Owner: [name or role responsible for managing this risk]
- Category: [security | operational | compliance | financial | delivery | vendor]
- Status: [Open | Mitigating | Accepted | Closed]

### Description

<!-- State the risk as: cause -> event -> consequence. What could
     happen, and why it matters. -->

### Assessment

- Likelihood: [Low | Medium | High]
- Impact: [Low | Medium | High]
- Overall rating: [derived from likelihood x impact]

### Current controls

<!-- What already reduces this risk today. -->

### Mitigation plan

<!-- Planned actions to reduce likelihood or impact, with owners and
     dates. If accepting the risk, record who accepted it and why. -->

| Action | Owner | Due date | Status |
|--------|-------|----------|--------|
| [action] | [name] | [date] | [status] |

### Review

- Next review date: [YYYY-MM-DD]
- Decision / notes: [any acceptance sign-off or change]
```

## Project one-pager / product brief

```markdown
# [Project or product name] — one-pager

- Sponsor: [name]
- Lead: [name]
- Date: [YYYY-MM-DD]
- Status: [Idea | Approved | In progress | Shipped]

## Problem

<!-- One paragraph: the customer or business problem, and evidence it
     is real and worth solving. -->

## Audience

<!-- Who has this problem and who benefits from solving it. -->

## Proposed solution

<!-- A short description of what we will build or change. Keep it at
     the level of intent, not implementation detail. -->

## Why now

<!-- The reason to do this now rather than later. -->

## Success metrics

<!-- How we will know it worked. Prefer measurable outcomes. -->

- [metric and target]

## Scope

- In scope: [what we will do]
- Out of scope: [what we will not do]

## Risks and open questions

<!-- Main uncertainties and dependencies. -->

## Rough plan and milestones

<!-- High-level phases and approximate timing. -->

## Cost and resources

<!-- People, time, and budget required. -->
```

## On-call handoff notes

```markdown
# On-call handoff: [YYYY-MM-DD]

- Outgoing: [name]
- Incoming: [name]
- Service(s): [names]

## Overall status

<!-- One line: quiet, noisy, or ongoing issue. -->

## Open incidents

<!-- Any active or recently resolved incidents the next responder
     must know about, with links. -->

- [incident, status, and what remains]

## Ongoing or planned changes

<!-- Deploys, migrations, maintenance windows, or experiments in
     flight that could cause alerts. -->

## Noisy or flaky alerts

<!-- Alerts that fired and their real meaning, so the next person is
     not misled. Note any temporary silences and their expiry. -->

## Watch items

<!-- Metrics or systems trending in a concerning direction. -->

## Pending follow-ups

<!-- Tasks handed to the next shift, with links to tickets. -->

## Notes

<!-- Anything else useful: access quirks, vendor issues, context. -->
```

## Change request (for regulated change control)

```markdown
# Change request: [Change title]

- Change ID: [ID]
- Requester: [name]
- Date submitted: [YYYY-MM-DD]
- Type: [Standard | Normal | Emergency]
- Priority: [Low | Medium | High]
- Status: [Submitted | Approved | Rejected | Implemented | Closed]

## Description of change

<!-- What is changing and why. Reference the ticket or requirement. -->

## Systems and components affected

<!-- Services, data, environments, and users impacted. -->

## Justification and business impact

<!-- The reason for the change and the impact of not doing it. -->

## Risk assessment

- Risk level: [Low | Medium | High]
- Potential impact if the change fails: [description]
- Impact on security, privacy, or compliance: [description]

## Implementation plan

<!-- Ordered steps, responsible parties, and timing. -->

## Test and validation plan

<!-- How success will be verified before and after the change. -->

## Backout / rollback plan

<!-- How to reverse the change if it fails, and the recovery time. -->

## Schedule

- Proposed window: [start and end, with timezone]
- Expected downtime: [duration or none]

## Approvals

| Role | Name | Decision | Date |
|------|------|----------|------|
| Change owner | [name] | [approve/reject] | [date] |
| Technical reviewer | [name] | [approve/reject] | [date] |
| Change advisory board | [name] | [approve/reject] | [date] |

## Post-implementation review

<!-- Outcome, issues encountered, and whether backout was needed. -->
```

## Data Protection Impact Assessment (DPIA) outline

```markdown
# Data Protection Impact Assessment: [Processing activity name]

- Assessor: [name]
- Date: [YYYY-MM-DD]
- Reviewers: [DPO / privacy contact]
- Status: [Draft | Reviewed | Approved]

## 1. Description of the processing

<!-- What personal data is processed, how, by whom, and for what
     purpose. Include data flows from collection to deletion. -->

- Data subjects: [who the data is about]
- Data categories: [types of personal data, note any special categories]
- Purposes: [why the data is processed]
- Recipients and processors: [who receives or handles the data]
- Retention period: [how long data is kept and deletion method]
- International transfers: [destinations and transfer mechanism]

## 2. Necessity and proportionality

<!-- Is the processing necessary for the purpose? Is it the least
     intrusive option? What is the lawful basis or authority? -->

- Lawful basis / authority: [basis for each purpose]
- Data minimization: [why each field is necessary]
- Accuracy and retention justification: [notes]
- How data subject rights are supported: [access, deletion, etc.]

## 3. Consultation

<!-- Stakeholders, and where relevant data subjects, consulted. -->

## 4. Risks to individuals

<!-- Identify privacy risks and rate each. -->

| Risk to individuals | Likelihood | Severity | Overall |
|---------------------|-----------|----------|---------|
| [e.g. unauthorized access to sensitive data] | [L/M/H] | [L/M/H] | [rating] |

## 5. Measures to reduce risk

<!-- For each risk, the mitigation and residual risk after it. -->

| Risk | Measure | Residual risk | Accepted by |
|------|---------|---------------|-------------|
| [risk] | [control] | [L/M/H] | [name] |

## 6. Outcome and sign-off

- Residual risk acceptable: [Yes | No]
- Measures approved by: [name, role]
- Consultation with supervisory authority required: [Yes | No]
- Review date: [YYYY-MM-DD]
```
