#!/usr/bin/env python3
import time, os
def check_health():
    modules = ["eco_zsona_miner", "eco_zsona_syncnet", "eco_zsona_node"]
    for m in modules:
        status = os.system(f"pgrep -f {m} > /dev/null")
        if status != 0:
            print(f"⚠️ {m} non attivo. Riavvio...")
            os.system(f"bash scripts/{m}.sh")
        else:
            print(f"✅ {m} attivo")
while True:
    check_health()
    time.sleep(60)

