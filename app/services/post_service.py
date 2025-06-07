import httpx
from dotenv import load_dotenv
import os

load_dotenv()
API_URL = os.getenv("API_URL")

async def get_all_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/posts")
        return response.json()
