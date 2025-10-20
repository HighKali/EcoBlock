#!/usr/bin/env python3
import json, csv, os

CHAIN_FILE = "wallet/zsona_chain.json"
CSV_FILE = "wallet/zsona_chain.csv"
JSON_FILE = "wallet/zsona_chain_export.json"

def export_chain():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    with open(CSV_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Index", "Timestamp", "From", "To", "Amount", "Hash"])
        for b in chain:
            tx = b["data"]
            writer.writerow([b["index"], b["timestamp"], tx["from"], tx["to"], tx["amount"], b["hash"]])
    with open(JSON_FILE, "w") as jf:
        json.dump(chain, jf, indent=2)
    return "📤 Chain esportata in CSV e JSON"

if __name__ == "__main__":
    print(export_chain())
