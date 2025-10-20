#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"

def explorer():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    for b in chain:
        print(f"🔎 Blocco {b['index']} | {b['data']['to']} +{b['data']['amount']} ZSONA | Hash: {b['hash'][:12]}...")

if __name__ == "__main__":
    explorer()
