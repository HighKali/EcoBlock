#!/bin/bash
echo "🧹 Rimozione ngrok v2 (se presente)..."
rm -f ~/EcoBlock/ngrok

echo "📦 Estrazione ngrok v3..."
unzip -o ngrok-v3-stable-linux-arm.zip
mv ngrok ~/EcoBlock/ngrok
chmod +x ~/EcoBlock/ngrok

echo "🔍 Verifica versione..."
~/EcoBlock/ngrok version

echo "🔐 Autenticazione ngrok v3..."
~/EcoBlock/ngrok config add-authtoken 32szAFccNTpxEa4dK8bl1s2V7P6_5Lg7x7fm4BvNtWuyRmM9u

echo "🚀 Avvio tunnel HTTPS in foreground su porta 8050..."
echo "📡 Attendi: l’URL pubblico apparirà qui sotto ⬇️"
~/EcoBlock/ngrok http 8050
