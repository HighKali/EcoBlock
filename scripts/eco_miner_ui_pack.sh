#!/bin/bash
DATE=$(date +%Y-%m-%d_%H-%M)
ZIP="EcoBlock_UI_Pack_$DATE.zip"
zip -r $ZIP dashboard/ wallet/miner_ui_live.svg dashboard/nodes_sync.svg dashboard/ui_theme.css -x "*.pyc" "__pycache__/*"
echo "📦 UI pack creato: $ZIP"
