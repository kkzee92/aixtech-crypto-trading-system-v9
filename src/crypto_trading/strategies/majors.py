"""Major asset (BTC/ETH) strategy example."""
from .base import BaseStrategy
from typing import Dict, Any

class MajorsStrategy(BaseStrategy):
    def __init__(self, params=None):
        super().__init__("majors", params)

    def generate_signal(self, features: Dict[str, Any]) -> Dict[str, Any]:
        # Example multi-factor logic (stub)
        trend = features.get("ema_trend", 0)
        rsi = features.get("rsi", 50)
        funding = features.get("funding_rate", 0)

        direction = "flat"
        strength = 0.0
        reason = []

        if trend > 0 and rsi < 70 and funding < 0.05:
            direction = "long"
            strength = min(1.0, abs(trend) * 0.5)
            reason.append("positive trend, RSI ok, funding not extreme")
        elif trend < 0 and rsi > 30:
            direction = "short"
            strength = min(1.0, abs(trend) * 0.4)
            reason.append("negative trend")

        return {
            "direction": direction,
            "strength": strength,
            "reason": "; ".join(reason) or "no edge",
            "asset_class": self.asset_class,
        }
