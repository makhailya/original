import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    :param transaction: словарь транзакции
    :return: сумма в рублях
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    headers = {"apikey": API_KEY}
    params = {
        "from": currency,
        "to": "RUB",
        "amount": amount
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    return float(data.get("result", 0.0))
