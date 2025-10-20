#!/usr/bin/env python3
from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
CHAIN_FILE = "wallet/zsona_chain.json"

@app.route("/node/receive", methods=["POST"])
def receive_chain():
    incoming = request.json.get("chain", [])
    if not incoming:
        return jsonify({"error": "Chain mancante"}), 400
    with open(CHAIN_FILE, "w") as f:
        json.dump(incoming, f, indent=2)
    return jsonify({"status": "✅ Chain aggiornata", "blocks": len(incoming)})

if __name__ == "__main__":
    app.run(port=8090)
