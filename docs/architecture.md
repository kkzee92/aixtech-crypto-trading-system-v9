# System Architecture

## High-Level Components
1. **Secure Ingestion Layer** – Public API clients with injectable fetchers, rate limiting, and schema validation.
2. **Processing & Feature Engineering** – Technical indicators, volume profiles, volatility regimes, relative strength. All offline-capable.
3. **Asset-Class Strategy Modules** – Pluggable strategies with configurable parameters per class.
4. **Risk Engine** – Position sizing, stop levels, portfolio heat, hard gates.
5. **Signal / Paper Book** – Generates alerts and maintains a simulated portfolio.
6. **Security Controls** – Cross-cutting: auth wrappers, audit logger, anomaly detector.

## Data Flow
See the mermaid diagram in README.md.

## Design Principles
- Modular and testable
- Offline-first for strategies and backtests
- Explicit security boundaries
- No live execution paths in core modules
