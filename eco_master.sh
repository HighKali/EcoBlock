#!/bin/bash
echo "🚀 Avvio script maestro EcoBlock–HostBlock"

# 🔁 Sync moduli e DEX
python3 eco_sync_zsona.py
python3 eco_dex_sync.py

# 📊 Grafico APY
python3 eco_chart_apy.py

# 🪪 Badge NFT firmati
python3 eco_badges.py

# 🗳️ Votazione su ecoheal
python3 eco_vote.py

# 🔐 Tutela automatica
VOTED_YES=$(cat voto_ecoheal.txt | grep "✅" | awk '{print $4}')
if [ "$VOTED_YES" -ge 7 ]; then
  echo "✅ Maggioranza raggiunta. Attivo ecoheal.py"
  python3 ecoheal.py
else
  echo "⚠️ Voto insufficiente. ecoheal.py non attivato"
fi

# 🧠 Analisi OSINT
python3 eco_osint_guard.py

# 🛰️ Avvio server Flask + WebSocket
pkill -f server.py
sleep 1
nohup python3 server.py > logs/server.log 2>&1 &
sleep 3

# 🌐 Genera dashboard
cat > index.html <<EOF
<!DOCTYPE html>
<html><head><title>EcoBlock Dashboard</title>
<link rel="stylesheet" href="style.css">
</head><body>
<h1 style="text-align:center;color:cyan;">🚀 EcoBlock–HostBlock Dashboard</h1>
<iframe src="chart_apy.html" width="100%" height="300" style="border:none;"></iframe>
<iframe src="badges.html" width="100%" height="200" style="border:none;"></iframe>
<img src="voto_ecoheal.png" width="100%">
<p style="text-align:center;color:#00FF00;">✨ Tutto sincronizzato e pubblicato. Powered by RackChain.</p>
</body></html>
EOF

cp index.html rackchain.html

# 📦 Pulizia
bash eco_purge.sh
git clean -fdx

# 📘 README aggiornato
python3 eco_readme.py

# 🛰️ Commit e push
git add .
git commit -m "🚀 Aggiornamento completo: sync, voto, firma, dashboard"
git push origin main

# 🔔 Notify
if [ -f .env ]; then
  source .env
  if [ ! -z "$TELEGRAM_TOKEN" ] && [ ! -z "$TELEGRAM_CHAT_ID" ]; then
    curl -s -X POST https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage \
      -d chat_id=$TELEGRAM_CHAT_ID \
      -d text="✅ EcoBlock aggiornato: $(date +%H:%M)"
  fi
fi

# 🔗 Alias
echo "alias eco_master='bash ~/EcoBlock/eco_master.sh'" >> ~/.profile
source ~/.profile

echo "✅ Tutto attivo. Usa 'eco_master' per rilanciare l’intero ecosistema."
