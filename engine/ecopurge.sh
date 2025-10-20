#!/bin/bash
echo "🧹 Pulizia file non rilevanti..."
find ~/ecoblock-dashboard -type f -name "*.tmp" -delete
echo "✅ Pulizia completata"
