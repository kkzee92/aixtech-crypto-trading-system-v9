"""CLI entry point."""
import argparse
from .strategies.majors import MajorsStrategy

def demo():
    print("AIxTech Crypto Trading Information System v9 - Demo (paper only)")
    strategy = MajorsStrategy()
    features = {"ema_trend": 0.8, "rsi": 55, "funding_rate": 0.01}
    signal = strategy.generate_signal(features)
    print(f"Sample signal for majors: {signal}")
    print("No orders were placed. This is informational only.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="?", default="demo")
    args = parser.parse_args()
    if args.command == "demo":
        demo()
    else:
        print("Unknown command. Use: python -m crypto_trading demo")
