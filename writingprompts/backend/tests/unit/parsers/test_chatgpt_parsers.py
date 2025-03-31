"""
Unit tests for ChatGPT parsers
"""

import unittest
from unittest.mock import MagicMock

from writingprompts.backend.src.parsers.chatgpt_parsers import parse_chatgpt_single_response


class TestChatGPTParsers(unittest.TestCase):
    """
    Tests for ChatGPT parsers
    """

    def test_parse_message_from_chat_completion(self):
        """
        Tests a single message can be parsed from a ChatGPT chat completion object.
        """
        # Arrange
        response_message = "Test"
        mock_chat_completion = MagicMock()
        mock_chat_completion.__getitem__.side_effect = lambda key: {
            "choices": [{"message": {"content": response_message}}]
        }[key]

        # Act
        result = parse_chatgpt_single_response(mock_chat_completion)

        # Assert
        self.assertEqual(result, response_message)
