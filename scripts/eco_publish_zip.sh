#!/bin/bash
DATE=$(date +%Y-%m-%d_%H-%M)
ZIP="EcoBlock_Distribuzione_Live_$DATE.zip"
zip -r $ZIP wallet/ dashboard/ scripts/ docs/ -x "*.pyc" "__pycache__/*" "*.log" "*.tar.gz"
echo "📦 Archivio blindato creato: $ZIP"
