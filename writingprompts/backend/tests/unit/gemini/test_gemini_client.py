"""
Unit Tests for Google Gemini client.
"""

from unittest import mock, TestCase
from unittest.mock import MagicMock

import pytest
from fastapi.exceptions import HTTPException
from google.genai.errors import APIError

from writingprompts.backend.src.gemini.client import GoogleGeminiClient


class TestGeminiClient(TestCase):
    """
    Gemini client tests
    """

    @mock.patch("google.genai.Client")
    def test_make_request(self, mock_gemini):
        """
        Test a request to the server returns expected response.
        """
        # Arrange
        query = "what is 1 + 1?"
        mocked_response = "2"

        mock_model_instance = MagicMock()
        mock_model_instance.models.generate_content.return_value = MagicMock(
            text=mocked_response
        )
        mock_gemini.return_value = mock_model_instance

        client = GoogleGeminiClient()

        # Act
        response = client.make_request(query)

        # Assert
        self.assertEqual(response, mocked_response)

    @mock.patch("google.genai.Client")
    @mock.patch("writingprompts.backend.src.gemini.client.GoogleGeminiClient")
    def test_make_request_rate_limit(self, _, mock_client_class):
        """
        Test a request to the server sends a proper exception when the rate limit is hit.
        """
        # Arrange
        query = "what is 1 + 1?"
        status_code = 429
        message = "oops"

        mock_models = mock.Mock()
        mock_models.generate_content.side_effect = APIError(
            code=status_code, response_json={"message": message}
        )

        mock_client_instance = mock.Mock()
        mock_client_instance.models = mock_models
        mock_client_class.return_value = mock_client_instance

        client = GoogleGeminiClient()

        # Act
        with pytest.raises(HTTPException) as e:
            client.make_request(query)

        # Assert
        self.assertEqual(e.value.status_code, 429)
        self.assertEqual(e.value.detail, message)
