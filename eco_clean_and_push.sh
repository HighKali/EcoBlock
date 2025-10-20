#!/bin/bash
echo "🧹 Pulizia file doppi, vuoti, obsoleti e corrotti..."

# Rimuove file vuoti
find . -type f -empty -delete

# Rimuove file duplicati (stesso contenuto)
fdupes -rdN .

# Rimuove file obsoleti e inutili
find . -type f \( -name "*.pyc" -o -name "*.log" -o -name "*.DS_Store" -o -name "*~" -o -name "*.bak" \) -delete

# Rimuove ambienti virtuali e cache
rm -rf venv __pycache__ .env .mypy_cache .pytest_cache

# Rimuove cartelle vuote
find . -type d -empty -delete

# Rimuove file corrotti (non leggibili)
find . -type f ! -exec head -c 1 {} \; -delete

echo "🔍 Verifica struttura..."
tree -L 2

echo "🔐 Commit e push su GitHub..."
git add .
git commit -m "🧹 Cleaned repo: removed duplicates, empty, obsolete and corrupted files"
git push

echo "✅ Repository aggiornato e blindato"
