#!/usr/bin/env python3
import json, os, sys
from datetime import datetime

LOG_PATH = "wallet/eco_log.json"

def log_event(action, files=None, status="ok"):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "files": files or [],
        "user": os.getenv("USER") or "unknown",
        "status": status
    }
    logs = []
    if os.path.exists(LOG_PATH):
        try:
            with open(LOG_PATH) as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append(entry)
    with open(LOG_PATH, "w") as f:
        json.dump(logs, f, indent=2)
    print(f"📜 Log registrato: {action} ({len(files or [])} file)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Uso: eco_log.py <azione> [file1 file2 ...]")
        sys.exit(1)
    action = sys.argv[1]
    files = sys.argv[2:]
    log_event(action, files)
