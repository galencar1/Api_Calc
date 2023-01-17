from fastapi import APIRouter
from endpoints import operation

router = APIRouter()
router.include_router(operation.router)
