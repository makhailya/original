from collections import Counter
from typing import Any


def process_bank_operations(data: list[dict[str, Any]], categories: list[str]) -> dict[str, int]:
    """
    Считает количество операций по категориям.

    :param data: список транзакций
    :param categories: список категорий для подсчёта
    :return: словарь {категория: количество}
    """
    descriptions = [item.get("description", "") for item in data]
    counter = Counter()

    for category in categories:
        counter[category] = sum(1 for desc in descriptions if category.lower() in desc.lower())

    return dict(counter)
