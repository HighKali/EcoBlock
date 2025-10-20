#!/bin/bash
echo "📦 Creazione archivio pubblicabile..."
DATE=$(date +%Y-%m-%d_%H-%M)
ZIP="EcoBlock_Public_$DATE.zip"
zip -r $ZIP wallet/ dashboard/ scripts/ docs/ -x "*.pyc" "__pycache__/*" "*.log" "*.tar.gz"
echo "✅ Archivio creato: $ZIP"
