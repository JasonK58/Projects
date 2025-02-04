"""
Unit Tests for Google Gemini client.
"""
Import sys
import unittest
from unittest import mock
from unittest.mock import MagicMock

from backend.src.gemini.client import GoogleGeminiClient


class TestGeminiClient(unittest.TestCase):
    """
    Gemini client tests
    """

    @mock.patch("google.generativeai.GenerativeModel")
    def test_make_request(self, mock_gemini):
        """
        Test a request to the client returns expected response.
        """
        # Arrange
        query = "what is 1 + 1?"
        mocked_response = "2"

        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.return_value = MagicMock(
            text=mocked_response
        )
        mock_gemini.return_value = mock_model_instance

        client = GoogleGeminiClient()

        # Act
        response = client.make_request(query)

        # Assert
        self.assertEqual(response, mocked_response)
