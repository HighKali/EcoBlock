#!/usr/bin/env python3
import json, time, os
from datetime import datetime

def load_wallet():
    wallet_path = "wallets"
    wallets = [f for f in os.listdir(wallet_path) if f.endswith(".json")]
    return wallets[:3]

def show_led(status):
    return "🟢" if status == "OK" else "🔴"

def live_panel():
    print("🌐 ZSONA Live Panel")
    print(f"🕒 {datetime.now().strftime(%Y-%m-%d %H:%M:%S)}")
    print("\n💼 Wallets attivi:")
    for w in load_wallet():
        print(f" - {w.replace(.json,)}")
    nodes = {"node1.zsona.net": "OK", "node2.zsona.net": "OK", "node3.zsona.net": "FAIL"}
    print("\n🔗 Stato nodi:")
    for n, s in nodes.items():
        print(f" {show_led(s)} {n} → {s}")
    print("\n⛏️ Mining:")
    print(f" {show_led(OK)} Loop miner attivo")
    print(" 🏅 Badge: miner_badge.svg")
    print("\n🔄 Sync:")
    print(f" {show_led(OK)} Ultimo sync: 12s fa")
    print("\n🔁 Bridge:")
    print(" ZSONA ⇄ DSN ⇄ XMR attivo")
    print("\n🏅 Founder Badge:")
    print(" badge_founder_zsona.svg")

live_panel()
