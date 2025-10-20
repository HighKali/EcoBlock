#!/usr/bin/env python3
import os, json, time, random, requests
STATE = os.path.join("wallet", "wallet_zsona.txt")
POOL_API = "https://api.oceanminer.org/status"
def get_uptime_score():
    uptime = time.time() - os.stat(STATE).st_ctime if os.path.exists(STATE) else 0
    return min(int(uptime / 3600), 100)
def get_ecoscore():
    return random.randint(10, 100)
def get_pool_hashrate():
    try:
        res = requests.get(POOL_API)
        data = res.json()
        return int(data.get("hashrate", 0))
    except:
        return 0
def mint_zsona():
    if not os.path.exists(STATE):
        with open(STATE, "w") as f:
            f.write(json.dumps({"balance": 0, "address": "ZSONA-undefined"}))
    with open(STATE) as f:
        data = json.load(f)
    reward = int((get_uptime_score() + get_ecoscore() + get_pool_hashrate() / 1000) / 2)
    data["balance"] += reward
    with open(STATE, "w") as f:
        f.write(json.dumps(data))
    return f"⛏️ Minted {reward} ZSONA (uptime + eco + pool)"
if __name__ == "__main__":
    print(mint_zsona())
