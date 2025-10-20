#!/bin/bash

echo "🌐 Avvio tunnel ngrok per dashboard (porta 8080)..."
./ngrok http 8080 > ~/dashboard_ngrok.log &
sleep 5
DASHBOARD_URL=$(grep -o 'https://[0-9a-zA-Z.-]*\.ngrok.io' ~/dashboard_ngrok.log | head -n1)

echo "🌐 Avvio tunnel ngrok per nodo RPC (porta 8000)..."
./ngrok http 8000 > ~/rpc_ngrok.log &
sleep 5
RPC_URL=$(grep -o 'https://[0-9a-zA-Z.-]*\.ngrok.io' ~/rpc_ngrok.log | head -n1)

echo "✅ Dashboard online: $DASHBOARD_URL"
echo "✅ Nodo RPC online: $RPC_URL"
