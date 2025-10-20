#!/usr/bin/env python3
import hashlib, json, time, os

CHAIN_FILE = "wallet/zsona_chain.json"

def load_chain():
    if not os.path.exists(CHAIN_FILE):
        return []
    with open(CHAIN_FILE) as f:
        return json.load(f)

def save_chain(chain):
    with open(CHAIN_FILE, "w") as f:
        json.dump(chain, f, indent=2)

def create_block(data):
    chain = load_chain()
    index = len(chain)
    timestamp = time.time()
    prev_hash = chain[-1]["hash"] if chain else "0"*64
    block_data = json.dumps(data, sort_keys=True)
    raw = f"{index}{timestamp}{block_data}{prev_hash}"
    block_hash = hashlib.sha256(raw.encode()).hexdigest()
    block = {
        "index": index,
        "timestamp": timestamp,
        "data": data,
        "prev_hash": prev_hash,
        "hash": block_hash
    }
    chain.append(block)
    save_chain(chain)
    return block

if __name__ == "__main__":
    tx = {"from": "ZSONA-kali13", "to": "ZSONA-ecoagent", "amount": 250}
    block = create_block(tx)
    print(f"🧱 Blocco creato: {block['index']} con hash {block['hash']}")
