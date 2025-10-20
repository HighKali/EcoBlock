#!/usr/bin/env python3
import requests
POOL_API = "https://api.oceanminer.org/status"
def get_pool_status():
    try:
        res = requests.get(POOL_API)
        data = res.json()
        return f"🌊 Ocean Miner: {data.get('hashrate', 'N/A')} H/s, Blocks: {data.get('blocks', 'N/A')}"
    except Exception as e:
        return f"❌ Errore pool: {e}"
if __name__ == "__main__":
    print(get_pool_status())
