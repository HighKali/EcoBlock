#!/bin/bash
echo "🛑 Arresto ecosistema EcoBlock..."
pkill -f eco_zsona_miner_loop.py && echo "⛏️ Miner loop fermato"
pkill -f eco_miner_guard.py && echo "🛡️ Watchdog fermato"
pkill -f eco_miner_stats.py && echo "📊 API reward fermata"
pkill -f eco_miner_ui_live_server.py && echo "🖼️ Server UI fermato"
pkill -f eco_miner_ui_live_refresh.py && echo "🔄 Refresh SVG fermato"
echo "✅ Tutti i processi EcoBlock sono stati fermati"
