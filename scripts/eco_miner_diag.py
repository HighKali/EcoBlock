#!/usr/bin/env python3
import os

def diagnose():
    print("🧪 Diagnosi moduli:")
    for f in os.listdir("scripts"):
        if f.startswith("eco_") and f.endswith(".py"):
            path = os.path.join("scripts", f)
            ok = os.access(path, os.X_OK)
            print(f"{f}: {'✅ Eseguibile' if ok else '❌ Non eseguibile'}")
    print("📄 Log miner:", "✅" if os.path.exists("wallet/miner.log") else "❌ Assente")

if __name__ == "__main__":
    diagnose()
