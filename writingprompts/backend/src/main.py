"""
Project entrypoint
"""

import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routers import home, writingprompt

app = FastAPI(root_path="/api/v1")

# Pytest is not reading the values from env, so a fallback of 'testing' is
# used to ensure the value is not empty when running the test suite.
origins = os.environ.get("WHITELIST_ORIGINS", "testing")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(home.home_router)
app.include_router(writingprompt.writing_prompt_router)
