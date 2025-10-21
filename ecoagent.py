import time, os
from datetime import datetime
log_path = "logs/ecoagent.log"
os.makedirs("logs", exist_ok=True)
entry = {"timestamp": datetime.utcnow().isoformat(), "uptime": os.popen("uptime").read().strip(), "battery": os.popen("termux-battery-status").read().strip() if os.name != "nt" else "N/A"}
with open(log_path, "a") as f: f.write(str(entry) + "\n")
print("✅ ecoagent.py: log energia registrato")
