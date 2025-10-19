#!/usr/bin/env python3
import os
import time

MODULES = [
    "ecoentry.sh", "ecoswap.sh", "ecoapi.sh", "ecopool.sh",
    "ecoignite.sh", "eco_node.py", "ecoauth.py", "ecopublish.sh"
]

def check_integrity():
    print("🔍 Verifica integrità moduli...")
    corrupted = []
    for module in MODULES:
        if not os.path.exists(module):
            print(f"❌ Manca: {module}")
            corrupted.append(module)
        elif os.path.getsize(module) < 10:
            print(f"⚠️ Sospetto danneggiamento: {module}")
            corrupted.append(module)
    return corrupted

def attempt_repair(modules):
    for m in modules:
        print(f"🛠️ Ripristino: {m}")
        with open(m, "w") as f:
            f.write("# Modulo ripristinato automaticamente\n")
        time.sleep(0.5)

if __name__ == "__main__":
    broken = check_integrity()
    if broken:
        attempt_repair(broken)
        print("✅ Riparazione completata.")
    else:
        print("✅ Tutti i moduli sono integri.")

