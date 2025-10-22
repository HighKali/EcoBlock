#!/usr/bin/env python3
import json, os
def explore_chain():
    path = "wallet/zsona_chain_live.csv"
    if not os.path.exists(path):
        print("❌ Nessun blocco trovato")
        return
    with open(path) as f:
        blocks = f.readlines()
    print("📦 ZSONA Blockchain Explorer")
    for b in blocks[-10:]:
        print("🧱", b.strip())
explore_chain()
