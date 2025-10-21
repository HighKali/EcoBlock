from flask import Flask, request, jsonify, render_template
import json, os
from datetime import datetime

app = Flask(__name__, template_folder="templates", static_folder="static")

# 🔐 Modulo ricezione
@app.route('/node/receive', methods=['POST'])
def receive():
    token = request.headers.get('X-ECO-TOKEN')
    if token != "eco_secret_8090":
        return jsonify({"error": "Token non valido"}), 403
    data = request.get_json()
    if not data or "chain" not in data:
        return jsonify({"error": "Chain mancante"}), 400
    os.makedirs("wallet", exist_ok=True)
    with open("wallet/zsona_chain.json", "w") as f:
        json.dump(data["chain"], f)
    log_chain_update(data["chain"])
    return jsonify({"status": "ok", "message": "Wallet aggiornato con successo"}), 200

# 🧠 Logging automatico
def log_chain_update(chain):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": "chain_update",
        "chain_id": chain.get("chain_id"),
        "balance": chain.get("balance"),
        "token": chain.get("token")
    }
    os.makedirs("wallet", exist_ok=True)
    with open("wallet/eco_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")

# 📡 Endpoint DEX
@app.route('/dex')
def dex():
    return jsonify({
        "status": "online",
        "pairs": ["DSN/USDT", "DSN/BTC"],
        "volume_24h": 125000,
        "fee": "0.3%",
        "liquidity": 500000
    })

# 📡 Endpoint Pool
@app.route('/pool')
def pool():
    return jsonify({
        "status": "active",
        "participants": 42,
        "total_staked": 750000,
        "reward_token": "NETkali $DSN",
        "apy": "12.5%"
    })

# 🖼️ Dashboard retrò
@app.route('/')
def dashboard():
    return render_template("dashboard.html")

# 🚀 Avvio server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)
