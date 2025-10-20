#!/usr/bin/env python3
import json, os
from flask import Flask, jsonify

app = Flask(__name__)
CHAIN_FILE = "wallet/zsona_chain.json"

@app.route("/stats")
def stats():
    if not os.path.exists(CHAIN_FILE):
        return jsonify({"blocks": 0, "total_reward": 0})
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    total = sum(b["data"]["amount"] for b in chain if "amount" in b["data"])
    return jsonify({"blocks": len(chain), "total_reward": total})

if __name__ == "__main__":
    app.run(port=8050)
