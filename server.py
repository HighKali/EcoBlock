from flask import Flask, send_from_directory, request
import subprocess, os

app = Flask(__name__, static_folder="dashboard")

@app.route("/")
def home():
    return send_from_directory("dashboard", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("dashboard", path)

@app.route("/run/<script>")
def run(script):
    args = request.args.get("args", "")
    path = f"./scripts/{script}.py" if script != "eco_publish" else f"./scripts/{script}.sh"
    try:
        cmd = ["bash", path] if path.endswith(".sh") else ["python", path] + args.split(",") if args else ["python", path]
        result = subprocess.check_output(cmd)
        return result.decode("utf-8")
    except Exception as e:
        return f"❌ Errore: {e}"

if __name__ == "__main__":
    app.run(port=8000)
