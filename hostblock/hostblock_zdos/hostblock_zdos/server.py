from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# 🔐 Carica variabili da .env
load_dotenv()

# ⚙️ Inizializza FastAPI
app = FastAPI(
    title="HostBlock zDOS",
    description="Nodo modulare per mining etico e RPC",
    version="1.0.0"
)

# 🌍 CORS universale
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 Endpoint principale
@app.get("/")
def read_root():
    return {
        "message": "🚀 HostBlock zDOS è attivo",
        "rpc": f"http://{os.getenv('RPC_HOST', '127.0.0.1')}:{os.getenv('RPC_PORT', '8080')}",
        "wallet": os.getenv("WALLET_ADDRESS", "undefined"),
        "chain": os.getenv("WALLET_CHAIN_ID", "undefined"),
        "mining": os.getenv("MINING_ENABLED", "false"),
        "sync": os.getenv("NODE_SYNC_ENABLED", "false")
    }

# 🔁 Importa moduli se presenti
try:
    from rpc.router import router as rpc_router
    app.include_router(rpc_router, prefix="/rpc")
except Exception:
    pass

try:
    from endpoints.wallet import router as wallet_router
    app.include_router(wallet_router)
except Exception:
    pass

try:
    from endpoints.status import router as status_router
    app.include_router(status_router)
except Exception:
    pass
