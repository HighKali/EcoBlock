#!/usr/bin/env python3
import random, os

THEME_FILE = "dashboard/ui_theme.css"
themes = [
    {"bg": "#000", "fg": "#0ff", "accent": "#ff00ff"},
    {"bg": "#111", "fg": "#ffcc00", "accent": "#00ffcc"},
    {"bg": "#222", "fg": "#00ff00", "accent": "#ff0000"},
]

def apply_random_theme():
    t = random.choice(themes)
    css = f"body{{background:{t['bg']};color:{t['fg']};}}h1{{color:{t['accent']};}}"
    with open(THEME_FILE, "w") as f:
        f.write(css)
    print(f"🎨 Tema casuale applicato: bg={t['bg']}, fg={t['fg']}, accent={t['accent']}")

if __name__ == "__main__":
    apply_random_theme()
