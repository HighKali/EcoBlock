from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ EcoBlock Flask server attivo!"

@app.route('/node/receive', methods=['POST'])
def receive():
    token = request.headers.get('X-ECO-TOKEN')
    if token != "eco_secret_8090":
        return jsonify({"error": "Token non valido"}), 403
    data = request.get_json()
    print(f"[{datetime.utcnow()}] Ricevuto: {data}")
    return jsonify({"status": "ok", "received": data}), 200

@app.route('/status')
def status():
    return jsonify({"status": "EcoBlock attivo", "timestamp": datetime.utcnow().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)
