"""Large altcoin strategy example."""
from .base import BaseStrategy
from typing import Dict, Any

class LargeAltsStrategy(BaseStrategy):
    def __init__(self, params=None):
        super().__init__("large_alts", params)

    def generate_signal(self, features: Dict[str, Any]) -> Dict[str, Any]:
        momentum = features.get("roc", 0)
        volume_ratio = features.get("volume_ratio", 1.0)
        rel_strength = features.get("rel_strength_vs_btc", 0)

        direction = "flat"
        strength = 0.0
        if momentum > 0.05 and volume_ratio > 1.5 and rel_strength > 0:
            direction = "long"
            strength = min(1.0, momentum * 2)
        return {
            "direction": direction,
            "strength": strength,
            "reason": "momentum + volume confirmation" if direction != "flat" else "no setup",
            "asset_class": self.asset_class,
        }
