#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"
SVG_FILE = "dashboard/nodes_sync.svg"

def sync_svg():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    svg = '<svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">'
    svg += '<rect width="400" height="200" fill="#000"/>'
    for i, b in enumerate(chain[-5:]):
        y = 40 + i * 30
        svg += f'<text x="20" y="{y}" fill="#0f0" font-size="14">Blocco {b["index"]} → {b["data"]["to"]} +{b["data"]["amount"]} ZSONA</text>'
    svg += '</svg>'
    with open(SVG_FILE, "w") as f:
        f.write(svg)
    return "🔄 SVG sincronizzato con ultimi blocchi"

if __name__ == "__main__":
    print(sync_svg())
