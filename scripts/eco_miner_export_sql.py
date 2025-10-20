#!/usr/bin/env python3
import json, os, sqlite3

CHAIN_FILE = "wallet/zsona_chain.json"
DB_FILE = "wallet/zsona_chain.db"

def export_sql():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS blocks")
    c.execute("CREATE TABLE blocks (idx INTEGER, ts INTEGER, sender TEXT, receiver TEXT, amount REAL, hash TEXT)")
    for b in chain:
        tx = b["data"]
        c.execute("INSERT INTO blocks VALUES (?, ?, ?, ?, ?, ?)", (b["index"], b["timestamp"], tx["from"], tx["to"], tx["amount"], b["hash"]))
    conn.commit()
    conn.close()
    return "🗃️ Chain esportata in SQLite"

if __name__ == "__main__":
    print(export_sql())
