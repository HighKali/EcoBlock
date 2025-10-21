#!/bin/bash
echo "🔁 Riavvio server Flask + sincronizzazione ZSONA"

# 📦 Crea cartella log se non esiste
mkdir -p logs

# 🔁 Termina processi attivi
pkill -f server.py
pkill -f eco_sync_zsona.py

# 🚀 Riavvia server Flask
nohup python3 server.py > logs/server.log 2>&1 &
sleep 2
lsof -i :8050 | grep LISTEN && echo "✅ Server Flask attivo su porta 8050" || echo "❌ Server Flask non rilevato"

# 🔄 Riavvia sincronizzazione ZSONA
nohup python3 eco_sync_zsona.py > logs/sync.log 2>&1 &
sleep 2
echo "✅ eco_sync_zsona.py avviato"

# 📡 Verifica endpoint
curl -s http://127.0.0.1:8050/dex | grep status && echo "✅ Endpoint /dex attivo" || echo "❌ Errore /dex"
curl -s http://127.0.0.1:8050/pool | grep status && echo "✅ Endpoint /pool attivo" || echo "❌ Errore /pool"
