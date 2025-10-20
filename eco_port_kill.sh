#!/bin/bash
PORT=8090
echo "🔍 Verifico processo sulla porta $PORT..."
PID=$(lsof -ti tcp:$PORT)

if [ -z "$PID" ]; then
  echo "✅ Nessun processo attivo su $PORT"
else
  echo "🛑 Processo trovato: PID=$PID → lo termino..."
  kill -9 $PID
  echo "✅ Processo terminato"
fi

echo "🚀 Riavvio eco_super_extreme_fix.py..."
python3 scripts/eco_super_extreme_fix.py
