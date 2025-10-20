#!/bin/bash
mkdir -p logs wallet

IP_MODE="local"; NOTIFY=true; LAUNCH=true; PACK=false
for arg in "$@"; do case $arg in
  --public) IP_MODE="public" ;;
  --local) IP_MODE="local" ;;
  --silent) NOTIFY=false ;;
  --log-only) LAUNCH=false ;;
  --pack) PACK=true ;;
esac; done

[ "$IP_MODE" = "public" ] && IP=$(ip route | grep default | awk '{print $9}' | head -n 1)
[ -z "$IP" ] && IP="127.0.0.1"

python3 -c "from eco_log import log_launch; log_launch('$IP')" || echo '{"timestamp":"'"$(date -Iseconds)"'","action":"launch","status":"ok","ip":"'"$IP"'"}' >> wallet/eco_log.json

[ "$NOTIFY" = true ] && [ -f .env ] && source .env && curl -s -X POST https://api.telegram.org/bot$BOT_TOKEN/sendMessage -d chat_id=$CHAT_ID -d text="✅ EcoBlock avviato su $IP:8050"

if [ "$LAUNCH" = true ]; then
  PORT=8090; PID=$(lsof -nP 2>/dev/null | grep ":$PORT" | awk '{print $2}' | head -n 1)
  [ -n "$PID" ] && echo "🛑 Kill PID=$PID" && kill -9 $PID
  nohup python3 scripts/eco_super_extreme_fix.py > logs/receive.log 2>&1 &
  nohup python3 server.py > logs/server.log 2>&1 &
  echo "🖼️ Dashboard: http://$IP:8050/panel"
  echo "📡 Modulo ricezione: http://$IP:8090/node/receive"
else
  echo "📝 Avvio registrato, modulo non lanciato (--log-only)"
fi

[ "$PACK" = true ] && echo "📦 Creo ZIP..." && zip -r EcoBlock-blindato.zip . -x "*.pyc" "__pycache__" "venv" ".git" "*.log" "logs/*.log" && echo "✅ Pacchetto creato"
