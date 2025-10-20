#!/usr/bin/env python3
import json, os
from eco_zsona_wallet import generate_wallet

WALLET_FILE = "wallet/wallet_zsona.txt"

def rotate_wallet():
    wallet = generate_wallet()
    with open(WALLET_FILE, "w") as f:
        json.dump(wallet, f, indent=2)
    return f"🔁 Nuovo wallet generato: {wallet['address']}"

if __name__ == "__main__":
    print(rotate_wallet())
