# tests/test_services.py
import json
import pytest
from src.services import investment_bank


@pytest.fixture
def sample_transactions():
    return [
        {"Дата операции": "2025-09-10", "Сумма операции": 1712},
        {"Дата операции": "2025-09-15", "Сумма операции": 243},   # округление от 243
        {"Дата операции": "2025-08-20", "Сумма операции": 500},   # другой месяц → игнор
        {"Дата операции": "2025-09-25", "Сумма операции": 999.5}, # нецелое число
        {"Дата операции": "ошибка", "Сумма операции": 100},       # некорректная дата
    ]

def test_investment_bank_basic(sample_transactions):
    result = investment_bank("2025-09", sample_transactions, 50)
    data = json.loads(result)


    assert data["month"] == "2025-09"
    # Проверяем округления:
    # 1712 → 1750 → 38
    # 243 → 250 → 7
    # 999.5 → 1000 → 0.5
    # итого = 45.5
    assert pytest.approx(data["saved"], 0.01) == 45.5


def test_investment_bank_different_limit(sample_transactions):
    result = investment_bank("2025-09", sample_transactions, 100)
    data = json.loads(result)

    # 1712 → 1800 → 88
    # 243 → 300 → 57
    # 999.5 → 1000 → 0.5
    # итого = 145.5
    assert pytest.approx(data["saved"], 0.01) == 145.5


def test_investment_bank_no_transactions():
    result = investment_bank("2025-07", [], 50)
    data = json.loads(result)

    assert data["month"] == "2025-07"
    assert data["saved"] == 0.0
