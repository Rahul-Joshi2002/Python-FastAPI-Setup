from fastapi import APIRouter
from app.services.post_service import get_all_posts

router = APIRouter()

@router.get("/")
async def read_posts():
    return await get_all_posts()
