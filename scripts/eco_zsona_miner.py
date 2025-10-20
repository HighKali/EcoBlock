#!/usr/bin/env python3
import json, time, hashlib, os
from eco_zsona_wallet import sign_data

CHAIN_FILE = "wallet/zsona_chain.json"
WALLET_FILE = "wallet/wallet_zsona.txt"

def load_wallet():
    if not os.path.exists(WALLET_FILE):
        return None
    with open(WALLET_FILE) as f:
        return json.load(f)

def load_chain():
    if not os.path.exists(CHAIN_FILE):
        return []
    with open(CHAIN_FILE) as f:
        return json.load(f)

def save_chain(chain):
    with open(CHAIN_FILE, "w") as f:
        json.dump(chain, f, indent=2)

def mine_block():
    wallet = load_wallet()
    if not wallet or "private" not in wallet or "address" not in wallet:
        return "❌ Wallet non inizializzato con chiave privata"
    chain = load_chain()
    index = len(chain)
    timestamp = time.time()
    prev_hash = chain[-1]["hash"] if chain else "0"*64
    reward = 100 + index
    tx = {
        "from": "eco_miner",
        "to": wallet["address"],
        "amount": reward
    }
    raw = f"{tx['from']}{tx['to']}{tx['amount']}"
    tx["signature"] = sign_data(wallet["private"], raw)
    tx["pubkey"] = wallet["pubkey"]
    block_data = json.dumps(tx, sort_keys=True)
    block_hash = hashlib.sha256(f"{index}{timestamp}{block_data}{prev_hash}".encode()).hexdigest()
    block = {
        "index": index,
        "timestamp": timestamp,
        "data": tx,
        "prev_hash": prev_hash,
        "hash": block_hash
    }
    chain.append(block)
    save_chain(chain)
    return f"⛏️ Blocco {index} minato con reward {reward} ZSONA"

if __name__ == "__main__":
    print(mine_block())
