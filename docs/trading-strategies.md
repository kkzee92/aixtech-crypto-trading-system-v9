# Trading Strategies by Asset Class

All strategies produce **signals only** (long, short, flat, or strength score). They never place orders.

## 1. Majors (BTC, ETH)
- **Trend following**: Multi-timeframe EMA / Supertrend
- **Mean reversion**: Bollinger + RSI extremes
- **Funding rate filter**: Avoid crowded longs when funding is highly positive
- **Volatility regime**: Reduce size in extreme ATR regimes

## 2. Large Alts (SOL, BNB, ADA, AVAX, etc.)
- **Momentum**: Rate-of-change + volume confirmation
- **Relative strength**: vs BTC and vs sector
- **Breakout**: Donchian or Keltner with volume spike
- Adaptive lookback based on realized volatility

## 3. DeFi (UNI, AAVE, LINK, etc.)
- **Yield + price**: Combine price momentum with TVL / utilization proxies (stubs)
- **Volatility harvesting**: Mean-reversion around fair value with wider bands
- Strict correlation limits to majors

## 4. Stablecoins (USDT, USDC, DAI)
- **Peg monitoring**: Deviation alerts
- **Basis / funding arb signals**: Between perps and spot (informational)
- Low risk allocation; primarily for cash management signals

## 5. High Volatility (Memecoins, new listings)
- **Time stops**: Mandatory exit after N bars
- **Size caps**: Hard maximum % of portfolio
- **Volume and liquidity filters**: Ignore low-liquidity pairs
- Extreme ATR filter: no entry if vol is too high

## Risk Overlay (All Classes)
- Maximum portfolio heat
- Correlation matrix checks (stub)
- Kill switch on anomalous data
- Position sizing via fixed fractional or volatility targeting

Parameters are configurable and meant to be backtested on historical or synthetic data.
