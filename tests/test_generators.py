import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"amount": "100", "currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {"amount": "200", "currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "operationAmount": {"amount": "300", "currency": {"code": "USD"}},
            "description": "Перевод с карты на карту",
        },
    ]


def test_filter_by_currency_usd(sample_transactions):
    usd_gen = filter_by_currency(sample_transactions, "USD")
    result = list(usd_gen)
    assert len(result) == 2
    assert all(tx["operationAmount"]["currency"]["code"] == "USD" for tx in result)


def test_filter_by_currency_empty(sample_transactions):
    eur_gen = filter_by_currency(sample_transactions, "EUR")
    assert list(eur_gen) == []


def test_transaction_descriptions(sample_transactions):
    desc_gen = transaction_descriptions(sample_transactions)
    result = list(desc_gen)
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize("start, end, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
])
def test_card_number_generator_range(start, end, expected):
    assert list(card_number_generator(start, end)) == expected


def test_card_number_generator_large():
    # Проверка крайних значений
    last = list(card_number_generator(9999999999999999, 9999999999999999))
    assert last == ["9999 9999 9999 9999"]
