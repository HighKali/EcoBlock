#!/usr/bin/env python3
import os

THEME_FILE = "dashboard/ui_theme.css"

def generate_theme():
    theme = """
body {
  background-color: #0a0a0a;
  color: #00ffcc;
  font-family: 'Courier New', monospace;
}
h1 {
  color: #ff00ff;
}
.block {
  border: 1px solid #00ffcc;
  padding: 10px;
  margin: 5px;
  background-color: #111;
}
"""
    with open(THEME_FILE, "w") as f:
        f.write(theme)
    return "🎨 Tema SVG/UI generato"

if __name__ == "__main__":
    print(generate_theme())
