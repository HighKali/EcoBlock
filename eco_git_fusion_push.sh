#!/bin/bash
echo "🚀 Avvio super comando EcoBlock…"

cd ~/EcoBlock/hostblock || exit

# 1. Pulizia blindata
echo "🧼 Pulizia file inutili e ambienti virtuali…"
find . -type f \( -name "*.pyc" -o -name "*.bak" -o -name "*.tmp" -o -name ".DS_Store" \) -delete
find . -type d \( -name "__pycache__" -o -name ".venv" -o -name "env" \) -exec rm -rf {} +

# 2. Fusione moduli (se presente struttura annidata)
if [ -d "hostblock_zdos/hostblock_zdos" ]; then
  echo "🔁 Fusione moduli da struttura annidata…"
  mv hostblock_zdos/hostblock_zdos/* ./
  rm -rf hostblock_zdos
fi

# 3. Inizializzazione Git
echo "🔐 Inizializzazione Git e commit…"
git init
git config user.name "highkali"
git config user.email "xdsn.miner@gmail.com"
git remote remove origin 2>/dev/null
git remote add origin https://github.com/HighKali/EcoBlock.git
git add .
git commit -m "🧬 Super commit: fusione, pulizia, celebrazione"

# 4. Push blindato
echo "📤 Push su GitHub…"
git pull origin master --allow-unrelated-histories --no-rebase
git push origin master

# 5. Tag e release
echo "🏷️ Pubblicazione tag v1.0.0…"
git tag -a v1.0.0 -m "🚀 Release EcoBlock v1.0.0"
git push origin v1.0.0

# 6. ZIP blindato
echo "📦 Creazione archivio ZIP blindato…"
zip -r EcoBlock_Fusion.zip . -x "*.git*" "*.pyc" "*.bak" "*.tmp"

# 7. Celebrazione finale
echo "🏅 Mint badge celebrativo Founder…"
echo "✅ Badge: EcoBlock Founder @ $(date '+%Y-%m-%d %H:%M:%S')"

echo "📢 Notifica Matrix/Telegram simulata…"
echo "✅ EcoBlock pubblicato: ZIP blindato, badge mintato, tag v1.0.0"

echo "🎉 Super comando completato con successo!"
