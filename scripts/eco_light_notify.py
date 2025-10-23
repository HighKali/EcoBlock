#!/usr/bin/env python3
import json, time

with open("scripts/eco_light_log.json") as f:
    txs = json.load(f)

for tx in txs:
    msg = f"""⚡ Transazione Lightning eseguita
🪙 Asset: {tx["asset"].upper()}
💸 Importo: {tx["amount"]} sats
📝 Memo: {tx["memo"]}
🔐 Hash: {tx["payment_hash"]}
🕒 Timestamp: {tx["timestamp"]}"""

    # Simulazione invio (sostituibile con webhook reali)
    print(f"📡 Inviato:\n{msg}\n")
    # Esempio: requests.post(telegram_url, json={"text": msg})

