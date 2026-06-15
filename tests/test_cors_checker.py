from unittest.mock import Mock, patch

from src.cors_checker import check_cors


@patch("src.cors_checker.requests.get")
def test_cors_detects_wildcard_with_credentials(mock_get):
    mock_response = Mock()
    mock_response.headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
    }
    mock_get.return_value = mock_response

    result = check_cors("http://localhost:5000")

    assert result[0]["potential_issue"] is True
    assert result[0]["access_control_allow_origin"] == "*"