#!/bin/bash
echo "📟 Stato processi EcoBlock:"
ps aux | grep -E 'eco_zsona_miner_loop|eco_miner_guard|eco_miner_stats|eco_miner_ui_live_server|eco_miner_ui_live_refresh' | grep -v grep
