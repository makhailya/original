import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_short():
    with pytest.raises(ValueError):
        get_mask_card_number("1234")  # слишком короткий номер не маскируется


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("123456789", "**6789"),
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_short():
    with pytest.raises(ValueError):
        get_mask_account("123")  # слишком короткий номер
