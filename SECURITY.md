# Security Policy

## Supported Versions
Only the `main` branch of this repository is actively maintained.

## Reporting a Vulnerability
Please open a private security advisory or contact the maintainer directly. Do not open public issues for vulnerabilities.

## Security Architecture Summary
This system follows zero-trust principles:

- **Identity & Access:** Least privilege modules. API keys loaded only from environment. No long-lived credentials in process memory where avoidable.
- **Data Protection:** Encryption in transit (TLS for all external calls). Encryption at rest recommended for any persisted signals or logs. Synthetic data only.
- **Secrets Management:** Environment variables or external secret stores. Never committed. gitleaks and pre-commit hooks recommended.
- **Monitoring & Audit:** Structured audit logging for all signal generation and risk decisions. Anomaly detection stubs for unusual data patterns.
- **Input Validation:** Strict schema validation on all external data. Reject malformed or suspicious payloads.
- **Risk Gates:** Hard-coded maximum position sizes, volatility filters, and kill-switches in the risk engine. Cannot be bypassed by strategies.

See [docs/security-architecture.md](docs/security-architecture.md) for the full threat model and controls.

## Disclosure
This is research software. No warranty. Use at your own risk.
