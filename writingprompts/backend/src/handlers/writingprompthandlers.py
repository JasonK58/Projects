"""
Handlers to generate writing prompts using ChatGPT.
"""

from ..gemini.client import GoogleGeminiClient


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

    query = (
        f"Create a {genre} one sentence writing prompt using the following keywords: "
        f"{keywords_formatted_string}."
    )

    gemini_client = GoogleGeminiClient()
    generated_prompt = gemini_client.make_request(query)

    return generated_prompt
