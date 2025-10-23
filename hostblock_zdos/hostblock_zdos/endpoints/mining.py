from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def mining_endpoint():
    return {"status": "active", "difficulty": 3, "algorithm": "ethash"}
