#!/usr/bin/env python3
import json, os, requests

CHAIN_FILE = "wallet/zsona_chain.json"
HOOK = "https://discord.com/api/webhooks/..."  # Inserisci webhook admin

def notify_admin():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    last = chain[-1]
    msg = f"🛡️ Admin Alert: Blocco {last['index']} → {last['data']['to']} +{last['data']['amount']} ZSONA"
    try:
        requests.post(HOOK, json={"content": msg})
        return "📣 Notifica inviata all’admin"
    except Exception as e:
        return f"❌ Errore notifica: {e}"

if __name__ == "__main__":
    print(notify_admin())
