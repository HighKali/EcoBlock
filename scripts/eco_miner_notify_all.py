#!/usr/bin/env python3
import json, os, requests

CHAIN_FILE = "wallet/zsona_chain.json"
HOOKS = [
    "https://discord.com/api/webhooks/...",  # Discord
    "https://matrix.org/api/webhooks/...",   # Matrix
    "https://api.telegram.org/bot.../sendMessage"  # Telegram
]

def notify_all():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    last = chain[-1]
    msg = f"📢 Broadcast: Blocco {last['index']} → {last['data']['to']} +{last['data']['amount']} ZSONA"
    for hook in HOOKS:
        try:
            payload = {"content": msg} if "discord" in hook or "matrix" in hook else {"chat_id": "@EcoBlock", "text": msg}
            requests.post(hook, json=payload)
        except Exception as e:
            print(f"❌ Errore con {hook}: {e}")
    print("📣 Notifica inviata su tutti i canali")

if __name__ == "__main__":
    notify_all()
