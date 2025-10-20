#!/bin/bash
echo "♻️ Ripristino backup..."
LATEST=$(ls -t backups/eco_backup_*.tar.gz | head -n1)
tar -xzf $LATEST -C ~/EcoBlock
echo "✅ Ripristinato da $LATEST"
