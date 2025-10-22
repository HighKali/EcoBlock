#!/usr/bin/env python3
import requests
def check_ngrok():
    try:
        r = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = r.json()["tunnels"]
        for t in tunnels:
            print(f"✅ {t["name"]}: {t["public_url"]}")
    except Exception as e:
        print(f"❌ Errore ngrok: {e}")
check_ngrok()
