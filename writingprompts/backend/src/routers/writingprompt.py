"""
Writing prompt routes
"""

from fastapi import APIRouter, HTTPException

from ..handlers.writingprompthandlers import create_writing_prompt
from ..models.requests import WritingPromptRequest
from ..models.responses import WritingPromptResponse

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

    if not prompt_request.genre:
        raise HTTPException(
            status_code=422,
            detail="Please provide a genre to generate a writing prompt.",
        )

    generated_prompt = create_writing_prompt(
        prompt_request.genre, prompt_request.keywords
    )

    response = WritingPromptResponse(msg=generated_prompt)

    return response
