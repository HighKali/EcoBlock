#!/bin/bash

echo "🚀 Avvio EcoBlock + Serveo Tunnel + QR"

# 🧠 Avvia server Flask se non attivo
if ! pgrep -f server.py > /dev/null; then
  echo "🛰️ Avvio server.py in background..."
  nohup python3 server.py > logs/server.log 2>&1 &
  sleep 3
else
  echo "✅ server.py già attivo"
fi

# 🔌 Avvia tunnel Serveo
echo "🌐 Connessione a Serveo..."
ssh -o StrictHostKeyChecking=no -R 80:localhost:8050 serveo.net > serveo.log 2>&1 &
sleep 5

# 🔗 Estrai URL Serveo
URL=$(grep -o 'https://[a-zA-Z0-9]\+\.serveo\.net' serveo.log | head -n1)

if [ -z "$URL" ]; then
  echo "❌ Errore: URL Serveo non trovato"
  exit 1
fi

echo "✅ URL pubblico: $URL"

# 📱 Genera QR code
if command -v qrencode > /dev/null; then
  qrencode -o qr_serveo.png "$URL"
  echo "📦 QR code salvato in qr_serveo.png"
else
  echo "⚠️ qrencode non installato. Installa con: sudo apt install qrencode"
fi

# 💡 LED log
if [ -f dex_led.log ]; then
  echo "💡 Stato DEX:"
  cat dex_led.log
else
  echo "🟡 dex_led.log non trovato"
fi

# 🕒 Timestamp
echo "🕒 Ultimo aggiornamento: $(date '+%Y-%m-%d %H:%M:%S')"
