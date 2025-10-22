#!/usr/bin/env python3
import qrcode, requests
r = requests.get("http://127.0.0.1:4040/api/tunnels")
url = r.json()["tunnels"][0]["public_url"]
img = qrcode.make(url)
img.save("dashboard/assets/eco_qr_public.png")
print(f"📱 QR code generato per: {url}")

