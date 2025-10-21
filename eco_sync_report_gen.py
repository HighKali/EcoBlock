import json

with open("wallet/zsona_sync_log.json") as f:
    lines = f.readlines()[-10:]

entries = [json.loads(line) for line in lines]

html = """
<!DOCTYPE html>
<html>
<head>
<title>EcoBlock ZSONA Sync Report</title>
<style>
body { background-color: black; color: #00FF00; font-family: monospace; }
h1 { color: cyan; text-align: center; text-shadow: 0 0 5px #0ff; }
table { width: 100%; border-collapse: collapse; margin-top: 20px; }
th, td { border: 1px solid cyan; padding: 8px; text-align: center; }
canvas { margin-top: 40px; }
</style>
</head>
<body>
<h1>EcoBlock ZSONA Sync Report</h1>
<table>
<tr><th>Timestamp</th><th>Chain ID</th><th>Token</th><th>DEX Volume</th><th>Pool APY</th></tr>
"""

timestamps = []
volumes = []
apys = []

for e in entries:
    ts = e["timestamp"]
    cid = e["chain_id"]
    tok = e["token"]
    vol = e["dex"].get("volume_24h", 0)
    apy = float(e["pool"].get("apy", "0").replace("%", ""))
    html += f"<tr><td>{ts}</td><td>{cid}</td><td>{tok}</td><td>{vol}</td><td>{apy}%</td></tr>\n"
    timestamps.append(ts)
    volumes.append(vol)
    apys.append(apy)

html += "</table>\n<canvas id='syncChart' width='800' height='400'></canvas>\n"
html += """
<script>
const ctx = document.getElementById('syncChart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: %s,
        datasets: [{
            label: 'DEX Volume',
            data: %s,
            borderColor: 'cyan',
            fill: false
        }, {
            label: 'Pool APY',
            data: %s,
            borderColor: 'lime',
            fill: false
        }]
    },
    options: {
        scales: {
            x: { ticks: { color: '#00FF00' } },
            y: { ticks: { color: '#00FF00' } }
        },
        plugins: {
            legend: { labels: { color: '#00FF00' } }
        }
    }
});
</script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</body>
</html>
""" % (timestamps, volumes, apys)

with open("eco_sync_report.html", "w") as f:
    f.write(html)

print("✅ Report generato: eco_sync_report.html")
