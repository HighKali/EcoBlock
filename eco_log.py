import json, os
from datetime import datetime
def log_launch(ip):
    entry = {"timestamp": datetime.utcnow().isoformat(), "action": "launch", "status": "ok", "ip": ip}
    os.makedirs("wallet", exist_ok=True)
    with open("wallet/eco_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
