#!/usr/bin/env python3
import json, os

NODES = [
    {"ip": "127.0.0.1", "port": 8090, "status": "🟢"},
    {"ip": "127.0.0.1", "port": 8040, "status": "🟢"}
]

SVG_FILE = "dashboard/nodes_map.svg"

def generate_map():
    svg = '<svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">'
    svg += '<rect width="400" height="200" fill="#111"/>'
    for i, node in enumerate(NODES):
        y = 40 + i * 40
        svg += f'<text x="20" y="{y}" fill="#0ff" font-size="14">{node["status"]} {node["ip"]}:{node["port"]}</text>'
    svg += '</svg>'
    with open(SVG_FILE, "w") as f:
        f.write(svg)
    return "🗺️ Mappa nodi SVG generata"

if __name__ == "__main__":
    print(generate_map())
