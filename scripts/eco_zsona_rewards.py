#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"

def calculate_rewards():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    rewards = {}
    for block in chain:
        tx = block["data"]
        addr = tx.get("to")
        amt = tx.get("amount", 0)
        if addr:
            rewards[addr] = rewards.get(addr, 0) + amt
    return rewards

if __name__ == "__main__":
    print(json.dumps(calculate_rewards(), indent=2))
