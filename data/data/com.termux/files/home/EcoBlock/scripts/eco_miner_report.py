#!/usr/bin/env python3
import json, os, time

CHAIN_FILE = "wallet/zsona_chain.json"
REPORT_FILE = "wallet/miner_report.log"

def log_report():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    with open(REPORT_FILE, "a") as log:
        for b in chain[-5:]:
            ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(b["timestamp"]))
            log.write(f"[{ts}] Blocco {b['index']} → {b['data']['to']} +{b['data']['amount']} ZSONA\n")
    return "📄 Report miner aggiornato"

if __name__ == "__main__":
    print(log_report())
