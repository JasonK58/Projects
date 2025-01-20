"""
Writing prompt routes
"""

from fastapi import APIRouter

from src.handlers.writingprompthandlers import create_writing_prompt
from src.models.requests import WritingPromptRequest
from src.models.responses import WritingPromptResponse

writing_prompt_router = APIRouter()


@writing_prompt_router.post("/writingprompt")
def create_prompt(prompt_request: WritingPromptRequest) -> WritingPromptResponse:
    """
    Endpoint to generate a writing prompt
    :param prompt_request: request body
    :type prompt_request: WritingPromptRequest
    :return: AI generated writing prompt
    :rtype: WritingPromptResponse
    """
    generated_prompt = create_writing_prompt(
        prompt_request.genre, prompt_request.keywords
    )

    response = WritingPromptResponse(msg=generated_prompt)

    return response
