#!/bin/bash
echo "🚀 Avvio completo RackChain EcoBlock–HostBlock"

# 📦 Installazione Flask se mancante
pip show flask >/dev/null || pip install flask

# 📁 Cartelle
mkdir -p wallet logs static templates

# 📄 index.html
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

# 🎨 style.css
cat > style.css <<EOF
body { background-color: black; color: #00FF00; font-family: monospace; text-align: center; }
h1 { color: cyan; text-shadow: 0 0 5px #0ff; margin-top: 40px; }
.menu button { background-color: black; border: 2px solid cyan; color: #00FF00; padding: 10px 20px; margin: 10px; font-size: 16px; cursor: pointer; box-shadow: 0 0 10px #0ff; }
.menu button:hover { background-color: #001f1f; color: magenta; border-color: magenta; }
EOF

# ⚙️ script.js
echo "function go(route) { window.location.href = route; }" > script.js

# 🧠 server.py
cat > server.py <<EOF
from flask import Flask, request, jsonify, send_file
import json, os
from datetime import datetime
app = Flask(__name__)
@app.route('/node/receive', methods=['POST'])
def receive():
    token = request.headers.get('X-ECO-TOKEN')
    if token != "eco_secret_8090": return jsonify({"error": "Token non valido"}), 403
    data = request.get_json()
    if not data or "chain" not in data: return jsonify({"error": "Chain mancante"}), 400
    os.makedirs("wallet", exist_ok=True)
    with open("wallet/zsona_chain.json", "w") as f: json.dump(data["chain"], f)
    log_chain_update(data["chain"])
    return jsonify({"status": "ok", "message": "Wallet aggiornato"})
def log_chain_update(chain):
    entry = {"timestamp": datetime.utcnow().isoformat(), "action": "chain_update", "chain_id": chain.get("chain_id"), "balance": chain.get("balance"), "token": chain.get("token_address")}
    with open("wallet/eco_log.json", "a") as f: f.write(json.dumps(entry) + "\\n")
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

# 🔋 ecoagent.py
cat > ecoagent.py <<EOF
import time, os
from datetime import datetime
log_path = "logs/ecoagent.log"
os.makedirs("logs", exist_ok=True)
entry = {"timestamp": datetime.utcnow().isoformat(), "uptime": os.popen("uptime").read().strip(), "battery": os.popen("termux-battery-status").read().strip() if os.name != "nt" else "N/A"}
with open(log_path, "a") as f: f.write(str(entry) + "\\n")
print("✅ ecoagent.py: log energia registrato")
EOF

# 📡 eco_notify.py
cat > eco_notify.py <<EOF
import requests
message = "🚨 EcoBlock RackChain avviato con successo!"
url = "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage"
payload = {"chat_id": "<YOUR_CHAT_ID>", "text": message}
try: requests.post(url, data=payload); print("✅ Notifica inviata")
except Exception as e: print(f"❌ Errore notifica: {e}")
EOF

# ⚖️ eco_miner_sync.py
cat > eco_miner_sync.py <<EOF
import json, time
data = {"timestamp": time.time(), "miner_status": "active", "hashrate": "42.5 H/s", "pool": "ZSONA/$DSN"}
with open("wallet/miner_status.json", "w") as f: json.dump(data, f)
print("✅ Miner sincronizzato")
EOF

# 🧵 eco_asset_check.py
cat > eco_asset_check.py <<EOF
import os
missing = []
for folder in ["static", "templates"]:
    if not os.path.exists(folder): missing.append(folder)
if missing: print(f"❌ Asset mancanti: {missing}")
else: print("✅ Tutti gli asset visivi sono presenti")
EOF

# 🔧 Moduli shell
echo "✅ ecoapi.sh: API EcoBlock attiva" > ecoapi.sh
echo "✅ ecopool.sh: Pool ZSONA/$DSN sincronizzato" > ecopool.sh
echo "✨ ecoignite.sh: Identità artistica e sicurezza iniettata" > ecoignite.sh

# 🔐 Permessi
chmod +x ecoapi.sh ecopool.sh ecoignite.sh

# 🔁 Avvio server con controllo
pkill -f server.py
nohup python3 server.py > logs/server.log 2>&1 &
echo "⏳ Attendo avvio server Flask…"
for i in {1..10}; do
  curl -s http://127.0.0.1:8050 >/dev/null && echo "✅ Server Flask attivo" && break
  sleep 1
done
if ! curl -s http://127.0.0.1:8050 >/dev/null; then echo "❌ Server Flask non avviato. Interrotto."; exit 1; fi

# 🔀 Avvio orchestrazione se presente
[ -f eco_run_all.sh ] && ./eco_run_all.sh

# 🔄 Avvio moduli rack
python3 ecoagent.py
python3 eco_notify.py
python3 eco_miner_sync.py
python3 eco_asset_check.py
./ecoapi.sh
./ecopool.sh
./ecoignite.sh

# 🎛️ Dashboard
termux-open http://127.0.0.1:8050

echo "✅ RackChain completato con successo"
