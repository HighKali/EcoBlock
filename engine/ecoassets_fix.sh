#!/bin/bash
PROJECT_DIR=~/ecoblock-dashboard
ASSETS_DIR="$PROJECT_DIR/assets"
LOG="$PROJECT_DIR/ecoassets.log"
echo "🖼️ Avvio EcoAssets Fix: $(date)" > "$LOG"
[ ! -d "$ASSETS_DIR" ] && echo "📁 Creo assets..." >> "$LOG" && mkdir -p "$ASSETS_DIR"
[ ! -f "$ASSETS_DIR/logo.svg" ] && echo '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><circle cx="50" cy="50" r="40" fill="#00ffcc"/></svg>' > "$ASSETS_DIR/logo.svg"
[ ! -f "$ASSETS_DIR/map.svg" ] && echo '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100"><rect x="10" y="10" width="180" height="80" stroke="#00ffcc" fill="none"/></svg>' > "$ASSETS_DIR/map.svg"
[ ! -f "$PROJECT_DIR/favicon.ico" ] && touch "$PROJECT_DIR/favicon.ico"
echo "✅ EcoAssets Fix completato." >> "$LOG"
