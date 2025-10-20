#!/usr/bin/env python3\nimport secrets\ndef generate_entropy(bits=256):\n entropy = secrets.token_hex(bits // 8)\n print(f"🔐 Entropia generata ({bits} bit):\\n{entropy}")\ngenerate_entropy()
