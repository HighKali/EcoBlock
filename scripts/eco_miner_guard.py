#!/usr/bin/env python3
import subprocess, time

def is_running():
    result = subprocess.run(["pgrep", "-f", "eco_zsona_miner_loop.py"], stdout=subprocess.PIPE)
    return bool(result.stdout.strip())

def restart_miner():
    subprocess.Popen(["python3", "scripts/eco_zsona_miner_loop.py"])
    print("🛡️ Miner riavviato")

if __name__ == "__main__":
    while True:
        if not is_running():
            print("⚠️ Miner non attivo, riavvio...")
            restart_miner()
        time.sleep(60)
