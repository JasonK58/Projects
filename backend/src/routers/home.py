"""
Home routes
"""

from typing import Union

from fastapi import APIRouter

home_router = APIRouter()


@home_router.get("/root/")
def read_root(query_parameters: Union[str, None] = None):
    """
    Route for landing page.
    :param query_parameters: query parameters (optional)
    :return: Hello World message and query parameters from request.
    """
    return {"msg": "Hello World", "q": query_parameters}
