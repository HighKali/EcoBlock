#!/usr/bin/env python3
import os

THEME_FILE = "dashboard/ui_theme.css"

def switch_theme(mode="dark"):
    if mode == "light":
        theme = "body { background:#fff; color:#000; } h1 { color:#0077cc; }"
    else:
        theme = "body { background:#000; color:#0ff; } h1 { color:#ff00ff; }"
    with open(THEME_FILE, "w") as f:
        f.write(theme)
    return f"🎨 Tema '{mode}' applicato"

if __name__ == "__main__":
    print(switch_theme("dark"))
