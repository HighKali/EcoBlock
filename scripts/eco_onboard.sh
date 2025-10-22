#!/bin/bash
echo "📦 Onboarding collaboratore ZSONA..."
bash scripts/eco_zsona_gen.sh
cp dashboard/assets/badge_founder_zsona.svg wallets/
echo "✅ Wallet generato e badge assegnato"
python3 scripts/eco_notify.py --msg "👤 Nuovo collaboratore onboarded con wallet e badge"

