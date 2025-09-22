import pandas as pd
from typing import List, Dict


def read_transactions_csv(path: str) -> List[Dict]:
    """
    Считывает транзакции из CSV-файла.

    :param path: путь к CSV-файлу
    :return: список транзакций (каждая строка как словарь)
    """
    try:
        df = pd.read_csv(path)
        return df.to_dict(orient="records")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []


def read_transactions_excel(path: str) -> List[Dict]:
    """
    Считывает транзакции из Excel-файла.

    :param path: путь к Excel-файлу
    :return: список транзакций (каждая строка как словарь)
    """
    try:
        df = pd.read_excel(path)
        return df.to_dict(orient="records")
    except (FileNotFoundError, ValueError):
        return []
