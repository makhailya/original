import re
from collections import Counter
from typing import Any


def process_bank_search(data: list[dict[str, Any]], search: str) -> list[dict[str, Any]]:
    """
    Ищет транзакции по ключевому слову в описании (регистронезависимо).
    """
    pattern = re.compile(search, re.IGNORECASE)
    return [item for item in data if "description" in item and pattern.search(item["description"])]


def process_bank_operations(data: list[dict[str, Any]], categories: list[str]) -> dict[str, int]:
    """
    Считает количество операций по категориям.
    """
    descriptions = [item.get("description", "") for item in data]
    counter = Counter()

    for category in categories:
        counter[category] = sum(1 for desc in descriptions if category.lower() in desc.lower())

    return dict(counter)
