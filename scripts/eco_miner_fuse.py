#!/usr/bin/env python3
import json, os

CHAIN_FILE = "wallet/zsona_chain.json"
FUSED_FILE = "wallet/zsona_chain_fused.json"

def fuse():
    if not os.path.exists(CHAIN_FILE):
        return "❌ Chain mancante"
    with open(CHAIN_FILE) as f:
        chain = json.load(f)
    fused = {b["index"]: b for b in chain}
    result = [fused[i] for i in sorted(fused)]
    with open(FUSED_FILE, "w") as f:
        json.dump(result, f, indent=2)
    return f"🔗 Chain fusa: {len(result)} blocchi unificati"

if __name__ == "__main__":
    print(fuse())
