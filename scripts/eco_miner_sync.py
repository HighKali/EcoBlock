#!/usr/bin/env python3
import requests, json

PEERS = ["http://127.0.0.1:8090/rewards"]
LOCAL_FILE = "wallet/zsona_rewards.json"

def sync_rewards():
    all_rewards = {}
    for peer in PEERS:
        try:
            res = requests.get(peer)
            data = res.json()
            for addr, amt in data.items():
                all_rewards[addr] = all_rewards.get(addr, 0) + amt
        except:
            continue
    with open(LOCAL_FILE, "w") as f:
        json.dump(all_rewards, f, indent=2)
    return f"🔄 Reward sincronizzati da {len(PEERS)} nodi"

if __name__ == "__main__":
    print(sync_rewards())
