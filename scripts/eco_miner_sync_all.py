#!/usr/bin/env python3
import os

def sync_all():
    print("🔄 Sync nodi...")
    os.system("python3 scripts/eco_miner_syncnet.py")
    print("📊 Sync reward...")
    os.system("python3 scripts/eco_miner_stats.py")
    print("🖼️ Sync dashboard...")
    os.system("python3 scripts/eco_miner_ui.py")
    print("🔄 Sync SVG...")
    os.system("python3 scripts/eco_miner_sync_svg.py")
    print("📄 Sync CSV...")
    os.system("python3 scripts/eco_miner_export_csv_live.py")
    print("🖼️ Sync UI live...")
    os.system("python3 scripts/eco_miner_ui_live.py")

if __name__ == "__main__":
    sync_all()
