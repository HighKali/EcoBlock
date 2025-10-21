import os
missing = []
for folder in ["static", "templates"]:
    if not os.path.exists(folder): missing.append(folder)
if missing: print(f"❌ Asset mancanti: {missing}")
else: print("✅ Tutti gli asset visivi sono presenti")
