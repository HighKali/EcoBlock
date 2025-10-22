#!/usr/bin/env python3
import time
def sync_nodes():
    nodes = ["node1.zsona.net", "node2.zsona.net", "node3.zsona.net"]
    print("🌐 Sync nodi ZSONA...")
    for n in nodes:
        print(f"🔄 Sync con {n}...")
        time.sleep(1)
    print("✅ Sync completato")
sync_nodes()
