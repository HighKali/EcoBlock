#!/usr/bin/env python3
import requests, json, os

REMOTE_NODES = ["http://127.0.0.1:8090", "http://127.0.0.1:8040"]
CHAIN_FILE = "wallet/zsona_chain.json"

def sync_remote():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    for node in REMOTE_NODES:
        try:
            r = requests.post(f"{node}/node/receive", json=chain)
            print(f"🌍 Sync → {node} → {r.status_code}")
        except Exception as e:
            print(f"❌ Errore sync con {node}: {e}")

if __name__ == "__main__":
    sync_remote()
