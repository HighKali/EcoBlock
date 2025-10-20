#!/bin/bash
echo "🚀 Installazione EcoBlock"
mkdir -p wallet
python3 scripts/eco_zsona_wallet.py > wallet/wallet_zsona.txt
python3 scripts/eco_zsona_miner.py
python3 scripts/eco_zsona_stats.py &
python3 scripts/eco_zsona_explorer.py &
python3 scripts/eco_zsona_node_sync.py &
python3 scripts/eco_status.py &
python3 server.py &
echo "✅ EcoBlock installato e avviato"
