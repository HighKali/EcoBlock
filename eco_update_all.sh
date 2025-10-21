#!/bin/bash
echo "🚀 Avvio EcoBlock: pulizia, sincronizzazione, report e aggiornamento GitHub"

# 🧹 Rimuove file corrotti
find wallet -type f \( -name "*.json" -o -name "*.log" \) -exec bash -c 'jq empty {} 2>/dev/null || rm -v {}' \;

# 📎 Ricrea file wallet
mkdir -p wallet
touch wallet/zsona_sync_log.json wallet/eco_log.json
echo '{"chain_id":"ZSONA-ROBERTO-0001","token_address":"0xfc90516a1f736FaC557e09D8853dB80dA192c296","dex":{"url":"http://127.0.0.1:8050/dex"},"pool":{"url":"http://127.0.0.1:8050/pool"},"balance":"0.00"}' > wallet/zsona_chain.json

# 🔁 Riavvia server Flask
pkill -f server.py
nohup python3 server.py > logs/server.log 2>&1 &
sleep 2
lsof -i :8050 | grep LISTEN && echo "✅ Server Flask attivo" || echo "❌ Server Flask non rilevato"

# 🔄 Esegue sincronizzazione ZSONA
python3 eco_sync_zsona.py &
sleep 5

# 🖼️ Genera report HTML
python3 eco_sync_report_gen.py

# 📊 Visualizza log
python3 eco_sync_log_viewer.py

# 🔐 Aggiorna repository GitHub
git add .
git commit -m "🧹 Pulizia, sincronizzazione ZSONA, report HTML e aggiornamento EcoBlock"
git push origin main
