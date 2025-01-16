"""
Handlers to generate writing prompts using ChatGPT.
"""

from src.chatgpt.client import ChatGptClient


def create_writing_prompt(genre: str, keywords: [str] = None) -> str:
    """
    Handler to generate writing prompt.
    :param genre: genre the prompt should be catered to.
    :type genre: str
    :param keywords: list of keywords to use for the prompt.
    :type keywords: [str] or None
    :return: Generated writing prompt.
    :rtype: str
    """
    keywords_formatted_string = ",".join(keywords) if keywords else ""

    prompt = (
        f"Create a {genre} writing prompt using the following keywords: "
        f"{keywords_formatted_string}."
    )

    chatgpt_client = ChatGptClient()
    generated_prompt = chatgpt_client.make_request(prompt)

    return generated_prompt
