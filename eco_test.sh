#!/bin/bash
echo "🔍 Test EcoBlock"
IP=$(ip route | grep default | awk '{print $9}' | head -n 1)
[ -z "$IP" ] && IP="127.0.0.1"
echo "✅ IP rilevato: $IP"
[ -f wallet/eco_log.json ] && echo "✅ Log presente" || echo "❌ Log mancante"
lsof -i :8050 | grep LISTEN && echo "✅ Server Flask attivo" || echo "❌ Server Flask non rilevato"
lsof -i :8090 | grep LISTEN && echo "✅ Modulo ricezione attivo" || echo "❌ Modulo ricezione non rilevato"
RESPONSE=$(curl -s -X POST http://127.0.0.1:8090/node/receive -H "Content-Type: application/json" -H "X-ECO-TOKEN: eco_secret_8090" -d @wallet/zsona_chain.json)
echo "$RESPONSE" | grep "Wallet aggiornato" && echo "✅ Ricezione funzionante" || echo "❌ Errore ricezione"
[ -f .env ] && source .env && curl -s -X POST https://api.telegram.org/bot$BOT_TOKEN/sendMessage -d chat_id=$CHAT_ID -d text="✅ Test EcoBlock completato" && echo "✅ Notifica Telegram inviata" || echo "⚠️ Notifica Telegram non configurata"
