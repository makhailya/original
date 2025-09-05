import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("value, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_mask_account_card_invalid():
    assert mask_account_card("Некорректные данные") == "Некорректные данные"


@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2020-01-01T00:00:00", "01.01.2020"),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected


def test_get_date_invalid():
    assert get_date("не дата") == "не дата"
