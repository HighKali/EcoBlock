#!/usr/bin/env python3
import json, os, requests

CHAIN_FILE = "wallet/zsona_chain.json"
PEERS = ["http://127.0.0.1:8090/node/receive"]

def broadcast_chain():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Nessuna chain da propagare"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    results = []
    for peer in PEERS:
        try:
            res = requests.post(peer, json={"chain": chain})
            results.append(f"{peer}: {res.status_code}")
        except Exception as e:
            results.append(f"{peer}: errore {e}")
    return "🔄 Propagazione: " + ", ".join(results)

if __name__ == "__main__":
    print(broadcast_chain())
