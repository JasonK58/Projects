"""
Unit Tests for ChatGPT client
"""

import unittest
from unittest import mock
from unittest.mock import MagicMock

from writingprompts.backend.src.handlers.writingprompthandlers import create_writing_prompt


class TestWritingPromptHandlers(unittest.TestCase):
    """
    Writing prompt handler tests
    """

    GENRE = "comedy"
    GENERATED_PROMPT = (
        "Two cops get in over their heads when they stumble upon a heist in action."
    )

    @mock.patch("google.generativeai.GenerativeModel")
    def test_create_writing_prompt_with_keywords(self, mock_gemini):
        """
        Test a request can be made to the client when provided keywords.
        """
        # Arrange
        keywords = ["cops", "heist"]

        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.return_value = MagicMock(
            text=self.GENERATED_PROMPT
        )
        mock_gemini.return_value = mock_model_instance

        # Act
        result = create_writing_prompt(self.GENRE, keywords)

        # Assert
        self.assertEqual(result, self.GENERATED_PROMPT)

    @mock.patch("google.generativeai.GenerativeModel")
    def test_create_writing_prompt_without_keywords(self, mock_gemini):
        """
        Test a request can be made to the client when provided no keywords.
        """
        # Arrange
        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.return_value = MagicMock(
            text=self.GENERATED_PROMPT
        )
        mock_gemini.return_value = mock_model_instance

        # Act
        result = create_writing_prompt(self.GENRE)

        # Assert
        self.assertEqual(result, self.GENERATED_PROMPT)
