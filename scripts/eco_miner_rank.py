#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"

def rank():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    scores = {}
    for b in chain:
        addr = b["data"]["to"]
        scores[addr] = scores.get(addr, 0) + b["data"]["amount"]
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for i, (addr, amt) in enumerate(ranked[:10]):
        print(f"🏆 {i+1}. {addr} → {amt} ZSONA")

if __name__ == "__main__":
    rank()
