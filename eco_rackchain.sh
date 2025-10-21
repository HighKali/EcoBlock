#!/bin/bash
echo "🚀 Avvio RackChain EcoBlock–HostBlock in corso…"

# 🧱 PATCH PANEL (IP detection + fallback)
echo "🔌 [1U] Patch Panel: rilevamento IP..."
IP=$(ip route get 1 | awk '{print $NF;exit}')
echo "🌐 IP rilevato: $IP"

# 🔀 SWITCH (orchestrazione)
echo "🔀 [1U] Switch: avvio orchestrazione eco_run_all.sh..."
./eco_run_all.sh || echo "⚠️ eco_run_all.sh fallito"

# 🖥️ SERVER (moduli attivi)
echo "🖥️ [2U] Server: verifica moduli Flask..."
curl -s http://127.0.0.1:8050 >/dev/null && echo "✅ Server attivo" || echo "❌ Server non raggiungibile"

# 🔐 FIREWALL (verifica ambienti)
echo "🛡️ [1U] Firewall: verifica ambienti..."
python3 eco_verify_env.py || echo "⚠️ eco_verify_env.py errore"

# 💾 STORAGE (report + log)
echo "💾 [3U] Storage: generazione report..."
python3 eco_sync_report_gen.py && echo "✅ Report generato"

# ⚡ PDU (monitoraggio energia)
echo "⚡ [2U] PDU: log energia e uptime..."
python3 ecoagent.py || echo "⚠️ ecoagent.py non disponibile"

# 📡 ROUTER (notifiche globali)
echo "📡 [2U] Router: invio notifiche..."
python3 eco_notify.py || echo "⚠️ eco_notify.py non configurato"

# 🔋 UPS (ripristino moduli)
echo "🔋 [3U] UPS: avvio auto-riparazione..."
python3 ecoheal.py || echo "⚠️ ecoheal.py non disponibile"

# ⚖️ LOAD BALANCER (miner pool)
echo "⚖️ [1U] Load Balancer: sincronizzazione miner..."
python3 eco_miner_sync.py || echo "⚠️ eco_miner_sync.py non disponibile"

# 🎛️ KVM SWITCH (dashboard laser)
echo "🎛️ [1U] KVM Switch: attivazione dashboard..."
termux-open http://127.0.0.1:8050

# 🧵 CABLE ORGANIZER (asset check)
echo "🧵 [1U] Cable Organizer: verifica asset visivi..."
python3 eco_asset_check.py || echo "⚠️ eco_asset_check.py non disponibile"

echo "✅ RackChain EcoBlock–HostBlock completato con successo."
