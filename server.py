from flask import Flask, send_file, jsonify
from flask_socketio import SocketIO, emit
import os
import json

app = Flask(__name__)
socketio = SocketIO(app)

# 🎛️ Dashboard principale
@app.route("/")
def home():
    return send_file("index.html")

# 🔐 Login laser
@app.route("/login")
def login():
    return send_file("login.html")

# 🧠 Report neon
@app.route("/rackchain")
def rackchain():
    return send_file("rackchain.html")

# 📊 DEX dinamico
@app.route("/dex")
def dex():
    if os.path.exists("dex_data.json"):
        return send_file("dex_data.json")
    else:
        return jsonify({"error": "DEX non disponibile"}), 404

# 🎨 Asset statici
@app.route("/style.css")
def style():
    return send_file("style.css")

@app.route("/script.js")
def script():
    return send_file("script.js")

# 🔐 Sicurezza fallback
@app.route("/.env")
def env_block():
    return jsonify({"error": "Accesso negato"}), 403

# 🔄 Evento WebSocket: sync update
@socketio.on("request_sync_status")
def handle_sync_request():
    if os.path.exists("dex_data.json"):
        with open("dex_data.json") as f:
            data = json.load(f)
        emit("sync_status", data)
    else:
        emit("sync_status", {"error": "DEX non disponibile"})

# ✅ Avvio server con WebSocket
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8050)
