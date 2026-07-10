# ADR 0007: Use PostgreSQL for the ledger service

A worked example of an architecture decision record (ADR). See
[chapter 1.6, Decision records](../chapters/01-06-decision-records.md) for the
practice, and [chapter 12.3, Templates](../chapters/12-03-templates.md) for blank
templates.

- **Status:** Accepted
- **Date:** 2026-02-14
- **Deciders:** Payments platform team; reviewed by the architecture group
- **Supersedes:** none

## Context

The new ledger service records financial transactions and must support strong
consistency, complex queries for reconciliation, and a clear audit trail. We
expect moderate write volume (hundreds of transactions per second at peak) and a
retention requirement measured in years. The team has deep SQL experience and a
regulatory obligation to demonstrate data integrity.

## Decision

We will use PostgreSQL as the primary store for the ledger service. We will model
transactions in a normalized schema, use serializable isolation for
balance-affecting operations, and keep an append-only journal table for the audit
trail.

## Alternatives considered

- **A document database.** Flexible schema, but weaker fit for the relational
  integrity and reconciliation queries the ledger needs. Rejected.
- **A managed cloud ledger service.** Attractive audit features, but it would
  increase jurisdictional exposure and lock-in for our most sensitive data.
  Rejected for this tier (see chapter 10.11, Digital sovereignty).

## Consequences

- We gain mature tooling, strong consistency, and a team that already knows the
  technology.
- We accept the operational work of running and scaling PostgreSQL, which the
  platform team will support with managed infrastructure as code.
- A follow-up ADR will cover the read-scaling approach if reporting load grows.

## Notes

- 2026-05-02: Reviewed one month on. The choice is holding up; reconciliation
  queries are fast enough without a read replica so far.
