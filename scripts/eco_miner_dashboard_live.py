#!/usr/bin/env python3
from flask import Flask, jsonify, render_template
import json, os

app = Flask(__name__)
CHAIN_FILE = "wallet/zsona_chain.json"

@app.route("/")
def home():
    return "<h1>📊 EcoBlock Live Dashboard</h1><p>Visita /latest per vedere l’ultimo blocco</p>"

@app.route("/latest")
def latest():
    if not os.path.exists(CHAIN_FILE):
        return jsonify({})
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    return jsonify(chain[-1])

@app.route("/rewards")
def rewards():
    if not os.path.exists(CHAIN_FILE):
        return jsonify({})
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    stats = {}
    for b in chain:
        addr = b["data"]["to"]
        stats[addr] = stats.get(addr, 0) + b["data"]["amount"]
    return jsonify(stats)

if __name__ == "__main__":
    app.run(port=8060)
