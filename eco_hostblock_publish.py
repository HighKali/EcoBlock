#!/usr/bin/env python3
import os, subprocess

def publish_release():
    print("📦 Pubblicazione release GitHub…")
    repo = "https://github.com/HighKali/EcoBlock.git"
    tag = "v1.0.0"
    zip_name = "EcoBlock_Fusion.zip"
    message = "🚀 Release ufficiale: EcoBlock + dashboard + hostblock"

    subprocess.run(["git", "tag", tag])
    subprocess.run(["git", "push", "origin", tag])
    print(f"✅ Tag {tag} pubblicato")

    if os.path.exists(zip_name):
        print(f"📁 ZIP trovato: {zip_name}")
    else:
        print("⚠️ ZIP non trovato, esegui eco_fatality_fix.py prima")

publish_release()
