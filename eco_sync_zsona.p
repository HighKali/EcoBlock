import json, time, requests
from datetime import datetime, timezone

def sync_chain():
    try:
        with open("wallet/zsona_chain.json") as f:
            chain = json.load(f)
    except Exception as e:
        print(f"❌ Errore lettura chain: {e}")
        return

    dex_url = chain.get("dex", {}).get("url")
    pool_url = chain.get("pool", {}).get("url")
    token = chain.get("token_address")

    if not dex_url or not pool_url:
        print("❌ URL DEX o Pool mancanti")
        return

    try:
        dex_response = requests.get(dex_url).json()
        pool_response = requests.get(pool_url).json()
    except Exception as e:
        print(f"❌ Errore sincronizzazione: {e}")
        return

    sync_data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "chain_id": chain.get("chain_id"),
        "token": token,
        "dex": dex_response,
        "pool": pool_response
    }

    try:
        with open("wallet/zsona_sync_log.json", "a") as f:
            f.write(json.dumps(sync_data) + "\n")
        print("✅ Sincronizzazione ZSONA completata")
    except Exception as e:
        print(f"❌ Errore salvataggio log: {e}")

if __name__ == "__main__":
    while True:
        sync_chain()
        time.sleep(300)  # ogni 5 minuti
