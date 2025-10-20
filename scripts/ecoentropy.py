#!/usr/bin/env python3
import secrets
def generate_entropy(bits=256):
    entropy = secrets.token_hex(bits // 8)
    print(f"🔐 Entropia generata ({bits} bit):\\n{entropy}")
generate_entropy()
