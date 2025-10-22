#!/bin/bash
echo "🚀 Avvio sincronizzazione DEX con fallback e verifica server"

# 🛰️ Avvia server se non attivo
if ! pgrep -f server.py > /dev/null; then
  echo "🧠 Server non attivo. Avvio ora..."
  nohup python3 server.py > logs/server.log 2>&1 &
  sleep 5
fi

# 🔍 Attendi che /dex sia disponibile
for i in {1..10}; do
  if curl -s http://127.0.0.1:8050/dex | grep -q "volume"; then
    echo "✅ /dex disponibile"
    break
  else
    echo "⏳ Attesa /dex… ($i)"
    sleep 2
  fi
done

# 🔄 Esegui sincronizzazione
python3 eco_dex_sync.py

# 📦 Verifica output
if [ -f dex_data.json ]; then
  echo "✅ File dex_data.json generato:"
  cat dex_data.json
else
  echo "❌ Errore: dex_data.json non trovato"
fi
