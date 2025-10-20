#!/bin/bash
echo "🚀 Avvio ecosistema EcoBlock..."

# Miner loop, watchdog, API
nohup python3 scripts/eco_zsona_miner_loop.py > wallet/miner_loop.log 2>&1 &
nohup python3 scripts/eco_miner_guard.py > wallet/miner_guard.log 2>&1 &
nohup python3 scripts/eco_miner_stats.py > wallet/api.log 2>&1 &

# Sync, dashboard, backup
python3 scripts/eco_miner_syncnet.py
python3 scripts/eco_miner_ui.py
bash scripts/eco_miner_backup.sh

# AI, ranking, HTML, pulizia, fusione
python3 scripts/eco_miner_ai.py
python3 scripts/eco_miner_rank.py
python3 scripts/eco_miner_export_html.py
python3 scripts/eco_miner_clean.py
python3 scripts/eco_miner_fuse.py

# Moduli live
python3 scripts/eco_miner_sync_svg.py
python3 scripts/eco_miner_export_csv_live.py
python3 scripts/eco_miner_notify_admin.py
python3 scripts/eco_miner_ui_live.py

# Temi, sync globale, Matrix, UI pack
python3 scripts/eco_miner_theme.py
python3 scripts/eco_miner_sync_all.py
python3 scripts/eco_miner_notify_matrix.py
bash scripts/eco_miner_ui_pack.sh

# Moduli finali
python3 scripts/eco_miner_ui_theme_switcher.py
python3 scripts/eco_miner_notify_status.py
python3 scripts/eco_miner_sync_remote.py
nohup python3 scripts/eco_miner_ui_live_server.py > wallet/ui_server.log 2>&1 &
nohup python3 scripts/eco_miner_ui_live_refresh.py > wallet/ui_refresh.log 2>&1 &
python3 scripts/eco_miner_notify_all.py
python3 scripts/eco_miner_ui_theme_random.py

# Git push
cd ~/EcoBlock
git add .
git commit -m "🔒 Finalizzazione totale: sync, UI, notifiche, temi, server al 2025-10-20 20:16"
git push

echo "✅ Ecosistema EcoBlock blindato e definitivo"
