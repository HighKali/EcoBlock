#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"

def analyze():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    reward_map = {}
    for b in chain:
        addr = b["data"]["to"]
        reward_map[addr] = reward_map.get(addr, 0) + b["data"]["amount"]
    top = sorted(reward_map.items(), key=lambda x: x[1], reverse=True)[:5]
    for addr, amt in top:
        print(f"🧠 AI: {addr} ha ricevuto {amt} ZSONA")
        
if __name__ == "__main__":
    analyze()
