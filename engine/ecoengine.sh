#!/bin/bash
PROJECT_DIR=~/ecoblock-dashboard
LOG="$PROJECT_DIR/ecoengine.log"
BRANCH="main"
PORT=8888
WEBHOOK_URL=""
cd "$PROJECT_DIR" || exit 1
echo "🚀 Avvio EcoEngine: $(date)" > "$LOG"
python ecoheal_ui_fix.py >> "$LOG" 2>&1
bash ecoassets_fix.sh >> "$LOG" 2>&1
bash ecominer.sh >> "$LOG" 2>&1
bash ecopurge.sh >> "$LOG" 2>&1
bash ecoignite.sh >> "$LOG" 2>&1
bash eco_publish.sh >> "$LOG" 2>&1
python ecoapi.py >> "$LOG" 2>&1
git add . >> "$LOG" 2>&1
git commit -m "EcoEngine: orchestrazione completa" >> "$LOG" 2>&1
git push origin "$BRANCH" >> "$LOG" 2>&1
if lsof -i :$PORT > /dev/null 2>&1; then
  echo "⚠️ Porta $PORT già in uso." >> "$LOG"
else
  nohup python -m http.server $PORT > /dev/null 2>&1 &
  echo "🟢 Server avviato su http://127.0.0.1:$PORT" >> "$LOG"
fi
[ -n "$WEBHOOK_URL" ] && curl -H "Content-Type: application/json" -X POST -d "{\"content\": \"🚀 EcoEngine completato\"}" "$WEBHOOK_URL"
echo "✅ EcoEngine completato. Log in ecoengine.log"
