#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_credentials():
    try:
        with open("credentials.txt", "r") as f:
            line = f.read().strip()
            nick, passwd = line.split(":")
            return nick, passwd
    except:
        return None, None

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

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    print("🔐 EcoAuth attivo su http://localhost:5000/login")
    app.run(host='0.0.0.0', port=5000)
