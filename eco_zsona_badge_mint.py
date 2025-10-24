#!/usr/bin/env python3
import time

def mint_badge():
    print("🏅 Mint NFT celebrativo Founder…")
    badge = {
        "name": "EcoBlock Founder",
        "description": "Sigillo celebrativo della fusione globale EcoBlock",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "chain": "ZSONA",
        "module": "hostblock"
    }
    print(f"✅ Badge mintato: {badge['name']} @ {badge['timestamp']}")

mint_badge()
