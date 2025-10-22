#!/usr/bin/env python3
import json, time
def mint_badge(wallet_address, badge_svg):
    tx = {
        "from": wallet_address,
        "to": "ZSONA_BADGE_CONTRACT",
        "type": "mint",
        "asset": badge_svg,
        "timestamp": time.time()
    }
    with open("minted_badges.json", "a") as f:
        f.write(json.dumps(tx) + "\\n")
    print(f"🏅 Badge founder mintato per: {wallet_address}")
mint_badge("DSNaf6cfac5102d81b6a37f95a551156ced", "badge_founder_zsona.svg")

