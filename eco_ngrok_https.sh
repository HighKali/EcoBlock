#!/bin/bash
echo "🌐 Avvio ngrok per EcoBlock Web App su porta 8050..."
if ! command -v ngrok &> /dev/null; then
  echo "❌ ngrok non è installato. Installalo da https://ngrok.com/download"
  exit 1
fi

# Avvia ngrok in background
nohup ngrok http 8050 > wallet/ngrok.log 2>&1 &

# Attendi e mostra URL pubblico
sleep 3
echo "📡 ngrok attivo. Interfaccia web: http://127.0.0.1:4040"
echo "🔗 Visita http://127.0.0.1:4040 per vedere l’URL pubblico HTTPS"
echo "✅ EcoBlock è ora accessibile via HTTPS (tunnel ngrok)"
