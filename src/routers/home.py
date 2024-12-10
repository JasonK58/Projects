"""
Home routes
"""

from typing import Union

from fastapi import APIRouter

home_router = APIRouter()


@home_router.get("/")
def read_root(q: Union[str, None] = None):
    """
    Route for landing page.
    :param q: query parameters (optional)
    :return: Hello World message and query parameters from request.
    """
    return {"msg": "Hello World", "q": q}
