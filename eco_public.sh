#!/bin/bash
echo "🌐 Attivazione EcoBlock–HostBlock in modalità pubblica"

# 🔍 Rileva IP pubblico
IP=$(curl -s https://api.ipify.org)
echo "🌍 IP pubblico rilevato: $IP"

# 🧠 Copia report su /rackchain
cp eco_rackchain_report.html rackchain.html

# 📘 Aggiorna README con link pubblico e QR
cat > README.md <<EOT
# 🚀 EcoBlock–HostBlock RackChain (Pubblico)

**Ultimo aggiornamento:** $(date +"%Y-%m-%d %H:%M:%S")

## 🌐 Accesso pubblico

- Dashboard: [http://$IP:8050](http://$IP:8050)
- Report neon: [http://$IP:8050/rackchain](http://$IP:8050/rackchain)

## 📱 QR Code

Scansiona per accedere alla dashboard:

\`\`\`bash
qrencode -t ANSIUTF8 "http://$IP:8050"
\`\`\`

## 🔧 Moduli attivi

- \`server.py\` — Server Flask
- \`eco_sync_zsona.py\` — Sincronizzazione
- \`eco_ui_check.py\` — Verifica moduli
- \`eco_notify.py\` — Notifiche Telegram
- \`eco_rackchain_report.html\` — Report neon
- \`rackchain.html\` — Accesso pubblico
- \`eco_sync_daemon.sh\` — Sync automatico

## 📦 Pubblicazione

\`\`\`bash
git add .
git commit -m "🌐 EcoBlock pubblicato su IP pubblico"
git push origin main
\`\`\`
EOT

# 🛰️ Commit e push
git add .
git commit -m "🌐 EcoBlock pubblicato su IP pubblico con QR"
git push origin main

echo "✅ EcoBlock ora accessibile pubblicamente su http://$IP:8050"
echo "📱 Scansiona il QR con 'qrencode -t ANSIUTF8 \"http://$IP:8050\"'"
