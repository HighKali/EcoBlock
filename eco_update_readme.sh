#!/bin/bash
echo "📝 Aggiornamento automatico README.md in corso…"
cat > README.md <<EOT
# 🚀 EcoBlock–HostBlock RackChain

**Ultimo aggiornamento:** 2025-10-21 19:40:39

## 🔧 Moduli attivi

- `server.py` — Server Flask con route modulari
- `eco_run_all.sh` — Orchestrazione completa
- `eco_sync_zsona.py` — Sincronizzazione ZSONA
- `eco_sync_report_gen.py` — Generazione report HTML
- `eco_ui_check.py` — Verifica moduli Flask
- `eco_log.py` — Logging automatico
- `ecoheal.py` — Riparazione moduli corrotti
- `ecoagent.py` — Monitoraggio energia e uptime
- `eco_notify.py` — Notifiche Telegram/Matrix
- `eco_miner_sync.py` — Stato miner ZSONA/$DSN
- `ecozip.sh` — Backup selettivo
- `eco_rackchain_commit.sh` — Avvio, verifica, pubblicazione
- `eco_rackchain_all.sh` — Installazione e setup completo

## 🎛️ Dashboard laser

Accessibile su [http://127.0.0.1:8050](http://127.0.0.1:8050)  
Include moduli attivi: Faucet DSN, Faucet ZSONA, Miner Web, Wallet, DEX, POOL, Report

## 🔐 Sicurezza e fallback

- Token `X-ECO-TOKEN` per ricezione POST
- Verifica `.env` con `eco_verify_env.py`
- Auto-riparazione moduli mancanti
- Logging e backup automatico

## 🛰️ Sincronizzazione

- Volume DEX e APY POOL aggiornati
- Report HTML generato in `eco_sync_report.html`
- Log JSON in `wallet/zsona_sync_log.json`

## 📦 Pubblicazione

```bash
git add .
git commit -m "🚀 RackChain aggiornato automaticamente"
git push origin main
```
EOT
echo "✅ README.md aggiornato"
