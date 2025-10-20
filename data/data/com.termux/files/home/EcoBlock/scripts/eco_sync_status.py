#!/usr/bin/env python3
import os
modules = [
    "ecoentry.sh", "ecoagent.py", "ecoheal_ui_fix.py", "ecoheal_ui_art.py",
    "ecoapi.py", "eco_ngrok_start.sh", "server.py", "dashboard/index.html"
]
print("🔍 Verifica moduli EcoBlock:")
for m in modules:
    path = os.path.join("scripts", m) if not m.startswith("dashboard") else os.path.join("dashboard", m)
    print(f"✅ {m} trovato" if os.path.exists(path) else f"❌ {m} mancante")
