#!/bin/bash

echo "🌐 Pubblicazione EcoExplorer su GitHub Pages..."

cd ~/EcoBlock

# Crea branch gh-pages se non esiste
git checkout --orphan gh-pages

# Pulisce tutto tranne la UI
find . ! -path "./ui/*" ! -path "./.git*" ! -name "ui" -prune -exec rm -rf {} +

# Copia solo i file HTML e CSS
cp ui/*.html .
cp ui/*.css . 2>/dev/null

# Commit e push
git add .
git commit -m "🌐 Pubblicazione EcoExplorer su GitHub Pages"
git push origin gh-pages --force

# Torna su main
git checkout main

echo "✅ Dashboard pubblicata su: https://highkali.github.io/EcoBlock"

