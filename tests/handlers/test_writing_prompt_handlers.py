"""
Unit Tests for ChatGPT client
"""

import unittest
from unittest import mock
from unittest.mock import MagicMock

from src.handlers.writingprompthandlers import create_writing_prompt


class TestWritingPromptHandlers(unittest.TestCase):
    """
    Writing prompt handler tests
    """

    GENRE = "comedy"
    GENERATED_PROMPT = (
        "Two cops get in over their heads when they stumble upon a heist in action."
    )

    @mock.patch("os.environ", {"OPENAI_API_KEY": "mocked_key"})
    @mock.patch("src.chatgpt.client.OpenAI")
    def test_create_writing_prompt_with_keywords(self, mock_open_ai):
        """
        Test a request can be made to the client when provided keywords.
        """
        # Arrange
        keywords = ["cops", "heist"]

        mock_openai_instance = mock_open_ai.return_value

        mock_chat_completions_create = MagicMock()
        mock_chat_completions_create.return_value = {
            "choices": [{"message": {"content": self.GENERATED_PROMPT}}]
        }

        mock_openai_instance.chat.completions.create = mock_chat_completions_create

        # Act
        result = create_writing_prompt(self.GENRE, keywords)

        # Assert
        self.assertEqual(result, self.GENERATED_PROMPT)

    @mock.patch("os.environ", {"OPENAI_API_KEY": "mocked_key"})
    @mock.patch("src.chatgpt.client.OpenAI")
    def test_create_writing_prompt_without_keywords(self, mock_open_ai):
        """
        Test a request can be made to the client when provided no keywords.
        """
        # Arrange
        mock_openai_instance = mock_open_ai.return_value

        mock_chat_completions_create = MagicMock()
        mock_chat_completions_create.return_value = {
            "choices": [{"message": {"content": self.GENERATED_PROMPT}}]
        }

        mock_openai_instance.chat.completions.create = mock_chat_completions_create

        # Act
        result = create_writing_prompt(self.GENRE)

        # Assert
        self.assertEqual(result, self.GENERATED_PROMPT)
