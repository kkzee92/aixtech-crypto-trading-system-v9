# Cyber & Data Security Architecture

## Threat Model (High Level)
- API key leakage
- Data poisoning of market feeds
- Unauthorized signal generation or risk gate bypass
- Secret exposure in logs or commits
- Supply-chain attacks on dependencies

## Controls
| Control | Implementation | Status |
|---------|----------------|--------|
| Least privilege | Separate modules for ingest, strategy, risk | Implemented |
| Secrets via env | `os.environ` only; never in code | Enforced by policy |
| Input validation | Pydantic/schema checks on all external data | Stub |
| Audit logging | Structured logs for every signal and risk decision | Stub |
| Anomaly detection | Simple statistical bounds on price/volume | Stub |
| Secret scanning | gitleaks in CI | Configured |
| Dependency hygiene | Dependabot + licence allow-list | Recommended |
| Encryption | TLS for transit; recommend at-rest for persisted data | Documented |

## Zero-Trust Principles Applied
- Never trust external data without validation
- Never trust a strategy to respect risk limits (risk engine is authoritative)
- Continuous verification via tests and CI gates
- Assume breach: design so that a compromised strategy cannot move funds (paper-only)

## Data Classification
- Public market data: low sensitivity
- Generated signals: medium (protect integrity)
- Any future user config: high (encrypt)

No personal data is processed.
