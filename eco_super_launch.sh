#!/bin/bash
mkdir -p logs wallet

IP=$(ip route | grep default | awk '{print $9}' | head -n 1)
[ -z "$IP" ] && IP="127.0.0.1"

python3 -c "from eco_log import log_launch; log_launch('$IP')" || echo '{"timestamp":"'"$(date -Iseconds)"'","action":"launch","status":"ok","ip":"'"$IP"'"}' >> wallet/eco_log.json

[ -f .env ] && source .env && curl -s -X POST https://api.telegram.org/bot$BOT_TOKEN/sendMessage -d chat_id=$CHAT_ID -d text="🚀 EcoBlock dashboard avviata su $IP:8050"

pkill -f server.py
nohup python3 server.py > logs/server.log 2>&1 &

echo "🖼️ Dashboard: http://$IP:8050"
echo "📡 Modulo ricezione: http://$IP:8090/node/receive"
