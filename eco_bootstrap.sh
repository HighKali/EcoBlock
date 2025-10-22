#!/bin/bash
echo "🚀 Bootstrap completo EcoBlock–HostBlock"

# 🔐 Crea .env con chiavi API
cat > .env <<EOF
# 🌐 DEX & Swap Pool
DEX_API_KEY=public_dex_key_eco123
DEX_BASE_URL=https://api.ecodex.io/v1
SWAP_POOL_ENDPOINT=https://api.ecodex.io/v1/swap/pool
SWAP_EXECUTE_ENDPOINT=https://api.ecodex.io/v1/swap/execute

# ⛏️ Mining Pool
MINING_POOL_API=https://api.ecominer.io/v1/pool
MINING_POOL_KEY=public_miner_key_eco456

# 🛰️ ZSONA Blockchain
ZSONA_RPC=https://rpc.zsona.net
ZSONA_CHAIN_ID=zsona-mainnet
ZSONA_EXPLORER=https://explorer.zsona.net

# 🔔 Telegram Notify
TELEGRAM_TOKEN=public_telegram_token_eco789
TELEGRAM_CHAT_ID=123456789

# 🔐 Wallet & Entropy
WALLET_ENTROPY_SEED=eco_entropy_seed_xyz
WALLET_GENERATOR_ENDPOINT=https://api.ecoblock.io/v1/wallet/generate

# 🧠 Governance
GOVERNANCE_CONTRACT=https://api.ecogov.io/v1/vote
GOVERNANCE_KEY=public_gov_key_eco321

# 🗺️ SVG Map
MAP_DATA_ENDPOINT=https://api.ecomap.io/v1/coordinates
EOF

chmod 600 .env
echo "✅ .env creato e protetto"

# 🧠 Verifica che server.py abbia la route /dex
if ! grep -q "@app.route(\"/dex\")" server.py; then
  echo "🔧 Aggiungo route /dex a server.py"
  echo -e "\n@app.route(\"/dex\")\ndef dex():\n    return send_file(\"dex_data.json\")" >> server.py
fi

# 🛰️ Avvia server Flask
pkill -f server.py
sleep 1
nohup python3 server.py > logs/server.log 2>&1 &
echo "⏳ Avvio server Flask…"
sleep 5

# 🔄 Attendi che /dex sia disponibile
echo "🔍 Verifica disponibilità /dex"
for i in {1..10}; do
  if curl -s http://127.0.0.1:8050/dex | grep -q "volume"; then
    echo "✅ /dex disponibile"
    break
  else
    echo "⏳ Attesa /dex…"
    sleep 2
  fi
done

# 🔁 Esegui eco_dex_sync.py
python3 eco_dex_sync.py

# 🔗 Integra in eco_master.sh
if ! grep -q "source .env" eco_master.sh; then
  sed -i '1s/^/source .env\n/' eco_master.sh
  echo "🔗 .env integrato in eco_master.sh"
fi

echo "✅ Bootstrap completato. Tutto pronto per 'eco_master'"
