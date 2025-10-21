#!/bin/bash
echo "🔧 Correzione automatica degli ultimi 3 errori..."

# 1️⃣ Correggi le route nel server.py
echo "🛠️ Correzione server.py..."
sed -i 's/@app.route("\/") *; */@app.route("\/")\n/g' server.py
sed -i 's/def home(): return send_file("index.html")/def home():\n    return send_file("index.html")/g' server.py
sed -i 's/@app.route("\/style.css") *; */@app.route("\/style.css")\n/g' server.py
sed -i 's/def style(): return send_file("style.css")/def style():\n    return send_file("style.css")/g' server.py
sed -i 's/@app.route("\/script.js") *; */@app.route("\/script.js")\n/g' server.py
sed -i 's/def script(): return send_file("script.js")/def script():\n    return send_file("script.js")/g' server.py
sed -i 's/@app.route("\/report") *; */@app.route("\/report")\n/g' server.py
sed -i 's/def report(): return send_file("eco_sync_report.html")/def report():\n    return send_file("eco_sync_report.html")/g' server.py

# 2️⃣ Riavvia il server Flask con controllo reale
echo "🔁 Riavvio server Flask..."
pkill -f server.py
mkdir -p logs
nohup python3 server.py > logs/server.log 2>&1 &
echo "⏳ Attendo avvio server Flask…"
for i in {1..10}; do
  if curl -s http://127.0.0.1:8050 | grep -q "EcoBlock"; then
    echo "✅ Server Flask attivo"
    break
  fi
  sleep 1
done
if ! curl -s http://127.0.0.1:8050 | grep -q "EcoBlock"; then
  echo "❌ Server Flask non avviato. Log:"
  tail -n 20 logs/server.log
  exit 1
fi

# 3️⃣ Esegui eco_rackchain_commit.sh
echo "🚀 Esecuzione flusso completo RackChain..."
./eco_rackchain_commit.sh

echo "✅ Correzione e rilancio completati"
