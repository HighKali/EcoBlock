#!/usr/bin/env python3
import secrets, hashlib, ecdsa, json, os

def generate_wallet():
    private_key = secrets.token_bytes(32)
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    pubkey = vk.to_string().hex()
    address = "ZSONA-" + hashlib.sha256(pubkey.encode()).hexdigest()[:32]
    return {
        "private": private_key.hex(),
        "pubkey": pubkey,
        "address": address
    }

def sign_data(private_hex, data):
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_hex), curve=ecdsa.SECP256k1)
    signature = sk.sign(data.encode())
    return signature.hex()

def verify_signature(pubkey_hex, data, signature_hex):
    vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(pubkey_hex), curve=ecdsa.SECP256k1)
    try:
        return vk.verify(bytes.fromhex(signature_hex), data.encode())
    except:
        return False

if __name__ == "__main__":
    wallet = generate_wallet()
    print(f"🔐 Private: {wallet['private']}")
    print(f"🔓 Public: {wallet['pubkey']}")
    print(f"🏦 Address: {wallet['address']}")
    os.makedirs("wallet", exist_ok=True)
    with open("wallet/wallet_zsona.txt", "w") as f:
        json.dump(wallet, f, indent=2)
    print("✅ Wallet salvato in formato JSON")
