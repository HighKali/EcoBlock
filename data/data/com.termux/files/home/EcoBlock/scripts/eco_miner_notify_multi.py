#!/usr/bin/env python3
import requests, json

HOOKS = [
    "https://discord.com/api/webhooks/...",  # Discord
    "https://api.telegram.org/bot.../sendMessage?chat_id=...&text=",  # Telegram
    "https://your-email-endpoint.com/notify"  # Email webhook
]

def notify_all(block_info):
    for hook in HOOKS:
        try:
            if "discord" in hook:
                requests.post(hook, json={"content": block_info})
            elif "telegram" in hook:
                requests.get(hook + block_info)
            else:
                requests.post(hook, json={"message": block_info})
        except Exception as e:
            print(f"❌ Errore su {hook}: {e}")
    return "✅ Notifiche multiple inviate"

if __name__ == "__main__":
    print(notify_all("⛏️ Blocco 3 minato con reward 103 ZSONA"))
