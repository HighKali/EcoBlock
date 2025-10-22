#!/usr/bin/env python3
import json, requests, time
from datetime import datetime
import folium

def get_ip_location(ip):
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        loc = r.json().get("loc", "0,0").split(",")
        return float(loc[0]), float(loc[1])
    except:
        return 0.0, 0.0

with open("nodes/nodes_status.json") as f:
    nodes = json.load(f)

m = folium.Map(location=[0, 0], zoom_start=2, tiles="CartoDB dark_matter")

for node in nodes:
    lat, lon = get_ip_location(node["ip"])
    badge = "🏅" if node.get("badge") == "founder" else ""
    role = node.get("role", "node")
    status = "🟢" if node.get("sync") else "🔴"
    folium.Marker(
        location=[lat, lon],
        popup=f"{badge} {role.upper()}\\n{status} {node[ip]}",
        icon=folium.Icon(color="green" if node.get("sync") else "red")
    ).add_to(m)

m.save("dashboard/eco_world_map.html")
print("🌍 eco_world_map.html generata con nodi attivi")

