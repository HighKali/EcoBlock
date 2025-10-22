#!/bin/bash
echo "📦 Onboarding collaboratore ZSONA..."
bash scripts/eco_zsona_gen.sh
cp dashboard/assets/badge_founder_zsona.svg wallets/
python3 scripts/eco_badge_mint.py
python3 scripts/eco_qr_public.py
python3 scripts/eco_notify.py --msg "👤 Collaboratore onboarded con wallet, badge NFT e QR"

