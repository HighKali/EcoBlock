from fastapi import APIRouter
import os
import time

router = APIRouter()

@router.get("/status/node")
def node_status():
    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "sync_enabled": os.getenv("NODE_SYNC_ENABLED"),
        "refresh_interval": os.getenv("STATUS_REFRESH_INTERVAL"),
        "log_path": os.getenv("STATUS_LOG_PATH"),
        "status": "📡 Nodo sincronizzato"
    }
