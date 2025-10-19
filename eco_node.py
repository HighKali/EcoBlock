#!/usr/bin/env python3
from flask import Flask, jsonify
import os

app = Flask(__name__)

def read_wallet(file):
    try:
        with open(file, 'r') as f:
            return f.read().strip()
    except:
        return "Not found"

@app.route('/status')
def status():
    return jsonify({
        "node": "EcoBlock Local Node",
        "zsona_wallet": read_wallet("wallet_zsona.txt"),
        "dsn_wallet": read_wallet("wallet_dsn.txt"),
        "xmr_wallet": read_wallet("wallet_xmr.txt"),
        "status": "🟢 Online"
    })

@app.route('/hashrate')
def hashrate():
    return jsonify({
        "hashrate": "Pending integration",
        "pool": "pool.zsona.org:3333"
    })

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    print("🧠 EcoBlock Node attivo su http://localhost:8080/status")
    app.run(host='0.0.0.0', port=8080)
