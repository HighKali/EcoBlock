#!/bin/bash
echo "🌍 Pubblicazione EcoBlock..."
cd ~/EcoBlock
git add .
git commit -m "🚀 EcoBlock aggiornato e blindato"
git push origin main --force
ZIP_NAME="EcoBlock_$(date +%Y%m%d_%H%M).zip"
zip -r $ZIP_NAME . -x "*.git*" "__pycache__/*" "*.env" "*.log" "ngrok-stable-linux-arm.zip"
echo "✅ Archivio creato: $ZIP_NAME"
