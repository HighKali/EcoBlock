#!/bin/bash
mkdir -p logs

echo "🧠 Avvio modulo ricezione chain..."
PORT=8090
PID=$(lsof -nP | grep ":$PORT" | awk '{print $2}' | head -n 1)
if [ -n "$PID" ]; then
  echo "🛑 Termino processo esistente su $PORT (PID=$PID)..."
  kill -9 $PID
fi
nohup python3 scripts/eco_super_extreme_fix.py > logs/receive.log 2>&1 &

echo "🚀 Avvio server Flask su IP locale..."
nohup python3 server.py > logs/server.log 2>&1 &

IP="127.0.0.1"
echo "🖼️ Dashboard disponibile su: http://$IP:8050/panel"
echo "📡 Modulo ricezione attivo su: http://$IP:8090/node/receive"
