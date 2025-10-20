#!/bin/bash

echo "=== EcoBlock Repair & Sync ==="

# 1. Verifica struttura
REPO=~/EcoBlock
MODULES=(dashboard hostblock shared engine assets)

for DIR in "${MODULES[@]}"; do
  if [ ! -d "$REPO/$DIR" ]; then
    echo "Missing directory: $DIR — attempting recovery..."
    if [ -d "$REPO/ecoblock-hostblock/$DIR" ]; then
      mv "$REPO/ecoblock-hostblock/$DIR" "$REPO/"
      echo "Recovered: $DIR"
    else
      echo "Recovery failed: $DIR not found"
    fi
  fi
done

# 2. Ricrea eco_ngrok_start.sh se mancante
NGROK_SCRIPT="$REPO/engine/eco_ngrok_start.sh"
if [ ! -f "$NGROK_SCRIPT" ]; then
  echo "Creating eco_ngrok_start.sh..."
  cat > "$NGROK_SCRIPT" << 'EOF'
#!/bin/bash
echo "Starting ngrok tunnel for dashboard (8080)..."
./ngrok http 8080 > ~/dashboard_ngrok.log &
sleep 5
DASHBOARD_URL=$(grep -o 'https://[0-9a-zA-Z.-]*\.ngrok.io' ~/dashboard_ngrok.log | head -n1)

echo "Starting ngrok tunnel for RPC node (8000)..."
./ngrok http 8000 > ~/rpc_ngrok.log &
sleep 5
RPC_URL=$(grep -o 'https://[0-9a-zA-Z.-]*\.ngrok.io' ~/rpc_ngrok.log | head -n1)

echo "Dashboard URL: $DASHBOARD_URL"
echo "RPC Node URL: $RPC_URL"
EOF
  chmod +x "$NGROK_SCRIPT"
fi

# 3. Aggiorna ecoentry.sh (senza emoji)
ENTRY_SCRIPT="$REPO/ecoentry.sh"
cat > "$ENTRY_SCRIPT" << 'EOF'
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
EOF
chmod +x "$ENTRY_SCRIPT"

# 4. Rimuovi clone temporaneo se presente
rm -rf "$REPO/ecoblock-hostblock"

# 5. Avvia tutto
echo "Running ecoentry.sh..."
bash "$ENTRY_SCRIPT"
