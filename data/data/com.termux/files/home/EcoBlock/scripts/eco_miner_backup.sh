#!/bin/bash
DATE=$(date +%Y-%m-%d_%H-%M)
mkdir -p ~/EcoBlock/backups
tar --exclude='__pycache__' --exclude='*.pyc' -czf ~/EcoBlock/backups/eco_backup_$DATE.tar.gz ~/EcoBlock/wallet ~/EcoBlock/scripts
echo "🗂️ Backup creato: eco_backup_$DATE.tar.gz"
