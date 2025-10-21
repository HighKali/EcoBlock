import sys
sys.path.insert(0, "./svgwrite")
import svgwrite

dwg = svgwrite.Drawing('dashboard.svg', profile='full', size=('800px', '600px'), style="background:#000")
modules = [("GeoBlock", "#00ffff", 50), ("EcoEntropy", "#ff00ff", 150), ("EcoMap", "#00ff00", 250), ("EcoPurge", "#ff9900", 350), ("Wallet", "#ffffff", 450)]
for name, color, y in modules:
    dwg.add(dwg.rect(insert=(50, y), size=(700, 60), rx=10, ry=10, fill=color, opacity=0.2))
    dwg.add(dwg.text(name, insert=(60, y + 40), fill=color, font_size="24px", font_family="Courier New"))
dwg.add(dwg.text("🌐 EcoBlock Laser Dashboard", insert=(200, 40), fill="#ff00ff", font_size="28px", font_family="Courier New"))
dwg.save()
print("✅ SVG dashboard generata: dashboard.svg")
