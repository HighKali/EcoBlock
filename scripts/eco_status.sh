#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"

def status():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    last = chain[-1]
    print(f"⛏️ Ultimo blocco: {last['index']} → {last['data']['to']} +{last['data']['amount']} ZSONA")
    print(f"🔗 Hash: {last['hash']}")
    print(f"📦 Totale blocchi: {len(chain)}")

if __name__ == "__main__":
    status()
