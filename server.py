from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/style.css")
def style():
    return send_file("style.css")

@app.route("/script.js")
def script():
    return send_file("script.js")

@app.route("/faucet_dsn")
def faucet_dsn():
    return "<h2>Modulo attivo: Faucet DSN</h2>"

@app.route("/faucet_zsona")
def faucet_zsona():
    return "<h2>Modulo attivo: Faucet ZSONA</h2>"

@app.route("/miner")
def miner():
    return "<h2>Modulo attivo: Miner Web ZSONA</h2>"

@app.route("/wallet")
def wallet():
    return "<h2>Modulo attivo: Wallet</h2>"

@app.route("/dex")
def dex():
    return "<h2>Modulo attivo: DEX ZSONA/$DSN</h2>"

@app.route("/pool")
def pool():
    return "<h2>Modulo attivo: POOL ZSONA/$DSN</h2>"

@app.route("/report")
def report():
    return send_file("eco_sync_report.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
