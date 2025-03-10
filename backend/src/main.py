"""
Project entrypoint
"""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routers import home, writingprompt

app = FastAPI(root_path="/api/v1")

origins = [
    "https://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home.home_router)
app.include_router(writingprompt.writing_prompt_router)
