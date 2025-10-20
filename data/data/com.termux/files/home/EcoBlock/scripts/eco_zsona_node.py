#!/usr/bin/env python3
from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
STATE = os.path.join("wallet", "wallet_zsona.txt")

@app.route("/node/receive", methods=["POST"])
def receive_tx():
    tx = request.json
    if not tx or "from" not in tx or "to" not in tx or "amount" not in tx:
        return jsonify({"error": "Invalid transaction"}), 400
    # Simulazione validazione
    return jsonify({"status": "✅ Transazione ricevuta", "tx": tx})

if __name__ == "__main__":
    app.run(port=8090)
