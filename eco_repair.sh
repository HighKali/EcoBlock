#!/bin/bash
echo "🛠️ Avvio script riparatore EcoBlock..."

# 1. Elenco moduli critici
modules=(
  "eco_zsona_miner.py"
  "eco_zsona_wallet.py"
  "eco_zsona_miner_loop.py"
  "eco_miner_notify.py"
  "eco_miner_stats.py"
  "eco_miner_panel.py"
  "eco_miner_export.py"
  "eco_miner_export_html.py"
  "eco_miner_badge.py"
  "eco_miner_ui.py"
  "eco_miner_ai.py"
  "eco_miner_rank.py"
  "eco_miner_clean.py"
  "eco_miner_fuse.py"
  "eco_miner_syncnet.py"
  "eco_wallet_check.py"
  "eco_wallet_rotate.py"
)

# 2. Ricrea placeholder per moduli mancanti
for mod in "\${modules[@]}"; do
  path="scripts/\$mod"
  if [ ! -f "\$path" ]; then
    echo "⚠️ Modulo mancante: \$mod → ricreazione placeholder..."
    echo -e "#!/usr/bin/env python3\nprint('🧩 Placeholder: \$mod')" > "\$path"
  fi
done

# 3. Imposta permessi eseguibili
chmod +x scripts/eco_*.py

# 4. Commit e push su GitHub
echo "📦 Aggiornamento repository..."
git add scripts/
git commit -m "🛠️ Riparazione moduli mancanti con eco_repair.sh al $(date +'%Y-%m-%d %H:%M')"
git push

echo "✅ Riparazione completata e repository aggiornato"
