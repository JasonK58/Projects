"""
ChatGPT Client class
"""

import os
import string

from openai import OpenAI

MODEL = "gpt-4o"
ROLE = "user"


class ChatGptClient:
    """
    ChatGPT client to make server requests
    """

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def make_request(self, content_message: string):
        """
        Makes a request to ChatGPT server
        :return: Generated AI response
        """
        chat_completion = self.client.chat.completions.create(
            messages=[{"role": ROLE, "content": content_message}], model=MODEL
        )

        return chat_completion
