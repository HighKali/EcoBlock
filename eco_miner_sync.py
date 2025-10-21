import json, time
data = {"timestamp": time.time(), "miner_status": "active", "hashrate": "42.5 H/s", "pool": "ZSONA/"}
with open("wallet/miner_status.json", "w") as f: json.dump(data, f)
print("✅ Miner sincronizzato")
