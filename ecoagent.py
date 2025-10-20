#!/usr/bin/env python3
import platform, os, datetime
def eco_status():
    print("🧠 EcoAgent Diagnostica")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"User: {os.environ.get("USER", "unknown")}")
    print("Moduli chiave:")
    for f in ["ecoentry.sh", "ecoheal_ui_fix.py", "ecoapi.py", "eco_log.py"]:
        print(f" - {f}: {"✅" if os.path.exists(f) else "❌"}")
    with open("logs/eco.log", "a") as log:
        log.write(f"[{datetime.datetime.now()}] EcoAgent eseguito\\n")
eco_status()
