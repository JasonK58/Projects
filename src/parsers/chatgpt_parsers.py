"""
Parsers for ChatGPT
"""

from openai.types.chat import ChatCompletion


def parse_chatgpt_single_response(chat_completion: ChatCompletion) -> str:
    """
    Parses single response message from chatGPT completion object.
    :param chat_completion: ChatGPT response object.
    :type chat_completion: ChatCompletion
    :return: AI response message
    :rtype: str
    """

    return chat_completion["choices"][0]["message"]["content"]
