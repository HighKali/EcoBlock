#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"

def alert():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    alerts = []
    for b in chain:
        if b["data"]["amount"] > 1000:
            alerts.append(f"⚠️ Reward anomalo: Blocco {b['index']} → {b['data']['amount']} ZSONA")
        if not b["hash"]:
            alerts.append(f"❌ Hash mancante: Blocco {b['index']}")
    print("\n".join(alerts) if alerts else "✅ Nessuna anomalia rilevata")

if __name__ == "__main__":
    alert()
