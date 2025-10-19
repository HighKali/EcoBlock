#!/usr/bin/env python3
import requests, json, time

EDIT_URL = "http://localhost:7070/state"
STATUS_URL = "http://localhost:8080/status"

def get_status():
    try:
        r = requests.get(STATUS_URL)
        return r.json()
    except:
        return {}

def get_state():
    try:
        r = requests.get(EDIT_URL)
        return r.json()
    except:
        return {}

def propose_reward(state):
    balance = state.get("zsona_balance", 0)
    workers = state.get("workers", [])
    if not workers or balance < 100:
        return None
    reward = balance // len(workers)
    return {w: reward for w in workers}

def redistribute(state):
    rewards = propose_reward(state)
    if not rewards:
        return {"status": "❌ Nessun reward disponibile"}
    new_balance = state["zsona_balance"] - sum(rewards.values())
    state["zsona_balance"] = new_balance
    state["last_rewards"] = rewards
    r = requests.post(EDIT_URL, json=state)
    return r.json()

def monitor():
    print("🤖 EcoAgent attivo. Analizzo stato ogni 30s...")
    while True:
        status = get_status()
        state = get_state()
        print(f"📊 Bilancio attuale: {state.get('zsona_balance')} zsona")
        if state.get("workers"):
            print(f"👷 Worker attivi: {len(state['workers'])}")
            result = redistribute(state)
            print(f"💸 Reward distribuiti: {result.get('new_state', {}).get('last_rewards')}")
        else:
            print("⚠️ Nessun worker registrato.")
        time.sleep(30)

if __name__ == "__main__":
    monitor()
