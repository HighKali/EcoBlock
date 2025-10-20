#!/usr/bin/env python3
import json, requests, os

CHAIN_FILE = "wallet/zsona_chain.json"
PEERS = ["http://127.0.0.1:8090/node/receive"]

def broadcast_chain():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    for peer in PEERS:
        try:
            res = requests.post(peer, json={"chain": chain})
            print(f"📡 Chain inviata a {peer} → {res.status_code}")
        except Exception as e:
            print(f"❌ Errore su {peer}: {e}")

if __name__ == "__main__":
    broadcast_chain()
