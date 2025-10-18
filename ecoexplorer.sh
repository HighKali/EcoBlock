#!/bin/bash
echo "🌐 EcoExplorer: stato moduli e wallet"

echo "📁 Moduli presenti:"
ls -1 *.sh *.py 2>/dev/null

echo ""
echo "🔐 Wallet:"
[ -f wallet_zsona.txt ] && echo "ZSONA: $(cat wallet_zsona.txt)"
[ -f wallet_dsn.txt ] && echo "DSN: $(cat wallet_dsn.txt)"
[ -f wallet_xmr.txt ] && echo "XMR: $(cat wallet_xmr.txt)"

echo ""
echo "🧠 Stato nodo:"
curl -s http://localhost:8080/status || echo "❌ Nodo non attivo"

echo ""
echo "🔐 Stato login:"
curl -s -X POST http://localhost:5000/login -H "Content-Type: application/json" \
  -d '{"nickname":"test","password":"test"}' || echo "❌ Auth non attivo"
