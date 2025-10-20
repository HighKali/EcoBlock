#!/usr/bin/env python3
import datetime, os
path=os.path.expanduser("~/EcoBlock/logs/eco.log")
with open(path,"a") as f:
    f.write(f"[{datetime.datetime.now()}] 🧠 EcoBlock avviato correttamente\\n")
