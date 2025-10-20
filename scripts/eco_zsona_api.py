#!/usr/bin/env python3
import json, os
from flask import Flask, jsonify
app = Flask(__name__)
STATE = os.path.join("wallet", "wallet_zsona.txt")
@app.route("/api/zsona")
def zsona_balance():
    if not os.path.exists(STATE):
        return jsonify({"error": "Wallet non inizializzato"}), 404
    with open(STATE) as f:
        data = json.load(f)
    return jsonify(data)
if __name__ == "__main__":
    app.run(port=8080)
