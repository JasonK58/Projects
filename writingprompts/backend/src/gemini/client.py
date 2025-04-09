"""
Google Gemini AI client.
"""

import os

from fastapi import HTTPException
from google import genai
from google.genai.errors import APIError


class GoogleGeminiClient:  # pylint: disable=too-few-public-methods
    """
    Client to make requests to Google Gemini.
    """

    MODEL = os.environ.get("GEMINI_MODEL")

    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def make_request(self, query: str) -> str:
        """
        Make a request to the Gemini API.
        :param query: query to ask Gemini.
        :type query: str
        :return: Response from Gemini
        :rtype: str
        """
        try:
            response = self.client.models.generate_content(
                model=self.MODEL, contents=query
            )
        except APIError as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e

        return response.text
