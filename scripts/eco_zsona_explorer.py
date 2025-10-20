#!/usr/bin/env python3
from flask import Flask, jsonify, render_template_string
import json, os

app = Flask(__name__)
CHAIN_FILE = "wallet/zsona_chain.json"

@app.route("/")
def explorer():
    return render_template_string("""
    <html><head><title>ZSONA Explorer</title></head>
    <body style="background:#0f1117;color:#fff;font-family:sans-serif">
    <h1>🧱 ZSONA Blockchain Explorer</h1>
    <div id="chain"></div>
    <script>
      fetch("/chain").then(r => r.json()).then(data => {
        document.getElementById("chain").innerHTML = data.map(b =>
          `<div style='margin:10px;padding:10px;border:1px solid #00ffc8'>
            <b>Blocco ${b.index}</b><br>
            ⏱️ ${new Date(b.timestamp*1000).toLocaleString()}<br>
            🔗 Hash: ${b.hash}<br>
            📦 Dati: ${JSON.stringify(b.data)}
          </div>`
        ).join("");
      });
    </script>
    </body></html>
    """)

@app.route("/chain")
def chain():
    if not os.path.exists(CHAIN_FILE):
        return jsonify([])
    with open(CHAIN_FILE) as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(port=8060)
