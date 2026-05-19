from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Генератор, возвращающий транзакции в заданной валюте.

    :param transactions: список транзакций (словарей)
    :param currency: код валюты (например, "USD")
    :return: итератор транзакций
    """
    for tx in transactions:
        if tx.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield tx


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описания транзакций.

    :param transactions: список транзакций
    :return: итератор строк с описанием
    """
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение (целое число)
    :param end: конечное значение (целое число)
    :return: итератор отформатированных номеров карт
    """
    for number in range(start, end + 1):
        yield f"{number:016d}"[:16].replace(
            f"{number:016d}"[:16], " ".join([f"{number:016d}"[i:i + 4] for i in range(0, 16, 4)])
        )
