#!/usr/bin/env python3
import secrets, hashlib
def generate_keypair():
    private_key = secrets.token_hex(32)
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    address = "ZSONA-" + public_key[:32]
    return private_key, address
if __name__ == "__main__":
    pk, addr = generate_keypair()
    print(f"🔐 Private Key: {pk}\n🏦 Address: {addr} (compatible $DSN)")
