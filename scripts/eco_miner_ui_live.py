#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"
SVG_FILE = "wallet/miner_ui_live.svg"

def ui_live():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    last = chain[-1]
    svg = f'''<svg width="400" height="120" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="120" fill="#000"/>
  <text x="20" y="30" fill="#0ff" font-size="18">EcoBlock Live UI</text>
  <text x="20" y="60" fill="#fff" font-size="14">Blocco: {last["index"]}</text>
  <text x="20" y="80" fill="#0f0" font-size="14">Address: {last["data"]["to"]}</text>
  <text x="20" y="100" fill="#ff0" font-size="14">Reward: {last["data"]["amount"]} ZSONA</text>
</svg>'''
    with open(SVG_FILE, "w") as f:
        f.write(svg)
    return "🖼️ UI SVG live aggiornata"

if __name__ == "__main__":
    print(ui_live())
