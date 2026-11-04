# Agent Rules for AIxTech Crypto Trading System v9

This is the single source of truth for AI coding agents working on this repository.

## Core Principles
1. **Paper-only / research only.** Never implement live order execution, private key handling, or fund movement. Any execution code must be clearly marked as paper/simulation and gated.
2. **No secrets.** Never hard-code API keys, private keys, seed phrases, or credentials. Use environment variables or documented secret managers only.
3. **No production personal data.** Do not ingest, store, or log real customer data, KYC info, emails, phone numbers, or identifiers. Use synthetic fixtures only.
4. **Security first.** Prefer explicit, auditable controls. Follow least privilege. Document threat models for new components.
5. **Testable acceptance.** Every task must have clear acceptance criteria and corresponding tests.
6. **Disclosure.** AI-assisted changes must be noted in commit messages (`AI-Assisted: yes`) and in `docs/ai-disclosure-log.md` when significant.

## Forbidden
- Live trading clients that can place real orders
- Private key or wallet management code
- Hard-coded secrets or credentials of any kind
- Real personal or customer data in fixtures, tests, or docs
- Bypassing risk gates or position size limits

## Allowed
- Public market data clients (with injectable fetchers for offline tests)
- Strategy signal generation and backtesting on historical/synthetic data
- Risk calculation and paper portfolio simulation
- Security control stubs (encryption wrappers, audit loggers, anomaly detectors)

## Definition of Done
CI green (lint, tests, secret scan, data guard) + human review of security-sensitive changes.
