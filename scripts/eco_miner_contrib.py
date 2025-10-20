#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"
LOG_FILE = "wallet/contributors.log"

def log_contributors():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    contrib = {}
    for b in chain:
        addr = b["data"]["to"]
        contrib[addr] = contrib.get(addr, 0) + b["data"]["amount"]
    with open(LOG_FILE, "w") as f:
        for addr, amt in contrib.items():
            f.write(f"{addr}: {amt} ZSONA\n")
    return "🏅 Collaboratori registrati"

if __name__ == "__main__":
    print(log_contributors())
