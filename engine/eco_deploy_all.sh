#!/bin/bash

# === EcoBlock Deploy All ===
# UI + Engine + ZIP + GitHub + Contributors

PROJECT_DIR=~/ecoblock-dashboard
LOG="$PROJECT_DIR/eco_deploy_all.log"
ZIP_SCRIPT="$PROJECT_DIR/ecozip.sh"
WEBHOOK_URL=""  # Inserisci qui il tuo webhook Discord se vuoi notifiche

echo "🚀 Avvio deploy completo: $(date)" > "$LOG"

# 1. UI Setup
echo "🎨 Esecuzione eco_ui_setup.sh..." >> "$LOG"
bash "$PROJECT_DIR/eco_ui_setup.sh" >> "$LOG" 2>&1

# 2. Orchestrazione
echo "🔧 Esecuzione ecoengine.sh..." >> "$LOG"
bash "$PROJECT_DIR/ecoengine.sh" >> "$LOG" 2>&1

# 3. Packaging ZIP
echo "📦 Esecuzione ecozip.sh..." >> "$LOG"
bash "$ZIP_SCRIPT" >> "$LOG" 2>&1

# 4. Generazione CONTRIBUTORS.md
CONTRIB="$PROJECT_DIR/CONTRIBUTORS.md"
cat << 'EOF' > "$CONTRIB"
# 🌍 EcoBlock Contributors

| Nome        | Ruolo                         | Specialità                                   | Impatto                         |
|-------------|-------------------------------|----------------------------------------------|----------------------------------|
| Roberto     | Fondatore e Architetto        | Blockchain etica, UI laser, automazione      | Visione, orchestrazione, arte   |
| Collaboratori futuri | TBD                 | TBD                                          | TBD                              |

> ✨ Questo file celebra chi costruisce EcoBlock. Ogni contributo è tracciato, visibile e valorizzato.

EOF
echo "✅ CONTRIBUTORS.md generato" >> "$LOG"

# 5. Commit e push
echo "📤 Commit e push su GitHub..." >> "$LOG"
cd "$PROJECT_DIR" || exit 1
git add . >> "$LOG" 2>&1
git commit -m "Deploy completo: UI, engine, ZIP, contributors" >> "$LOG" 2>&1
git push origin main >> "$LOG" 2>&1

# 6. Notifica Discord (se configurato)
if [ -n "$WEBHOOK_URL" ]; then
  curl -H "Content-Type: application/json" \
       -X POST \
       -d "{\"content\": \"🚀 Deploy EcoBlock completato. ZIP creato, contributors aggiornati.\"}" \
       "$WEBHOOK_URL"
  echo "🔔 Notifica Discord inviata" >> "$LOG"
else
  echo "ℹ️ Webhook Discord non configurato" >> "$LOG"
fi

echo "✅ Deploy completo eseguito. Log in eco_deploy_all.log"
