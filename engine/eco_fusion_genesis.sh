#!/bin/bash

# === EcoBlock + HostBlock zDOS: Fusione Genesis ===

REPO_DIR=~/ecoblock-hostblock
HOSTBLOCK_TEMP=~/hostblock-temp
WEBHOOK_URL=""  # Inserisci qui il tuo webhook Discord

echo "🌍 Inizio fusione genesis: $(date)" > "$REPO_DIR/genesis.log"

# 1. Crea struttura unificata
mkdir -p "$REPO_DIR/dashboard/assets" "$REPO_DIR/engine" "$REPO_DIR/hostblock" "$REPO_DIR/shared"

# 2. Copia EcoBlock
cp -r ~/ecoblock-dashboard/index.html "$REPO_DIR/dashboard/"
cp -r ~/ecoblock-dashboard/eco_ui_notify.js "$REPO_DIR/dashboard/"
cp -r ~/ecoblock-dashboard/assets/* "$REPO_DIR/dashboard/assets/"
cp -r ~/ecoblock-dashboard/*.sh "$REPO_DIR/engine/"
cp -r ~/ecoblock-dashboard/*.py "$REPO_DIR/shared/"

# 3. Clona HostBlock zDOS
git clone https://github.com/HighKali/hostblock-zdos "$HOSTBLOCK_TEMP"
cp -r "$HOSTBLOCK_TEMP"/* "$REPO_DIR/hostblock/"
rm -rf "$HOSTBLOCK_TEMP"

# 4. Genera README.md
cat << 'EOF' > "$REPO_DIR/README.md"
# 🌐 EcoBlock + HostBlock zDOS

Sistema unificato per dashboard visiva, orchestrazione automatizzata, RPC etico e mining collaborativo.

## 📦 Moduli principali
- Dashboard laser-style con notifiche animate
- Motore bash per orchestrazione completa
- RPC universale con FastAPI
- Moduli wallet, mining, sync condivisi
- Compatibile con Termux, Linux, VPS

## 🚀 Avvio rapido
```bash
cd ecoblock-hostblock
bash engine/eco_deploy_all.sh
