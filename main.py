from pprint import pprint
from src.file_reader import read_transactions_csv, read_transactions_excel

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


# main.py
def main() -> None:
    csv_path = "data/transactions.csv"
    xlsx_path = "data/transactions_excel.xlsx"

    print("=== CSV ===")
    transactions_csv = read_transactions_csv(csv_path)
    pprint(transactions_csv[:5])  # печатаем первые 5 записей

    print("\n=== XLSX ===")
    transactions_xlsx = read_transactions_excel(xlsx_path)
    pprint(transactions_xlsx[:5])


if __name__ == "__main__":
    main()
