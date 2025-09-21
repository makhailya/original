"""
Тестовый скрипт для проверки работы функций и логирования.
После запуска смотри файлы:
    • logs/masks.log
    • logs/utils.log
"""

from src.masks import get_mask_card_number, get_mask_account
from src.utils import read_transactions


def main() -> None:
    # Проверка маскировки карты
    print(get_mask_card_number("7000792289606361"))

    # Проверка маскировки счёта
    print(get_mask_account("73654108430135874305"))

    # Чтение JSON с транзакциями
    transactions = read_transactions("data/operations.json")
    print(transactions)


if __name__ == "__main__":
    main()
