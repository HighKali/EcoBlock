#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "✅ RPC server attivo"
if __name__ == "__main__":
    app.run(port=8000)
