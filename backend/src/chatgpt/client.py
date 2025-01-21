"""
ChatGPT Client class
"""

import os

from openai import OpenAI

from ..parsers.chatgpt_parsers import parse_chatgpt_single_response

MODEL = "gpt-3.5-turbo"
ROLE = "user"


class ChatGptClient:  # pylint: disable=too-few-public-methods
    """
    ChatGPT client to make server requests
    """

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def make_request(self, content_message: str) -> str:
        """
        Makes a request to ChatGPT server
        :param content_message: request message being sent to ChatGPT
        :type content_message: str
        :return: Generated AI response
        :rtype: str
        """
        chat_completion = self.client.chat.completions.create(
            messages=[{"role": ROLE, "content": content_message}], model=MODEL
        )

        parsed_response = parse_chatgpt_single_response(chat_completion)

        return parsed_response
