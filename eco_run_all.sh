#!/bin/bash
echo "🚀 Avvio completo EcoBlock: installazione, dashboard, moduli, sync, report, GitHub"

# 📦 Installazione Flask se mancante
pip show flask >/dev/null || pip install flask

# 🧹 Pulizia file corrotti
find wallet -type f \( -name "*.json" -o -name "*.log" \) -exec bash -c 'jq empty {} 2>/dev/null || rm -v {}' \;

# 📎 Ricrea wallet
mkdir -p wallet logs
touch wallet/zsona_sync_log.json wallet/eco_log.json
echo '{"chain_id":"ZSONA-ROBERTO-0001","token_address":"0xfc90516a1f736FaC557e09D8853dB80dA192c296","dex":{"url":"http://127.0.0.1:8050/dex"},"pool":{"url":"http://127.0.0.1:8050/pool"},"balance":"0.00"}' > wallet/zsona_chain.json

# 🖥️ Crea index.html
cat > index.html <<EOF
<!DOCTYPE html>
<html><head><title>EcoBlock ZSONA Portal</title><link rel="stylesheet" href="style.css"></head>
<body><h1>EcoBlock ZSONA Portal</h1><div class="menu">
<button onclick="go('/faucet_dsn')">Faucet DSN</button>
<button onclick="go('/faucet_zsona')">Faucet ZSONA</button>
<button onclick="go('/miner')">Miner Web</button>
<button onclick="go('/wallet')">Wallet</button>
<button onclick="go('/dex')">DEX</button>
<button onclick="go('/pool')">POOL</button>
<button onclick="go('/report')">Visualizza Report</button>
</div><script src="script.js"></script></body></html>
EOF

# 🎨 Crea style.css
cat > style.css <<EOF
body { background-color: black; color: #00FF00; font-family: monospace; text-align: center; }
h1 { color: cyan; text-shadow: 0 0 5px #0ff; margin-top: 40px; }
.menu button { background-color: black; border: 2px solid cyan; color: #00FF00; padding: 10px 20px; margin: 10px; font-size: 16px; cursor: pointer; box-shadow: 0 0 10px #0ff; }
.menu button:hover { background-color: #001f1f; color: magenta; border-color: magenta; }
EOF

# ⚙️ Crea script.js
echo "function go(route) { window.location.href = route; }" > script.js

# 🧠 Crea server.py
cat > server.py <<EOF
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
        f.write(json.dumps(entry) + "\\n")

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
EOF

# 🔁 Riavvia server Flask
pkill -f server.py
nohup python3 server.py > logs/server.log 2>&1 &
sleep 2
lsof -i :8050 | grep LISTEN && echo "✅ Server Flask attivo" || echo "❌ Server Flask non rilevato"

# 🔄 Avvia sincronizzazione ZSONA
python3 eco_sync_zsona.py &
sleep 5

# 🖼️ Genera report HTML
python3 eco_sync_report_gen.py

# 📊 Visualizza log
python3 eco_sync_log_viewer.py

# 🔐 Commit e push GitHub
git add .
git commit -m "🚀 Avvio completo EcoBlock: dashboard, moduli, sync, report, ricezione"
git push origin main

echo "✨ Dashboard laser attiva su http://127.0.0.1:8050"
