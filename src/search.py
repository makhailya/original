import re
from typing import Any


def process_bank_search(data: list[dict[str, Any]], search: str) -> list[dict[str, Any]]:
    """
    Ищет транзакции по ключевому слову в описании.

    :param data: список транзакций
    :param search: строка для поиска (регистронезависимый поиск)
    :return: список транзакций с совпадением
    """
    pattern = re.compile(search, re.IGNORECASE)
    return [item for item in data if "description" in item and pattern.search(item["description"])]
