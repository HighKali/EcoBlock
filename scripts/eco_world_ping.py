#!/usr/bin/env python3
import requests

def send_telegram(token, chat_id, msg):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": msg}
    requests.post(url, data=data)

def send_matrix(token, room_id, msg):
    url = f"https://matrix.org/_matrix/client/r0/rooms/{room_id}/send/m.room.message"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"msgtype": "m.text", "body": msg}
    requests.post(url, json=data, headers=headers)

def send_discord(webhook_url, msg):
    data = {"content": msg}
    requests.post(webhook_url, json=data)

with open("eco_world_announce.md") as f:
    message = f.read()

# Inserisci le tue credenziali qui
telegram_token = "YOUR_TELEGRAM_BOT_TOKEN"
telegram_chat_id = "YOUR_CHAT_ID"
matrix_token = "YOUR_MATRIX_ACCESS_TOKEN"
matrix_room_id = "!yourroomid:matrix.org"
discord_webhook = "https://discord.com/api/webhooks/..."

send_telegram(telegram_token, telegram_chat_id, message)
send_matrix(matrix_token, matrix_room_id, message)
send_discord(discord_webhook, message)

print("📡 eco_world_announce.md inviato a Telegram, Matrix e Discord")

