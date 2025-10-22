#!/usr/bin/env python3
import random
themes = ["dark", "neon", "retro", "matrix", "solarized"]
selected = random.choice(themes)
with open("static/style.css", "w") as f:
    f.write(f"/* 🌈 Tema attivo: {selected} */\\nbody {{ background: #000; color: #0ff; }}")
print(f"🎨 Tema dashboard cambiato: {selected}")

