#!/bin/bash
echo "🚀 Avvio e pubblicazione RackChain EcoBlock–HostBlock"

# 🔁 Avvio server Flask con log visivo
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

# 🔄 Sincronizzazione ZSONA
python3 eco_sync_zsona.py

# 🧠 Generazione report
python3 eco_sync_report_gen.py

# 📊 Visualizzazione log
python3 eco_sync_log_viewer.py

# 🧪 Verifica moduli
python3 eco_ui_check.py

# 🔐 Verifica variabili .env
python3 eco_verify_env.py

# 🔧 Riparazione moduli
python3 ecoheal.py

# 📦 Backup selettivo
bash ecozip.sh

# 🛰️ Commit e push GitHub
git add .
git commit -m "🚀 RackChain EcoBlock–HostBlock: sync, report, verifica, backup, pubblicazione"
git push origin main

# 🎛️ Dashboard laser
termux-open http://127.0.0.1:8050

echo "✅ RackChain pubblicato e sincronizzato con successo"
