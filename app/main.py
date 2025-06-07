from fastapi import FastAPI
from app.routes import post_routes

app = FastAPI(title="Python API Demo")
app.include_router(post_routes.router, prefix="/posts", tags=["Posts"])
