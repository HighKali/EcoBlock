# 🚀 EcoBlock–HostBlock RackChain (Pubblico)

**Ultimo aggiornamento:** 2025-10-21 20:33:37

## 🌐 Accesso pubblico

- Dashboard: [http://151.36.218.179:8050](http://151.36.218.179:8050)
- Report neon: [http://151.36.218.179:8050/rackchain](http://151.36.218.179:8050/rackchain)

## 📱 QR Code

Scansiona per accedere alla dashboard:

```bash
qrencode -t ANSIUTF8 "http://151.36.218.179:8050"
```

## 🔧 Moduli attivi

- `server.py` — Server Flask
- `eco_sync_zsona.py` — Sincronizzazione
- `eco_ui_check.py` — Verifica moduli
- `eco_notify.py` — Notifiche Telegram
- `eco_rackchain_report.html` — Report neon
- `rackchain.html` — Accesso pubblico
- `eco_sync_daemon.sh` — Sync automatico

## 📦 Pubblicazione

```bash
git add .
git commit -m "🌐 EcoBlock pubblicato su IP pubblico"
git push origin main
```
