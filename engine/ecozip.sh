#!/bin/bash
# === EcoZip ===
# Crea un archivio ZIP del progetto, escludendo virtualenv e file temporanei

PROJECT_DIR=~/ecoblock-dashboard
ZIP_NAME="ecoblock_release_$(date +%Y%m%d_%H%M).zip"
EXCLUDE="--exclude=*.pyc --exclude=__pycache__ --exclude=*.log --exclude=*.tmp --exclude=venv --exclude=.git"

echo "📦 Creazione ZIP: $ZIP_NAME"
cd "$PROJECT_DIR" || exit 1
zip -r "$ZIP_NAME" . $EXCLUDE
echo "✅ Archivio creato: $ZIP_NAME"
