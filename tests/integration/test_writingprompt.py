"""
Integration tests for writing prompt endpoint.
"""

import json
import unittest
from unittest import mock
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from main import app


class TestWritingPrompt(unittest.TestCase):
    """
    Writing prompt integration tests.
    """

    UNPROCESSABLE_CONTENT_CODE = 422

    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Function to setup test resources.
        """
        self.client = TestClient(app)  # pylint: disable=attribute-defined-outside-init

    @mock.patch("google.generativeai.GenerativeModel")
    def test_create_prompt(self, mock_gemini):
        """
        Test a valid request to the client returns expected response.
        """
        # Arrange
        keywords = ["cop", "heist"]
        request_body = {"genre": "comedy", "keywords": keywords}
        response_text = (
            "A retired cop stumbles on the heist of a "
            "lifetime while chasing his dropped hotdog"
        )

        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.return_value = MagicMock(
            text=response_text
        )
        mock_gemini.return_value = mock_model_instance

        # Act
        response = self.client.post("/writingprompt", json=request_body)
        data = json.loads(response.text)

        # Assert
        self.assertTrue(response.text)
        self.assertTrue(data["msg"])
        for key in keywords:
            self.assertIn(key, data["msg"])

    @mock.patch("google.generativeai.GenerativeModel")
    def test_create_prompt_no_keywords(self, mock_gemini):
        """
        Test a valid request to the client without keywords returns expected response.
        """
        # Arrange
        request_body = {"genre": "comedy"}
        response_text = "Shenanigans occur on a man's first day as a daycare owner."

        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.return_value = MagicMock(
            text=response_text
        )
        mock_gemini.return_value = mock_model_instance

        # Act
        response = self.client.post("/writingprompt", json=request_body)
        data = json.loads(response.text)

        # Assert
        self.assertTrue(response.text)
        self.assertTrue(data["msg"])

    def test_create_prompt_no_request_body(self):
        """
        Test an error response is returned if no request body is provided.
        """
        # Act
        response = self.client.post("/writingprompt")

        # Assert
        self.assertEqual(response.status_code, self.UNPROCESSABLE_CONTENT_CODE)

    def test_create_prompt_no_genre(self):
        """
        Test an error response is returned if no genre is provided in the request.
        """
        # Arrange
        request_body = {"keywords": ["clown", "party"]}
        # Act
        response = self.client.post("/writingprompt", json=request_body)

        # Assert
        self.assertEqual(response.status_code, self.UNPROCESSABLE_CONTENT_CODE)
