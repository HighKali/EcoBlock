#!/bin/bash

# === EcoBlock Update All ===
# Esegue setup UI + orchestrazione completa

PROJECT_DIR=~/ecoblock-dashboard
LOG="$PROJECT_DIR/eco_update_all.log"

echo "🚀 Avvio aggiornamento completo: $(date)" > "$LOG"

# 1. Setup UI visiva e notifiche
echo "🎨 Esecuzione eco_ui_setup.sh..." >> "$LOG"
bash "$PROJECT_DIR/eco_ui_setup.sh" >> "$LOG" 2>&1

# 2. Orchestrazione completa
echo "🔧 Esecuzione ecoengine.sh..." >> "$LOG"
bash "$PROJECT_DIR/ecoengine.sh" >> "$LOG" 2>&1

echo "✅ Aggiornamento completo eseguito. Log in eco_update_all.log"
