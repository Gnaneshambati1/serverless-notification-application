import json
from unittest.mock import patch, MagicMock
from sendEmail import lambda_handler


def test_missing_email_returns_400():
    result = lambda_handler({"subject": "Test"}, None)
    assert result["statusCode"] == 400


@patch("sendEmail.ses")
def test_valid_request_returns_200(mock_ses):
    mock_ses.send_email.return_value = {"MessageId": "abc123"}
    result = lambda_handler(
        {"email": "test@example.com", "subject": "Hi", "message": "Hello"}, None
    )
    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert body["messageId"] == "abc123"
