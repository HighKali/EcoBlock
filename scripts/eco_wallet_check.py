#!/usr/bin/env python3
import json, os
WALLET_FILE = "wallet/wallet_zsona.txt"

def check_wallet():
    if not os.path.exists(WALLET_FILE):
        return "❌ Wallet mancante"
    if os.stat(WALLET_FILE).st_size == 0:
        return "❌ Wallet vuoto"
    try:
        with open(WALLET_FILE) as f:
            w = json.load(f)
        keys = ["private", "pubkey", "address"]
        if all(k in w for k in keys):
            return "✅ Wallet valido"
        else:
            return "❌ Wallet incompleto"
    except:
        return "❌ Wallet corrotto"

if __name__ == "__main__":
    print(check_wallet())
