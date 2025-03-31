"""
FastAPI request body models.
"""

from typing import Optional, List

from pydantic import BaseModel


class WritingPromptRequest(BaseModel):
    """
    Request body for generating a writing prompt
    """

    genre: str
    keywords: Optional[List[str]] = None
