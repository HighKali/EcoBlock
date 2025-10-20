#!/usr/bin/env python3
import json, os, sys
STATE = os.path.join("wallet", "wallet_zsona.txt")
def transfer(to, amount):
    if not os.path.exists(STATE):
        return "❌ Wallet non inizializzato"
    with open(STATE) as f:
        data = json.load(f)
    if data["balance"] >= amount:
        data["balance"] -= amount
        with open(STATE, "w") as f:
            f.write(json.dumps(data))
        return f"📤 Trasferiti {amount} ZSONA a {to}"
    else:
        return "❌ Fondi insufficienti"
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("❌ Uso: eco_zsona_transfer.py <destinatario> <importo>")
    else:
        print(transfer(sys.argv[1], int(sys.argv[2])))
