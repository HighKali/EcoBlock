#!/usr/bin/env python3
import json, hashlib, time, os
from eco_zsona_wallet import verify_signature

CHAIN_FILE = "wallet/zsona_chain.json"

def validate_chain():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Nessuna chain trovata"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    for i, block in enumerate(chain):
        raw = f"{block['index']}{block['timestamp']}{json.dumps(block['data'], sort_keys=True)}{block['prev_hash']}"
        expected_hash = hashlib.sha256(raw.encode()).hexdigest()
        if block["hash"] != expected_hash:
            return f"❌ Hash mismatch nel blocco {i}"
    return f"✅ Chain valida con {len(chain)} blocchi"

def validate_tx(tx):
    required = ["from", "to", "amount", "signature", "pubkey"]
    if not all(k in tx for k in required):
        return "❌ Transazione incompleta"
    raw = f"{tx['from']}{tx['to']}{tx['amount']}"
    if verify_signature(tx["pubkey"], raw, tx["signature"]):
        return "✅ Firma valida"
    else:
        return "❌ Firma non valida"

if __name__ == "__main__":
    print(validate_chain())
