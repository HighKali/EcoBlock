from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/wallet/balance")
def wallet_balance():
    # Simulazione: in produzione, interroga RPC reale
    return {
        "wallet": os.getenv("WALLET_ADDRESS"),
        "balance": "0.0000 $DSN",
        "status": "🧠 Wallet attivo"
    }

