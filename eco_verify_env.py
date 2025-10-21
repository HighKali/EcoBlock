#!/usr/bin/env python3
import os
required=["RPC_KEY","WALLET_SEED","NGROK_AUTH"]
path=os.path.expanduser("~/EcoBlock/.env.template")
print("🔍 Verifica .env:")
if not os.path.exists(path):
    print("❌ .env.template mancante")
else:
    content=open(path).read()
    [print(f"✅ {k} presente" if k in content else f"❌ {k} mancante") for k in required]
