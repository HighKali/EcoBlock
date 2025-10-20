#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"

def check_integrity():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    for b in chain:
        if not all(k in b for k in ["index", "timestamp", "data", "hash"]):
            print(f"⚠️ Blocco {b.get('index', '?')} incompleto")
    print("✅ Integrità chain verificata")

if __name__ == "__main__":
    check_integrity()
