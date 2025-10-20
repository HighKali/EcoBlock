#!/bin/bash
echo "🚀 Avvio ecosistema EcoBlock..."

# 1. Avvio miner loop e watchdog
echo "⛏️ Avvio miner loop..."
nohup python3 scripts/eco_zsona_miner_loop.py > wallet/miner_loop.log 2>&1 &

echo "🛡️ Avvio watchdog..."
nohup python3 scripts/eco_miner_guard.py > wallet/miner_guard.log 2>&1 &

# 2. Avvio API reward
echo "📊 Avvio API reward..."
nohup python3 scripts/eco_miner_stats.py > wallet/api.log 2>&1 &

# 3. Propagazione chain
echo "📡 Propagazione chain..."
python3 scripts/eco_miner_syncnet.py

# 4. Generazione dashboard SVG
echo "🖼️ Generazione dashboard SVG..."
python3 scripts/eco_miner_ui.py

# 5. Backup automatico
echo "🗂️ Backup in corso..."
bash scripts/eco_miner_backup.sh

# 6. Analisi AI e ranking
echo "🤖 Analisi chain..."
python3 scripts/eco_miner_ai.py
echo "🏆 Classifica address:"
python3 scripts/eco_miner_rank.py

# 7. Esportazione HTML
echo "🌐 Esportazione HTML..."
python3 scripts/eco_miner_export_html.py

# 8. Pulizia e fusione chain
echo "🧹 Pulizia chain..."
python3 scripts/eco_miner_clean.py
echo "🔗 Fusione chain..."
python3 scripts/eco_miner_fuse.py

# 9. Moduli live aggiuntivi
echo "🔄 Sync SVG..."
python3 scripts/eco_miner_sync_svg.py
echo "📄 CSV live..."
python3 scripts/eco_miner_export_csv_live.py
echo "📣 Notifica admin..."
python3 scripts/eco_miner_notify_admin.py
echo "🖼️ UI SVG live..."
python3 scripts/eco_miner_ui_live.py

# 10. Aggiornamento repository Git
echo "📦 Aggiornamento repository..."
cd ~/EcoBlock
git add .
git commit -m "🔄 Avvio completo con moduli live al 2025-10-20 19:36"
git push

echo "✅ Ecosistema EcoBlock avviato e repository aggiornato"
