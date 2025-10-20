#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"
HTML_FILE = "dashboard/eco_miner_chain.html"

def export_html():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    html = "<html><body><h1>EcoBlock Chain</h1><ul>"
    for b in chain:
        html += f"<li>Blocco {b['index']} → {b['data']['to']} +{b['data']['amount']} ZSONA</li>"
    html += "</ul></body></html>"
    with open(HTML_FILE, "w") as f:
        f.write(html)
    return "🌐 Chain esportata in HTML"

if __name__ == "__main__":
    print(export_html())
