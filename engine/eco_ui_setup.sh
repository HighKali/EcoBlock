#!/bin/bash

# === Eco UI Setup ===
# Genera notifiche animate, SVG laser-style, aggiorna dashboard

PROJECT_DIR=~/ecoblock-dashboard
ASSETS_DIR="$PROJECT_DIR/assets"
JS_FILE="$PROJECT_DIR/eco_ui_notify.js"
HTML_FILE="$PROJECT_DIR/index.html"
PY_ART="$PROJECT_DIR/ecoheal_ui_art.py"

mkdir -p "$ASSETS_DIR"

# 1. eco_ui_notify.js
cat << 'EOF' > "$JS_FILE"
function notify(message, type = "info") {
  const colors = {
    success: "#00ffcc",
    error: "#ff4444",
    info: "#cccccc"
  };
  const toast = document.createElement("div");
  toast.textContent = message;
  toast.style.position = "fixed";
  toast.style.bottom = "20px";
  toast.style.right = "20px";
  toast.style.background = colors[type] || colors.info;
  toast.style.color = "#000";
  toast.style.padding = "10px 20px";
  toast.style.borderRadius = "8px";
  toast.style.boxShadow = "0 0 10px rgba(0,0,0,0.3)";
  toast.style.zIndex = "9999";
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 4000);
}
EOF

# 2. ecoheal_ui_art.py
cat << 'EOF' > "$PY_ART"
import os
svg_logo = '''<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120">
<circle cx="60" cy="60" r="50" stroke="#00ffcc" stroke-width="4" fill="none"/>
<text x="60" y="65" font-size="14" text-anchor="middle" fill="#00ffcc">EcoBlock</text>
</svg>'''
svg_map = '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="150">
<rect x="10" y="10" width="280" height="130" stroke="#00ffcc" fill="none" stroke-width="2"/>
<line x1="10" y1="10" x2="290" y2="140" stroke="#00ffcc" stroke-width="1"/>
</svg>'''
assets_path = os.path.expanduser("~/ecoblock-dashboard/assets")
os.makedirs(assets_path, exist_ok=True)
with open(os.path.join(assets_path, "logo.svg"), "w") as f:
    f.write(svg_logo)
with open(os.path.join(assets_path, "map.svg"), "w") as f:
    f.write(svg_map)
print("✅ SVG laser-style aggiornati")
EOF

# 3. Aggiorna index.html per usare notify()
if grep -q "alert(" "$HTML_FILE"; then
  sed -i 's/alert(/notify(/g' "$HTML_FILE"
  sed -i '/<\/body>/i <script src="eco_ui_notify.js"></script>' "$HTML_FILE"
  echo "✅ index.html aggiornato con notifiche animate"
else
  echo "ℹ️ Nessun alert trovato in index.html"
fi

# 4. Esegui arte SVG
python "$PY_ART"

echo "✅ Eco UI Setup completato"
