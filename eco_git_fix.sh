#!/bin/bash

# 🔐 Configura Git
git config --global user.name "Roberto"
git config --global user.email "roberto@example.com"

# 🔁 Reimposta URL remoto (HTTPS con token o SSH)
# Sostituisci con il tuo token personale se usi HTTPS:
# git remote set-url origin https://<token>@github.com/HighKali/EcoBlock.git

# Se usi SSH:
# git remote set-url origin git@github.com:HighKali/EcoBlock.git

# 🔄 Verifica stato
echo "📦 Stato Git:"
git status

# 💾 Commit locale se ci sono modifiche
if [ -n "$(git status --porcelain)" ]; then
  git add .
  git commit -m "🔧 Fix Git e sincronizzazione automatica"
else
  echo "✅ Nessuna modifica locale da committare"
fi

# 🔄 Pull e rebase
git pull --rebase origin main

# 🚀 Push finale
git push origin main

echo "✅ Git sincronizzato con successo"
