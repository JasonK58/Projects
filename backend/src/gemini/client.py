"""
Google Gemini AI client.
"""

import os

import google.generativeai as genai


class GoogleGeminiClient:  # pylint: disable=too-few-public-methods
    """
    Client to make requests to Google Gemini.
    """

    MODEL = "gemini-1.5-flash"

    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(self.MODEL)

    def make_request(self, query: str) -> str:
        """
        Make a request to the Gemini API.
        :param query: query to ask Gemini.
        :type query: str
        :return: Response from Gemini
        :rtype: str
        """
        response = self.model.generate_content(query)

        return response.text
