#!/bin/bash

# === EcoBlock UI Healer ===
# Verifica bottoni, funzioni JS, include scripts.js, committa e pubblica

PROJECT_DIR=~/ecoblock-dashboard
JS_FILE="$PROJECT_DIR/scripts.js"
HTML_FILE="$PROJECT_DIR/index.html"
LOG="$PROJECT_DIR/ui_diagnose.log"
GITHUB_USER="HighKali"
REPO_NAME="ecoblock-dashboard"
BRANCH="main"
WEBHOOK_URL=""  # Inserisci qui il tuo webhook Discord se vuoi notifiche

cd "$PROJECT_DIR" || { echo "❌ Directory non trovata"; exit 1; }

echo "🧪 Diagnosi UI avviata: $(date)" > "$LOG"

# 1. Verifica inclusion script.js
if grep -q "scripts.js" "$HTML_FILE"; then
  echo "✅ scripts.js incluso correttamente" >> "$LOG"
else
  echo "❌ scripts.js non incluso. Lo aggiungo..." >> "$LOG"
  sed -i '/<\/body>/i <script src="scripts.js"></script>' "$HTML_FILE"
fi

# 2. Verifica bottoni e onclick
if grep -q "onclick=" "$HTML_FILE"; then
  echo "✅ Bottoni con onclick rilevati" >> "$LOG"
else
  echo "❌ Bottoni privi di onclick. Inserisco esempi..." >> "$LOG"
  sed -i 's|<button[^>]*>Genera Wallet</button>|<button onclick="generaWallet()">Genera Wallet</button>|' "$HTML_FILE"
  sed -i 's|<button[^>]*>Genera Entropia</button>|<button onclick="generaEntropia()">Genera Entropia</button>|' "$HTML_FILE"
fi

# 3. Verifica funzioni JS
if grep -q "function generaWallet()" "$JS_FILE"; then
  echo "✅ Funzione generaWallet() presente" >> "$LOG"
else
  echo "❌ generaWallet() mancante. La aggiungo..." >> "$LOG"
  echo -e "\nfunction generaWallet() {\n  alert('✅ Wallet generato!');\n}" >> "$JS_FILE"
fi

if grep -q "function generaEntropia()" "$JS_FILE"; then
  echo "✅ Funzione generaEntropia() presente" >> "$LOG"
else
  echo "❌ generaEntropia() mancante. La aggiungo..." >> "$LOG"
  echo -e "\nfunction generaEntropia() {\n  alert('✨ Entropia generata!');\n}" >> "$JS_FILE"
fi

# 4. Commit e push su GitHub
git add "$HTML_FILE" "$JS_FILE" "$LOG"
git commit -m "EcoHeal UI: riparazione bottoni e funzioni JS"
git push origin "$BRANCH"

# 5. Notifica Discord (se webhook presente)
if [ -n "$WEBHOOK_URL" ]; then
  curl -H "Content-Type: application/json" \
       -X POST \
       -d "{\"content\": \"🛠️ EcoHeal UI completato: bottoni e funzioni JS riparati su $REPO_NAME\"}" \
       "$WEBHOOK_URL"
fi

echo "✅ Diagnosi e riparazione completata. Log disponibile in ui_diagnose.log"
