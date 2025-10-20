#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"

def clean():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    cleaned = [b for b in chain if b.get("hash")]
    with open(CHAIN_FILE, "w") as f:
        json.dump(cleaned, f, indent=2)
    return f"🧹 Chain pulita: {len(cleaned)} blocchi validi"

if __name__ == "__main__":
    print(clean())
