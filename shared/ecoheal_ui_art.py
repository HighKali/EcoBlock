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
