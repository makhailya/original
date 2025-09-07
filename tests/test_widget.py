import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "invalid_input",
    [
        "",  # пустая строка
        "Некорректные данные",  # нет номера
        "Счет",  # только слово "Счет"
        "Visa",  # только название карты
    ],
)
def test_mask_account_card_invalid(invalid_input):
    # Функция должна вернуть исходное значение, если нет валидного номера
    assert mask_account_card(invalid_input) == invalid_input


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-01-01T00:00:00", "01.01.2020"),
        ("2019-12-31T23:59:59.999999", "31.12.2019"),
    ],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected


@pytest.mark.parametrize(
    "invalid_date",
    [
        "",  # пустая строка
        "не дата",  # некорректная строка
        "2024-13-01T00:00:00",  # некорректный месяц
    ],
)
def test_get_date_invalid(invalid_date):
    # Функция должна вернуть исходное значение, если дата некорректна
    assert get_date(invalid_date) == invalid_date
