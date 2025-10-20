#!/usr/bin/env python3
import json, os, requests

CHAIN_FILE = "wallet/zsona_chain.json"
HOOK = "https://discord.com/api/webhooks/..."  # Inserisci il tuo webhook

def notify_latest():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    last = chain[-1]
    msg = f"⛏️ Blocco {last['index']} → {last['data']['to']} +{last['data']['amount']} ZSONA"
    try:
        res = requests.post(HOOK, json={"content": msg})
        return f"✅ Notifica inviata ({res.status_code})"
    except Exception as e:
        return f"❌ Errore notifica: {e}"

if __name__ == "__main__":
    print(notify_latest())
