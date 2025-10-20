import os
import re
from datetime import datetime

project_dir = os.path.expanduser("~/ecoblock-dashboard")
html_path = os.path.join(project_dir, "index.html")
js_path = os.path.join(project_dir, "scripts.js")
log_path = os.path.join(project_dir, "ui_diagnose.log")

def log(message):
    with open(log_path, "a") as log_file:
        log_file.write(f"{datetime.now().isoformat()} - {message}\n")
    print(message)

def ensure_file(path, label):
    if not os.path.exists(path):
        log(f"❌ {label} non trovato: {path}")
        return False
    log(f"✅ {label} trovato: {path}")
    return True

def fix_script_inclusion():
    with open(html_path, "r") as f:
        html = f.read()
    if "scripts.js" not in html:
        log("❌ scripts.js non incluso. Lo aggiungo...")
        html = html.replace("</body>", '<script src="scripts.js"></script>\n</body>')
        with open(html_path, "w") as f:
            f.write(html)
    else:
        log("✅ scripts.js già incluso")

def fix_onclick_buttons():
    with open(html_path, "r") as f:
        html = f.read()
    buttons = re.findall(r'<button[^>]*>.*?</button>', html)
    fixed = 0
    new_html = html
    for btn in buttons:
        if "onclick=" not in btn:
            label = re.search(r'>(.*?)<', btn).group(1)
            func = "generaWallet" if "Wallet" in label else "generaEntropia" if "Entropia" in label else None
            if func:
                new_btn = btn.replace(">", f' onclick="{func}()">', 1)
                new_html = new_html.replace(btn, new_btn)
                fixed += 1
    if fixed > 0:
        with open(html_path, "w") as f:
            f.write(new_html)
        log(f"🔧 {fixed} bottoni riparati con onclick")
    else:
        log("✅ Tutti i bottoni già corretti")

def fix_js_functions():
    with open(js_path, "r") as f:
        js = f.read()
    added = 0
    if "function generaWallet()" not in js:
        js += "\nfunction generaWallet() {\n  alert('✅ Wallet generato!');\n}\n"
        log("🔧 Funzione generaWallet() aggiunta")
        added += 1
    if "function generaEntropia()" not in js:
        js += "\nfunction generaEntropia() {\n  alert('✨ Entropia generata!');\n}\n"
        log("🔧 Funzione generaEntropia() aggiunta")
        added += 1
    if added > 0:
        with open(js_path, "w") as f:
            f.write(js)
    else:
        log("✅ Funzioni JS già presenti")

def main():
    log("🛠️ Avvio EcoHeal UI Fix")
    if ensure_file(html_path, "index.html") and ensure_file(js_path, "scripts.js"):
        fix_script_inclusion()
        fix_onclick_buttons()
        fix_js_functions()
    log("✅ Riparazione completata.\n")

if __name__ == "__main__":
    main()
