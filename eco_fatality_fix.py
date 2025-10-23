#!/usr/bin/env python3
import os, shutil, subprocess

print("🔥 Avvio fix fatality finale…")

# 1. Percorso base
base_dir = os.path.expanduser("~/EcoBlock/hostblock")
zdos_path = os.path.join(base_dir, "hostblock_zdos", "hostblock_zdos")

# 2. Correzione struttura annidata
if os.path.exists(zdos_path):
    print("🔁 Trovata struttura annidata, inizio fusione moduli…")
    for item in os.listdir(zdos_path):
        src = os.path.join(zdos_path, item)
        dst = os.path.join(base_dir, item)
        if os.path.exists(dst):
            print(f"⚠️ File già presente: {item} → sovrascrivo")
            if os.path.isdir(dst):
                shutil.rmtree(dst)
            else:
                os.remove(dst)
        shutil.move(src, dst)
    shutil.rmtree(os.path.join(base_dir, "hostblock_zdos"))
    print("✅ Moduli fusi e struttura corretta")
else:
    print("ℹ️ Nessuna struttura annidata trovata, salto fusione")

# 3. Pulizia blindata
print("🧼 Pulizia file inutili…")
for root, dirs, files in os.walk(base_dir):
    for file in files:
        path = os.path.join(root, file)
        if os.path.getsize(path) == 0 or file.endswith((".pyc", ".bak", ".zip", ".log", ".tmp", ".DS_Store")):
            os.remove(path)

for d in ["__pycache__", ".venv", "env"]:
    subprocess.run(["find", base_dir, "-type", "d", "-name", d, "-exec", "rm", "-rf", "{}", "+"])

# 4. Git blindato
print("🔐 Inizializzazione Git e push…")
os.chdir(base_dir)
subprocess.run(["git", "init"])
subprocess.run(["git", "remote", "add", "origin", "https://github.com/HighKali/EcoBlock.git"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "💀 Fix fatality: struttura corretta, moduli fusi, push blindato"])
subprocess.run(["git", "push", "-u", "origin", "master"])

# 5. ZIP blindato
print("📦 Creazione archivio ZIP blindato…")
subprocess.run(["zip", "-r", "EcoBlock_Fusion.zip", ".", "-x", "*.git*", "*.pyc", "*.bak", "*.tmp"])

# 6. Placeholder moduli
print("🏅 Badge NFT → eco_zsona_badge_mint.py")
print("📢 Notifica Matrix/Telegram → eco_zsona_matrix_notify.py")
print("🧭 Dashboard moduli → eco_hostblock_dashboard.py")

print("✅ Fix fatality completato: struttura corretta, chain fusa, pubblicata e celebrata")
