#!/usr/bin/env python3
import json, os
from flask import Flask, jsonify

app = Flask(__name__)
CHAIN_FILE = "wallet/zsona_chain.json"

@app.route("/rewards")
def rewards():
    if not os.path.exists(CHAIN_FILE):
        return jsonify({})
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    stats = {}
    for b in chain:
        tx = b["data"]
        addr = tx.get("to")
        amt = tx.get("amount", 0)
        if addr:
            stats[addr] = stats.get(addr, 0) + amt
    return jsonify(stats)

if __name__ == "__main__":
    app.run(port=8040)
