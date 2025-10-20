#!/usr/bin/env python3
import requests, json
HOOK = "https://discord.com/api/webhooks/..."  # Inserisci il tuo webhook

def notify_mining(block_info):
    payload = {
        "content": f"⛏️ Nuovo blocco minato:\n{block_info}"
    }
    try:
        res = requests.post(HOOK, json=payload)
        return f"✅ Notifica inviata ({res.status_code})"
    except Exception as e:
        return f"❌ Errore notifica: {e}"

if __name__ == "__main__":
    print(notify_mining("Blocco 0 - reward 100 ZSONA"))
