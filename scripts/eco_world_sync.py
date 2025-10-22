#!/usr/bin/env python3
import json, os, time

def check_node(ip):
    # Simulazione ping/sync check
    return os.system(f"ping -c 1 -W 1 {ip} > /dev/null") == 0

with open("nodes/nodes_list.json") as f:
    raw_nodes = json.load(f)

updated = []
for node in raw_nodes:
    status = {
        "ip": node["ip"],
        "role": node.get("role", "node"),
        "badge": node.get("badge", ""),
        "sync": check_node(node["ip"]),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    updated.append(status)

with open("nodes/nodes_status.json", "w") as f:
    json.dump(updated, f, indent=2)

print("🔁 Stato nodi aggiornato in nodes_status.json")

