#!/usr/bin/env python3
import os

def tui():
    print("🖥️ EcoBlock Terminal UI")
    print("[1] Stato miner")
    print("[2] Diagnosi")
    print("[3] Self-heal")
    print("[4] Verifica ambiente")
    print("[5] Esci")
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
            break
        else:
            print("❌ Scelta non valida")

if __name__ == "__main__":
    tui()
