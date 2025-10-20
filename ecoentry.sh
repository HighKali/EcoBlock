#!/bin/bash
echo "Launching EcoBlock + HostBlock..."
bash ./engine/eco_ngrok_start.sh || {
  echo "eco_ngrok_start.sh failed"; exit 1;
}
echo "Generating CONTRIBUTORS.md..."
git shortlog -sne | tee CONTRIBUTORS.md
ZIP_NAME="EcoBlock_$(date '+%Y%m%d_%H%M').zip"
zip -r $ZIP_NAME . -x "*.git*" "__pycache__/*" "*.env" "*.log"
echo "Done. Archive created: $ZIP_NAME"
