#!/usr/bin/env python3
import json, os, requests

CHAIN_FILE = "wallet/zsona_chain.json"
PEERS = ["http://127.0.0.1:8090/node/receive"]

def merge_and_sync():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain locale mancante"
    with open(CHAIN_FILE) as f:
        local = json.load(f)
    for peer in PEERS:
        try:
            res = requests.get(peer.replace("/node/receive", "/chain"))
            remote = res.json()
            if len(remote) > len(local):
                with open(CHAIN_FILE, "w") as f:
                    json.dump(remote, f, indent=2)
                return f"🔄 Chain aggiornata da {peer}"
        except:
            continue
    return "✅ Chain locale già aggiornata"

if __name__ == "__main__":
    print(merge_and_sync())
