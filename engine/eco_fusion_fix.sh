#!/bin/bash

echo "🔧 Correzione fusione EcoBlock + HostBlock..."

# 1. Percorso sorgente
SRC=~/EcoBlock/ecoblock-hostblock

# 2. Copia file mancanti o aggiornati
for DIR in dashboard hostblock shared engine assets; do
  if [ -d "$SRC/$DIR" ]; then
    echo "📁 Verifica: $DIR"
    cp -ru "$SRC/$DIR/" "$HOME/EcoBlock/$DIR/"
  else
    echo "⚠️ Directory mancante: $SRC/$DIR"
  fi
done

# 3. Rimuovi clone temporaneo
rm -rf "$SRC"

# 4. Verifica script ngrok
if [ -f ~/EcoBlock/engine/eco_ngrok_start.sh ]; then
  echo "✅ eco_ngrok_start.sh trovato"
else
  echo "❌ eco_ngrok_start.sh mancante. Verifica il clone."
  exit 1
fi

# 5. Avvia ecoentry
echo "🚀 Avvio ecoentry.sh..."
bash ~/EcoBlock/ecoentry.sh
