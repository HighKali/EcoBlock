#!/bin/bash
echo "📦 Creo pacchetto blindato..."
zip -r EcoBlock-blindato.zip . -x "*.pyc" "__pycache__" "venv" ".git" "*.log" "logs/*.log"
echo "✅ Pacchetto creato: EcoBlock-blindato.zip"
