#!/bin/bash
echo "📦 EcoBlock: impacchettamento e pubblicazione..."

cd ~
[ ! -d EcoBlock ] && echo "❌ Cartella EcoBlock non trovata." && exit 1

zip -r EcoBlock.zip EcoBlock > /dev/null
echo "✅ Archivio creato: ~/EcoBlock.zip"

cd EcoBlock
git init
git add .
git commit -m "🚀 Prima pubblicazione EcoBlock"
git branch -M main
git remote remove origin 2>/dev/null
git remote add origin https://github.com/TUO_USERNAME/EcoBlock.git
git push -u origin main
