"""
FastAPI Response body models.
"""

from pydantic import BaseModel


class WritingPromptResponse(BaseModel):
    """
    Response body for generating a writing prompt.
    """

    msg: str
