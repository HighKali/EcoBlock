from flask import Flask, send_file, jsonify, render_template
from flask_socketio import SocketIO
import os

app = Flask(__name__)
socketio = SocketIO(app)

# 🏠 Home
@app.route("/")
def home():
    return "✅ EcoBlock server attivo"

# 📊 DEX JSON
@app.route("/dex")
def dex():
    if os.path.exists("dex_data.json"):
        return send_file("dex_data.json")
    else:
        return jsonify({"error": "DEX non disponibile"}), 404

# 🪪 Badge NFT
@app.route("/badges.html")
def badges():
    return send_file("badges.html")

# 📈 Grafico APY
@app.route("/chart_apy.html")
def chart_apy():
    return send_file("chart_apy.html")

# 🗳️ Voto ecoheal
@app.route("/voto_ecoheal.png")
def voto():
    return send_file("voto_ecoheal.png")

# 💡 LED log
@app.route("/dex_led.log")
def dex_led():
    return send_file("dex_led.log")

# 🌐 Dashboard laser
@app.route("/rackchain")
def rackchain():
    return send_file("rackchain.html")

# 🛰️ ZSONA Blockchain info
@app.route("/zsona")
def zsona():
    return jsonify({
        "rpc": "https://rpc.zsona.net",
        "chain_id": "zsona-mainnet",
        "explorer": "https://explorer.zsona.net"
    })

# 🔍 Stato moduli
@app.route("/status")
def status():
    return jsonify({
        "ecoheal": os.path.exists("ecoheal.log"),
        "dex": os.path.exists("dex_data.json"),
        "last_sync": open("dex_data.json").read() if os.path.exists("dex_data.json") else "N/A"
    })

# 🔔 WebSocket ping
@socketio.on("ping")
def handle_ping(data):
    print("📡 Ping ricevuto:", data)
    socketio.emit("pong", {"status": "🟢 Server attivo"})

# 🚀 Avvio server
if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1", port=8050)
