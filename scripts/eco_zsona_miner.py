#!/usr/bin/env python3
import time, hashlib, os
def mine_loop():
    print("⛏️ Avvio mining ZSONA...")
    for i in range(5):
        entropy = os.urandom(32).hex()
        block = hashlib.sha256(entropy.encode()).hexdigest()
        print(f"🧱 Blocco {i+1}: {block[:16]}...")
        time.sleep(1)
    print("🏅 Badge miner generato: miner_badge.svg")
mine_loop()
