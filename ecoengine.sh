#!/bin/bash

# === EcoBlock Engine ===
# Unifica moduli, verifica, mining, backup e pubblicazione GitHub
# Autore: Roberto (EcoBlock Architect)
# Data: $(date '+%Y-%m-%d')

# === CONFIG ===
REPO_PATH="$HOME/EcoBlock"
LOG="$REPO_PATH/logs/ecoengine.log"
BRANCH="main"
GIT_USER="highkali"
GIT_EMAIL="xdsn.miner@gmail.com"

# === FUNZIONI ===

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG"
}

run_module() {
  local name="$1"
  local path="$REPO_PATH/modules/$name"
  if [[ -x "$path" ]]; then
    log "Esecuzione modulo: $name"
    "$path" >> "$LOG" 2>&1
    log "Modulo $name completato"
  else
    log "Modulo $name non trovato o non eseguibile"
  fi
}

check_git_changes() {
  cd "$REPO_PATH" || exit
  git config user.name "$GIT_USER"
  git config user.email "$GIT_EMAIL"
  git add .
  if ! git diff --cached --quiet; then
    log "Modifiche rilevate, eseguo commit"
    git commit -m "EcoEngine update: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG" 2>&1
    git push origin "$BRANCH" >> "$LOG" 2>&1
    log "Commit e push completati"
  else
    log "Nessuna modifica da pubblicare"
  fi
}

# === AVVIO ===

log "=== Avvio EcoEngine ==="

run_module "ecoautofix.sh"
run_module "ecopurge.sh"
run_module "ecoignite.sh"
run_module "ecominer.sh"
run_module "ecoverify.sh"
run_module "ecoentropy.py"
run_module "publish.sh"

check_git_changes

log "=== EcoEngine completato ==="
