from unittest.mock import Mock, patch

from src.sql_injection import test_sql_injection as run_sql_injection_check


@patch("src.sql_injection.requests.get")
def test_sql_injection_detects_server_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.text = "sql syntax error"
    mock_get.return_value = mock_response

    config = {
        "target": {
            "base_url": "http://localhost:5000",
            "test_parameter": "q",
        },
        "endpoints": {
            "sql_injection": "/search",
        },
        "sql_injection": {
            "payloads": ["' OR 1=1 --"],
        },
    }

    result = run_sql_injection_check(config)

    assert result[0]["potential_issue"] is True
    assert result[0]["status_code"] == 500