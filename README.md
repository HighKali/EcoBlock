# 🌍 EcoBlock — Ethical Blockchain Launcher

Avvio universale con autenticazione, logging, packaging, notifiche e IP dinamico.

## 🚀 Uso
./eco_secure_launch.sh [--local|--public] [--silent] [--log-only] [--pack]

## 🔐 Token richiesto
Header: X-ECO-TOKEN: eco_secret_8090

## 📦 Packaging
./eco_secure_launch.sh --pack → EcoBlock-blindato.zip

## 📣 Notifica Telegram
Configura .env con BOT_TOKEN e CHAT_ID

## 📝 Logging
wallet/eco_log.json registra ogni avvio

## 📁 Struttura
EcoBlock/{scripts, wallet, logs, eco_secure_launch.sh, eco_log.py, README.md}
