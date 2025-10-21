#!/usr/bin/env python3
import subprocess, time, os

def start_module(name, file, port):
    print(f"🚀 Avvio {name} su porta {port}...")
    try:
        subprocess.Popen(["python3", file])
        time.sleep(1)
    except Exception as e:
        print(f"❌ Errore avvio {name}: {e}")

def check_port(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def status():
    print("\n📡 Stato moduli:")
    for name, port in [("EcoNode", 8080), ("EcoAuth", 5000), ("EcoEdit", 7070)]:
        online = check_port(port)
        print(f" - {name}: {'🟢 Online' if online else '🔴 Offline'}")

def open_layout():
    html_path = os.path.expanduser("~/EcoBlock/ui/index.html")
    if os.path.exists(html_path):
        print("🎨 Apri layout: ~/EcoBlock/ui/index.html")
    else:
        print("❌ Layout non trovato.")

if __name__ == "__main__":
    os.chdir(os.path.expanduser("~/EcoBlock"))
    start_module("EcoNode", "eco_node.py", 8080)
    start_module("EcoAuth", "ecoauth.py", 5000)
    start_module("EcoEdit", "ecoedit.py", 7070)
    time.sleep(2)
    status()
    open_layout()

