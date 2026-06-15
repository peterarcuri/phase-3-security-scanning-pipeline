from unittest.mock import Mock, patch

from src.header_audit import audit_headers


@patch("src.header_audit.requests.get")
def test_header_audit_returns_missing_headers(mock_get):
    mock_response = Mock()
    mock_response.headers = {}
    mock_get.return_value = mock_response

    config = {
        "target": {
            "base_url": "http://localhost:5000",
        },
        "headers": {
            "required": [
                "Content-Security-Policy",
                "X-Frame-Options",
                "X-Content-Type-Options",
            ],
        },
    }

    result = audit_headers(config)

    assert isinstance(result, list)
    assert len(result) > 0