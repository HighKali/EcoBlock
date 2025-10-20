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

def check_file_exists(path, label):
    if not os.path.exists(path):
        log(f"❌ {label} non trovato: {path}")
        return False
    log(f"✅ {label} trovato: {path}")
    return True

def check_script_inclusion():
    with open(html_path, "r") as f:
        html = f.read()
    if "scripts.js" in html:
        log("✅ scripts.js incluso correttamente in index.html")
    else:
        log("❌ scripts.js non incluso in index.html")

def check_onclick_buttons():
    with open(html_path, "r") as f:
        html = f.read()
    buttons = re.findall(r'<button[^>]*>', html)
    if not buttons:
        log("❌ Nessun <button> trovato in index.html")
        return
    missing = [btn for btn in buttons if "onclick=" not in btn]
    if missing:
        log(f"⚠️ {len(missing)} bottoni senza onclick rilevati:")
        for b in missing:
            log(f"   - {b.strip()}")
    else:
        log("✅ Tutti i bottoni hanno attributo onclick")

def check_js_functions():
    with open(js_path, "r") as f:
        js = f.read()
    for func in ["generaWallet", "generaEntropia"]:
        if re.search(rf"function\s+{func}\s*\(", js):
            log(f"✅ Funzione {func}() presente in scripts.js")
        else:
            log(f"❌ Funzione {func}() mancante in scripts.js")

def main():
    log("🔍 Avvio diagnosi UI EcoBlock")
    if check_file_exists(html_path, "index.html") and check_file_exists(js_path, "scripts.js"):
        check_script_inclusion()
        check_onclick_buttons()
        check_js_functions()
    log("✅ Diagnosi completata.\n")

if __name__ == "__main__":
    main()
