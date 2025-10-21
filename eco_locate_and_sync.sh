#!/bin/bash
echo "🔍 Localizzazione moduli EcoBlock..."

mkdir -p ~/EcoBlock/scripts

# Sposta moduli Python
for f in ecoagent.py ecoentropy.py eco_sync_status.py eco_log.py eco_test_rpc.py eco_ui_check.py; do
  path=$(find ~/EcoBlock -type f -name "$f" | head -n 1)
  if [ -n "$path" ]; then
    mv "$path" ~/EcoBlock/scripts/
    echo "✅ Spostato: $f"
  else
    echo "⚠️ Non trovato: $f"
  fi
done

# Sposta script di pubblicazione
pub=$(find ~/EcoBlock -type f -name "eco_publish.sh" | head -n 1)
if [ -n "$pub" ]; then
  mv "$pub" ~/EcoBlock/scripts/eco_publish.sh
  echo "✅ Spostato: eco_publish.sh"
else
  echo "⚠️ eco_publish.sh non trovato"
fi

# Copia moduli condivisi
cp ~/EcoBlock/shared/ecoapi.py ~/EcoBlock/shared/ecoheal_ui_fix.py ~/EcoBlock/shared/ecoheal_ui_art.py ~/EcoBlock/scripts/ 2>/dev/null
cp ~/EcoBlock/engine/eco_ngrok_start.sh ~/EcoBlock/scripts/eco_ngrok_start.sh 2>/dev/null

# Sincronizza path nel verificatore
sed -i 's|os.path.join(os.environ.get("HOME", ""), "EcoBlock", m)|os.path.join("scripts", m) if not m.startswith("dashboard") else os.path.join("dashboard", m)|' ~/EcoBlock/scripts/eco_sync_status.py 2>/dev/null

# Crea server Flask
cat <<EOF > ~/EcoBlock/server.py
from flask import Flask, send_from_directory
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
    path = f"./scripts/{script}.py" if script != "eco_publish" else f"./scripts/{script}.sh"
    try:
        result = subprocess.check_output(["bash", path] if path.endswith(".sh") else ["python", path])
        return result.decode("utf-8")
    except Exception as e:
        return f"❌ Errore: {e}"

if __name__ == "__main__":
    app.run(port=8000)
EOF

echo "🚀 Server pronto. Avvio..."
python3 ~/EcoBlock/server.py
