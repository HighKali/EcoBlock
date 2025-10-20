#!/usr/bin/env python3
from flask import Flask, jsonify, render_template
import json, os

app = Flask(__name__)
CHAIN_FILE = "wallet/zsona_chain.json"

@app.route("/")
def home():
    return "<h1>🌍 EcoBlock Web Interface</h1><p>Visita /chain per vedere la blockchain</p>"

@app.route("/chain")
def chain():
    if not os.path.exists(CHAIN_FILE):
        return jsonify([])
    with open(CHAIN_FILE) as f:
        return jsonify(json.load(f))

@app.route("/latest")
def latest():
    if not os.path.exists(CHAIN_FILE):
        return jsonify({})
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    return jsonify(chain[-1])

if __name__ == "__main__":
    app.run(port=8050)
