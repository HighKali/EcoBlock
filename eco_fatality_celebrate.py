#!/usr/bin/env python3
import eco_hostblock_publish, eco_zsona_badge_mint, eco_zsona_matrix_notify

print("🎉 Avvio celebrazione finale…")
eco_hostblock_publish.publish_release()
eco_zsona_badge_mint.mint_badge()
eco_zsona_matrix_notify.send_notification()
print("✅ Celebrazione completata")
