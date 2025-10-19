#!/usr/bin/env python3
import json

with open("ecostate.json") as f:
    state = json.load(f)

wallet = state.get("xmr_wallet", "XMR-" + state.get("nickname", "EcoBlock"))
worker = state.get("nickname", "EcoBlock")
pool = "pool.supportxmr.com:3333"

config = f"""#!/bin/bash
echo "⛏️ Mining EcoBlock via XMRig..."
./xmrig -o {pool} -u {wallet} -p {worker} -t 4 --donate-level 0
"""

with open("ecominer.sh", "w") as f:
    f.write(config)

print("✅ ecominer.sh generato con:")
print(f"🧠 Wallet: {wallet}")
print(f"👷 Worker: {worker}")
print(f"🌐 Pool: {pool}")
