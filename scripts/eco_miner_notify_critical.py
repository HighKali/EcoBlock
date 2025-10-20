#!/usr/bin/env python3
import json, os, requests

CHAIN_FILE = "wallet/zsona_chain.json"
HOOK = "https://discord.com/api/webhooks/..."  # Inserisci il tuo webhook

def notify_critical():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    alerts = []
    for b in chain:
        if b["data"]["amount"] > 1000:
            alerts.append(f"⚠️ Reward anomalo: Blocco {b['index']} → {b['data']['amount']} ZSONA")
        if not b["hash"]:
            alerts.append(f"❌ Hash mancante: Blocco {b['index']}")
    if alerts:
        msg = "\n".join(alerts)
        try:
            requests.post(HOOK, json={"content": msg})
            return "🚨 Notifica critica inviata"
        except Exception as e:
            return f"❌ Errore notifica: {e}"
    return "✅ Nessuna anomalia da notificare"

if __name__ == "__main__":
    print(notify_critical())
