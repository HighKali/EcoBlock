#!/usr/bin/env python3
import os

def self_heal():
    repaired = 0
    for f in os.listdir("scripts"):
        if f.startswith("eco_") and f.endswith(".py"):
            path = os.path.join("scripts", f)
            if not os.access(path, os.X_OK):
                os.chmod(path, 0o755)
                repaired += 1
    return f"🩺 Moduli riparati: {repaired}"

if __name__ == "__main__":
    print(self_heal())
