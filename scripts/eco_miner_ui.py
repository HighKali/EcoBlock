#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"
SVG_FILE = "wallet/miner_ui.svg"

def generate_ui():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    blocks = len(chain)
    last = chain[-1]
    addr = last["data"]["to"]
    amt = last["data"]["amount"]
    svg = f'''<svg width="400" height="120" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="120" fill="#111"/>
  <text x="20" y="30" fill="#0f0" font-size="18">EcoBlock Miner UI</text>
  <text x="20" y="60" fill="#0ff" font-size="14">Blocco: {blocks}</text>
  <text x="20" y="80" fill="#fff" font-size="14">Address: {addr}</text>
  <text x="20" y="100" fill="#ff0" font-size="14">Reward: {amt} ZSONA</text>
</svg>'''
    with open(SVG_FILE, "w") as f:
        f.write(svg)
    return "🖼️ Dashboard SVG generata"

if __name__ == "__main__":
    print(generate_ui())
