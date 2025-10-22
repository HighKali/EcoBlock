import requests, json, os, time
from dotenv import load_dotenv

load_dotenv()

DEX_API_KEY = os.getenv("DEX_API_KEY")
DEX_BASE_URL = os.getenv("DEX_BASE_URL")

# 🔍 Attendi che il server sia pronto
def wait_for_server():
    for _ in range(10):
        try:
            r = requests.get("http://127.0.0.1:8050")
            if r.status_code == 200:
                return True
        except:
            time.sleep(2)
    return False

if not wait_for_server():
    print("❌ Server non disponibile su 127.0.0.1:8050")
    exit()

# 📡 Interroga l’API DEX
dex_data = {}
try:
    headers = {"Authorization": f"Bearer {DEX_API_KEY}"}
    r = requests.get(f"{DEX_BASE_URL}/stats", headers=headers, timeout=5)
    data = r.json()
    dex_data["volume"] = data.get("volume", "N/A")
    dex_data["apy"] = data.get("apy", "N/A")
except Exception as e:
    print(f"⚠️ Errore API DEX: {e}")
    print("🔁 Genero dati simulati di fallback")
    dex_data["volume"] = "124.7K"
    dex_data["apy"] = "6.8"

# 📊 Timestamp
dex_data["last_sync"] = time.strftime("%Y-%m-%d %H:%M:%S")

# 💾 Salva su disco
with open("dex_data.json", "w") as f:
    json.dump(dex_data, f, indent=2)

print("✅ DEX sincronizzato:", dex_data)
