#!/bin/bash
echo "🔐 Generazione chiave privata..."
PRIVATE_KEY=$(openssl rand -hex 32)
read -p "✅ Confermi la generazione della chiave? (y/n): " CONFIRM
[ "$CONFIRM" != "y" ] && echo "❌ Annullato." && exit 1

cd ~ && rm -rf EcoBlock && mkdir EcoBlock && cd EcoBlock
git clone https://github.com/HighKali/EcoBlock.git . && git pull --rebase

ZSONA_ADDRESS="ZSONA-ROBERTO-0001"
echo "$ZSONA_ADDRESS | balance: 1000000 | max_mineable: 99999999999999999" > wallet_zsona.txt
echo "DSN-$PRIVATE_KEY" > wallet_dsn.txt
echo "XMR-$PRIVATE_KEY" > wallet_xmr.txt

read -p "👤 Nickname: " NICK
read -s -p "🔒 Password: " PASSWD
echo "$NICK:$PASSWD" > credentials.txt

echo "window.ethereum.request({ method: 'eth_requestAccounts' })" > dex_connect.js

mkdir -p ui
cat > ui/index.html <<EOF
<!DOCTYPE html>
<html><head><title>EcoBlock Wallet</title><link rel="stylesheet" href="../style.css"></head>
<body>
<h1>🌍 EcoBlock Wallet</h1>
<p>👤 Nickname: $NICK</p>
<p>🔐 ZSONA: $ZSONA_ADDRESS</p>
<p>💰 DSN: DSN-$PRIVATE_KEY</p>
<p>🪙 XMR: XMR-$PRIVATE_KEY</p>
<script src="../dex_connect.js"></script>
</body></html>
EOF

echo "✅ Setup completato. Apri ui/index.html"
