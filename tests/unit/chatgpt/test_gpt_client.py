"""
Unit Tests for ChatGPT client
"""

import unittest
from unittest import mock
from unittest.mock import MagicMock

from src.chatgpt.client import ChatGptClient


class TestGptClient(unittest.TestCase):
    """
    ChatGPT client tests
    """

    @mock.patch("os.environ", {"OPENAI_API_KEY": "mocked_key"})
    @mock.patch("src.chatgpt.client.OpenAI")
    def test_make_request(self, mock_open_ai):
        """
        Test a request can be made to the client.
        """
        # Arrange
        content_message = "What is 1 + 1?"
        response_message = "The answer is 2."
        mock_openai_instance = mock_open_ai.return_value

        mock_chat_completions_create = MagicMock()
        mock_chat_completions_create.return_value = {
            "choices": [{"message": {"content": response_message}}]
        }

        mock_openai_instance.chat.completions.create = mock_chat_completions_create

        client = ChatGptClient()

        # Act
        response = client.make_request(content_message)

        # Assert
        self.assertEqual(response, response_message)
