#!/usr/bin/env python3
import os

def menu():
    print("🔧 EcoBlock Miner Panel")
    print("[1] Minaggio singolo")
    print("[2] Verifica wallet")
    print("[3] Rotazione wallet")
    print("[4] Sync reward")
    print("[5] Genera badge")
    print("[6] Report miner")
    print("[7] Esporta chain")
    print("[0] Esci")

def run():
    while True:
        menu()
        choice = input("Seleziona: ")
        if choice == "1":
            os.system("python3 scripts/eco_zsona_miner.py")
        elif choice == "2":
            os.system("python3 scripts/eco_wallet_check.py")
        elif choice == "3":
            os.system("python3 scripts/eco_wallet_rotate.py")
        elif choice == "4":
            os.system("python3 scripts/eco_miner_sync.py")
        elif choice == "5":
            os.system("python3 scripts/eco_miner_badge.py")
        elif choice == "6":
            os.system("python3 scripts/eco_miner_report.py")
        elif choice == "7":
            os.system("python3 scripts/eco_miner_export.py")
        elif choice == "0":
            break
        else:
            print("❌ Scelta non valida")

if __name__ == "__main__":
    run()
