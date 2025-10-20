#!/usr/bin/env python3
import json, os

CONFIG_FILE = "wallet/miner_config.json"

def admin():
    config = {
        "max_reward": 500,
        "mining_interval": 30,
        "nodes": ["127.0.0.1:8090", "127.0.0.1:8040"]
    }
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
    print("🛠️ Configurazione miner salvata in miner_config.json")

if __name__ == "__main__":
    admin()
