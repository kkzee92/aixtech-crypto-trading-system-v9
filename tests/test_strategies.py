from crypto_trading.strategies.majors import MajorsStrategy
from crypto_trading.strategies.alts import LargeAltsStrategy

def test_majors_long_signal():
    s = MajorsStrategy()
    features = {"ema_trend": 1.0, "rsi": 55, "funding_rate": 0.0}
    sig = s.generate_signal(features)
    assert sig["direction"] == "long"
    assert sig["strength"] > 0

def test_alts_flat():
    s = LargeAltsStrategy()
    features = {"roc": 0.01, "volume_ratio": 1.0, "rel_strength_vs_btc": -0.1}
    sig = s.generate_signal(features)
    assert sig["direction"] == "flat"
