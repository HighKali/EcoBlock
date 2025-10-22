#!/usr/bin/env python3
import hashlib
def validate_block(block_data):
    block_hash = hashlib.sha256(block_data.encode()).hexdigest()
    signature = hashlib.sha256((block_hash + "validator_key").encode()).hexdigest()
    print(f"✅ Blocco validato: {block_hash[:16]}...")
    print(f"🔏 Firma: {signature[:32]}")
validate_block("tx:ZSONA→DSN:100")
