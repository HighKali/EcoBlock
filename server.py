from flask import Flask, request, jsonify, send_file
import json, os
from datetime import datetime

app = Flask(__name__)

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
    return jsonify({"status": "ok", "message": "Wallet aggiornato"})

def log_chain_update(chain):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": "chain_update",
        "chain_id": chain.get("chain_id"),
        "balance": chain.get("balance"),
        "token": chain.get("token_address")
    }
    with open("wallet/eco_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")

@app.route("/")             ; def home(): return send_file("index.html")
@app.route("/style.css")    ; def style(): return send_file("style.css")
@app.route("/script.js")    ; def script(): return send_file("script.js")
@app.route("/report")       ; def report(): return send_file("eco_sync_report.html")
@app.route("/faucet_dsn")   ; def faucet_dsn(): return "<h2>Modulo attivo: Faucet DSN</h2>"
@app.route("/faucet_zsona") ; def faucet_zsona(): return "<h2>Modulo attivo: Faucet ZSONA</h2>"
@app.route("/miner")        ; def miner(): return "<h2>Modulo attivo: Miner Web ZSONA</h2>"
@app.route("/wallet")       ; def wallet(): return "<h2>Modulo attivo: Wallet</h2>"
@app.route("/dex")          ; def dex(): return jsonify({"volume_24h": 125000})
@app.route("/pool")         ; def pool(): return jsonify({"apy": "12.5%"})

if __name__ == "__main__": app.run(host="0.0.0.0", port=8050)
