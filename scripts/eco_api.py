#!/usr/bin/env python3
from flask import Flask, jsonify, request
import json, time

app = Flask(__name__)

@app.route("/api/onboarded", methods=["GET"])
def get_onboarded():
    with open("data/onboarded.json") as f:
        return jsonify(json.load(f))

@app.route("/api/onboard", methods=["POST"])
def onboard_user():
    data = request.json
    data["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("data/onboarded.json", "r+") as f:
        onboarded = json.load(f)
        onboarded.append(data)
        f.seek(0)
        json.dump(onboarded, f, indent=2)
    return jsonify({"status": "ok", "msg": "✅ Onboard registrato"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

