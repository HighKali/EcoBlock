#!/usr/bin/env python3
from flask import Flask, render_template_string, jsonify
import json, os, time, random, requests

app = Flask(__name__)
STATE = os.path.join("wallet", "wallet_zsona.txt")
POOL_API = "https://api.oceanminer.org/status"

@app.route("/")
def dashboard():
    return render_template_string("""
    <html>
    <head>
      <title>ZSONA Dashboard</title>
      <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body style="background:#0f1117;color:#fff;font-family:sans-serif">
      <h1>🌐 EcoBlock ZSONA Dashboard</h1>
      <canvas id="uptimeChart" width="400" height="200"></canvas>
      <canvas id="rewardChart" width="400" height="200"></canvas>
      <canvas id="poolChart" width="400" height="200"></canvas>
      <script>
        async function fetchData() {
          const res = await fetch("/data");
          const data = await res.json();
          renderCharts(data);
        }

        function renderCharts(data) {
          new Chart(document.getElementById("uptimeChart"), {
            type: "line",
            data: {
              labels: data.timestamps,
              datasets: [{ label: "Uptime Score", data: data.uptime, borderColor: "#00ffc8" }]
            }
          });
          new Chart(document.getElementById("rewardChart"), {
            type: "bar",
            data: {
              labels: data.timestamps,
              datasets: [{ label: "ZSONA Minted", data: data.reward, backgroundColor: "#00ffc8" }]
            }
          });
          new Chart(document.getElementById("poolChart"), {
            type: "line",
            data: {
              labels: data.timestamps,
              datasets: [{ label: "Pool Hashrate", data: data.hashrate, borderColor: "#00ffc8" }]
            }
          });
        }

        fetchData();
      </script>
    </body>
    </html>
    """)

@app.route("/data")
def data():
    timestamps = [time.strftime("%H:%M", time.localtime(time.time() - i*60)) for i in range(10)][::-1]
    uptime = [random.randint(10,100) for _ in range(10)]
    reward = [random.randint(5,50) for _ in range(10)]
    try:
        res = requests.get(POOL_API)
        pool = int(res.json().get("hashrate", 0))
    except:
        pool = 0
    hashrate = [pool + random.randint(-100,100) for _ in range(10)]
    return jsonify({"timestamps": timestamps, "uptime": uptime, "reward": reward, "hashrate": hashrate})

if __name__ == "__main__":
    app.run(port=5000)
