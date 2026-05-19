from src.formatters import format_transaction


def test_format_transaction_rub():
    tx = {
        "date": "2019-12-08T12:00:00.000000",
        "description": "Открытие вклада",
        "from": "Счет 1234567890123456",
        "operationAmount": {"amount": "40542", "currency": {"code": "RUB"}}
    }
    out = format_transaction(tx)
    assert "08.12.2019" in out
    assert "Открытие вклада" in out
    assert "Счет" in out
    assert "Сумма: 40542 руб." in out
