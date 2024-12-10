"""
Project entrypoint
"""

from fastapi import FastAPI

from src.routers import home

app = FastAPI()

app.include_router(home.home_router)
