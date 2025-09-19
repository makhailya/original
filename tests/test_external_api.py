from unittest.mock import patch
from external_api import convert_to_rub

@patch("external_api.requests.get")
def test_convert_usd_to_rub(mock_get):
    mock_get.return_value.json.return_value = {"result": 7500.0}
    mock_get.return_value.raise_for_status = lambda: None

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }

    result = convert_to_rub(transaction)
    assert result == 7500.0
