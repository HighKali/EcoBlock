import json, time, requests
from datetime import datetime

def sync_chain():
    with open("wallet/zsona_chain.json") as f:
        chain = json.load(f)

    dex_url = chain["dex"]["url"]
    pool_url = chain["pool"]["url"]
    token = chain["token_address"]

    try:
        dex_response = requests.get(dex_url).json()
        pool_response = requests.get(pool_url).json()
    except Exception as e:
        print(f"❌ Errore sincronizzazione: {e}")
        return

    sync_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "chain_id": chain["chain_id"],
        "token": token,
        "dex": dex_response,
        "pool": pool_response
    }

    with open("wallet/zsona_sync_log.json", "a") as f:
        f.write(json.dumps(sync_data) + "\n")

    print("✅ Sincronizzazione ZSONA completata")

if __name__ == "__main__":
    while True:
        sync_chain()
        time.sleep(300)  # ogni 5 minuti
