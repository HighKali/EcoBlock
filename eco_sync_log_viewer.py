import json

def view_logs():
    try:
        with open("wallet/zsona_sync_log.json") as f:
            lines = f.readlines()
    except:
        print("❌ Log non trovato")
        return

    print("📊 Log sincronizzazione ZSONA")
    print("-" * 80)
    for line in lines[-5:]:
        entry = json.loads(line)
        print(f"{entry['timestamp']} | Chain: {entry['chain_id']} | Token: {entry['token']}")
        print(f"DEX Volume: {entry['dex'].get('volume_24h')} | Pool APY: {entry['pool'].get('apy')}")
        print("-" * 80)

if __name__ == "__main__":
    view_logs()
