from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json, os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template("dashboard.html", timestamp=datetime.utcnow().isoformat())

@app.route('/node/receive', methods=['POST'])
def receive():
    token = request.headers.get('X-ECO-TOKEN')
    if token != "eco_secret_8090":
        return jsonify({"error": "Token non valido"}), 403
    data = request.get_json()
    if not data or "chain" not in data:
        return jsonify({"error": "Chain mancante"}), 400
    with open("wallet/zsona_chain_live.json", "w") as f:
        json.dump(data["chain"], f)
    return jsonify({"status": "ok", "message": "Entropia generata. Wallet aggiornato."}), 200

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)
