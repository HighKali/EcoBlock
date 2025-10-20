#!/usr/bin/env python3
import requests
url="http://127.0.0.1:8000/status"
try:
    r=requests.get(url)
    print("✅ RPC status:",r.json())
except Exception as e:
    print("❌ RPC non raggiungibile:",e)
