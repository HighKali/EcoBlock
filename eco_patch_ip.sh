#!/bin/bash
echo "🔧 Patch IP per eco_launch.sh..."

mkdir -p ~/EcoBlock/logs

cat <<LAUNCH > ~/EcoBlock/eco_launch.sh
#!/bin/bash
mkdir -p logs

echo "🧠 Avvio modulo ricezione chain..."
PORT=8090
PID=$(lsof -ti tcp:$PORT)
if [ -n "$PID" ]; then
  echo "🛑 Termino processo esistente su $PORT (PID=$PID)..."
  kill -9 $PID
fi
nohup python3 scripts/eco_super_extreme_fix.py > logs/receive.log 2>&1 &

echo "🚀 Avvio server Flask su IP pubblico..."
nohup python3 server.py > logs/server.log 2>&1 &

IP=$(ip addr show | grep 'inet ' | grep -v '127.0.0.1' | awk '{print $2}' | cut -d/ -f1 | head -n 1)
echo "🖼️ Dashboard disponibile su: http://$IP:8050/panel"
echo "📡 Modulo ricezione attivo su: http://$IP:8090/node/receive"
LAUNCH

chmod +x ~/EcoBlock/eco_launch.sh
echo "✅ eco_launch.sh aggiornato e blindato"
