#!/usr/bin/env python3
import json, os, csv

CHAIN_FILE = "wallet/zsona_chain.json"
CSV_FILE = "wallet/zsona_chain_live.csv"

def export_csv():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Index", "Timestamp", "From", "To", "Amount", "Hash"])
        for b in chain:
            tx = b["data"]
            writer.writerow([b["index"], b["timestamp"], tx["from"], tx["to"], tx["amount"], b["hash"]])
    return "📄 Chain esportata in CSV live"

if __name__ == "__main__":
    print(export_csv())
