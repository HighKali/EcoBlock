#!/usr/bin/env python3
import requests, json, os
STATE = os.path.join("wallet", "wallet_zsona.txt")
SYNC_ENDPOINT = "https://api.ecoblock.network/sync"
def sync_balance():
    if not os.path.exists(STATE):
        return "❌ Wallet non inizializzato"
    with open(STATE) as f:
        data = json.load(f)
    try:
        res = requests.post(SYNC_ENDPOINT, json={"address": data["address"], "balance": data["balance"]})
        return f"🔄 Sync OK: {res.status_code}"
    except Exception as e:
        return f"❌ Errore sync: {e}"
if __name__ == "__main__":
    print(sync_balance())
