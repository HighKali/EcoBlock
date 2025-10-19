#!/bin/bash
echo "🚀 Avvio completo EcoBlock..."

cd ~/EcoBlock

echo "🧠 Avvio nodo..."
nohup python3 eco_node.py > node.log 2>&1 &

echo "🔐 Avvio autenticazione..."
nohup python3 ecoauth.py > auth.log 2>&1 &

echo "🧩 Avvio editor..."
nohup python3 ecoedit.py > edit.log 2>&1 &

sleep 2
echo "📡 Stato moduli:"
curl -s http://localhost:8080/status
curl -s http://localhost:7070/state
