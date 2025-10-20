from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/status")
def rpc_status():
    return {
        "status": "✅ RPC operativo",
        "host": os.getenv("RPC_HOST"),
        "port": os.getenv("RPC_PORT"),
        "chain": os.getenv("WALLET_CHAIN_ID"),
        "wallet": os.getenv("WALLET_ADDRESS")
    
