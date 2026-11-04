"""Base strategy interface. All strategies are paper-only signal generators."""
from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseStrategy(ABC):
    def __init__(self, asset_class: str, params: Dict[str, Any] | None = None):
        self.asset_class = asset_class
        self.params = params or {}

    @abstractmethod
    def generate_signal(self, features: Dict[str, Any]) -> Dict[str, Any]:
        """Return signal dict: direction, strength, reason. Never execute."""
        raise NotImplementedError
