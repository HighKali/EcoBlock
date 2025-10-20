#!/usr/bin/env python3
import os

def tui():
    print("🖥️ EcoBlock Terminal UI")
    print("[1] Stato miner")
    print("[2] Diagnosi")
    print("[3] Self-heal")
    print("[4] Verifica ambiente")
    print("[5] Analisi AI")
    print("[6] Classifica address")
    print("[7] Esporta HTML")
    print("[8] Pulizia chain")
    print("[9] Fusione chain")
    print("[10] Genera tema UI")
    print("[11] Sync globale")
    print("[12] Notifica Matrix/Telegram")
    print("[13] Crea UI Pack")
    print("[14] Cambia tema")
    print("[15] Sync remoto")
    print("[16] Notifica stato miner")
    print("[17] Avvia server UI live")
    print("[18] Esci")
    while True:
        choice = input("Seleziona: ")
        if choice == "1":
            os.system("python3 scripts/eco_status.py")
        elif choice == "2":
            os.system("python3 scripts/eco_miner_diag.py")
        elif choice == "3":
            os.system("python3 scripts/eco_miner_selfheal.py")
        elif choice == "4":
            os.system("python3 scripts/eco_verify_env.py")
        elif choice == "5":
            os.system("python3 scripts/eco_miner_ai.py")
        elif choice == "6":
            os.system("python3 scripts/eco_miner_rank.py")
        elif choice == "7":
            os.system("python3 scripts/eco_miner_export_html.py")
        elif choice == "8":
            os.system("python3 scripts/eco_miner_clean.py")
        elif choice == "9":
            os.system("python3 scripts/eco_miner_fuse.py")
        elif choice == "10":
            os.system("python3 scripts/eco_miner_theme.py")
        elif choice == "11":
            os.system("python3 scripts/eco_miner_sync_all.py")
        elif choice == "12":
            os.system("python3 scripts/eco_miner_notify_matrix.py")
        elif choice == "13":
            os.system("bash scripts/eco_miner_ui_pack.sh")
        elif choice == "14":
            os.system("python3 scripts/eco_miner_ui_theme_switcher.py")
        elif choice == "15":
            os.system("python3 scripts/eco_miner_sync_remote.py")
        elif choice == "16":
            os.system("python3 scripts/eco_miner_notify_status.py")
        elif choice == "17":
            os.system("python3 scripts/eco_miner_ui_live_server.py &")
        elif choice == "18":
            break
        else:
            print("❌ Scelta non valida")

if __name__ == "__main__":
    tui()
