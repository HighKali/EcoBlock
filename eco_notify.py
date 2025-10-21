import requests
message = "🚨 EcoBlock RackChain avviato con successo!"
url = "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage"
payload = {"chat_id": "<YOUR_CHAT_ID>", "text": message}
try: requests.post(url, data=payload); print("✅ Notifica inviata")
except Exception as e: print(f"❌ Errore notifica: {e}")
