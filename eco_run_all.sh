# 🔁 Riavvia server Flask con controllo attivo
pkill -f server.py
nohup python3 server.py > logs/server.log 2>&1 &

echo "⏳ Attendo avvio server Flask…"
for i in {1..10}; do
  curl -s http://127.0.0.1:8050 >/dev/null && echo "✅ Server Flask attivo" && break
  sleep 1
done

if ! curl -s http://127.0.0.1:8050 >/dev/null; then
  echo "❌ Server Flask non avviato. Interrotto."
  exit 1
fi
