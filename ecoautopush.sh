#!/bin/bash

echo "🚀 EcoAutoPush: aggiornamento repository EcoBlock"

cd ~/EcoBlock || exit 1

# 🔍 Verifica modifiche
echo "📦 File modificati:"
git status

# 📦 Aggiungi tutto
git add .

# 📝 Commit con timestamp
NOW=$(date +"%Y-%m-%d %H:%M:%S")
git commit -m "🧠 AutoPush: aggiornamento EcoBlock @ $NOW"

# 🚀 Push su GitHub
git push origin main

# 🏷️ Crea tag incrementale
LATEST_TAG=$(git tag | sort -V | tail -n 1)
if [[ $LATEST_TAG =~ v([0-9]+)\.([0-9]+)\.([0-9]+) ]]; then
  MAJOR=${BASH_REMATCH[1]}
  MINOR=${BASH_REMATCH[2]}
  PATCH=${BASH_REMATCH[3]}
  NEW_TAG="v$MAJOR.$MINOR.$((PATCH+1))"
else
  NEW_TAG="v1.0.1"
fi

git tag -a "$NEW_TAG" -m "🔖 AutoTag: $NEW_TAG @ $NOW"
git push origin "$NEW_TAG"

echo "✅ Commit e tag completati: $NEW_TAG"
