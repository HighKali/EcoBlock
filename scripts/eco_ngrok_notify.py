#!/usr/bin/env python3
import requests, time

found = False
for attempt in range(10):
    for port in ["4040", "4041"]:
        try:
            r = requests.get(f"http://127.0.0.1:{port}/api/tunnels", timeout=2)
            tunnels = r.json().get("tunnels", [])
            for t in tunnels:
                public_url = t.get("public_url", "")
                if public_url.startswith("https://"):
                    print(f"✅ Tunnel HTTPS attivo: {public_url}")
                    with open("wallet/ngrok_url.txt", "w") as f:
                        f.write(public_url + "\n")
                    found = True
                    break
            if found:
                break
        except Exception:
            continue
    if found:
        break
    time.sleep(1)

if not found:
    print("❌ Nessun tunnel HTTPS trovato. ngrok potrebbe non essere connesso.")
    with open("wallet/ngrok_error.log", "w") as f:
        f.write("Tunnel non trovato dopo 10 tentativi.\n")
    print("💡 Suggerimenti:")
    print("- Verifica che ngrok sia avviato correttamente")
    print("- Usa 'ngrok http 8050' in foreground per vedere errori")
    print("- Controlla che il server Flask sia attivo su porta 8050")
