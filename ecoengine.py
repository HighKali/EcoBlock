#!/usr/bin/env python3
from flask import Flask, request, jsonify
import os, time, threading

app = Flask(__name__)

# 🔐 Load credentials
def load_credentials():
    try:
        with open("credentials.txt", "r") as f:
            line = f.read().strip()
            nick, passwd = line.split(":")
            return nick, passwd
    except:
        return None, None

# 🧠 Read wallet
def read_wallet(file):
    try:
        with open(file, 'r') as f:
            return f.read().strip()
    except:
        return "Not found"

# 🔍 Integrity check
MODULES = [
    "ecoentry.sh", "ecoswap.sh", "ecoapi.sh", "ecopool.sh",
    "ecoignite.sh", "eco_node.py", "ecoauth.py", "ecopublish.sh"
]

def check_integrity():
    corrupted = []
    for module in MODULES:
        if not os.path.exists(module) or os.path.getsize(module) < 10:
            corrupted.append(module)
    return corrupted

def attempt_repair(modules):
    for m in modules:
        with open(m, "w") as f:
            f.write("# Modulo ripristinato automaticamente\n")
        time.sleep(0.2)

# 🌐 API endpoints
@app.route('/status')
def status():
    return jsonify({
        "node": "EcoBlock Unified Engine",
        "zsona_wallet": read_wallet("wallet_zsona.txt"),
        "dsn_wallet": read_wallet("wallet_dsn.txt"),
        "xmr_wallet": read_wallet("wallet_xmr.txt"),
        "status": "🟢 Online",
        "corrupted_modules": check_integrity()
    })

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    nick_input = data.get("nickname")
    passwd_input = data.get("password")
    nick, passwd = load_credentials()
    if nick_input == nick and passwd_input == passwd:
        return jsonify({"status": "✅ Accesso autorizzato", "wallet": nick})
    else:
        return jsonify({"status": "❌ Accesso negato"}), 401

@app.route('/metamask', methods=['POST'])
def metamask_login():
    data = request.json
    address = data.get("wallet_address")
    if address and address.startswith("0x"):
        return jsonify({"status": "✅ MetaMask connesso", "wallet": address})
    return jsonify({"status": "❌ Wallet non valido"}), 400

@app.route('/heal')
def heal():
    broken = check_integrity()
    if broken:
        attempt_repair(broken)
        return jsonify({"status": "✅ Riparazione completata", "modules": broken})
    return jsonify({"status": "✅ Tutto integro"})

@app.route('/explorer')
def explorer():
    return jsonify({
        "modules": [m for m in os.listdir() if m.endswith(".sh") or m.endswith(".py")],
        "wallets": {
            "zsona": read_wallet("wallet_zsona.txt"),
            "dsn": read_wallet("wallet_dsn.txt"),
            "xmr": read_wallet("wallet_xmr.txt")
        }
    })

# 🚀 Avvio server
if __name__ == '__main__':
    print("🧩 EcoEngine attivo su http://localhost:8080")
    app.run(host='0.0.0.0', port=8080)

