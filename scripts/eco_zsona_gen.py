#!/usr/bin/env python3
import secrets, hashlib, json, os

def generate_zsona_wallet():
    entropy = secrets.token_hex(32)
    address = "DSN" + hashlib.sha256(entropy.encode()).hexdigest()[:32]
    wallet = {
        "address": address,
        "private_key": entropy,
        "balance": 1000000,
        "symbol": "ZSONA",
        "compatible_with": ["XMR", "DSN"],
        "note": "Algoritmo: CryptoNight-Lite"
    }
    os.makedirs("wallets", exist_ok=True)
    with open(f"wallets/{address}.json", "w") as f:
        json.dump(wallet, f, indent=2)
    print(f"✅ Wallet ZSONA creato: {address}")
    print(f"🔐 Chiave privata: {entropy}")
    print(f"💰 Bilancio iniziale: 1.000.000 ZSONA")

generate_zsona_wallet()
