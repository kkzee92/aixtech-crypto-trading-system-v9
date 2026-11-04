"""DeFi strategy example."""
from .base import BaseStrategy
from typing import Dict, Any

class DeFiStrategy(BaseStrategy):
    def __init__(self, params=None):
        super().__init__("defi", params)

    def generate_signal(self, features: Dict[str, Any]) -> Dict[str, Any]:
        price_mom = features.get("price_momentum", 0)
        tvl_change = features.get("tvl_change_proxy", 0)
        vol = features.get("realized_vol", 0.5)

        direction = "flat"
        strength = 0.0
        if price_mom > 0 and tvl_change > 0 and vol < 1.2:
            direction = "long"
            strength = 0.6
        return {
            "direction": direction,
            "strength": strength,
            "reason": "price + TVL proxy alignment" if direction != "flat" else "filters not met",
            "asset_class": self.asset_class,
        }
