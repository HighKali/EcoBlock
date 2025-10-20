#!/bin/bash
echo "🔍 Verifica DNS..."
ping -c 1 dns.google.com &>/dev/null
if [ $? -ne 0 ]; then
  echo "⚠️ DNS non raggiungibile. Riparo /etc/resolv.conf..."
  echo -e "nameserver 8.8.8.8\nnameserver 1.1.1.1" > $PREFIX/etc/resolv.conf
else
  echo "✅ DNS funzionante"
fi

echo "🧪 Test connessione ngrok..."
ping -c 1 tunnel.us.ngrok.com &>/dev/null
if [ $? -ne 0 ]; then
  echo "❌ tunnel.us.ngrok.com non raggiungibile. Verifica rete o VPN"
else
  echo "✅ ngrok server raggiungibile"
fi

echo "🚀 Riavvio ngrok su porta 8050..."
pkill ngrok &>/dev/null
nohup ngrok http 8050 > wallet/ngrok.log 2>&1 &

sleep 5
echo "📡 Estrazione URL pubblico..."
python3 scripts/eco_ngrok_notify.py
URL=$(curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'https://[^"]*')
if [ -z "$URL" ]; then
  echo "❌ Nessun URL trovato. ngrok potrebbe non essere connesso."
else
  echo "✅ Tunnel attivo: $URL"
fi
