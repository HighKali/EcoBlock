#!/usr/bin/env python3
import os
assets=["logo.svg","map.svg","index.html","eco_ui_notify.js"]
base=os.path.expanduser("~/EcoBlock/dashboard")
print("🔍 Verifica asset UI:")
for a in assets:
    path=os.path.join(base,a) if a.endswith(".html") or a.endswith(".js") else os.path.join(base,"assets",a)
    print(f"✅ {a} trovato" if os.path.exists(path) else f"❌ {a} mancante")
