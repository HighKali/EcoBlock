#!/usr/bin/env python3
import os, shutil

def verify_env():
    print("🔍 Verifica ambiente:")
    for cmd in ["python3", "git", "flask", "requests"]:
        path = shutil.which(cmd)
        print(f"{cmd}: {'✅ Trovato' if path else '❌ Mancante'}")
    print("📁 Cartelle:", "wallet/" if os.path.exists("wallet") else "❌ wallet mancante")

if __name__ == "__main__":
    verify_env()
