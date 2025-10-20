#!/usr/bin/env python3
from flask import Flask, request, jsonify
import json, os
from datetime import datetime

app = Flask(__name__)
LOG_PATH = "wallet/chain_received.json"

@app.route("/node/receive", methods=["POST"])
def receive_chain():
    raw = request.json
    chain = []

    # Diagnostica tipo
    print(f"🔍 Tipo ricevuto: {type(raw)}")

    # Correzione automatica
    if isinstance(raw, list):
        chain = raw
    elif isinstance(raw, dict) and "chain" in raw:
        chain = raw["chain"]
    else:
        print("❌ Formato non valido")
        return jsonify({"error": "Formato non valido"}), 400

    # Logging
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "length": len(chain),
        "preview": chain[:3]
    }
    with open(LOG_PATH, "w") as f:
        json.dump(log_entry, f, indent=2)
    print(f"✅ Chain ricevuta: {len(chain)} blocchi")

    return jsonify({"status": "ok", "received": len(chain)}), 200

if __name__ == "__main__":
    app.run(port=8090)
