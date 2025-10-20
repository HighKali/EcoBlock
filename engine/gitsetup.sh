#!/bin/bash

# === EcoBlock Git Setup ===
# Inizializza, configura, committa e pubblica su GitHub

REPO_NAME="ecoblock-dashboard"
GITHUB_USER="HighKali"
GIT_EMAIL="xdsn.miner@gmail.com"
BRANCH="main"
COMMIT_MSG="EcoBlock Dashboard: layout laser, moduli interattivi, pronto per Vercel"

echo "📁 Spostamento nella directory del progetto..."
cd ~/ecoblock-dashboard || { echo "❌ Directory non trovata"; exit 1; }

echo "🔧 Inizializzo Git..."
git init
git config user.name "$GITHUB_USER"
git config user.email "$GIT_EMAIL"
git branch -m "$BRANCH"

echo "📦 Aggiungo tutti i file..."
git add .

echo "📝 Eseguo il commit..."
git commit -m "$COMMIT_MSG"

echo "🌐 Collego il repository remoto..."
git remote add origin "https://github.com/$GITHUB_USER/$REPO_NAME.git"

echo "🚀 Eseguo il push su GitHub..."
git push -u origin "$BRANCH"

echo "✅ Completato! Controlla su: https://github.com/$GITHUB_USER/$REPO_NAME"
