#!/usr/bin/env python3
from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
DATA_FILE = "ecostate.json"
HTML_FILE = "ui/index.html"

default_state = {
    "nickname": "kali13",
    "zsona_balance": 1000000,
    "dsn_balance": 0,
    "xmr_balance": 0,
    "contacts": [],
    "nodes": ["localhost:8080"],
    "workers": []
}

def load_state():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump(default_state, f, indent=2)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    with open(DATA_FILE, "w") as f:
        json.dump(state, f, indent=2)
    update_layout(state)

def update_layout(state):
    html = f"""<!DOCTYPE html>
<html><head><title>EcoBlock Wallet</title><link rel="stylesheet" href="../style.css"></head>
<body>
<h1>🌍 EcoBlock Wallet</h1>
<p>👤 Nickname: {state['nickname']}</p>
<p>💰 zsona: {state['zsona_balance']}</p>
<p>🪙 DSN: {state['dsn_balance']}</p>
<p>🧪 XMR: {state['xmr_balance']}</p>
<h3>👥 Contatti:</h3>
<ul>{"".join(f"<li>{c}</li>" for c in state['contacts'])}</ul>
<h3>🧠 Nodi:</h3>
<ul>{"".join(f"<li>{n}</li>" for n in state['nodes'])}</ul>
<h3>👷 Worker:</h3>
<ul>{"".join(f"<li>{w}</li>" for w in state['workers'])}</ul>
</body></html>"""
    with open(HTML_FILE, "w") as f:
        f.write(html)

@app.route('/state', methods=['GET'])
def get_state():
    return jsonify(load_state())

@app.route('/state', methods=['POST'])
def update_state():
    data = request.json
    state = load_state()
    state.update(data)
    save_state(state)
    return jsonify({"status": "✅ Stato aggiornato", "new_state": state})

@app.route('/add', methods=['POST'])
def add_item():
    data = request.json
    state = load_state()
    for key in ["contacts", "nodes", "workers"]:
        if key in data:
            state[key].append(data[key])
    save_state(state)
    return jsonify({"status": "✅ Elemento aggiunto", "new_state": state})

@app.route('/reset', methods=['POST'])
def reset():
    save_state(default_state)
    return jsonify({"status": "♻️ Stato resettato", "state": default_state})

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    print("🧩 EcoEdit attivo su http://localhost:7070")
    app.run(host='0.0.0.0', port=7070)
