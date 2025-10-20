#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"
BADGE_FILE = "wallet/miner_badge.svg"

def generate_badge():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    last = chain[-1]
    addr = last["data"]["to"]
    amt = last["data"]["amount"]
    hash = last["hash"][:12]
    svg = f'''<svg width="300" height="100" xmlns="http://www.w3.org/2000/svg">
  <rect width="300" height="100" fill="#222"/>
  <text x="10" y="30" fill="#0f0" font-size="16">Miner: {addr}</text>
  <text x="10" y="55" fill="#0ff" font-size="14">Reward: {amt} ZSONA</text>
  <text x="10" y="80" fill="#fff" font-size="12">Hash: {hash}...</text>
</svg>'''
    with open(BADGE_FILE, "w") as f:
        f.write(svg)
    return "🏅 Badge SVG generato"

if __name__ == "__main__":
    print(generate_badge())
