#!/bin/bash
echo "🛑 Arresto miner e dashboard..."
pkill -f eco_zsona_miner_loop.py
pkill -f eco_miner_guard.py
pkill -f eco_miner_stats.py
echo "✅ Tutti processi fermati"
