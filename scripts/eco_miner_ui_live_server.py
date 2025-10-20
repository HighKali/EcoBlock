#!/usr/bin/env python3
from flask import Flask, send_file, request
import os, json, random, requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🖼️ EcoBlock UI Live</h1><p>Visita <a href='/ui'>/ui</a> o <a href='/panel'>/panel</a></p>"

@app.route("/ui")
def ui():
    path = "wallet/miner_ui_live.svg"
    if not os.path.exists(path):
        return "<h2>🕓 UI non ancora generata. Riprova tra qualche secondo.</h2>", 202
    return send_file(path)

@app.route("/panel")
def panel():
    path = "dashboard/eco_miner_ui_live_panel.html"
    if not os.path.exists(path):
        return "<h2>❌ Pannello non trovato</h2>", 404
    return send_file(path)

@app.route("/theme/<mode>")
def theme(mode):
    theme_file = "dashboard/ui_theme.css"
    themes = {
        "dark": "body{background:#000;color:#0ff;}h1{color:#ff00ff;}",
        "light": "body{background:#fff;color:#000;}h1{color:#0077cc;}",
        "random": random.choice([
            "body{background:#111;color:#ffcc00;}h1{color:#00ffcc;}",
            "body{background:#222;color:#00ff00;}h1{color:#ff0000;}",
            "body{background:#000;color:#0ff;}h1{color:#ff00ff;}"
        ])
    }
    css = themes.get(mode, themes["dark"])
    with open(theme_file, "w") as f:
        f.write(css)
    return f"🎨 Tema '{mode}' applicato"

@app.route("/sync")
def sync():
    chain_file = "wallet/zsona_chain.json"
    nodes = ["http://127.0.0.1:8090", "http://127.0.0.1:8040"]
    if not os.path.exists(chain_file):
        return "❌ Chain mancante", 500
    with open(chain_file) as f:
        chain = json.load(f)
    for node in nodes:
        try:
            r = requests.post(f"{node}/node/receive", json=chain)
            print(f"📡 Chain inviata a {node} → {r.status_code}")
        except Exception as e:
            print(f"❌ Errore sync con {node}: {e}")
    return "🔄 Sync remoto completato"

@app.route("/notify")
def notify():
    chain_file = "wallet/zsona_chain.json"
    hooks = [
        "https://discord.com/api/webhooks/...",  # Discord
        "https://matrix.org/api/webhooks/...",   # Matrix
        "https://api.telegram.org/bot.../sendMessage"  # Telegram
    ]
    if not os.path.exists(chain_file):
        return "❌ Chain mancante", 500
    with open(chain_file) as f:
        chain = json.load(f)
    last = chain[-1]
    msg = f"📢 Broadcast: Blocco {last['index']} → {last['data']['to']} +{last['data']['amount']} ZSONA"
    for hook in hooks:
        try:
            payload = {"content": msg} if "discord" in hook or "matrix" in hook else {"chat_id": "@EcoBlock", "text": msg}
            requests.post(hook, json=payload)
        except Exception as e:
            print(f"❌ Errore con {hook}: {e}")
    return "📣 Notifica inviata su tutti i canali"

if __name__ == "__main__":
    app.run(port=8050)
