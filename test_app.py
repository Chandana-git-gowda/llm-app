from unittest.mock import patch, MagicMock
from app import ask_llm


def test_ask_llm_returns_string():
    """Test that ask_llm returns a string response."""
    # Create a fake response that looks like Anthropic's response
    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = "Hello! How can I help you?"

    # Replace the real API client with our fake one
    with patch("app.client") as mock_client:
        mock_client.messages.create.return_value = mock_response
        result = ask_llm("Say hello")

    # Check: is the result a string?
    assert isinstance(result, str)
    # Check: is it not empty?
    assert len(result) > 0


def test_ask_llm_returns_expected_content():
    """Test that ask_llm returns the exact mocked content."""
    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = "I am a helpful assistant."

    with patch("app.client") as mock_client:
        mock_client.messages.create.return_value = mock_response
        result = ask_llm("Who are you?")

    # Check: does it return exactly what we mocked?
    assert result == "I am a helpful assistant."