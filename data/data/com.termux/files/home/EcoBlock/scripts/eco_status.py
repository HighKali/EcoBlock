#!/usr/bin/env python3
from flask import Flask, jsonify
import os, time

app = Flask(__name__)
@app.route("/status")
def status():
    return jsonify({
        "status": "🟢 Online",
        "uptime": f"{int(time.time() - os.stat(__file__).st_ctime)} sec",
        "modules": ["eco_zsona_mint", "eco_zsona_sync", "eco_zsona_transfer", "eco_ui_dashboard"]
    })

if __name__ == "__main__":
    app.run(port=8070)
