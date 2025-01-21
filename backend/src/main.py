"""
Project entrypoint
"""

from fastapi import FastAPI

from .routers import home, writingprompt

app = FastAPI()

app.include_router(home.home_router)
app.include_router(writingprompt.writing_prompt_router)
