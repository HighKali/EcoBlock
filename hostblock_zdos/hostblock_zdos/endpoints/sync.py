from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def sync_endpoint():
    return {"synced": True, "last_block": 19238492}
